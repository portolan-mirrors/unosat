#!/usr/bin/env python3
"""Build one PMTiles file per collection with tylertoo.

The tileset is written next to the collection's GeoParquet with the same stem
(<id>.pmtiles), so `portolan add` registers it as the collection's tiles.

tylertoo is built from git, not crates.io; the commit is pinned in
TYLERTOO_REV and in CI. Max zoom is set per family, not "auto", because auto
under-zooms detailed polygons (tylertoo#601).

    WORK=... python3 tools/tile.py [--only id1,id2] [--jobs 16] [--force]
"""

import argparse
import json
import os
import subprocess
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TYLERTOO_REV = "c338560f16ef97dcc1a2269c8b204eae923a344f"
MAX_ZOOM = {"damage-sites": 15, "affected-structures": 15, "shelters": 15, "damage-areas": 15,
            "shelter-areas": 15, "damage-lines": 15}
DEFAULT_MAX_ZOOM = 13


# tylertoo refuses one row whose decoded size passes 64 MiB, a fixed limit
# with no runtime override at c338560. UNOSAT has single multipolygons with up
# to about two million parts. For the tiling copy only, rows above this WKB
# size are exploded into their parts (and a part still too big is clipped on a
# grid), which keeps every vertex and attribute; see explode().
EXPLODE_BYTES = 16 << 20
TOO_BIG = ("read batch memory limit", "byte-array ceiling")
EMPTY = "no output rows produced"


def error_line(r):
    text = (r.stderr or "") + (r.stdout or "")
    errs = [l for l in text.splitlines() if l.startswith("Error") or "panicked" in l]
    return (errs[-1] if errs else text[-300:]).strip()


def explode(src, dst, columns=None):
    """Write the tiling copy of src with no row over EXPLODE_BYTES of WKB.

    A multi-part row is split into its parts. A single part still over the
    size (one water polygon has 8 million vertices and 113,712 holes) is
    clipped on an 8 x 8 grid over its bounding box; the cells' area equals
    the polygon's to 13 significant digits. GEOS cannot clip some invalid
    polygons; a cell whose clip fails is clipped from ST_MakeValid(part)
    instead, so that repair reaches the tiles of that one cell only. Attributes are copied to
    every piece. Only the tiling copy is changed, never the GeoParquet.
    """
    L = EXPLODE_BYTES
    cols = "* EXCLUDE (bbox)" if columns is None else ", ".join(columns + ["geometry"])
    size = "octet_length(ST_AsWKB(geometry))"
    sql = f"""LOAD spatial; SET preserve_insertion_order = false; SET memory_limit = '120GB';
COPY (
  WITH src AS (SELECT {cols} FROM read_parquet('{src}')),
  parts AS (
    SELECT * EXCLUDE (geometry, __d), __d.geom AS geometry
    FROM (SELECT *, UNNEST(ST_Dump(geometry)) AS __d FROM src WHERE {size} > {L})),
  big AS (
    SELECT *, ST_XMin(geometry) AS __x0, ST_YMin(geometry) AS __y0,
           (ST_XMax(geometry) - ST_XMin(geometry)) / 8 AS __dx,
           (ST_YMax(geometry) - ST_YMin(geometry)) / 8 AS __dy,
           ST_Dimension(geometry) AS __dim
    FROM parts WHERE {size} > {L}),
  cells AS (
    SELECT * EXCLUDE (geometry, __x0, __y0, __dx, __dy, __i, __j, __env),
           COALESCE(TRY(ST_Intersection(geometry, __env)), ST_Intersection(ST_MakeValid(geometry), __env)) AS __c
    FROM (SELECT *, ST_MakeEnvelope(__x0 + __i * __dx, __y0 + __j * __dy,
                                                     __x0 + (__i + 1) * __dx, __y0 + (__j + 1) * __dy) AS __env
          FROM big, range(8) t1(__i), range(8) t2(__j))),
  clipped AS (
    SELECT * EXCLUDE (__c, __d2, __dim), __d2.geom AS geometry
    FROM (SELECT *, UNNEST(ST_Dump(__c)) AS __d2 FROM cells WHERE NOT ST_IsEmpty(__c))
    WHERE ST_Dimension(__d2.geom) = __dim)
  SELECT * FROM src WHERE geometry IS NULL OR {size} <= {L}
  UNION ALL BY NAME SELECT * FROM parts WHERE {size} <= {L}
  UNION ALL BY NAME SELECT * FROM clipped
) TO '{dst}' (FORMAT parquet);
"""
    r = subprocess.run(["duckdb", "-no-agent"], input=sql, capture_output=True, text=True)
    return None if r.returncode == 0 else (r.stderr or r.stdout)[-300:]


def run_tylertoo(tin, out, info, spill):
    spill.mkdir(parents=True, exist_ok=True)
    cmd = ["tylertoo", "tiles", str(tin), str(out), "--layer-name", info["family"],
           "--max-zoom", str(MAX_ZOOM.get(info["family"], DEFAULT_MAX_ZOOM)),
           "--name", info["collection"], "--attribution", "UNITAR-UNOSAT",
           "--exclude-property", "bbox", "--spill-dir", str(spill), "-f"]
    env = dict(os.environ, RAYON_NUM_THREADS="4")
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=3600, env=env)
    except subprocess.TimeoutExpired:
        return "timeout after 3600 s"
    finally:
        subprocess.run(["rm", "-rf", str(spill)])
    if r.returncode or not out.exists():
        return error_line(r)
    return None


def tile(info, work, force):
    coll = ROOT / "catalog" / info["path"]
    src = coll / f"{info['collection']}.parquet"
    out = coll / f"{info['collection']}.pmtiles"
    if out.exists() and not force and out.stat().st_mtime > src.stat().st_mtime:
        return info["collection"], "cached"
    tmp = Path(work) / "tile-tmp"
    tmp.mkdir(parents=True, exist_ok=True)
    made = []
    tin = src
    try:
        if info["crs"] not in ("EPSG:4326", "EPSG:3857"):
            # The GeoParquet keeps the source CRS; only the tiling copy is
            # reprojected.
            tin = tmp / f"{info['collection']}.4326.parquet"
            made.append(tin)
            r = subprocess.run(["gpio", "convert", "reproject", str(src), str(tin), "-d", "EPSG:4326"],
                               capture_output=True, text=True)
            if r.returncode:
                return info["collection"], "reproject failed: " + (r.stderr or r.stdout)[-300:]
        spill = Path(work) / "spill" / info["collection"]
        err = run_tylertoo(tin, out, info, spill)
        note = ""
        if err and any(t in err for t in TOO_BIG):
            x = tmp / f"{info['collection']}.exploded.parquet"
            made.append(x)
            e2 = explode(tin, x)
            if e2:
                return info["collection"], f"explode failed: {e2}"
            err = run_tylertoo(x, out, info, spill)
            note = " (oversized rows exploded into parts)"
        if err and EMPTY in err:
            out.unlink(missing_ok=True)
            return info["collection"], "empty: no drawable geometry, no tiles"
        if err:
            out.unlink(missing_ok=True)
            return info["collection"], "tylertoo failed: " + err
        return info["collection"], f"ok {out.stat().st_size / 1e6:.1f} MB{note}"
    finally:
        for f in made:
            f.unlink(missing_ok=True)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--explode":
        # tools/tile.py --explode SRC DST [col,col,...]: used by tile_combined.sh.
        cols = sys.argv[4].split(",") if len(sys.argv) > 4 else None
        err = explode(sys.argv[2], sys.argv[3], cols)
        sys.exit(f"explode failed: {err}" if err else 0)
    ap = argparse.ArgumentParser()
    ap.add_argument("--only")
    ap.add_argument("--jobs", type=int, default=16)
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    work = os.environ["WORK"]
    infos = [json.load(open(f)) for f in sorted((ROOT / "manifest" / "collections").glob("*.json"))]
    infos = [i for i in infos if i.get("status") == "ok"]
    if a.only:
        infos = [i for i in infos if i["collection"] in a.only.split(",")]
    print(f"{len(infos)} collections", file=sys.stderr)
    bad = 0
    with ProcessPoolExecutor(a.jobs) as ex:
        futs = [ex.submit(tile, i, work, a.force) for i in infos]
        for n, f in enumerate(as_completed(futs), 1):
            cid, msg = f.result()
            if msg.startswith("empty"):
                print(f"  EMPTY {cid}: {msg}", file=sys.stderr, flush=True)
            elif not msg.startswith(("ok", "cached")):
                bad += 1
                print(f"  FAIL {cid}: {msg}", file=sys.stderr, flush=True)
            elif "exploded" in msg:
                print(f"  {cid}: {msg}", file=sys.stderr, flush=True)
            if n % 50 == 0:
                print(f"  {n}/{len(futs)}", file=sys.stderr, flush=True)
            if not msg.startswith("cached"):
                # The record says whether the collection has tiles, for the
                # metadata and docs steps.
                rec = ROOT / "manifest" / "collections" / f"{cid}.json"
                d = json.load(open(rec))
                d["tiles"] = msg
                rec.write_text(json.dumps(d, indent=1, default=str, ensure_ascii=False) + "\n")
    print(f"done, {bad} failures", file=sys.stderr)


if __name__ == "__main__":
    main()

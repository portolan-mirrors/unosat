#!/usr/bin/env python3
"""Render every collection thumbnail with chiitiler (the portolan-thumbnails
skill), over the Esri World Light Gray basemap.

For each collection, try a full-extent 3:2 frame, then 3:2 windows on the
densest cluster at increasing zoom, up to the archive's max zoom. Score each
frame by the share of non-white pixels in the probe render (the collection's
own layers on white, no basemap). Keep the first frame with coverage >= 8%,
else the best one.

    python3 tools/thumbs.py SKILL_SCRIPTS_DIR WORK_DIR [collection_dir ...]

SKILL_SCRIPTS_DIR is a copy of the skill's scripts/ with the basemap raster
source capped at maxzoom 15: past 15 Esri returns "Map data not yet available"
tiles in many areas.
"""
import json, subprocess, sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from PIL import Image

S, WORK = sys.argv[1], Path(sys.argv[2])
CAT = Path(__file__).resolve().parent.parent / "catalog"
GOOD = 0.08
# UNOSAT "affected roads" layers of many events carry template features
# stacked near 29.8E 9.3N (South Sudan); never frame a thumbnail on them.
JUNK = (29.6, 9.0, 30.4, 9.5)


def sh(*a, **k):
    return subprocess.run(a, capture_output=True, text=True, **k).stdout


def coverage(png):
    im = Image.open(png).convert("L")
    h = im.histogram()
    return 1 - sum(h[245:]) / sum(h)


def frame(**kw):
    args = ["python3", f"{S}/frame.py", "--size", "1024", "--max-context", "99"]
    for k, v in kw.items():
        args += [f"--{k}", str(v)]
    return json.loads(sh(*args))


def render(c, w, bbox):
    out = sh("bash", f"{S}/render_one.sh", f"{c}/", bbox, env={"WORK": str(w), "PATH": "/usr/bin:/bin"}).strip()
    p = w / "probe.png"
    return (coverage(p) if "gate1=FAIL" not in out and p.exists() else 0.0), out.splitlines()[-1] if out else "no output"


def to_wgs84(pq):
    kv = sh("duckdb", "-no-agent", "-json", input=f"SELECT decode(value) v FROM parquet_kv_metadata('{pq}') WHERE decode(key)='geo';")
    try:
        crs = json.loads(json.loads(kv[kv.index("[{"):])[0]["v"])["columns"]["geometry"].get("crs") or {}
        code = int((crs.get("id") or {}).get("code") or 4326)
    except (ValueError, KeyError, TypeError):
        code = 4326
    xy = ("(bbox.xmin+bbox.xmax)/2", "(bbox.ymin+bbox.ymax)/2")
    if code == 4326:
        return xy
    pt = f"ST_Transform(ST_Point({xy[0]}, {xy[1]}), 'EPSG:{code}', 'EPSG:4326', always_xy := true)"
    return (f"ST_X({pt})", f"ST_Y({pt})")


def densest(pq, xy, z):
    cell = 40075016.7 * 1024 / (256 * 2 ** z) / 111319.49 / 1.5
    sql = f"""INSTALL spatial; LOAD spatial;
WITH c0 AS (SELECT {xy[0]} x, {xy[1]} y FROM read_parquet('{pq}') WHERE bbox.xmin IS NOT NULL),
c AS (SELECT * FROM c0 WHERE NOT (x BETWEEN {JUNK[0]} AND {JUNK[2]} AND y BETWEEN {JUNK[1]} AND {JUNK[3]})),
g AS (SELECT floor(x/{cell}) gx, floor(y/{cell}) gy, count(*) n FROM c GROUP BY 1,2),
t AS (SELECT gx, gy FROM g ORDER BY n DESC LIMIT 1)
SELECT avg(x) x, avg(y) y FROM c, t
WHERE x BETWEEN (gx-1)*{cell} AND (gx+2)*{cell} AND y BETWEEN (gy-1)*{cell} AND (gy+2)*{cell};"""
    o = sh("duckdb", "-no-agent", "-json", input=sql)
    r = json.loads(o[o.index("[{"):])[0]
    return r["x"], r["y"]


def one(c):
    c = Path(c)
    rel = c.relative_to(CAT).as_posix()
    w = WORK / "w" / rel.replace("/", "__")
    w.mkdir(parents=True, exist_ok=True)
    (w / "basemap.url").write_text((WORK / "basemap.url").read_text())
    info = json.loads(sh("python3", f"{S}/read_collection.py", str(c)))
    hdr = json.loads(sh("python3", f"{S}/frame.py", "--pmtiles", info["pmtiles"]))
    tries = []
    a = frame(bbox=info["bbox"])
    tries.append(("A", a["bbox"], a["zoom"]))
    cov, out = render(c, w, a["bbox"])
    best = (cov, "A", a["bbox"], round(a["zoom"], 2), out)
    if cov < GOOD:
        pq = next(c.glob("*.parquet"))
        xy = to_wgs84(pq)
        for z in range(max(int(a["zoom"]) + 1, 1), hdr["max_zoom"] + 1):
            try:
                x, y = densest(pq, xy, z)
            except (ValueError, KeyError, TypeError):
                break
            b = frame(center=f"{x},{y}", zoom=z)
            cov, out = render(c, w, b["bbox"])
            if cov > best[0]:
                best = (cov, "B", b["bbox"], z, out)
            if cov >= GOOD:
                break
        if best[1] != "B" or cov != best[0]:
            render(c, w, best[2])  # re-render the winner to the thumbnail path
    return f"{rel}\t{best[1]}\t{best[2]}\t{best[3]}\t{best[0]:.3f}\t{best[4]}"


if __name__ == "__main__":
    cols = sys.argv[3:] or sorted(str(p.parent) for p in CAT.rglob("collection.json")
                                  if (p.parent / f"{p.parent.name}.pmtiles").exists())
    with ProcessPoolExecutor(16) as ex:
        for line in ex.map(one, cols):
            print(line, flush=True)

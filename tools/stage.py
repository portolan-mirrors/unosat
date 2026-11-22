#!/usr/bin/env python3
"""Stage the downloaded UNOSAT files as Portolan collections.

Run with ``python3 -I``: the inputs are untrusted downloads.

Layout (one event = one subcatalog, one schema family = one collection):

    catalog/<hazard>/[<year>/]<event>/<event>-<family>/<event>-<family>.parquet

Steps:
  1. Per source file (cached in $WORK/conv/<key>/): extract the zip, list the
     spatial layers with GDAL, and convert each layer with
     ``gpio convert geoparquet --layer <name>``. Layer names come from GDAL
     because the gpio and portolan layer listing is broken for some FileGDBs
     (geoparquet-io#1472, portolan-cli#1127).
  2. Per event: group the layers by schema family, geometry class, license and
     CRS, union each group into one table with ``source_layer`` and
     ``source_file`` columns (DuckDB), and normalize it with
     ``gpio convert geoparquet``.
  3. Write $WORK/colls/<collection>.json with the layers, sources, HDX
     datasets and coded-value domains, for the metadata step.

    WORK=... python3 -I tools/stage.py [--events a,b] [--jobs 32]
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog"
sys.path.insert(0, str(ROOT / "tools"))
from fetch import aria, local_path, ok as fetched  # noqa: E402

TIMEOUT = 3600

# Family rules: (family, field regex, layer-name regex). First match wins.
# A cloud mask in a flood bundle carries Water_Class columns too, so the
# analysis-extent rule is checked first and only on the layer name.
RULES = [
    ("analysis-extent", None, r"analysis.?extent|\baoi\b|cloud|obstruct|no.?data|footprint|coverage"),
    ("damage", r"^(main_dam|main_damag|main_damage_site_class|damage_cla|dam_site|damage_type|grouped_da)", None),
    ("water-extent", r"^(water_cla|water_stat|waterclass)", r"flood|water|inund|wet"),
    ("shelters", r"^(campname|camptype|campstatus|shelter|structure_|idp)", r"camp|shelter|idp|refugee|settlement"),
    ("landslides", None, r"landslide|mudflow|debris"),
    ("affected-structures", None, r"affected.?struct|building|structure"),
]
NAMES = {
    ("damage", "points"): "damage-sites",
    ("damage", "polygons"): "damage-areas",
    ("water-extent", "polygons"): "water-extent",
    ("analysis-extent", "polygons"): "analysis-extent",
    ("shelters", "points"): "shelters",
    ("shelters", "polygons"): "shelter-areas",
    ("landslides", "polygons"): "landslides",
    ("affected-structures", "points"): "affected-structures",
}


def run(cmd, timeout=TIMEOUT):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)


def slug(s, n=100):
    return (re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_") or "layer")[:n]


def geom_class(name):
    n = (name or "").lower()
    return "points" if "point" in n else "lines" if "line" in n or "curve" in n else "polygons" if "polygon" in n or "surface" in n else "mixed"


def family(layer, fields, gclass):
    base = "other"
    for fam, fre, lre in RULES:
        if fre and any(re.search(fre, f, re.I) for f in fields):
            base = fam
            break
        if lre and re.search(lre, layer, re.I):
            base = fam
            break
    return NAMES.get((base, gclass), f"{base}-{gclass}")


# ---------------------------------------------------------------- step 1

def extract(zpath, dest):
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)

    def safe_extract(z, d):
        for m in z.infolist():
            t = (d / m.filename).resolve()
            if str(t).startswith(str(d.resolve()) + os.sep):
                z.extract(m, d)

    with zipfile.ZipFile(zpath) as z:
        safe_extract(z, dest)
    for inner in list(dest.rglob("*.zip")):
        if zipfile.is_zipfile(inner):
            sub = inner.with_suffix("")
            sub.mkdir(exist_ok=True)
            with zipfile.ZipFile(inner) as z:
                safe_extract(z, sub)
    # GDAL only opens a FileGDB whose folder name ends in .gdb.
    for d in sorted(dest.rglob("*"), key=lambda p: -len(p.parts)):
        if d.is_dir() and not d.name.lower().endswith(".gdb") and any(d.glob("*.gdbtable")):
            d.rename(d.with_name(re.sub(r"[_ .]?gdb$", "", d.name, flags=re.I) + ".gdb"))


def datasources(root):
    out = []
    gdbs = []
    for p in sorted(root.rglob("*")):
        low = p.name.lower()
        if any(p.is_relative_to(g) for g in gdbs):
            continue
        # A .gdb folder is a datasource only if it holds the tables itself;
        # some zips nest FR.gdb/FR.gdb.
        if p.is_dir() and low.endswith(".gdb") and any(p.glob("*.gdbtable")):
            gdbs.append(p)
            out.append(p)
        elif p.is_file() and low.endswith((".shp", ".gpkg", ".kml", ".geojson")) \
                and not any(part.lower().endswith(".gdb") for part in p.relative_to(root).parts[:-1]):
            out.append(p)
    return out


def probe(ds):
    from osgeo import gdal, ogr, osr
    gdal.UseExceptions()
    gdal.SetConfigOption("SHAPE_RESTORE_SHX", "YES")
    h = gdal.OpenEx(str(ds), gdal.OF_VECTOR)
    domains = {}
    try:
        for n in h.GetFieldDomainNames() or []:
            d = h.GetFieldDomain(n)
            if d.GetDomainType() == ogr.OFDT_CODED:
                domains[n] = {str(k): v for k, v in d.GetEnumeration().items()}
    except Exception:
        pass
    wgs = osr.SpatialReference()
    wgs.ImportFromEPSG(4326)
    wgs.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER)
    layers = []
    for i in range(h.GetLayerCount()):
        L = h.GetLayer(i)
        try:
            n_features = L.GetFeatureCount()
        except RuntimeError as e:
            # A corrupt table (seen in two UNOSAT geodatabases) fails here;
            # record it and keep the datasource's other layers.
            layers.append({"layer": L.GetName(), "probe_error": str(e)[:300]})
            continue
        if L.GetGeomType() == ogr.wkbNone or n_features == 0:
            continue
        fd = L.GetLayerDefn()
        fields = [{"name": fd.GetFieldDefn(j).GetName(), "type": fd.GetFieldDefn(j).GetTypeName(),
                   "domain": fd.GetFieldDefn(j).GetDomainName() or None,
                   "alias": fd.GetFieldDefn(j).GetAlternativeName() or None} for j in range(fd.GetFieldCount())]
        srs = L.GetSpatialRef()
        crs, wgs84_h = None, False
        if srs is not None:
            srs.AutoIdentifyEPSG()
            if srs.GetAuthorityName(None):
                crs = f"{srs.GetAuthorityName(None)}:{srs.GetAuthorityCode(None)}"
            g = srs.GetAttrValue("GEOGCS") or ""
            wgs84_h = (crs == "EPSG:4326") or (srs.IsCompound() and "WGS 84" in g and srs.IsGeographic())
            if not crs and srs.IsCompound() and srs.IsProjected() and srs.GetAuthorityCode("PROJCS"):
                crs = f"EPSG:{srs.GetAuthorityCode('PROJCS')}"
            if not crs:
                crs = srs.GetName()
        layers.append({"layer": L.GetName(), "features": L.GetFeatureCount(),
                       "geometry_type": ogr.GeometryTypeToName(L.GetGeomType()),
                       "crs": crs, "wgs84_horizontal": bool(wgs84_h), "fields": fields})
    return layers, domains


# GDAL's default ring nesting is quadratic on many-part polygons (one UNOSAT
# flood extent did not finish in 5 minutes). Esri writes each hole right after
# its outer ring, so the linear mode applies. On the layers compared it gave
# byte-identical WKB to the default and ran in 1-2 s.
GDAL_ENV = {"OGR_ORGANIZE_POLYGONS": "CCW_INNER_JUST_AFTER_CW_OUTER", "SHAPE_RESTORE_SHX": "YES"}


def gpio(args):
    """Run gpio, rerunning a crash. gpio 1.7.0 (DuckDB 1.5.6) segfaults on
    about a quarter of runs over identical input, more often under load; a
    rerun of the same input works. The row-count checks guard the output."""
    for _ in range(20):
        r = run(["gpio", *args])
        if r.returncode >= 0:
            return r
    return r


def duck(sql):
    """Run SQL with the DuckDB CLI and return the rows as lists of values."""
    r = subprocess.run(["duckdb", "-no-agent", "-json"], input="LOAD spatial;\n" + sql + ";\n",
                       capture_output=True, text=True, timeout=TIMEOUT)
    if r.returncode:
        raise RuntimeError("duckdb: " + (r.stderr or r.stdout)[-400:])
    out = r.stdout.strip()
    return [list(row.values()) for row in json.loads(out)] if out else []


def nrows(path):
    return int(duck(f"SELECT count(*) FROM read_parquet('{path}')")[0][0])


def convert_layer(ds, layer, out, tmpdir, expected):
    """ogr2ogr (system GDAL) to GeoPackage, then gpio to GeoParquet 2.0.

    GeoPackage, not FlatGeobuf, because FlatGeobuf rejects NULL geometries and
    features whose type differs from the layer's; UNOSAT layers have both.

    gpio's default geometry repair (ST_MakeValid) took over 120 s on one layer
    that converts in 4 s without it, and a mirror keeps source geometry as is.
    The output must hold exactly the source's feature count.
    """
    fgb = tmpdir / (out.stem + ".gpkg")
    env = dict(os.environ, **GDAL_ENV)
    # Shapefiles mix Polygon and MultiPolygon in one layer; promoting to multi
    # is lossless and gives the layer one geometry type.
    cmd = ["ogr2ogr", "-f", "GPKG", "-nlt", "PROMOTE_TO_MULTI", str(fgb), str(ds)]
    if ds.is_dir() or ds.suffix.lower() in (".gpkg", ".kml"):
        cmd.append(layer)
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=TIMEOUT, env=env)
    if r.returncode or not fgb.exists():
        fgb.unlink(missing_ok=True)
        return "ogr2ogr: " + (r.stderr or r.stdout)[-400:]
    r = gpio(["convert", "geoparquet", str(fgb), str(out), "--geoparquet-version", "2.0", "--no-repair-geometry"])
    fgb.unlink(missing_ok=True)
    if r.returncode or not out.exists():
        return "gpio: " + (r.stderr or r.stdout)[-400:]
    n = nrows(out)
    if n != expected:
        # A geodatabase header can count deleted records (the .gdbtablx
        # mismatch GDAL warns about). The real count is what GDAL iterates.
        real = iterated_count(ds, layer)
        if n != real:
            out.unlink()
            return f"row count {n} != source feature count {expected} (iterated {real})"
        return {"header_count": expected, "features": real}
    return None


def iterated_count(ds, layer):
    from osgeo import gdal
    gdal.UseExceptions()
    h = gdal.OpenEx(str(ds), gdal.OF_VECTOR)
    lyr = h.GetLayerByName(layer) if h.GetLayerCount() > 1 or layer else h.GetLayer(0)
    lyr = lyr or h.GetLayer(0)
    lyr.SetIgnoredFields(["OGR_GEOMETRY"])  # count rows without parsing geometry
    return sum(1 for _ in lyr)


def stage_source(work, key, path, kind):
    import time
    out = work / "conv" / key
    meta = out / "layers.json"
    if meta.exists():
        return key, "cached"
    shutil.rmtree(out, ignore_errors=True)
    out.mkdir(parents=True)
    tmpdir = work / "tmp" / key
    tmpdir.mkdir(parents=True, exist_ok=True)
    res = {"file": path.name, "kind": kind, "layers": [], "errors": []}
    x = work / "x" / key
    try:
        is7z = open(path, "rb").read(6) == b"7z\xbc\xaf\x27\x1c"
        if zipfile.is_zipfile(path) or is7z:
            if not (x / ".extracted").exists():
                if is7z:
                    shutil.rmtree(x, ignore_errors=True)
                    x.mkdir(parents=True)
                    r = run(["7z", "x", "-y", f"-o{x}", str(path)])
                    if r.returncode:
                        raise RuntimeError("7z: " + r.stdout[-300:])
                    bad = [q for q in x.rglob("*") if not q.resolve().is_relative_to(x.resolve())]
                    if bad:
                        raise RuntimeError(f"7z entry outside the extraction folder: {bad[0]}")
                else:
                    extract(path, x)
                (x / ".extracted").touch()
            dss = datasources(x)
        else:
            dss = [path]
        if not dss:
            res["errors"].append("no vector datasource found")
        for n, ds in enumerate(dss):
            try:
                layers, domains = probe(ds)
            except Exception as e:
                res["errors"].append(f"{ds.name}: {e}")
                continue
            for L in layers:
                if L.get("probe_error"):
                    res["layers"].append({"layer": L["layer"], "datasource": ds.name, "features": None,
                                          "status": "error", "error": "unreadable layer: " + L["probe_error"],
                                          "parquet": None})
                    continue
                fname = f"{n:02d}_{slug(L['layer'])}.parquet"
                t0 = time.time()
                try:
                    err = convert_layer(ds, L["layer"], out / fname, tmpdir, L["features"])
                except subprocess.TimeoutExpired:
                    err = f"timeout after {TIMEOUT}s"
                if isinstance(err, dict):
                    L = {**L, **err}
                    err = None
                status = "error" if err else "ok"
                if not err:
                    # A layer whose every geometry is null or empty maps
                    # nothing (six UNOSAT line layers are like this). It is
                    # recorded, not merged.
                    f = out / fname
                    geo = [c[0] for c in duck(f"SELECT column_name, column_type FROM (DESCRIBE SELECT * FROM read_parquet({q(str(f))}))")
                           if c[1].upper().startswith("GEOMETRY") or c[1].upper() == "BLOB" and c[0].lower() in ("shape", "geom", "geometry")][0]
                    if not duck(f'SELECT count(*) FROM read_parquet({q(str(f))}) WHERE "{geo}" IS NOT NULL AND NOT ST_IsEmpty("{geo}"::GEOMETRY)')[0][0]:
                        status = "empty"
                fields = [f["name"] for f in L["fields"]]
                res["layers"].append({**L, "datasource": ds.name, "parquet": None if err else fname,
                                      "status": status, "error": err,
                                      "seconds": round(time.time() - t0, 2),
                                      "family": family(L["layer"], fields, geom_class(L["geometry_type"])),
                                      "domains": {f["name"]: domains[f["domain"]] for f in L["fields"]
                                                  if f["domain"] in domains}})
    except Exception as e:
        res["errors"].append(f"{type(e).__name__}: {e}")
    meta.write_text(json.dumps(res, indent=1, default=str))
    shutil.rmtree(tmpdir, ignore_errors=True)
    bad = sum(L["status"] != "ok" for L in res["layers"]) + len(res["errors"])
    return key, f"{len(res['layers'])} layers, {bad} errors"


# ---------------------------------------------------------------- step 2

def event_dir(ev, n_events_by_hazard):
    base = CATALOG / ev["hazard"]
    if n_events_by_hazard[ev["hazard"]] >= 20:
        base = base / str(ev["year"])
    return base / ev["id"]


def q(s):
    return "'" + str(s).replace("'", "''") + "'"


def merge(work, coll_id, parts, dest, crs=None):
    """Union the layer files of one collection into dest (DuckDB, then gpio)."""
    dropped_m = []

    def union(as_text):
        dropped_m.clear()
        out = []
        for p in parts:
            f = str(work / "conv" / p["key"] / p["parquet"])
            cols = duck(f"SELECT column_name, column_type FROM (DESCRIBE SELECT * FROM read_parquet({q(f)}))")
            geo = [c[0] for c in cols if c[1].upper().startswith("GEOMETRY")][0]
            # 2D geometry with a WGS 84 horizontal CRS ("WGS 84 + EGM96
            # height") is written without a CRS, which GeoParquet reads as CRS84.
            if p["wgs84_horizontal"]:
                g = f'"{geo}"::GEOMETRY'
            elif crs and re.fullmatch(r"EPSG:\d+", crs):
                g = f'"{geo}"::GEOMETRY::GEOMETRY(\'{crs}\')'
            else:
                g = f'"{geo}"'
            # DuckDB writes a column that mixes Z and ZM geometry as untyped
            # BLOB, which gpio cannot read. M (an ArcGIS route measure) is
            # dropped from such parts; X, Y and Z are kept.
            has_m = duck(f'SELECT bool_or(ST_HasM("{geo}"::GEOMETRY)) FROM read_parquet({q(f)})')[0][0]
            if has_m:
                g = (f'ST_Force3DZ({g}::GEOMETRY, 0)' if p["wgs84_horizontal"] else
                     f'ST_Force3DZ("{geo}"::GEOMETRY, 0)::GEOMETRY(\'{crs}\')' if crs and re.fullmatch(r"EPSG:\d+", crs)
                     else f'ST_Force3DZ("{geo}", 0)')
                dropped_m.append(p["layer"])
            # "fid" is the GeoPackage row id added by the intermediate step.
            keep = [c[0] for c in cols if c[0] not in (geo, "bbox", "fid")]
            body = "".join((f'"{c}"::VARCHAR AS "{c}", ' if as_text else f'"{c}", ') for c in keep)
            # Decode coded values with this source's own geodatabase domain.
            # Domains differ between exports, so each part is decoded with
            # its own table before the union.
            for fld, dom in sorted(p["domains"].items()):
                if fld in keep and dom:
                    cases = " ".join(f"WHEN {q(k)} THEN {q(v)}" for k, v in dom.items())
                    body += f'CASE CAST("{fld}" AS VARCHAR) {cases} END AS "{fld}_label", '
            out.append(f"SELECT {body}{g} AS geometry, {q(p['layer'])} AS source_layer, "
                       f"{q(p['source_file'])} AS source_file FROM read_parquet({q(f)})")
        return " UNION ALL BY NAME ".join(out)

    tmp = work / "merge" / f"{coll_id}.parquet"
    tmp.parent.mkdir(parents=True, exist_ok=True)
    note = None
    try:
        duck(f"COPY ({union(False)}) TO '{tmp}' (FORMAT parquet)")
    except RuntimeError as e:
        # The same column name with incompatible types across layers: keep
        # the values as text rather than drop a layer.
        note = f"column types conflicted across layers, so all attribute columns are text ({str(e)[:160]})"
        duck(f"COPY ({union(True)}) TO '{tmp}' (FORMAT parquet)")
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp2 = tmp.with_suffix(".gpio.parquet")
    r = gpio(["convert", "geoparquet", str(tmp), str(tmp2), "--geoparquet-version", "2.0", "--no-repair-geometry"])
    tmp.unlink(missing_ok=True)
    if r.returncode or not tmp2.exists():
        raise RuntimeError((r.stderr or r.stdout)[-500:])
    # portolan add rewrites a file that has no bbox covering column, and that
    # rewrite repairs geometry (it changed 15,837 polygons in one test). With
    # the column present, add leaves the file byte-identical.
    tmp3 = tmp.with_suffix(".bbox.parquet")
    tmp3.unlink(missing_ok=True)
    r = gpio(["add", "bbox", str(tmp2), str(tmp3)])
    tmp2.unlink(missing_ok=True)
    if r.returncode or not tmp3.exists():
        raise RuntimeError((r.stderr or r.stdout)[-500:])
    os.replace(tmp3, dest)  # gpio refuses to overwrite, and a rebuild must
    if dropped_m:
        m = f"M values were dropped from {len(dropped_m)} layer(s) that mix Z and ZM geometry: {', '.join(sorted(set(dropped_m)))}"
        note = f"{note}; {m}" if note else m
    expected = sum(p["features"] for p in parts)
    n = nrows(dest)
    if n != expected:
        raise RuntimeError(f"merged rows {n} != sum of layer features {expected}")
    return note


def stage_collection(work, coll_id, parts, dest, info):
    try:
        note = merge(work, coll_id, parts, dest, info.get("crs"))
        info["merge_note"] = note
        info["status"] = "ok"
    except Exception as e:
        info["status"] = "error"
        info["error"] = str(e)[-600:]
    # The record lives in the repository, so a refresh that rebuilds one event
    # still has every other collection's record.
    d = ROOT / "manifest" / "collections"
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{coll_id}.json").write_text(json.dumps(info, indent=1, default=str, ensure_ascii=False) + "\n")
    return coll_id, info["status"] + (f": {info.get('error','')[:200]}" if info["status"] != "ok" else "")


# ---------------------------------------------------------------- driver

def dead(work, cand):
    """True when this copy was converted and gave no usable layer."""
    meta = work / "conv" / local_path(work, cand["url"]).parent.name / "layers.json"
    if not meta.exists():
        return False
    return not any(L["status"] == "ok" for L in json.load(open(meta))["layers"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--events", help="comma-separated event/collection ids from the manifest")
    ap.add_argument("--jobs", type=int, default=32)
    a = ap.parse_args()
    work = Path(os.environ["WORK"])
    pkgs = json.load(open(ROOT / "manifest" / "packages.json"))
    events = defaultdict(lambda: {"packages": []})
    for p in pkgs:
        e = events[p["collection"]]
        e.update(id=p["collection"], hazard=p["hazard"], year=p["year"], code=p["event_code"])
        e["packages"].append(p)
    n_by_h = defaultdict(int)
    for e in events.values():
        n_by_h[e["hazard"]] += 1
    want = set(a.events.split(",")) if a.events else set(events)

    # Step 1: convert every source of the wanted events.
    sources = {}
    for eid in want:
        for p in events[eid]["packages"]:
            for s in p["sources"]:
                for cand in [s["primary"], *s["fallbacks"]]:
                    if cand["kind"] in ("gdb", "shp", "gpkg", "kmz", "kml") and fetched(work, cand):
                        sources[s["primary"]["url"]] = cand
                        break
    def convert(cands):
        jobs = {local_path(work, c["url"]).parent.name: (local_path(work, c["url"]), c["kind"]) for c in cands}
        print(f"step 1: {len(jobs)} source files", file=sys.stderr)
        with ProcessPoolExecutor(a.jobs) as ex:
            futs = [ex.submit(stage_source, work, k, p, kd) for k, (p, kd) in jobs.items()]
            for i, f in enumerate(as_completed(futs), 1):
                k, msg = f.result()
                print(f"  [{i}/{len(futs)}] {k} {msg}", file=sys.stderr, flush=True)

    convert(sources.values())
    # A primary copy that converted to nothing (a broken upstream export) is
    # replaced by the dataset's next copy, fetched now if it was not before.
    redo = {}
    for eid in want:
        for p in events[eid]["packages"]:
            for s in p["sources"]:
                c = sources.get(s["primary"]["url"])
                if not c or not dead(work, c):
                    continue
                rest = [f for f in [s["primary"], *s["fallbacks"]] if f is not c
                        and f["kind"] in ("gdb", "shp", "gpkg", "kml") and not dead(work, f)]
                if rest:
                    redo[s["primary"]["url"]] = rest[0]
    if redo:
        need = [f for f in redo.values() if not fetched(work, f)]
        if need:
            aria(str(work), need, "stage-fallback")
        redo = {u: f for u, f in redo.items() if fetched(work, f)}
        print(f"step 1b: {len(redo)} broken primaries replaced by another copy", file=sys.stderr)
        convert(redo.values())
        for u, f in redo.items():
            if not dead(work, f):
                sources[u] = f

    # Step 2: group layers into collections per event.
    tasks = []
    for eid in sorted(want):
        ev = events[eid]
        groups = defaultdict(list)
        lic_of = {}
        for p in ev["packages"]:
            for s in p["sources"]:
                c = sources.get(s["primary"]["url"])
                if not c:
                    continue
                key = local_path(work, c["url"]).parent.name
                meta = json.load(open(work / "conv" / key / "layers.json"))
                for L in meta["layers"]:
                    if L["status"] != "ok":
                        continue
                    lic = p["license"]["spdx"]
                    crs = "EPSG:4326" if L["wgs84_horizontal"] else (L["crs"] or "unknown")
                    gk = (L["family"], lic, crs)
                    part = {"key": key, "parquet": L["parquet"], "layer": L["layer"], "source_file": meta["file"],
                            "source_url": c["url"], "wgs84_horizontal": L["wgs84_horizontal"],
                            "features": L["features"], "fields": L["fields"], "domains": L["domains"],
                            "hdx_dataset": p["name"]}
                    # A zip shared by several datasets of the event is merged once.
                    if not any(q["key"] == key and q["parquet"] == L["parquet"] for q in groups[gk]):
                        groups[gk].append(part)
                    else:
                        for q in groups[gk]:
                            if q["key"] == key and q["parquet"] == L["parquet"]:
                                q.setdefault("also_hdx", []).append(p["name"])
                    lic_of[gk] = p["license"]
        fams = defaultdict(list)
        for gk in groups:
            fams[gk[0]].append(gk)
        for fam, gks in fams.items():
            for gk in sorted(gks):
                suffix = ""
                if len(gks) > 1:
                    lic_n = len({g[1] for g in gks}) > 1
                    crs_n = len({g[2] for g in gks}) > 1
                    suffix = (f"-{slug(gk[1]).lower()}" if lic_n else "") + (f"-{slug(gk[2]).lower()}" if crs_n else "")
                cid = f"{eid}-{fam}{suffix}"
                dest = event_dir(ev, n_by_h) / cid / f"{cid}.parquet"
                info = {"collection": cid, "event": eid, "event_code": ev["code"], "hazard": ev["hazard"],
                        "year": ev["year"], "family": fam, "license": lic_of[gk], "crs": gk[2],
                        "path": str(dest.parent.relative_to(CATALOG)), "parts": groups[gk],
                        "hdx_datasets": sorted({p["name"] for p in ev["packages"]})}
                tasks.append((cid, groups[gk], dest, info))
    # Drop the records of the rebuilt events first, so a collection that no
    # longer exists upstream does not survive as a stale record.
    for f in (ROOT / "manifest" / "collections").glob("*.json"):
        if json.load(open(f)).get("event") in want:
            f.unlink()
    print(f"step 2: {len(tasks)} collections", file=sys.stderr)
    with ProcessPoolExecutor(a.jobs) as ex:
        futs = [ex.submit(stage_collection, work, *t) for t in tasks]
        for f in as_completed(futs):
            cid, msg = f.result()
            print(f"  {cid}: {msg}", file=sys.stderr, flush=True)


if __name__ == "__main__":
    main()

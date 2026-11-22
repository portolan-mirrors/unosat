#!/usr/bin/env python3
"""Build the cross-event collections catalog/combined/{damage-sites,water-extent}.

Each one stacks every per-event collection of that family whose license allows
redistribution of a combined work (CC BY-SA, CC BY 4.0, CC BY 3.0 IGO); the
CC BY-NC-SA 3.0 collections are left out. Every row keeps its own `license`.

The per-event schemas differ, so only a few harmonized columns are carried:

- damage_class / water_class: the `<field>_label` column decoded from the
  source geodatabase domain when there is one; else the raw text when the raw
  column holds text labels. A numeric code with no domain stays null in the
  class column; its raw value is always in damage_class_code / water_class_code.
- Wide multi-epoch layers (Gaza and similar: Main_Damage_Site_Class_2 ... _N)
  give one row per site. The row takes the highest-numbered epoch whose class
  code is not null, and its date, sensor, and confidence; `assessment_epoch`
  records which (1 = the unnumbered columns; null for single-epoch layers).
- geometry is 2D EPSG:4326; collections in another CRS are reprojected.

    python3 tools/combine.py [--only damage-sites|water-extent]
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from stage import duck, nrows, q, run  # noqa: E402
from meta import CONTACT, HOST, PRODUCER, write  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog"
WORK = Path(os.environ.get("WORK", "/scratch/unosat/work"))
OPEN = {"CC-BY-SA", "CC-BY-4.0", "CC-BY-IGO-3.0"}

SPEC = {
    "damage-sites": {
        "class": "damage_class",
        "raw": ["Main_Damage_Site_Class", "Main_Damag", "Main_Dmg", "Damage_Cla", "Dam_Site"],
        "epoch_base": "Main_Damage_Site_Class",
    },
    "water-extent": {
        "class": "water_class",
        "raw": ["Water_Class", "Water_Clas", "WaterClass", "Water_Cl"],
        "epoch_base": None,
    },
}
DATE = ["SensorDate", "Sensor_Date", "Sensor_Dat", "SensorDa_1"]
SENSOR = ["SensorID", "Sensor_ID"]
CONF = ["ConfidenceID", "Confidence_ID", "Confidence"]
NUMERIC_TEXT = r"^\s*-?\d+(\.\d+)?\s*$"


def textual(col, types):
    """A text label from `col`: the decoded twin if any, else non-numeric text."""
    if f"{col}_label" in types:
        return f'"{col}_label"'
    if col in types and types[col].startswith("VARCHAR"):
        return f"""CASE WHEN regexp_matches("{col}", '{NUMERIC_TEXT}') OR trim("{col}") = '' THEN NULL ELSE trim("{col}") END"""
    return None


def first(cols, types, fn):
    for c in cols:
        if c in types:
            e = fn(c, types)
            if e:
                return e, c
    return None, None


def as_date(col):
    return (f"""COALESCE(TRY_CAST("{col}" AS DATE), TRY_CAST(TRY_STRPTIME(CAST("{col}" AS VARCHAR), '%Y/%m/%d') AS DATE),"""
            f""" TRY_CAST(TRY_STRPTIME(CAST("{col}" AS VARCHAR), '%d/%m/%Y') AS DATE))""")


def select_for(rec, fam):
    spec = SPEC[fam]
    path = CATALOG / rec["path"] / f"{rec['collection']}.parquet"
    types = {r[0]: r[1] for r in duck(f"SELECT column_name, column_type FROM (DESCRIBE SELECT * FROM read_parquet({q(path)}))")}
    geom = "ST_Force2D(geometry::GEOMETRY)"
    if rec["crs"] != "EPSG:4326":
        geom = f"ST_Force2D(ST_Transform(geometry::GEOMETRY, {q(rec['crs'])}, 'EPSG:4326', always_xy := true))"

    raw_e, raw_c = first(spec["raw"], types, lambda c, t: f'"{c}"')
    cls = textual(raw_c, types) if raw_c else None
    code = f"CAST({raw_e} AS VARCHAR)" if raw_e else "NULL"
    date_e = next((as_date(c) for c in DATE if c in types), "NULL")
    sens = next((e for c in SENSOR if (e := textual(c, types))), "NULL")
    conf = next((e for c in CONF if (e := textual(c, types))), "NULL")
    epoch = "NULL"

    base = spec["epoch_base"]
    epochs = sorted((int(m.group(1)) for c in types if base and (m := re.fullmatch(rf"{base}_(\d+)", c))), reverse=True)
    if epochs:
        def pick(make, fallback):
            arms = []
            for n in epochs:
                v = make(n)
                arms.append(f'WHEN "{base}_{n}" IS NOT NULL THEN {v if v else "NULL"}')
            return f"CASE {' '.join(arms)} ELSE {fallback} END"
        cls = pick(lambda n: textual(f"{base}_{n}", types), cls or "NULL")
        code = pick(lambda n: f'CAST("{base}_{n}" AS VARCHAR)', code)
        date_e = pick(lambda n: as_date(f"SensorDate_{n}") if f"SensorDate_{n}" in types else None, date_e)
        sens = pick(lambda n: textual(f"SensorID_{n}", types) if f"SensorID_{n}" in types else None, sens)
        conf = pick(lambda n: textual(f"ConfidenceID_{n}", types) if f"ConfidenceID_{n}" in types else None, conf)
        epoch = pick(lambda n: str(n), "1")

    ev_code = q(rec["event_code"]) if rec.get("event_code") else "NULL"
    sql = (f"SELECT {q(rec['event'])} AS event, CAST({ev_code} AS VARCHAR) AS event_code, "
           f"{q(rec['collection'])} AS collection, source_layer, source_file, {q(rec['license']['spdx'])} AS license, "
           f"CAST({cls or 'NULL'} AS VARCHAR) AS {spec['class']}, CAST({code} AS VARCHAR) AS {spec['class']}_code, "
           f"CAST({date_e} AS DATE) AS sensor_date, CAST({sens} AS VARCHAR) AS sensor, "
           f"CAST({conf} AS VARCHAR) AS confidence, CAST({epoch} AS INTEGER) AS assessment_epoch, "
           f"{geom} AS geometry FROM read_parquet({q(path)})")
    return sql, nrows(path), {"class_from": raw_c, "epochs": len(epochs) + (1 if epochs else 0)}


def build(fam):
    t0 = time.time()
    recs = [json.load(open(f)) for f in sorted((ROOT / "manifest" / "collections").glob("*.json"))]
    recs = [r for r in recs if r.get("status") == "ok" and r["family"] == fam]
    used = [r for r in recs if r["license"]["spdx"] in OPEN]
    left = [r for r in recs if r["license"]["spdx"] not in OPEN]
    parts, expected, notes = [], 0, {}
    for r in used:
        s, n, info = select_for(r, fam)
        parts.append(s)
        expected += n
        notes[r["collection"]] = info
    out_dir = CATALOG / "combined" / fam
    out_dir.mkdir(parents=True, exist_ok=True)
    tmp = WORK / "merge" / f"combined-{fam}.parquet"
    tmp2 = tmp.with_suffix(".gpio.parquet")
    tmp.parent.mkdir(parents=True, exist_ok=True)
    sqlfile = WORK / "merge" / f"combined-{fam}.sql"
    sqlfile.write_text("LOAD spatial;\nSET preserve_insertion_order = false;\n"
                       f"COPY ({' UNION ALL '.join(parts)}) TO {q(tmp)} (FORMAT parquet);\n")
    r = subprocess.run(["duckdb", "-no-agent"], stdin=open(sqlfile), capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f"duckdb failed: {r.stderr[-800:]}")
    dest = out_dir / f"{fam}.parquet"
    for _ in range(5):  # gpio segfaults intermittently; see stage.py
        r = run(["gpio", "convert", "geoparquet", str(tmp), str(tmp2), "--geoparquet-version", "2.0", "--no-repair-geometry"])
        if r.returncode >= 0:
            break
    if r.returncode or not tmp2.exists():
        raise SystemExit(f"gpio convert failed: {(r.stderr or r.stdout)[-500:]}")
    for _ in range(5):
        r = run(["gpio", "add", "bbox", str(tmp2), str(dest)])
        if r.returncode >= 0:
            break
    if r.returncode or not dest.exists():
        raise SystemExit(f"gpio add bbox failed: {(r.stderr or r.stdout)[-500:]}")
    tmp.unlink(missing_ok=True)
    tmp2.unlink(missing_ok=True)
    n = nrows(dest)
    if n != expected:
        raise SystemExit(f"{fam}: {n} rows != {expected} input rows")
    cls = SPEC[fam]["class"]
    dist = duck(f"SELECT {cls}, count(*) FROM read_parquet({q(dest)}) GROUP BY 1 ORDER BY 2 DESC LIMIT 25")
    lic = duck(f"SELECT license, count(*) FROM read_parquet({q(dest)}) GROUP BY 1 ORDER BY 2 DESC")
    write_meta(fam, used, left, notes)
    return {"family": fam, "collections": len(used), "excluded_nc": len(left), "rows": n,
            "mb": round(dest.stat().st_size / 1e6, 1), "seconds": round(time.time() - t0, 1),
            "class_distribution": dist, "license_rows": lic,
            "class_null_collections": sorted(c for c, i in notes.items() if not i["class_from"]),
            "wide_collections": sorted(c for c, i in notes.items() if i["epochs"])}


def write_meta(fam, used, left, notes):
    cls = SPEC[fam]["class"]
    label = {"damage-sites": "Damage sites", "water-extent": "Water extent"}[fam]
    what = {"damage-sites": "damage-site points (one point per assessed structure or site)",
            "water-extent": "satellite-detected water polygons"}[fam]
    write(CATALOG / "combined" / fam, {
        "title": f"{label}, all events",
        "description": (
            f"UNOSAT {what} from {len(used)} per-event collections, in one GeoParquet file with a shared set of "
            f"columns: `event`, `event_code`, `collection`, `source_layer`, `source_file`, `license`, `{cls}`, "
            f"`{cls}_code`, `sensor_date`, `sensor`, `confidence`, `assessment_epoch`, and 2D EPSG:4326 geometry. "
            f"Rows carry their own `license` column. Included: CC BY-SA (as HDX states it, no version), CC BY 4.0, "
            f"and CC BY 3.0 IGO. The {len(left)} collections under CC BY-NC-SA 3.0 are left out; they are in their "
            f"event subcatalogs. For every source column, use the per-event collection named in `collection`. "
            f"Read [AGENTS.md](AGENTS.md) for the columns and query recipes."),
        "contact": CONTACT,
        "license": "other",
        "license_url": "https://data.humdata.org/organization/unosat",
        "providers": [PRODUCER, HOST],
        "attribution": "UNITAR-UNOSAT",
        "source_url": "https://data.humdata.org/organization/unosat",
        "processing_notes": (
            f"Built by tools/combine.py from the per-event GeoParquet collections, with DuckDB (UNION ALL) and "
            f"geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column). `{cls}` is the label decoded from the "
            f"source geodatabase domain where one exists, else the raw text when the source column holds text "
            f"labels. `{cls}_code` is the raw value as text. Collections in EPSG:3857 or UTM were reprojected to "
            f"EPSG:4326; Z values were dropped. Wide multi-epoch layers (one row per site, with columns "
            f"`Main_Damage_Site_Class_2` to `_N`) take the highest-numbered epoch whose class is not null, and that "
            f"epoch's date, sensor, and confidence; `assessment_epoch` records it (1 = the unnumbered columns). "
            f"The row count equals the sum of the input collections."),
        "known_issues": (
            f"Class labels are not normalized across events: UNOSAT's domains and text exports spell the same class "
            f"in different ways (for example, Destroyed and Completely Destroyed), and some domains number classes "
            f"differently. `{cls}` is null where the source holds a numeric code with no domain to decode it "
            f"(shapefile exports). A row's `license` is the license of its HDX dataset; a combined work under mixed "
            f"licenses must meet each one, including share-alike for CC BY-SA rows."),
        "keywords": ["UNOSAT", "damage assessment" if fam == "damage-sites" else "floods", "humanitarian"],
    }, f"Combined collection {fam}")
    write(CATALOG / "combined", {
        "title": "Combined, all events",
        "description": (
            "Cross-event collections: damage sites and water extents from every event whose license allows a "
            "combined copy, with one shared set of columns. Per-row licenses are in the `license` column. "
            "Read [AGENTS.md](AGENTS.md) for how they were built."),
    }, "Subcatalog: combined")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", choices=list(SPEC))
    a = ap.parse_args()
    for fam in [a.only] if a.only else list(SPEC):
        print(json.dumps(build(fam), indent=1, default=str))


if __name__ == "__main__":
    main()

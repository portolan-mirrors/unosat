#!/usr/bin/env python3
"""Write styles/default.json (MapLibre) for each collection.

The colouring column is chosen per family from the columns the collection
actually has, preferring the decoded "<field>_label" columns. Match branches
are emitted only for values present in the data (up to 8, most frequent
first); other values get the fallback colour. The data browser builds a legend
only from a fill layer with a match expression, so polygon styles get one and
point styles do not.

    WORK=... python3 tools/styles.py [--only id1,id2]
"""

import argparse
import json
import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CANDIDATES = {
    "water": ["Water_Class_label", "Water_Clas", "Water_Class", "WaterClass", "Water_Cl"],
    "damage": ["Main_Damage_Site_Class_label", "Main_Damag", "Main_Dmg", "Damage_Cla", "Main_Damage_Site_Class",
               "Grouped_Damage_Classes_label", "Dam_Site"],
    "shelter": ["CampStatus", "CampType", "Shelter_St"],
}
FAMILY_KIND = {"water-extent": "water", "damage-sites": "damage", "damage-areas": "damage",
               "damage-lines": "damage", "affected-structures": "damage", "shelters": "shelter",
               "shelter-areas": "shelter"}
# Colours for labels that UNOSAT's own domains define. Anything else cycles
# through PALETTE.
KNOWN = {
    "Destroyed": "#7f0000", "Completely Destroyed": "#7f0000", "Severe Damage": "#d7301f",
    "Severely Damaged": "#d7301f", "Highly Damaged": "#d7301f", "Moderate Damage": "#fc8d59",
    "Moderately Damaged": "#fc8d59", "Possible Damage": "#fdcc8a", "Damaged": "#ef6548",
    "No Visible Damage": "#969696", "Flood Water": "#08519c", "Flood water": "#08519c",
    "Preflood Water": "#9ecae1", "Pre-flood water": "#9ecae1", "Satellite Detected Water": "#3182bd",
    "Flood-Affected Land / Possible Flood water": "#6baed6", "Maximum Flood Water Extent (Cumulative)": "#2171b5",
}
PALETTE = ["#1b9e77", "#d95f02", "#7570b3", "#e7298a", "#66a61e", "#e6ab02", "#a6761d", "#666666"]
BASE = {"water-extent": "#2171b5", "analysis-extent": "#e6550d", "damage-sites": "#d7301f",
        "damage-areas": "#d7301f", "affected-structures": "#ae017e", "shelters": "#238b45",
        "shelter-areas": "#238b45", "landslides": "#8c510a"}


def duck(sql):
    r = subprocess.run(["duckdb", "-no-agent", "-json"], input=sql + ";\n", capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(r.stderr[-300:])
    return json.loads(r.stdout) if r.stdout.strip() else []


def choose(parquet, family):
    cols = [c["column_name"] for c in duck(f"DESCRIBE SELECT * FROM read_parquet('{parquet}')")]
    for c in CANDIDATES.get(FAMILY_KIND.get(family, ""), []):
        if c not in cols:
            continue
        rows = duck(f"""SELECT "{c}"::VARCHAR v, count(*) n FROM read_parquet('{parquet}')
                        WHERE "{c}" IS NOT NULL AND trim("{c}"::VARCHAR) <> '' GROUP BY 1 ORDER BY 2 DESC""")
        if rows and len(rows) <= 40:
            return c, rows
    return None, []


def style(info):
    cid, fam = info["collection"], info["family"]
    coll = ROOT / "catalog" / info["path"]
    parquet = coll / f"{cid}.parquet"
    col, rows = choose(parquet, fam)
    geom = "points" if fam in ("damage-sites", "affected-structures", "shelters") or fam.endswith("-points") else \
        "lines" if fam.endswith("-lines") else "mixed" if fam.endswith("-mixed") else "polygons"
    base = BASE.get(fam, "#555555")
    color = base
    shown = []
    if col:
        shown = rows[:8]
        expr = ["match", ["to-string", ["get", col]]]
        used = 0
        for r in shown:
            c = KNOWN.get(r["v"])
            if not c:
                c = PALETTE[used % len(PALETTE)]
                used += 1
            expr += [r["v"], c]
        color = expr + ["#bdbdbd"]
    src = {"type": "vector", "url": f"pmtiles://../{cid}.pmtiles"}
    layer = {"source": "data", "source-layer": fam}
    if geom == "polygons":
        opacity = 0.12 if fam == "analysis-extent" else 0.7
        # An analysis extent is a frame around the other layers: a light fill
        # and a strong outline, so it reads at card size and on the map.
        ext = fam == "analysis-extent"
        layers = [{**layer, "id": f"{fam}-fill", "type": "fill", "paint": {"fill-color": color, "fill-opacity": opacity}},
                  {**layer, "id": f"{fam}-outline", "type": "line",
                   "paint": {"line-color": base if (ext or not col) else "#333333",
                             "line-width": 2 if ext else 0.5, "line-opacity": 0.9 if ext else 0.6}}]
    elif geom == "points":
        layers = [{**layer, "id": f"{fam}-points", "type": "circle",
                   "paint": {"circle-color": color, "circle-radius": ["interpolate", ["linear"], ["zoom"], 4, 3, 10, 4, 14, 5.5, 16, 7],
                             "circle-stroke-color": "#333333", "circle-stroke-width": 0.6}}]
    elif geom == "mixed":
        # One layer per geometry type, so points and polygons both draw.
        def gt(*t):
            return ["in", ["geometry-type"], ["literal", list(t)]]
        layers = [{**layer, "id": f"{fam}-fill", "type": "fill", "filter": gt("Polygon", "MultiPolygon"),
                   "paint": {"fill-color": color, "fill-opacity": 0.6}},
                  {**layer, "id": f"{fam}-lines", "type": "line", "filter": gt("LineString", "MultiLineString", "Polygon", "MultiPolygon"),
                   "paint": {"line-color": color, "line-width": 1.5}},
                  {**layer, "id": f"{fam}-points", "type": "circle", "filter": gt("Point", "MultiPoint"),
                   "paint": {"circle-color": color, "circle-radius": ["interpolate", ["linear"], ["zoom"], 4, 2, 12, 4, 16, 7],
                             "circle-stroke-color": "#ffffff", "circle-stroke-width": 0.5}}]
    else:
        layers = [{**layer, "id": f"{fam}-lines", "type": "line", "paint": {"line-color": color, "line-width": 2.5}}]
    name = f"{fam.replace('-', ' ').capitalize()}" + (f" by {col.removesuffix('_label')}" if col else "")
    doc = {"version": 8, "name": name, "sources": {"data": src}, "layers": layers}
    (coll / "styles").mkdir(exist_ok=True)
    (coll / "styles" / "default.json").write_text(json.dumps(doc, indent=2) + "\n")
    return {"collection": cid, "style_column": col, "legend": geom == "polygons" and bool(col),
            "values": shown, "other_values": max(0, len(rows) - len(shown))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only")
    a = ap.parse_args()
    work = Path(os.environ["WORK"])
    infos = [json.load(open(f)) for f in sorted((ROOT / "manifest" / "collections").glob("*.json"))]
    infos = [i for i in infos if i.get("status") == "ok" and (not a.only or i["collection"] in a.only.split(","))]
    report = [style(i) for i in infos]
    (work / "styles.json").write_text(json.dumps(report, indent=1))
    print(f"{len(report)} styles, {sum(r['legend'] for r in report)} with a legend, "
          f"{sum(1 for r in report if r['style_column'])} coloured by a column")


if __name__ == "__main__":
    main()

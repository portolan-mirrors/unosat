#!/usr/bin/env python3
"""Write AGENTS.md for every collection and event from the staging records.

Each query in these files names the published URL and is run by
tests/test_queries.py, so a recipe that stops working fails CI. Counts are
never written as numbers; the file gives the query that computes them.

    python3 tools/agents.py
"""

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog"
PUBLIC = "https://data.source.coop/portolan-mirrors/unosat"
BROWSE = "https://source.coop/portolan-mirrors/unosat"


def collection_md(c, cols):
    cid = c["collection"]
    url = f"{PUBLIC}/{c['path']}/{cid}.parquet"
    labels = [x for x in cols if x.endswith("_label")]
    crs = c["crs"]
    crs_text = ("EPSG:4326 (longitude, latitude). Source layers in \"WGS 84 + EGM96 height\" are 2D, so the "
                "vertical part was dropped." if crs == "EPSG:4326" else
                f"{crs}, the CRS of the source layers. Reproject before you join it with EPSG:4326 data, "
                f"for example `ST_Transform(geometry, '{crs}', 'EPSG:4326', always_xy := true)`.")
    lines = [
        f"# {cid}: agent guide",
        "",
        f"One GeoParquet file: `{url}`.",
        "",
        "- Each row is one feature of a UNOSAT source layer. `source_layer` and `source_file` name the layer "
        "and the HDX file it came from. One event often has several layers of the same kind (for example, one "
        "per satellite image date), so filter on `source_layer` before you count or map.",
        f"- CRS: {crs_text}",
        "- Geometry is as published, not repaired. Use `ST_MakeValid` before overlay operations.",
        "- A column a source layer did not have is null for that layer's rows.",
    ]
    if labels:
        lines.append(f"- Coded columns have a decoded twin: {', '.join(f'`{x}`' for x in labels)}. Read the "
                     "`_label` column; the code lists differ between source files.")
    lines += [
        "",
        "## Rows per source layer",
        "",
        "```sql",
        "INSTALL spatial; LOAD spatial;",
        "SELECT source_layer, count(*) AS features",
        f"FROM read_parquet('{url}')",
        "GROUP BY source_layer ORDER BY source_layer;",
        "```",
    ]
    if labels:
        lab = labels[0]
        lines += [
            "",
            f"## Features by `{lab}`",
            "",
            "```sql",
            f"SELECT source_layer, {lab}, count(*) AS features",
            f"FROM read_parquet('{url}')",
            "GROUP BY ALL ORDER BY source_layer, features DESC;",
            "```",
        ]
    lines += [
        "",
        "## Load in Python",
        "",
        "```python",
        "import geopandas as gpd",
        f"gdf = gpd.read_parquet('{url}')",
        "```",
        "",
        f"The [data browser]({BROWSE}) shows the map, schema, and license. "
        "The event's other collections are siblings in the parent catalog.",
        "",
    ]
    return "\n".join(lines)


def main():
    recs = [json.load(open(f)) for f in sorted((ROOT / "manifest" / "collections").glob("*.json"))]
    recs = [r for r in recs if r.get("status") == "ok"]
    by_event = defaultdict(list)
    for r in recs:
        cj = CATALOG / r["path"] / "collection.json"
        if not cj.exists():
            continue
        cols = [x["name"] for x in json.load(open(cj)).get("table:columns", [])]
        (CATALOG / r["path"] / "AGENTS.md").write_text(collection_md(r, cols))
        by_event[Path(r["path"]).parent].append(r)
    for edir, rs in by_event.items():
        lines = [f"# {edir.name}: agent guide", "",
                 "One UNOSAT event. Each child collection merges the source layers of one kind:", ""]
        for r in sorted(rs, key=lambda r: r["collection"]):
            lines.append(f"- [`{r['collection']}`]({r['collection']}/AGENTS.md): {r['family']}, "
                         f"{len(r['parts'])} source layer{'s' if len(r['parts']) > 1 else ''}, {r['crs']}, "
                         f"license {r['license']['title']}")
        lines += ["", "Each collection's own AGENTS.md has the URL and query recipes.", ""]
        (CATALOG / edir / "AGENTS.md").write_text("\n".join(lines))
    # The combined collections have no staging record; their guides are fixed text.
    for fam, cls in (("damage-sites", "damage_class"), ("water-extent", "water_class")):
        d = CATALOG / "combined" / fam
        if not (d / "collection.json").exists():
            continue
        url = f"{PUBLIC}/combined/{fam}/{fam}.parquet"
        text = [f"# combined/{fam}: agent guide", "",
                f"One GeoParquet file: `{url}`. It joins the {fam} collections of every event under CC BY-SA, "
                "CC BY, or CC BY-IGO. CC BY-NC-SA 3.0 collections are left out.", "",
                "- `event` is the event subcatalog id, `collection` the source collection, and `source_layer` and "
                "`source_file` the original layer and HDX file.",
                f"- `{cls}` is the decoded class label; `{cls}_code` is the raw value as text. Labels are not "
                f"normalized across events, so group on `{cls}` per event.",
                "- `license` is the license of the row's HDX dataset.",
                "- `assessment_epoch` says which epoch of a wide multi-epoch layer the row took; null for ordinary layers.",
                "- Geometry is EPSG:4326, 2D, and not repaired.", "",
                "## Rows by event and class", "", "```sql", "INSTALL spatial; LOAD spatial;",
                f"SELECT event, {cls}, count(*) AS features", f"FROM read_parquet('{url}')",
                "GROUP BY ALL ORDER BY event, features DESC LIMIT 50;", "```", ""]
        (d / "AGENTS.md").write_text("\n".join(text))

    if (CATALOG / "combined" / "catalog.json").exists():
        (CATALOG / "combined" / "AGENTS.md").write_text("\n".join([
            "# combined: agent guide", "",
            "Two collections that join every event's damage sites and water extents into one file each, with",
            "harmonized class columns. Use them for questions across events; use the event collections for the",
            "full source columns. The [root agent guide](../AGENTS.md) explains the layout.", "",
            "- [`damage-sites`](damage-sites/AGENTS.md)", "- [`water-extent`](water-extent/AGENTS.md)", ""]))

    # Hazard and year subcatalogs: point to their children.
    n = 0
    for d in sorted({e.parent for e in by_event} | {e.parent.parent for e in by_event}):
        if d == Path(".") or d.parent == d or not (CATALOG / d / "catalog.json").exists() or d in by_event:
            continue
        kids = sorted(x.name for x in (CATALOG / d).iterdir() if (x / "catalog.json").exists())
        lines = [f"# {d.as_posix()}: agent guide", "",
                 "Each child below is " + ("a year of events." if all(k.isdigit() for k in kids) else "one UNOSAT event.")
                 + " The [root agent guide](" + "../" * len(d.parts) + "AGENTS.md) explains the layout.", ""]
        lines += [f"- [`{k}`]({k}/AGENTS.md)" for k in kids] + [""]
        (CATALOG / d / "AGENTS.md").write_text("\n".join(lines))
        n += 1
    print(f"{len(recs)} collection guides, {len(by_event)} event guides, {n} hazard/year guides")


if __name__ == "__main__":
    main()

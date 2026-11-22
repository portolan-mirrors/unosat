#!/usr/bin/env python3
"""Write .portolan/metadata.yaml for the root, hazard, year, event, and collection levels.

Every sentence is either copied from HDX (titles, notes, caveats, licenses) or
built from the staging records in $WORK/colls (layer names, row counts,
source files). Nothing is invented: a family's description says only how the
layers were grouped, and the source layer names are listed so a reader can
check the grouping.

    WORK=... python3 tools/meta.py
"""

import json
import re
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog"
HOST = {"name": "Portolan Mirrors", "roles": ["host"], "url": "https://source.coop/portolan-mirrors/unosat",
        "description": "Maintains this Portolan mirror: the GeoParquet and PMTiles copies, STAC metadata, and documentation."}
PRODUCER = {"name": "United Nations Satellite Centre (UNOSAT), UNITAR", "roles": ["producer", "licensor"],
            "url": "https://unosat.org",
            "description": "Produced the satellite-derived geodata and published it on the Humanitarian Data Exchange."}
CONTACT = {"name": "Portolan Mirrors", "email": "nissim@radiant.earth"}

HAZARD = {
    "floods": ("Floods", "Flood"), "tropical-cyclones": ("Tropical cyclones", "Tropical cyclone"),
    "earthquakes": ("Earthquakes", "Earthquake"), "complex-emergencies": ("Complex emergencies", "Complex emergency"),
    "landslides": ("Landslides", "Landslide"), "fires": ("Fires", "Fire"), "volcanoes": ("Volcanoes", "Volcano"),
    "other-events": ("Other events", "Event"), "no-event-code": ("Datasets without an event code", "Dataset"),
}
FAMILY = {
    "analysis-extent": ("Analysis extent", "Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint)."),
    "damage-sites": ("Damage sites", "Point layers with a damage class column (such as `Main_Damage_Site_Class`): one point per assessed structure or site."),
    "damage-areas": ("Damage areas", "Polygon layers with a damage class column: damaged areas, zones, or density cells."),
    "damage-lines": ("Damaged lines", "Line layers with a damage class column, such as damaged roads or bridges."),
    "water-extent": ("Water extent", "Polygon layers with a water class column (such as `Water_Class`), or whose names mention flood, water, or inundation: satellite-detected water."),
    "shelters": ("Shelters", "Point layers with shelter or camp columns, or whose names mention camps, shelters, IDPs, or settlements."),
    "shelter-areas": ("Shelter areas", "Polygon layers with shelter or camp columns, or whose names mention camps, shelters, IDPs, or settlements."),
    "landslides": ("Landslides", "Polygon layers whose names mention landslides, mudflows, or debris."),
    "affected-structures": ("Affected structures", "Point layers whose names mention affected structures or buildings."),
}
LICENSE = {  # HDX license -> (metadata.yaml license, license_url)
    "CC-BY-SA": ("other", "https://opendefinition.org/licenses/cc-by-sa/"),
    "CC-BY-4.0": ("CC-BY-4.0", "https://creativecommons.org/licenses/by/4.0/"),
    "CC-BY-IGO-3.0": ("CC-BY-3.0-IGO", "https://creativecommons.org/licenses/by/3.0/igo/legalcode"),
    "CC-BY-NC-SA-3.0": ("CC-BY-NC-SA-3.0", "https://creativecommons.org/licenses/by-nc-sa/3.0/"),
}
URL = re.compile(r"(?<![(\[<])\bhttps?://[^\s)\]>]+")


def family_text(fam):
    if fam in FAMILY:
        return FAMILY[fam]
    base, _, g = fam.rpartition("-")
    label = (base.replace("-", " ").capitalize() if base and base != "other" else "Other") + f" {g}"
    return label, f"{g.capitalize()} layers that match none of the named groups. The source layer names below say what each holds."


def md(text):
    """HDX notes use bare URLs; the data browser renders only markdown links."""
    text = re.sub(r"\s+\n", "\n", text or "").strip()
    return URL.sub(lambda m: f"[{m.group(0).rstrip('.,;')}]({m.group(0).rstrip('.,;')})", text)


def ydump(d, ind=0):
    """Minimal YAML writer: strings are always JSON-quoted, so YAML parses them verbatim."""
    out = []
    pad = "  " * ind
    for k, v in d.items():
        if v is None or v == [] or v == "":
            continue
        if isinstance(v, dict):
            out.append(f"{pad}{k}:")
            out.append(ydump(v, ind + 1))
        elif isinstance(v, list):
            out.append(f"{pad}{k}:")
            for x in v:
                if isinstance(x, dict):
                    first = True
                    for kk, vv in x.items():
                        lead = f"{pad}  - " if first else f"{pad}    "
                        out.append(f"{lead}{kk}: {json.dumps(vv, ensure_ascii=False)}")
                        first = False
                else:
                    out.append(f"{pad}  - {json.dumps(x, ensure_ascii=False)}")
        else:
            out.append(f"{pad}{k}: {json.dumps(v, ensure_ascii=False)}")
    return "\n".join(out)


def write(dirpath, doc, header):
    p = dirpath / ".portolan" / "metadata.yaml"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(f"# {header}\n# Generated by tools/meta.py. Edit the generator, not this file.\n\n" + ydump(doc) + "\n")


def code_date(code):
    m = re.match(r"[A-Z]{2}(\d{4})(\d{2})(\d{2})", code or "")
    if m and int(m.group(1)) >= 2000:
        try:
            return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            return None
    return None


def hdx_range(pkgs):
    lo, hi = [], []
    for p in pkgs:
        m = re.match(r"\[(\d{4}-\d{2}-\d{2})T[^ ]* TO (\d{4}-\d{2}-\d{2})", p.get("dataset_date") or "")
        if m:
            lo.append(m.group(1))
            hi.append(m.group(2))
    return (min(lo), max(hi)) if lo else (None, None)


def event_title(ev, pkgs):
    if not ev["code"]:
        return pkgs[0]["title"].strip()
    _, single = HAZARD[ev["hazard"]]
    countries = sorted({c for p in pkgs for c in p["country_names"]})
    where = ", ".join(countries[:3]) + (f" and {len(countries) - 3} more" if len(countries) > 3 else "")
    d = code_date(ev["code"])
    when = d.strftime("%-d %B %Y") if d else str(ev["year"])
    return f"{single}, {where}, {when} ({ev['code']})" if where else f"{single}, {when} ({ev['code']})"


def hdx_links(names, by_name, limit=12):
    names = sorted(names, key=lambda n: by_name[n]["title"])
    lines = [f"- [{by_name[n]['title'].strip()}]({by_name[n]['hdx_url']})" for n in names[:limit]]
    if len(names) > limit:
        lines.append(f"- and {len(names) - limit} more; the event's [catalog page](../catalog.json) lists them all.")
    return "\n".join(lines)


def main():
    pkgs = json.load(open(ROOT / "manifest" / "packages.json"))
    by_name = {p["name"]: p for p in pkgs}
    events = defaultdict(list)
    for p in pkgs:
        events[p["collection"]].append(p)
    colls = [json.load(open(f)) for f in sorted((ROOT / "manifest" / "collections").glob("*.json"))]
    colls = [c for c in colls if c.get("status") == "ok"]
    by_event = defaultdict(list)
    for c in colls:
        by_event[c["event"]].append(c)
    today = date.today().isoformat()

    # Root.
    write(CATALOG, {
        "title": "UNOSAT Rapid Mapping Archive",
        "description": (
            "A mirror of the satellite-derived geodata that the United Nations Satellite Centre (UNOSAT) publishes on the "
            "[Humanitarian Data Exchange](https://data.humdata.org/organization/unosat): flood and water extents, damage "
            "assessments, shelter and camp mapping, landslides, and analysis extents for disasters and crises since 2010. "
            "Each event is a subcatalog, grouped by hazard and year. Inside an event, the source layers of one kind "
            "(for example, all damage-site point layers) are merged into one GeoParquet collection, with the source layer "
            "and file kept on every row. Licenses differ by dataset and are set on each collection. "
            "Read [AGENTS.md](AGENTS.md) before you query."),
        "contact": CONTACT,
        "license": "other",
        "license_url": "https://data.humdata.org/organization/unosat",
        "providers": [PRODUCER, HOST],
        "keywords": ["UNOSAT", "UNITAR", "rapid mapping", "satellite imagery analysis", "disasters", "humanitarian",
                     "floods", "damage assessment"],
        "attribution": "UNITAR-UNOSAT",
        "source_url": "https://data.humdata.org/organization/unosat",
    }, "Catalog root. Collections inherit these fields unless they set their own.")

    # Hazard and year subcatalogs.
    years = defaultdict(lambda: defaultdict(set))
    for c in colls:
        parts = Path(c["path"]).parts
        if len(parts) == 4:
            years[parts[0]][parts[1]].add(c["event"])
    for hz in sorted({Path(c["path"]).parts[0] for c in colls}):
        plural, single = HAZARD[hz]
        evs = {c["event"] for c in colls if Path(c["path"]).parts[0] == hz}
        by_year = "Events are grouped by year." if hz in years else ""
        write(CATALOG / hz, {
            "title": plural,
            "description": f"UNOSAT geodata for {len(evs)} {plural.lower() if hz != 'no-event-code' else 'datasets that carry no UNOSAT event code'}. "
                           f"Each child is one event, named by its UNOSAT event code. {by_year} "
                           f"Read [AGENTS.md](AGENTS.md) for how the archive is laid out.".replace("  ", " "),
        }, f"Hazard subcatalog: {hz}")
        for y, ys in years.get(hz, {}).items():
            write(CATALOG / hz / y, {
                "title": f"{plural}, {y}",
                "description": f"UNOSAT geodata for {len(ys)} {plural.lower()} whose event code dates from {y}. "
                               f"Read [AGENTS.md](AGENTS.md) for how the archive is laid out.",
            }, f"Year subcatalog: {hz}/{y}")

    # Events and collections.
    for eid, cs in sorted(by_event.items()):
        ev = {"code": cs[0]["event_code"], "hazard": cs[0]["hazard"], "year": cs[0]["year"]}
        ps = events[eid]
        title = event_title(ev, ps)
        edir = CATALOG / Path(cs[0]["path"]).parent
        main = max(ps, key=lambda p: len(p.get("notes") or ""))
        notes = md(main.get("notes"))
        if len(notes) > 1500:
            notes = notes[:1500].rsplit(" ", 1)[0] + " […]"
        write(edir, {
            "title": title,
            "description": (f"UNOSAT geodata for {title}, from {len(ps)} dataset{'s' if len(ps) > 1 else ''} on the "
                            f"Humanitarian Data Exchange. HDX describes the event:\n\n{notes}\n\n"
                            f"HDX datasets:\n\n{hdx_links([p['name'] for p in ps], by_name)}\n\n"
                            f"Read [AGENTS.md](AGENTS.md) for how the collections were built."),
        }, f"Event subcatalog: {eid}")
        for c in cs:
            fam_label, fam_desc = family_text(c["family"])
            names = sorted({p["hdx_dataset"] for p in c["parts"]} | {n for p in c["parts"] for n in p.get("also_hdx", [])})
            cps = [by_name[n] for n in names]
            lic, lic_url = LICENSE[c["license"]["spdx"]]
            rows = sum(p["features"] for p in c["parts"])
            layers = sorted({p["layer"] for p in c["parts"]})
            lo, hi = hdx_range(cps)
            crs_note = ("" if c["crs"] in ("EPSG:4326",) else
                        f" The geometry is in {c['crs']}, the CRS of the source layers; the PMTiles copy is in Web Mercator.")
            cdesc = (f"{fam_label} for {title}: {rows:,} features merged from {len(c['parts'])} source layer"
                     f"{'s' if len(c['parts']) > 1 else ''}. {fam_desc} The `source_layer` and `source_file` columns "
                     f"name the layer and file each row came from.{crs_note}\n\n"
                     f"From these HDX datasets:\n\n{hdx_links(names, by_name)}\n\n"
                     f"Read [AGENTS.md](AGENTS.md) for the columns and query recipes.")
            caveats = sorted({md(p.get("caveats")) for p in cps if p.get("caveats")})
            known = []
            if c["license"]["spdx"] == "CC-BY-SA":
                known.append("HDX states the license as \"Creative Commons Attribution Share-Alike (CC BY-SA)\" with no version, "
                             "so the collection's license is `other`, linked to the license definition HDX gives.")
            if c.get("merge_note"):
                known.append("When the layers were merged, " + c["merge_note"] + ".")
            known += caveats
            notes = (f"Downloaded from HDX on {today} and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry "
                     f"types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, "
                     f"no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, "
                     f"dropped, or reprojected. Each layer's row count was checked against the source feature count. "
                     f"Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. "
                     f"Coded geodatabase domains are decoded into `<field>_label` columns, per source file. "
                     f"Source layers: {', '.join(f'`{x}`' for x in layers[:40])}"
                     + (f" and {len(layers) - 40} more" if len(layers) > 40 else "") + ".")
            doc = {
                "title": f"{fam_label}: {title}",
                "description": cdesc,
                "license": lic,
                "license_url": lic_url,
                "providers": [PRODUCER, HOST],
                "attribution": "UNITAR-UNOSAT",
                "source_url": cps[0]["hdx_url"],
                "processing_notes": notes,
                "known_issues": " ".join(known),
                "keywords": sorted({t for p in cps for t in p.get("tags", [])} | {HAZARD[c["hazard"]][1].lower()}),
            }
            if lo:
                doc["defaults"] = {"temporal": {"start": lo, "end": hi}}
            write(CATALOG / c["path"], doc, f"Collection {c['collection']}")
    print(f"{len(by_event)} events, {len(colls)} collections")


if __name__ == "__main__":
    main()

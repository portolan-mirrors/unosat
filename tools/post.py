#!/usr/bin/env python3
"""Finish the STAC that `portolan add` wrote.

1. Column descriptions in each collection's table:columns. Coded values are
   described from the geodatabase domains of the collection's own source
   files; nothing is described from a guess. `portolan add` keeps a
   description on later runs.
2. Root links that `add` does not write: vcs, issues, and the absolute self
   link (PORTO-CORE-081).

    WORK=... python3 tools/post.py
"""

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog"
PUBLIC = "https://data.source.coop/portolan-mirrors/unosat"
REPO = "https://github.com/portolan-mirrors/unosat"

FIXED = {
    "source_layer": "Name of the layer in the source file that this row came from.",
    "source_file": "Name of the file downloaded from HDX that this row came from.",
    "geometry": "Feature geometry, as UNOSAT published it (not repaired).",
    "bbox": "Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering.",
}
# Names whose meaning the name itself states. Matched case-insensitively.
NAMED = [
    (r"^area_m2$", "Area in square metres, as UNOSAT computed it."),
    (r"^area_ha$", "Area in hectares, as UNOSAT computed it."),
    (r"^area_km2$", "Area in square kilometres, as UNOSAT computed it."),
    (r"^shape_(area|length|leng)$", "Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure."),
    (r"^(eventcode|event_code|eventcod)$", "UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog."),
    (r"^(notes?|comments?)$", "Free-text notes by the analyst."),
    (r"^(sensordate|sensor_date|sensor_dat|sensorda_1)$", "Acquisition date of the satellite image the feature was mapped from."),
    (r"^globalid$", "ArcGIS global identifier of the feature."),
]


def describe(name, domains, n_parts_with):
    if name in FIXED:
        return FIXED[name]
    if name.endswith("_label"):
        return f"`{name[:-6]}` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it."
    if name in domains:
        doms = domains[name]
        if len(doms) == 1:
            d = next(iter(doms))
            pairs = "; ".join(f"{k} = {v}" for k, v in sorted(dict(d).items(), key=lambda kv: (len(kv[0]), kv[0])))
            if len(pairs) > 900:
                pairs = pairs[:900].rsplit(";", 1)[0] + "; …"
            return f"Coded value. The source geodatabase domain gives: {pairs}. The decoded text is in `{name}_label`."
        return (f"Coded value. The {len(doms)} source files of this collection use {len(doms)} different domains for it, "
                f"so read `{name}_label`, which is decoded per source file.")
    for pat, text in NAMED:
        if re.match(pat, name, re.I):
            return text
    return None


HOSTING = "https://source.coop/portolan-mirrors/unosat"
BROWSER = "https://browser.portolan-sdi.org/#/external/"
OWNED = ("vcs", "issues", "about")


def browser_url(public_json):
    return BROWSER + public_json.removeprefix("https://")


def prune_children():
    """Drop child links whose target no longer exists (a collection removed
    because every geometry was empty)."""
    n = 0
    for f in CATALOG.rglob("catalog.json"):
        c = json.load(open(f))
        keep = [l for l in c["links"] if l["rel"] != "child" or (f.parent / l["href"]).resolve().exists()]
        if len(keep) != len(c["links"]):
            n += len(c["links"]) - len(keep)
            c["links"] = keep
            f.write_text(json.dumps(c, indent=2, ensure_ascii=False) + "\n")
    return n


def nav_links():
    """The four navigation links on every catalog and collection; see the
    portolan-bootstrap navigation contract. Links this step owns are replaced,
    all others kept."""
    n = 0
    for f in sorted(list(CATALOG.rglob("catalog.json")) + list(CATALOG.rglob("collection.json"))):
        rel = f.relative_to(CATALOG).as_posix()
        pub = f"{PUBLIC}/{rel}"
        c = json.load(open(f))
        links = [l for l in c["links"] if l["rel"] not in OWNED
                 and not (l["rel"] == "alternate" and l.get("href", "").startswith(BROWSER))
                 and not (l["rel"] == "self" and rel == "catalog.json")]
        if rel == "catalog.json":
            links.append({"rel": "self", "href": pub, "type": "application/json"})
        links += [
            {"rel": "alternate", "href": browser_url(pub), "type": "text/html", "title": "Open in data browser"},
            {"rel": "vcs", "href": REPO, "type": "text/html", "title": "Source repository"},
            {"rel": "issues", "href": f"{REPO}/issues", "type": "text/html", "title": "Report a problem"},
            {"rel": "about", "href": HOSTING, "type": "text/html", "title": "Hosting repository"},
        ]
        c["links"] = links
        f.write_text(json.dumps(c, indent=2, ensure_ascii=False) + "\n")
        n += 1
    return n


def readme_nav():
    """Add the navigation line under each README title (portolan readme does
    not write it). Run after `portolan readme`; idempotent."""
    mark = "<!-- nav -->"
    n = 0
    for readme in sorted(CATALOG.rglob("README.md")):
        d = readme.parent
        j = d / "collection.json" if (d / "collection.json").exists() else d / "catalog.json"
        if not j.exists():
            continue
        pub = f"{PUBLIC}/{j.relative_to(CATALOG).as_posix()}"
        line = (f"{mark}[Open in data browser]({browser_url(pub)}) · [Source repository]({REPO}) · "
                f"[Report a problem]({REPO}/issues) · [Hosting repository]({HOSTING})")
        lines = [l for l in readme.read_text().splitlines() if not l.startswith(mark)]
        i = next((k for k, l in enumerate(lines) if l.startswith("# ")), -1)
        lines[i + 1:i + 1] = ["", line] if i + 1 < len(lines) and lines[i + 1].strip() else [line]
        # portolan readme links a child by its collection id, which is the full
        # catalog path, so the relative link is wrong. Link the child's own
        # directory and its data browser page instead.
        rel_dir = d.relative_to(CATALOG).as_posix()
        for k, l in enumerate(lines):
            m = re.match(r"^### \[([^\]]+)\]\(([^)]*)\)\s*$", l)
            if m:
                child = m.group(1).rstrip("/").split("/")[-1]
                cj = d / child / ("collection.json" if (d / child / "collection.json").exists() else "catalog.json")
                if cj.exists():
                    cpub = f"{PUBLIC}/{(rel_dir + '/' if rel_dir != '.' else '')}{child}/{cj.name}"
                    lines[k] = f"### [{child}]({child}/README.md) · [data browser]({browser_url(cpub)})"
        text = "\n".join(lines)
        text = re.sub(r"\n{3,}", "\n\n", text) + "\n"
        readme.write_text(text)
        n += 1
    return n


def main():
    import sys
    if "--readme" in sys.argv:
        print(f"navigation line in {readme_nav()} READMEs")
        return
    n_desc = n_cols = 0
    for f in sorted((ROOT / "manifest" / "collections").glob("*.json")):
        info = json.load(open(f))
        if info.get("status") != "ok":
            continue
        cj = CATALOG / info["path"] / "collection.json"
        if not cj.exists():
            continue
        c = json.load(open(cj))
        domains = defaultdict(set)
        for p in info["parts"]:
            for fld, dom in p.get("domains", {}).items():
                if dom:
                    domains[fld].add(tuple(sorted(dom.items())))
        for col in c.get("table:columns", []):
            n_cols += 1
            if col.get("description"):
                n_desc += 1
                continue
            d = describe(col["name"], domains, None)
            if d:
                col["description"] = d
                n_desc += 1
        # portolan add does not apply defaults.temporal to a collection-level
        # asset, so set the HDX dataset dates here when the extent is open.
        iv = c["extent"]["temporal"]["interval"]
        y = (CATALOG / info["path"] / ".portolan" / "metadata.yaml").read_text()
        m1, m2 = re.search(r'start: "([\d-]+)"', y), re.search(r'end: "([\d-]+)"', y)
        if iv == [[None, None]] and m1 and m2:
            c["extent"]["temporal"]["interval"] = [[m1.group(1) + "T00:00:00Z", m2.group(1) + "T23:59:59Z"]]
        cj.write_text(json.dumps(c, indent=2, ensure_ascii=False) + "\n")

    n_pruned = prune_children()
    n_nav = nav_links()
    print(f"pruned {n_pruned} child links to missing collections")
    print(f"{n_desc}/{n_cols} columns described, navigation links on {n_nav} objects")


if __name__ == "__main__":
    main()

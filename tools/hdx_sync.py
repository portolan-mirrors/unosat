#!/usr/bin/env python3
"""Read the UNOSAT organization on HDX and write the source manifest.

The manifest is the single input of the build. It records, per HDX dataset,
the UNOSAT event it belongs to, its license, and the zip files the build
converts. With --diff it also prints the collections whose sources changed
since the committed manifest, which is what the scheduled refresh rebuilds.

    python3 tools/hdx_sync.py                 # rewrite manifest/packages.json
    python3 tools/hdx_sync.py --diff OLD.json # also print changed collection ids
"""

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://data.humdata.org/api/3/action/package_search"
UA = "portolan-mirrors-unosat/1.0 (+https://github.com/portolan-mirrors/unosat)"
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "manifest" / "packages.json"

# Excluded on purpose. The record's license_other reads "Humanitarian use
# only", which does not permit general redistribution.
EXCLUDE = {"ethiopia-flooding-somali-region"}

# UNOSAT event code: two-letter hazard prefix, the event date, ISO3 country.
CODE = re.compile(r"\b([A-Z]{2})(\d{8})([A-Z]{3})\b")
NOTES_CODE = re.compile(r"UNOSAT code:?\**\s*([A-Z]{2}\d{8}[A-Z]{3})")

# Folder names follow the HDX crisis tags UNOSAT applies to the same datasets.
HAZARD = {
    "FL": "floods",
    "TC": "tropical-cyclones",
    "EQ": "earthquakes",
    "CE": "complex-emergencies",
    "FR": "fires",
    "VO": "volcanoes",
    "LS": "landslides",
}

SPDX = {
    "cc-by-sa": "CC-BY-SA",  # HDX states no version; see make_stac.py
    "cc-by": "CC-BY-4.0",
    "cc-by-igo": "CC-BY-IGO-3.0",
}


def fetch_all():
    rows, start, out = 1000, 0, []
    while True:
        q = urllib.parse.urlencode(
            {"fq": "organization:unosat", "rows": rows, "start": start, "sort": "name asc"}
        )
        req = urllib.request.Request(f"{API}?{q}", headers={"User-Agent": UA})
        for attempt in range(5):
            try:
                with urllib.request.urlopen(req, timeout=120) as r:
                    res = json.load(r)["result"]
                break
            except Exception:
                if attempt == 4:
                    raise
                time.sleep(10 * (attempt + 1))
        out += res["results"]
        start += rows
        if start >= res["count"]:
            return out
        time.sleep(1)


def kind(res):
    """Return gdb, shp, or None for a resource, from its file name first."""
    name = (res.get("name") or "") + " " + (res.get("url") or "")
    low = name.lower()
    fmt = (res.get("format") or "").lower()
    if "gdb" in low or fmt == "geodatabase":
        return "gdb"
    if fmt == "shp" or "shp" in low:
        return "shp"
    if fmt == "geopackage":
        return "gpkg"
    if fmt in ("kmz", "kml"):
        return fmt
    if fmt == "xlsx" or low.rstrip().endswith(".xlsx"):
        return "xlsx"
    return None


def stem(res):
    """A key that pairs X_gdb.zip with X_SHP.zip so one of them is chosen."""
    n = Path(urllib.parse.urlparse(res.get("url") or "").path).name.lower()
    n = re.sub(r"\(\d+\)", "", n)
    n = re.sub(r"[ ._-]*(gdb|shp|shapefile|zip)+", "", n)
    return n.strip(" ._-")


def license_of(p):
    lid = p.get("license_id")
    if lid in SPDX:
        return {"spdx": SPDX[lid], "title": p.get("license_title"), "url": p.get("license_url")}
    other = (p.get("license_other") or "").strip()
    if "NonCommercial-ShareAlike 3.0" in other:
        return {
            "spdx": "CC-BY-NC-SA-3.0",
            "title": other,
            "url": "https://creativecommons.org/licenses/by-nc-sa/3.0/",
        }
    return {"spdx": "other", "title": other or p.get("license_title"), "url": p.get("license_url")}


def event_code(p):
    m = NOTES_CODE.search(p.get("notes") or "")
    if m:
        return m.group(1), "notes"
    codes = {CODE.search(r.get("url") or "").group(0) for r in p["resources"] if CODE.search(r.get("url") or "")}
    if len(codes) == 1:
        return codes.pop(), "resource"
    m = CODE.search((p.get("name") or "").upper())
    if m:
        return m.group(0), "name"
    return None, None


def year_of(p, code):
    # One code is mistyped upstream (EQ00231104NPL), so a code year before
    # UNOSAT existed falls through to the dataset date.
    if code and int(code[2:6]) >= 2000:
        return int(code[2:6])
    d = p.get("dataset_date") or ""
    m = re.search(r"(\d{4})", d)
    return int(m.group(1)) if m else int(p["metadata_created"][:4])


def summarize(p):
    code, code_src = event_code(p)
    by_stem = {}
    for r in p["resources"]:
        k = kind(r)
        if not k or not r.get("url"):
            continue
        # Only the gdb/shp/gpkg copies of one export are alternatives of each
        # other. KMZ and XLSX files are separate products and always kept.
        key = stem(r) if k in ("gdb", "shp", "gpkg") else f"{k}:{r['url']}"
        by_stem.setdefault(key, []).append((k, r))
    sources = []
    for _, group in sorted(by_stem.items()):
        # Prefer the geodatabase: it keeps full field names and the coded
        # value domains. Keep the shapefile as the fallback if the gdb fails.
        group.sort(key=lambda kr: {"gdb": 0, "gpkg": 1, "shp": 2}.get(kr[0], 3))
        alts = [
            {
                "kind": k,
                "url": r["url"].strip(),
                "name": r.get("name"),
                "size": r.get("size"),
                "hash": (r.get("hash") or "").strip('"') or None,
                "last_modified": r.get("last_modified"),
            }
            for k, r in group
        ]
        sources.append({"primary": alts[0], "fallbacks": alts[1:]})
    prefix = code[:2] if code else None
    return {
        "name": p["name"],
        "id": p["id"],
        "title": p["title"].strip(),
        "event_code": code,
        "event_code_from": code_src,
        "hazard": HAZARD.get(prefix, "other-events") if code else "no-event-code",
        "year": year_of(p, code),
        "collection": code.lower() if code else p["name"],
        "countries": sorted(g["name"] for g in p.get("groups", [])),
        "country_names": sorted(g.get("title") or g["name"] for g in p.get("groups", [])),
        "tags": sorted(t["name"] for t in p.get("tags", [])),
        "license": license_of(p),
        "dataset_date": p.get("dataset_date"),
        "metadata_created": p.get("metadata_created"),
        "metadata_modified": p.get("metadata_modified"),
        "hdx_url": f"https://data.humdata.org/dataset/{p['name']}",
        "notes": p.get("notes"),
        "caveats": p.get("caveats"),
        "sources": sources,
    }


def fingerprint(pkg):
    """What a rebuild depends on: the source files, and the metadata the
    STAC is written from (title, notes, caveats, license, dates)."""
    files = [(s["primary"]["url"], s["primary"]["size"], s["primary"]["hash"], s["primary"]["last_modified"])
             for s in pkg["sources"]]
    meta = [pkg.get(k) for k in ("title", "notes", "caveats", "dataset_date", "country_names")]
    return [files, meta, pkg["license"]["spdx"], pkg["collection"]]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--diff", type=Path, help="previous manifest; print changed collection ids")
    ap.add_argument("--from-dump", type=Path, help="use a saved package_search dump (testing)")
    a = ap.parse_args()
    raw = json.load(open(a.from_dump)) if a.from_dump else fetch_all()
    pkgs = [summarize(p) for p in raw if p["name"] not in EXCLUDE]
    pkgs.sort(key=lambda x: x["name"])
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(pkgs, indent=1, ensure_ascii=False) + "\n")
    print(f"{len(pkgs)} datasets, {len({p['collection'] for p in pkgs})} collections", file=sys.stderr)
    if a.diff:
        old = {p["name"]: p for p in json.load(open(a.diff))} if a.diff.exists() else {}
        changed = {p["collection"] for p in pkgs if p["name"] not in old or fingerprint(old[p["name"]]) != fingerprint(p)}
        # A dataset removed from HDX changes the event it belonged to.
        names = {p["name"] for p in pkgs}
        changed |= {o["collection"] for n, o in old.items() if n not in names}
        changed = sorted(changed)
        print("\n".join(changed))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Download the source files the manifest names into $WORK/dl.

Each URL lands in its own directory, dl/<key>/<file>, where <key> is a hash of
the URL, so a shared zip is fetched once. The primary copy is tried first; a
fallback copy is fetched only when the primary fails. Downloads are untrusted
data and are never executed.

    WORK=/scratch/unosat/work python3 tools/fetch.py [--collections a,b,...]
"""

import argparse
import hashlib
import json
import os
import subprocess
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = "portolan-mirrors-unosat/1.0 (+https://github.com/portolan-mirrors/unosat)"


def key(url):
    return hashlib.sha1(url.encode()).hexdigest()[:16]


def local_path(work, url):
    name = Path(urllib.parse.unquote(urllib.parse.urlparse(url).path)).name or "download"
    return Path(work) / "dl" / key(url) / name


def ok(work, src):
    p = local_path(work, src["url"])
    return p.exists() and (not src.get("size") or p.stat().st_size == src["size"])


def aria(work, srcs, tag):
    lst = Path(work) / f"aria-{tag}.txt"
    with open(lst, "w") as f:
        for s in srcs:
            p = local_path(work, s["url"])
            f.write(f"{s['url'].replace(' ', '%20')}\n  dir={p.parent}\n  out={p.name}\n")
    subprocess.run(
        ["aria2c", "-i", str(lst), "-j", "32", "-x", "4", "--continue=true", "--auto-file-renaming=false",
         "--allow-overwrite=true", "--max-tries=5", "--retry-wait=10", "--console-log-level=warn",
         "--summary-interval=0", f"--user-agent={UA}"],
        check=False,
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--collections", help="comma-separated collection ids (default: all)")
    a = ap.parse_args()
    work = os.environ["WORK"]
    pkgs = json.load(open(ROOT / "manifest" / "packages.json"))
    want = set(a.collections.split(",")) if a.collections else None
    sources = {}
    for p in pkgs:
        if want and p["collection"] not in want:
            continue
        for s in p["sources"]:
            sources[s["primary"]["url"]] = s
    todo = [s["primary"] for s in sources.values() if not ok(work, s["primary"])]
    print(f"{len(sources)} sources, {len(todo)} to fetch", file=sys.stderr)
    if todo:
        aria(work, todo, "primary")
    fb = []
    for s in sources.values():
        if not ok(work, s["primary"]):
            fb += [f for f in s["fallbacks"] if not ok(work, f)][:1]
    if fb:
        print(f"{len(fb)} primaries failed, trying fallbacks", file=sys.stderr)
        aria(work, fb, "fallback")
    status = {}
    for url, s in sources.items():
        got = next((x for x in [s["primary"], *s["fallbacks"]] if ok(work, x)), None)
        status[url] = {"used": got["url"] if got else None, "kind": got["kind"] if got else None,
                       "path": str(local_path(work, got["url"])) if got else None}
    out = Path(work) / "fetch_status.json"
    old = json.load(open(out)) if out.exists() else {}
    old.update(status)
    out.write_text(json.dumps(old, indent=1))
    missing = [u for u, v in status.items() if not v["used"]]
    print(f"missing after fallbacks: {len(missing)}", file=sys.stderr)
    for u in missing:
        print("  MISSING", u, file=sys.stderr)


if __name__ == "__main__":
    main()

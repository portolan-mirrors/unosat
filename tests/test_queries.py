#!/usr/bin/env python3
"""Run the SQL recipes in catalog/**/AGENTS.md against the published data.

A recipe fails when DuckDB exits non-zero or returns no rows. Mark a fence
that is meant to return nothing with an HTML comment `<!-- no-rows -->` on the
line before it.

The archive has about 1,400 guides, so the scheduled job runs all of them and
pull requests run a sample (--sample N) plus the guides they change (--only).

Needs the DuckDB CLI on PATH, and network access to data.source.coop.

    python3 tests/test_queries.py [--sample 40] [--only path1,path2] [--jobs 16]
"""

import argparse
import hashlib
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FENCE = re.compile(r"(<!-- no-rows -->\n)?^```sql\n(.*?)^```\s*$", re.M | re.S)


def run(guide, line, sql, expect_rows):
    r = subprocess.run(["duckdb", "-no-agent", "-csv", "-c", sql], capture_output=True, text=True, timeout=600)
    where = f"{guide.relative_to(ROOT)}:{line}"
    if r.returncode:
        return f"{where}: {(r.stderr or r.stdout).strip()[-300:]}"
    rows = [x for x in r.stdout.strip().splitlines()[1:] if x.strip()]
    if expect_rows and not rows:
        return f"{where}: returned no rows"
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sample", type=int, help="run the guides of N collections, chosen by a stable hash")
    ap.add_argument("--only", help="comma-separated AGENTS.md paths to run")
    ap.add_argument("--jobs", type=int, default=16)
    a = ap.parse_args()
    guides = sorted((ROOT / "catalog").rglob("AGENTS.md"))
    if a.only:
        want = {(ROOT / p).resolve() for p in a.only.split(",") if p}
        guides = [g for g in guides if g.resolve() in want]
    elif a.sample:
        # The shallow guides (root, hazard, year) always run; collections are sampled.
        shallow = [g for g in guides if len(g.relative_to(ROOT / "catalog").parts) <= 3]
        deep = sorted((g for g in guides if g not in shallow),
                      key=lambda g: hashlib.sha1(str(g.relative_to(ROOT)).encode()).hexdigest())
        guides = shallow + deep[: a.sample]
    jobs = []
    for g in guides:
        text = g.read_text()
        for m in FENCE.finditer(text):
            jobs.append((g, text[: m.start()].count("\n") + 1, m.group(2), m.group(1) is None))
    with ThreadPoolExecutor(a.jobs) as ex:
        fails = [f for f in ex.map(lambda j: run(*j), jobs) if f]
    for f in fails:
        print("FAIL", f)
    print(f"{len(jobs) - len(fails)}/{len(jobs)} queries passed in {len(guides)} guides")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())

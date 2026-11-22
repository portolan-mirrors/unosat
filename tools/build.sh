#!/usr/bin/env bash
# Build the catalog, from the HDX manifest to finished STAC.
#
#   WORK=/path/to/scratch tools/build.sh             # every event
#   WORK=... EVENTS=fl20240825bgd,eq20230206syr tools/build.sh
#
# WORK holds downloads and conversion caches; it is never published. The data
# files (GeoParquet, PMTiles) are written under catalog/ next to their
# collection.json and are gitignored. Publish with tools/publish.py.
#
# With EVENTS set, only those events are fetched, staged, tiled, styled, and
# added. Metadata, READMEs, and agent guides are regenerated for the whole
# tree, because they are built from the committed records in
# manifest/collections/ and need no data.
#
# SKIP_SYNC=1 skips the HDX query and uses the committed manifest.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
: "${WORK:?set WORK to a scratch directory}"
export WORK
JOBS="${JOBS:-32}"
EVENTS="${EVENTS:-}"

step() { printf '\n=== %s\n' "$*"; }

if [[ -z "${SKIP_SYNC:-}" ]]; then
  step "HDX manifest"
  python3 -I tools/hdx_sync.py
fi

step "fetch"
if [[ -n "$EVENTS" ]]; then
  python3 -I tools/fetch.py --collections "$EVENTS"
else
  python3 -I tools/fetch.py
fi

step "stage (convert and merge)"
if [[ -n "$EVENTS" ]]; then
  python3 -I tools/stage.py --events "$EVENTS" --jobs "$JOBS"
else
  python3 -I tools/stage.py --jobs "$JOBS"
fi

# The collection ids and event directories of the selected events, read from
# the records stage.py just wrote.
ONLY=""
EVENT_DIRS=()
if [[ -n "$EVENTS" ]]; then
  ONLY="$(python3 -I - "$EVENTS" <<'EOF'
import json, sys
from pathlib import Path
want = set(sys.argv[1].split(","))
ids = []
for f in sorted(Path("manifest/collections").glob("*.json")):
    r = json.load(open(f))
    if r.get("event") in want and r.get("status") == "ok":
        ids.append(r["collection"])
print(",".join(ids))
EOF
)"
  mapfile -t EVENT_DIRS < <(python3 -I - "$EVENTS" <<'EOF'
import json, sys
from pathlib import Path
want = set(sys.argv[1].split(","))
dirs = set()
for f in sorted(Path("manifest/collections").glob("*.json")):
    r = json.load(open(f))
    if r.get("event") in want and r.get("status") == "ok":
        dirs.add(str(Path(r["path"]).parent))
print("\n".join(sorted(dirs)))
EOF
)
  if [[ -z "$ONLY" ]]; then
    echo "no staged collection for EVENTS=$EVENTS"
  fi
fi

step "tiles (tylertoo)"
if [[ -n "$EVENTS" ]]; then
  [[ -n "$ONLY" ]] && python3 -I tools/tile.py --only "$ONLY"
else
  python3 -I tools/tile.py
fi

step "styles"
if [[ -n "$EVENTS" ]]; then
  [[ -n "$ONLY" ]] && python3 -I tools/styles.py --only "$ONLY"
else
  python3 -I tools/styles.py
fi

# The combined collections read every per-event GeoParquet, so they are
# rebuilt only on a full build, where all the data is on disk.
if [[ -z "$EVENTS" ]]; then
  step "combined collections"
  python3 -I tools/combine.py
  bash tools/tile_combined.sh
  python3 -I tools/combined_styles.py
fi

step "metadata.yaml"
python3 -I tools/meta.py

step "portolan add"
(
  cd catalog
  if [[ -n "$EVENTS" ]]; then
    for d in "${EVENT_DIRS[@]}"; do
      [[ -n "$d" ]] && portolan add "$d/" --workers 8 --no-thumbnails
    done
  else
    # One add per event directory: a single `portolan add .` over the whole
    # archive ran 20 minutes without writing anything (portolan-cli 0.9.0).
    python3 -c 'import json,glob,os; print("\n".join(sorted({os.path.dirname(json.load(open(f))["path"]) for f in glob.glob("../manifest/collections/*.json")})))' |
      while read -r d; do portolan add "$d/" --workers 8 --no-thumbnails; done
    portolan add combined/ --workers 8 --no-thumbnails
  fi
)

step "column descriptions and navigation links"
python3 -I tools/post.py

step "agent guides"
python3 -I tools/agents.py

step "READMEs"
(cd catalog && portolan readme)
python3 -I tools/post.py --readme

step "gates"
python3 tests/run_all.py

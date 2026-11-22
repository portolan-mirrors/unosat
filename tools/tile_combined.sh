#!/usr/bin/env bash
# Build the PMTiles of the two combined (cross-event) collections.
#
# They have no record in manifest/collections, so tools/tile.py does not see
# them. The flags match tile.py. The water-extent tiling copy keeps only the
# properties a map needs, and explodes rows over 16 MB of WKB into their
# parts: tylertoo refuses one row over 64 MiB decoded (fixed at c338560),
# and the combined file has 513 rows over 16 MB, some of them single polygons
# with millions of vertices. The GeoParquet itself is unchanged.
#
#     WORK=/scratch/unosat/work tools/tile_combined.sh
set -euo pipefail
ROOT=$(cd "$(dirname "$0")/.." && pwd)
C=$ROOT/catalog/combined
: "${WORK:?set WORK}"
WATER_MAX_ZOOM=${WATER_MAX_ZOOM:-12}
mkdir -p "$WORK/spill/c-dmg" "$WORK/spill/c-wat" "$WORK/tile-tmp"

# Damage sites: 5.5M points; about 4 s on 64 cores.
tylertoo tiles "$C/damage-sites/damage-sites.parquet" "$C/damage-sites/damage-sites.pmtiles" \
  --layer-name damage-sites --max-zoom 15 --name combined-damage-sites \
  --attribution UNITAR-UNOSAT --exclude-property bbox \
  --spill-dir "$WORK/spill/c-dmg" -f

# Water extent: 6.0M polygons, 14.9 GB.
X=$WORK/tile-tmp/combined-water-extent.exploded.parquet
if [ ! -s "$X" ] || [ "$C/water-extent/water-extent.parquet" -nt "$X" ]; then
  # Same explode as tools/tile.py (parts, then an 8 x 8 grid clip of any
  # part still too big), keeping only the map properties.
  python3 -I "$ROOT/tools/tile.py" --explode "$C/water-extent/water-extent.parquet" "$X" \
    event,collection,source_layer,license,water_class,sensor_date
fi
tylertoo tiles "$X" "$C/water-extent/water-extent.pmtiles" \
  --layer-name water-extent --max-zoom "$WATER_MAX_ZOOM" --name combined-water-extent \
  --attribution UNITAR-UNOSAT --spill-dir "$WORK/spill/c-wat" -f
rm -rf "$WORK/spill/c-dmg" "$WORK/spill/c-wat"

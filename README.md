# UNOSAT Rapid Mapping Archive (Portolan mirror)

This repository builds and maintains a [Portolan](https://www.portolan-sdi.org/)
mirror of the geodata that the United Nations Satellite Centre (UNOSAT) publishes
on the [Humanitarian Data Exchange](https://data.humdata.org/organization/unosat)
(HDX). The data are satellite-derived flood and water extents, damage
assessments, shelter and camp mapping, landslides, and analysis extents.

- Published catalog: <https://data.source.coop/portolan-mirrors/unosat/catalog.json>
- Hosting page: <https://source.coop/portolan-mirrors/unosat>
- Request: [portolan-sdi/portolan-data#57](https://github.com/portolan-sdi/portolan-data/issues/57)

The repository holds the STAC metadata and the build scripts. The data files
(GeoParquet and PMTiles) are in the bucket only. Git ignores them.

## Layout

```text
catalog/<hazard>/[<year>/]<event>/<event>-<family>/
    collection.json   <event>-<family>.parquet   <event>-<family>.pmtiles
    styles/default.json   AGENTS.md   README.md   .portolan/metadata.yaml
```

- An event is one UNOSAT event code (for example `FL20240825BGD`), or one HDX
  dataset when the dataset has no code. Each event is a subcatalog.
- A hazard with 20 or more events is grouped by year (PORTO-CORE-078).
- A collection merges the source layers of one kind ("family") in one event,
  for example all damage-site point layers. The `source_layer` and
  `source_file` columns name the origin of each row.
- One event can have more than one collection of a family when its layers have
  different licenses or CRSs. The collection id then has a suffix.

## The pipeline

`tools/build.sh` runs the steps in this order:

| Step | Script | What it does |
|---|---|---|
| 1 | `tools/hdx_sync.py` | Reads the UNOSAT organization on HDX and writes `manifest/packages.json` |
| 2 | `tools/fetch.py` | Downloads the source files with aria2c into `$WORK/dl` |
| 3 | `tools/stage.py` | Converts each layer to GeoParquet, merges each family into one file per collection, writes `manifest/collections/*.json` |
| 4 | `tools/tile.py` | Builds one PMTiles file per collection with tylertoo |
| 5 | `tools/styles.py` | Writes `styles/default.json` from the values in the data |
| 6 | `tools/meta.py` | Writes `.portolan/metadata.yaml` at each level from HDX metadata |
| 7 | `portolan add` | Writes the STAC JSON |
| 8 | `tools/post.py` | Adds column descriptions and the navigation links |
| 9 | `tools/agents.py` | Writes the agent guides (`AGENTS.md`) |
| 10 | `portolan readme`, `tools/post.py --readme` | Writes the READMEs and their navigation line |
| 11 | `tests/run_all.py` | Runs the gates |

### Conversion

Each layer goes through two commands:

1. `ogr2ogr -f GPKG -nlt PROMOTE_TO_MULTI` (system GDAL), with
   `OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER` and
   `SHAPE_RESTORE_SHX=YES`.
2. `gpio convert geoparquet --geoparquet-version 2.0 --no-repair-geometry`.

The geometry is not repaired. A mirror keeps the source geometry. The default
repair in gpio also took more than 120 s on one layer that converts in 4 s
without it.

Each output must have the same row count as the source layer. Two known
causes make the counts differ:

- **gpio segfaults.** gpio 1.7.0 (DuckDB 1.5.6) segfaults on about one run in
  four over the same GeoPackage, in its bounds query. `stage.py` runs gpio
  again, up to five times, when it ends on a signal.
- **Deleted geodatabase records.** A File Geodatabase header can count
  deleted records (the `.gdbtablx` mismatch that GDAL warns about). When the
  counts differ, `stage.py` counts the features that GDAL iterates. It accepts
  the output only when that count matches.

## Rebuild

You need GDAL with its Python bindings, aria2, the DuckDB CLI, gpio 1.7.0,
portolan-cli 0.9.0, rashid 0.4.x, and tylertoo built from git at the commit in
`tools/tile.py` (`TYLERTOO_REV`).

```bash
export WORK=/path/to/scratch        # downloads and caches; never published
tools/build.sh                      # all events
EVENTS=fl20240825bgd tools/build.sh # some events
SKIP_SYNC=1 tools/build.sh          # use the committed manifest
```

## Publish

This catalog publishes with `tools/publish.py`, not with `portolan push`.
`publish.py` uploads all of `catalog/`, data files included, and it compares
each file with the bucket listing. It never deletes.

```bash
python3 tools/publish.py            # dry run
python3 tools/publish.py --confirm  # upload; needs Source Cooperative credentials
```

## CI

| Workflow | When | What |
|---|---|---|
| `ci.yml` | push, pull request | Lint, `portolan metadata validate`, the gates with `CI_LIGHT=1` |
| `refresh.yml` | weekly, manual | Finds the changed HDX datasets, rebuilds their events, validates, publishes, and commits to `main` |
| `live-claims.yml` | weekly, manual, pull requests on agent guides | Runs the SQL in the agent guides against the published data. A failed weekly run opens a tracking issue |
| `links.yml`, `vale.yml` | pull request | Link and prose checks from portolan-ops |

`refresh.yml` uploads through GitHub OIDC with the role
`arn:aws:iam::939788573396:role/source-coop-portolan-mirrors`. There is no
stored key.

## Licenses

The HDX license of each dataset is kept on its collection. The archive has
CC BY-SA (HDX gives no version), CC BY 4.0, CC BY 3.0 IGO, and CC BY-NC-SA 3.0.
The HDX dataset `ethiopia-flooding-somali-region` is excluded, because its
terms are "Humanitarian use only".

The code in this repository is under the license in [LICENSE](LICENSE).

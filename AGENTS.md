## This Repository

The build scripts and STAC metadata of the Portolan mirror of the UNOSAT
geodata on HDX. Read [README.md](README.md) first: it gives the layout, the
pipeline, and the CI.

### Edit the generator, not the output

Everything under `catalog/` is generated. `tools/meta.py` writes the
`metadata.yaml` files, `portolan add` writes the STAC JSON, `tools/post.py`
adds column descriptions and navigation links, `tools/agents.py` writes the
agent guides, and `portolan readme` writes the READMEs. A hand edit is lost on
the next `tools/build.sh` or weekly refresh. Change the script.

The records in `manifest/collections/` are written by `tools/stage.py`. The
other steps read them, so a refresh can rebuild one event without the data of
the others. Do not edit them by hand.

### The publish boundary

`catalog/` is the published catalog. `tools/publish.py` uploads everything in
it, the gitignored GeoParquet and PMTiles included, and nothing outside it.
This catalog publishes with `tools/publish.py`, never with `portolan push`:
the two do not share state. Publishing never deletes an object.

### Data never enters git

Never commit a GeoParquet, PMTiles, GeoPackage, or zip file. `.gitignore`
blocks them. Downloads and caches go in `$WORK`, outside the repository.

### Conversion rules

- Keep `--no-repair-geometry`. The mirror keeps the source geometry.
- Keep the row-count check in `tools/stage.py`. It caught a silent truncation
  (2,208 of 635,744 rows) before the GeoPackage intermediate replaced
  FlatGeobuf.
- gpio 1.7.0 segfaults on about one run in four over the same GeoPackage.
  `stage.py` retries a run that ends on a signal. Do not remove the retry
  until a gpio release is tested with many runs of the same input.
- A File Geodatabase header can count deleted records. `stage.py` then counts
  the features that GDAL iterates, and accepts only that count.

### The conformance allow-list

`ACCEPTED` in `tests/test_conformance.py` is empty. Never add an entry without
a matching row in `docs/conformance.md` giving the rule, where it fires, why it
is accepted, and the issue tracking its removal.

### Published agent guides

Every claim in a `catalog/**/AGENTS.md` is quoted from HDX or measured from the
data. Counts are given as queries, not numbers. `tests/test_queries.py` runs
every SQL fence against the published data, and `live-claims.yml` runs it each
week.

### Pinned tools

| Tool | Version | Where it is pinned |
|---|---|---|
| tylertoo | git `c338560f16ef97dcc1a2269c8b204eae923a344f` | `tools/tile.py`, `refresh.yml` |
| gpio (geoparquet-io) | 1.7.0 | `refresh.yml` |
| portolan-cli | 0.9.0 | `ci.yml`, `refresh.yml` |
| rashid | `>=0.4.0,<0.5.0` | `tests/test_conformance.py`, `ci.yml`, `refresh.yml` |
| DuckDB CLI | v2.0.0 | `refresh.yml`, `live-claims.yml` |

Move a pin in every place in the same change.

### Conventions

Use conventional commits. Write prose in Simplified Technical English.

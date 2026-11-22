# AGENTS.md: UNOSAT Rapid Mapping Archive

Guidance for AI agents and automated clients. The public root is
`https://data.source.coop/portolan-mirrors/unosat/catalog.json`.

## What this catalog holds

A mirror of the vector geodata that UNOSAT (UNITAR) publishes on the
[Humanitarian Data Exchange](https://data.humdata.org/organization/unosat).

- `<hazard>/[<year>/]<event>/` is one event subcatalog. The event id is the
  UNOSAT event code in lower case, for example `eq20230206syr`
  (earthquake, 2023-02-06, Syria). Datasets with no event code use their HDX
  dataset name. Floods and tropical cyclones are grouped by year.
- `<event>/<event>-<family>/` is one collection with one GeoParquet file,
  `<event>-<family>.parquet`, and a PMTiles file beside it. A family merges all
  source layers of one kind: `analysis-extent`, `damage-sites`,
  `damage-areas`, `water-extent`, `shelters`, `shelter-areas`, `landslides`,
  `affected-structures`, or `other-<points|lines|polygons>`. A collection id
  ends in a CRS or license suffix when one event has layers of the same family
  in different CRSs or under different licenses.
- `combined/damage-sites` and `combined/water-extent` join the damage-site
  and water-extent collections of all events into one file each, with
  harmonized class columns. They hold only the openly licensed collections
  (CC BY-SA, CC BY, CC BY-IGO). Collections under CC BY-NC-SA 3.0 are left out.

Each collection has its own AGENTS.md with its URL and recipes.

## How to read it

Damage classes in the combined damage-sites file, by event:

```sql
INSTALL spatial; LOAD spatial;
SELECT event, damage_class, count(*) AS sites
FROM read_parquet('https://data.source.coop/portolan-mirrors/unosat/combined/damage-sites/damage-sites.parquet')
GROUP BY ALL ORDER BY event, sites DESC
LIMIT 20;
```

Water-extent features in a bounding box, read with the bbox column so DuckDB
fetches only the row groups that can match:

```sql
INSTALL spatial; LOAD spatial;
SELECT event, water_class, sensor_date, ST_Area_Spheroid(geometry) / 1e6 AS km2
FROM read_parquet('https://data.source.coop/portolan-mirrors/unosat/combined/water-extent/water-extent.parquet')
WHERE bbox.xmin < 91.5 AND bbox.xmax > 89.5 AND bbox.ymin < 25 AND bbox.ymax > 23
LIMIT 20;
```

To list every collection, walk the STAC tree from `catalog.json`, or read the
`collection` column of the combined files.

## Join keys

No two collections share a feature key. `event` (the subcatalog id) and
`event_code` relate rows to events. `event_code` is what the feature itself
records, and it does not always equal the subcatalog's code. `source_layer`
and `source_file` name the original layer and HDX file.

## Quirks that produce silently wrong answers

- One event often has several layers of the same kind, one per image date or
  per release. Filter on `source_layer`, or on `assessment_epoch` and
  `sensor_date` in the combined files, before you count. The Gaza releases
  repeat the same sites in each release.
- Coded columns differ between source files. In a per-event collection, read
  the `<field>_label` column, which is decoded per source file. A numeric
  `Water_Clas` from a shapefile has no domain, and two different water-class
  code lists exist, so the code alone is ambiguous.
- Class labels are not normalized: "Possible damage" and "Possible Damage" are
  separate values.
- Many "affected roads" line layers (for example `PL_20240501_AffectedRoad_*`
  in Kenya, `*_AffectedRoads_*` in Myanmar and Cabo Verde) also hold a block
  of template features near 29.8°E, 9.3°N in South Sudan, far from the event.
  Drop them by bbox before you map or measure:
  `WHERE NOT (bbox.xmin BETWEEN 29.6 AND 30.4 AND bbox.ymin BETWEEN 9.0 AND 9.5)`.
- Geometry is as published and not repaired. Use `ST_MakeValid` before
  overlay operations.
- Most collections are EPSG:4326. A collection whose id ends in a CRS suffix
  such as `-epsg_32646` is in that CRS. The combined files are all EPSG:4326.
- `Shape_Area` and `Shape_Length` are in the units of the source CRS, which is
  degrees for EPSG:4326.

## Licenses

The license is set per collection. 320 HDX datasets are CC BY-NC-SA 3.0. The
rest are CC BY-SA (HDX gives no version), CC BY 4.0, or CC BY 3.0 IGO. Check
`license` on the collection, or the `license` column in the combined files.

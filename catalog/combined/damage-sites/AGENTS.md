# combined/damage-sites: agent guide

One GeoParquet file: `https://data.source.coop/portolan-mirrors/unosat/combined/damage-sites/damage-sites.parquet`. It joins the damage-sites collections of every event under CC BY-SA, CC BY, or CC BY-IGO. CC BY-NC-SA 3.0 collections are left out.

- `event` is the event subcatalog id, `collection` the source collection, and `source_layer` and `source_file` the original layer and HDX file.
- `damage_class` is the decoded class label; `damage_class_code` is the raw value as text. Labels are not normalized across events, so group on `damage_class` per event.
- `license` is the license of the row's HDX dataset.
- `assessment_epoch` says which epoch of a wide multi-epoch layer the row took; null for ordinary layers.
- Geometry is EPSG:4326, 2D, and not repaired.

## Rows by event and class

```sql
INSTALL spatial; LOAD spatial;
SELECT event, damage_class, count(*) AS features
FROM read_parquet('https://data.source.coop/portolan-mirrors/unosat/combined/damage-sites/damage-sites.parquet')
GROUP BY ALL ORDER BY event, features DESC LIMIT 50;
```

# combined/water-extent: agent guide

One GeoParquet file: `https://data.source.coop/portolan-mirrors/unosat/combined/water-extent/water-extent.parquet`. It joins the water-extent collections of every event under CC BY-SA, CC BY, or CC BY-IGO. CC BY-NC-SA 3.0 collections are left out.

- `event` is the event subcatalog id, `collection` the source collection, and `source_layer` and `source_file` the original layer and HDX file.
- `water_class` is the decoded class label; `water_class_code` is the raw value as text. Labels are not normalized across events, so group on `water_class` per event.
- `license` is the license of the row's HDX dataset.
- `assessment_epoch` says which epoch of a wide multi-epoch layer the row took; null for ordinary layers.
- Geometry is EPSG:4326, 2D, and not repaired.

## Rows by event and class

```sql
INSTALL spatial; LOAD spatial;
SELECT event, water_class, count(*) AS features
FROM read_parquet('https://data.source.coop/portolan-mirrors/unosat/combined/water-extent/water-extent.parquet')
GROUP BY ALL ORDER BY event, features DESC LIMIT 50;
```

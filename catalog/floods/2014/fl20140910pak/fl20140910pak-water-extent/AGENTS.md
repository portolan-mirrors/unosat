# fl20140910pak-water-extent: agent guide

One GeoParquet file: `https://data.source.coop/portolan-mirrors/unosat/floods/2014/fl20140910pak/fl20140910pak-water-extent/fl20140910pak-water-extent.parquet`.

- Each row is one feature of a UNOSAT source layer. `source_layer` and `source_file` name the layer and the HDX file it came from. One event often has several layers of the same kind (for example, one per satellite image date), so filter on `source_layer` before you count or map.
- CRS: EPSG:4326 (longitude, latitude). Source layers in "WGS 84 + EGM96 height" are 2D, so the vertical part was dropped.
- Geometry is as published, not repaired. Use `ST_MakeValid` before overlay operations.
- A column a source layer did not have is null for that layer's rows.
- Coded columns have a decoded twin: `Confidence_ID_label`, `Field_Validation_label`, `SenorID_old_label`, `Sensor_ID_label`, `StaffID_label`, `Water_Class_label`, `Water_StatusID_label`. Read the `_label` column; the code lists differ between source files.

## Rows per source layer

```sql
INSTALL spatial; LOAD spatial;
SELECT source_layer, count(*) AS features
FROM read_parquet('https://data.source.coop/portolan-mirrors/unosat/floods/2014/fl20140910pak/fl20140910pak-water-extent/fl20140910pak-water-extent.parquet')
GROUP BY source_layer ORDER BY source_layer;
```

## Features by `Confidence_ID_label`

```sql
SELECT source_layer, Confidence_ID_label, count(*) AS features
FROM read_parquet('https://data.source.coop/portolan-mirrors/unosat/floods/2014/fl20140910pak/fl20140910pak-water-extent/fl20140910pak-water-extent.parquet')
GROUP BY ALL ORDER BY source_layer, features DESC;
```

## Load in Python

```python
import geopandas as gpd
gdf = gpd.read_parquet('https://data.source.coop/portolan-mirrors/unosat/floods/2014/fl20140910pak/fl20140910pak-water-extent/fl20140910pak-water-extent.parquet')
```

The [data browser](https://source.coop/portolan-mirrors/unosat) shows the map, schema, and license. The event's other collections are siblings in the parent catalog.

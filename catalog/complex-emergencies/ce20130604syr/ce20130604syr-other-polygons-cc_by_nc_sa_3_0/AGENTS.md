# ce20130604syr-other-polygons-cc_by_nc_sa_3_0: agent guide

One GeoParquet file: `https://data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20130604syr/ce20130604syr-other-polygons-cc_by_nc_sa_3_0/ce20130604syr-other-polygons-cc_by_nc_sa_3_0.parquet`.

- Each row is one feature of a UNOSAT source layer. `source_layer` and `source_file` name the layer and the HDX file it came from. One event often has several layers of the same kind (for example, one per satellite image date), so filter on `source_layer` before you count or map.
- CRS: EPSG:4326 (longitude, latitude). Source layers in "WGS 84 + EGM96 height" are 2D, so the vertical part was dropped.
- Geometry is as published, not repaired. Use `ST_MakeValid` before overlay operations.
- A column a source layer did not have is null for that layer's rows.

## Rows per source layer

```sql
INSTALL spatial; LOAD spatial;
SELECT source_layer, count(*) AS features
FROM read_parquet('https://data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20130604syr/ce20130604syr-other-polygons-cc_by_nc_sa_3_0/ce20130604syr-other-polygons-cc_by_nc_sa_3_0.parquet')
GROUP BY source_layer ORDER BY source_layer;
```

## Load in Python

```python
import geopandas as gpd
gdf = gpd.read_parquet('https://data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20130604syr/ce20130604syr-other-polygons-cc_by_nc_sa_3_0/ce20130604syr-other-polygons-cc_by_nc_sa_3_0.parquet')
```

The [data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20130604syr/ce20130604syr-other-polygons-cc_by_nc_sa_3_0/collection.json) shows the map, schema, and license. The event's other collections are siblings in the parent catalog.

# tropical-cyclone-maria-inventory-of-landslides-and-flooded-areas-2762-analysis-extent: agent guide

One GeoParquet file: `https://data.source.coop/portolan-mirrors/unosat/no-event-code/tropical-cyclone-maria-inventory-of-landslides-and-flooded-areas-2762/tropical-cyclone-maria-inventory-of-landslides-and-flooded-areas-2762-analysis-extent/tropical-cyclone-maria-inventory-of-landslides-and-flooded-areas-2762-analysis-extent.parquet`.

- Each row is one feature of a UNOSAT source layer. `source_layer` and `source_file` name the layer and the HDX file it came from. One event often has several layers of the same kind (for example, one per satellite image date), so filter on `source_layer` before you count or map.
- CRS: EPSG:32620, the CRS of the source layers. Reproject before you join it with EPSG:4326 data, for example `ST_Transform(geometry, 'EPSG:32620', 'EPSG:4326', always_xy := true)`.
- Geometry is as published, not repaired. Use `ST_MakeValid` before overlay operations.
- A column a source layer did not have is null for that layer's rows.

## Rows per source layer

```sql
INSTALL spatial; LOAD spatial;
SELECT source_layer, count(*) AS features
FROM read_parquet('https://data.source.coop/portolan-mirrors/unosat/no-event-code/tropical-cyclone-maria-inventory-of-landslides-and-flooded-areas-2762/tropical-cyclone-maria-inventory-of-landslides-and-flooded-areas-2762-analysis-extent/tropical-cyclone-maria-inventory-of-landslides-and-flooded-areas-2762-analysis-extent.parquet')
GROUP BY source_layer ORDER BY source_layer;
```

## Load in Python

```python
import geopandas as gpd
gdf = gpd.read_parquet('https://data.source.coop/portolan-mirrors/unosat/no-event-code/tropical-cyclone-maria-inventory-of-landslides-and-flooded-areas-2762/tropical-cyclone-maria-inventory-of-landslides-and-flooded-areas-2762-analysis-extent/tropical-cyclone-maria-inventory-of-landslides-and-flooded-areas-2762-analysis-extent.parquet')
```

The [data browser](https://source.coop/portolan-mirrors/unosat) shows the map, schema, and license. The event's other collections are siblings in the parent catalog.

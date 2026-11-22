# tc20231206slb-damage-sites: agent guide

One GeoParquet file: `https://data.source.coop/portolan-mirrors/unosat/tropical-cyclones/2023/tc20231206slb/tc20231206slb-damage-sites/tc20231206slb-damage-sites.parquet`.

- Each row is one feature of a UNOSAT source layer. `source_layer` and `source_file` name the layer and the HDX file it came from. One event often has several layers of the same kind (for example, one per satellite image date), so filter on `source_layer` before you count or map.
- CRS: EPSG:4326 (longitude, latitude). Source layers in "WGS 84 + EGM96 height" are 2D, so the vertical part was dropped.
- Geometry is as published, not repaired. Use `ST_MakeValid` before overlay operations.
- A column a source layer did not have is null for that layer's rows.
- Coded columns have a decoded twin: `ConfidenceID_label`, `FieldValidation_label`, `Grouped_Damage_Classes_label`, `Main_Damage_Site_Class_label`, `SensorID_label`, `SiteID_label`, `StaffID_label`. Read the `_label` column; the code lists differ between source files.

## Rows per source layer

```sql
INSTALL spatial; LOAD spatial;
SELECT source_layer, count(*) AS features
FROM read_parquet('https://data.source.coop/portolan-mirrors/unosat/tropical-cyclones/2023/tc20231206slb/tc20231206slb-damage-sites/tc20231206slb-damage-sites.parquet')
GROUP BY source_layer ORDER BY source_layer;
```

## Features by `ConfidenceID_label`

```sql
SELECT source_layer, ConfidenceID_label, count(*) AS features
FROM read_parquet('https://data.source.coop/portolan-mirrors/unosat/tropical-cyclones/2023/tc20231206slb/tc20231206slb-damage-sites/tc20231206slb-damage-sites.parquet')
GROUP BY ALL ORDER BY source_layer, features DESC;
```

## Load in Python

```python
import geopandas as gpd
gdf = gpd.read_parquet('https://data.source.coop/portolan-mirrors/unosat/tropical-cyclones/2023/tc20231206slb/tc20231206slb-damage-sites/tc20231206slb-damage-sites.parquet')
```

The [data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/tropical-cyclones/2023/tc20231206slb/tc20231206slb-damage-sites/collection.json) shows the map, schema, and license. The event's other collections are siblings in the parent catalog.

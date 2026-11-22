# ce20231007pse-damage-sites: agent guide

One GeoParquet file: `https://data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20231007pse/ce20231007pse-damage-sites/ce20231007pse-damage-sites.parquet`.

- Each row is one feature of a UNOSAT source layer. `source_layer` and `source_file` name the layer and the HDX file it came from. One event often has several layers of the same kind (for example, one per satellite image date), so filter on `source_layer` before you count or map.
- CRS: EPSG:4326 (longitude, latitude). Source layers in "WGS 84 + EGM96 height" are 2D, so the vertical part was dropped.
- Geometry is as published, not repaired. Use `ST_MakeValid` before overlay operations.
- A column a source layer did not have is null for that layer's rows.
- Coded columns have a decoded twin: `ConfidenceID_label`, `FieldValidation_label`, `Grouped_Damage_Classes_label`, `Main_Damage_Site_Class_label`, `SensorID_label`, `SiteID_label`, `ConfidenceID_2_label`, `Main_Damage_Site_Class_2_label`, `SensorID_2_label`, `Damage_Status_2_label`, `StaffID_label`, `ConfidenceID_6_label`, `Main_Damage_Site_Class_6_label`, `SensorID_6_label`, `ConfidenceID_10_label`, `ConfidenceID_11_label`, `ConfidenceID_12_label`, `ConfidenceID_13_label`, `ConfidenceID_14_label`, `ConfidenceID_3_label`, `ConfidenceID_4_label`, `ConfidenceID_5_label`, `ConfidenceID_7_label`, `ConfidenceID_8_label`, `ConfidenceID_9_label`, `Damage_Status_10_label`, `Damage_Status_11_label`, `Damage_Status_12_label`, `Damage_Status_13_label`, `Damage_Status_14_label`, `Damage_Status_3_label`, `Damage_Status_4_label`, `Damage_Status_5_label`, `Damage_Status_6_label`, `Damage_Status_7_label`, `Damage_Status_8_label`, `Damage_Status_9_label`, `Main_Damage_Site_Class_10_label`, `Main_Damage_Site_Class_11_label`, `Main_Damage_Site_Class_12_label`, `Main_Damage_Site_Class_13_label`, `Main_Damage_Site_Class_14_label`, `Main_Damage_Site_Class_3_label`, `Main_Damage_Site_Class_4_label`, `Main_Damage_Site_Class_5_label`, `Main_Damage_Site_Class_7_label`, `Main_Damage_Site_Class_8_label`, `Main_Damage_Site_Class_9_label`, `SensorID_10_label`, `SensorID_11_label`, `SensorID_12_label`, `SensorID_13_label`, `SensorID_14_label`, `SensorID_3_label`, `SensorID_4_label`, `SensorID_5_label`, `SensorID_7_label`, `SensorID_8_label`, `SensorID_9_label`, `Construction_Status_label`. Read the `_label` column; the code lists differ between source files.

## Rows per source layer

```sql
INSTALL spatial; LOAD spatial;
SELECT source_layer, count(*) AS features
FROM read_parquet('https://data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20231007pse/ce20231007pse-damage-sites/ce20231007pse-damage-sites.parquet')
GROUP BY source_layer ORDER BY source_layer;
```

## Features by `ConfidenceID_label`

```sql
SELECT source_layer, ConfidenceID_label, count(*) AS features
FROM read_parquet('https://data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20231007pse/ce20231007pse-damage-sites/ce20231007pse-damage-sites.parquet')
GROUP BY ALL ORDER BY source_layer, features DESC;
```

## Load in Python

```python
import geopandas as gpd
gdf = gpd.read_parquet('https://data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20231007pse/ce20231007pse-damage-sites/ce20231007pse-damage-sites.parquet')
```

The [data browser](https://source.coop/portolan-mirrors/unosat) shows the map, schema, and license. The event's other collections are siblings in the parent catalog.

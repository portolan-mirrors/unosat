# ce20220223ukr-damage-sites-cc_by_sa: agent guide

One GeoParquet file: `https://data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20220223ukr/ce20220223ukr-damage-sites-cc_by_sa/ce20220223ukr-damage-sites-cc_by_sa.parquet`.

- Each row is one feature of a UNOSAT source layer. `source_layer` and `source_file` name the layer and the HDX file it came from. One event often has several layers of the same kind (for example, one per satellite image date), so filter on `source_layer` before you count or map.
- CRS: EPSG:3857, the CRS of the source layers. Reproject before you join it with EPSG:4326 data, for example `ST_Transform(geometry, 'EPSG:3857', 'EPSG:4326', always_xy := true)`.
- Geometry is as published, not repaired. Use `ST_MakeValid` before overlay operations.
- A column a source layer did not have is null for that layer's rows.
- Coded columns have a decoded twin: `Analyst_label`, `ConfidenceID_label`, `ConfidenceID_2_label`, `ConfidenceID_3_label`, `ConfidenceID_4_label`, `ConfidenceID_5_label`, `ConfidenceID_6_label`, `Damage_Status_2_label`, `Damage_Status_3_label`, `Damage_Status_4_label`, `Damage_Status_5_label`, `Damage_Status_6_label`, `FieldValidation_label`, `Grouped_Damage_Classes_label`, `Main_Damage_Site_Clas3_label`, `Main_Damage_Site_Class_label`, `Main_Damage_Site_Class_2_label`, `Main_Damage_Site_Class_4_label`, `Main_Damage_Site_Class_5_label`, `Main_Damage_Site_Class_6_label`, `SensorID_label`, `SensorID_2_label`, `SensorID_3_label`, `SensorID_4_label`, `SensorID_5_label`, `SensorID_6_label`, `SiteID_label`, `StaffID_label`. Read the `_label` column; the code lists differ between source files.

## Rows per source layer

```sql
INSTALL spatial; LOAD spatial;
SELECT source_layer, count(*) AS features
FROM read_parquet('https://data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20220223ukr/ce20220223ukr-damage-sites-cc_by_sa/ce20220223ukr-damage-sites-cc_by_sa.parquet')
GROUP BY source_layer ORDER BY source_layer;
```

## Features by `Analyst_label`

```sql
SELECT source_layer, Analyst_label, count(*) AS features
FROM read_parquet('https://data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20220223ukr/ce20220223ukr-damage-sites-cc_by_sa/ce20220223ukr-damage-sites-cc_by_sa.parquet')
GROUP BY ALL ORDER BY source_layer, features DESC;
```

## Load in Python

```python
import geopandas as gpd
gdf = gpd.read_parquet('https://data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20220223ukr/ce20220223ukr-damage-sites-cc_by_sa/ce20220223ukr-damage-sites-cc_by_sa.parquet')
```

The [data browser](https://source.coop/portolan-mirrors/unosat) shows the map, schema, and license. The event's other collections are siblings in the parent catalog.

# Water extent: Flood, Rwanda, 4 May 2023 (FL20230504RWA)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2023/fl20230504rwa/fl20230504rwa-water-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Water extent for Flood, Rwanda, 4 May 2023 (FL20230504RWA): 19 features merged from 19 source layers. Polygon layers with a water class column (such as `Water_Class`), or whose names mention flood, water, or inundation: satellite-detected water. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Damage assessment along the Mukungwa river, Western & Northern Provinces, Rwanda as of 10 May 2023](https://data.humdata.org/dataset/damage-assessment-along-the-mukungwa-river-western-northern-provinces-rwanda-as-of-10-may-)
- [Damage assessment along the Sebaya River, Rubavu and Karongi Districts, Western Province, Rwanda. - 6 May 2023](https://data.humdata.org/dataset/damage-assessment-along-the-sebaya-river-rubavu-and-karongi-districts-western-province-rwa)
- [Preliminary satellite flood and landslide assessment report, Along Sebaya River, Rubavu District, Karongi Districtn Western Province, Rwanda](https://data.humdata.org/dataset/preliminary-satellite-flood-and-landslide-assessment-report-along-sebaya-river-rubavu-dist)
- [Satellite detected landslides / mudslides over Kibingo, Congonil, Kagana and Ghanga Villages, Rutsiro District, Western Province, Rwanda  as of 7 May 2023](https://data.humdata.org/dataset/landslides-mudslides-over-kibingo-congonil-kagana-and-ghanga-villages-rutsiro-district-wes)
- [Satellite detected water extent along the Nyabarongo river West and South of Kigali City in Southern and Eastern Provinces, Rwanda as of 5 May 2023](https://data.humdata.org/dataset/water-extent-along-the-nyabarongo-river-west-and-south-of-kigali-city-in-southern-and-east)
- [Satellite detected water extent over Kigali City, Southern, Northern, Western, and Eastern Provinces, Rwanda  as of 3 May 2023](https://data.humdata.org/dataset/water-extent-over-kigali-city-southern-northern-western-and-eastern-provinces-rwanda-as-of)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [29.352283054000054, -2.345012327999939, 30.259031690000086, -1.6209659379999266]

## Temporal Coverage

- **Start**: 2023-05-05T00:00:00Z
- **End**: 2023-05-15T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Water_Class | int16 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Water_Class_label`, which is decoded per source file. |
| Sensor_ID | string | Coded value. The 3 source files of this collection use 3 different domains for it, so read `Sensor_ID_label`, which is decoded per source file. |
| Sensor_Date | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence_ID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `Confidence_ID_label`. |
| Field_Validation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `Field_Validation_label`. |
| Water_StatusID | int32 | Coded value. The source geodatabase domain gives: 1 = New Water / Water Increase; 2 = No water change / Static Level; 3 = No water / Water levels decreased. The decoded text is in `Water_StatusID_label`. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| SenorID_old | int16 | Coded value. The source geodatabase domain gives: 1 = MODIS; 2 = ASAR WSM; 3 = ASAR IMP; 4 = Radarsat; 5 = DMC; 6 = SPOT5; 7 = ALOS Palsar WB1; 8 = ASAR APP. The decoded text is in `SenorID_old_label`. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| StaffID | string | Coded value. The 3 source files of this collection use 3 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Confidence_ID_label | string | `Confidence_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Field_Validation_label | string | `Field_Validation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SenorID_old_label | string | `SenorID_old` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Sensor_ID_label | string | `Sensor_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Water_Class_label | string | `Water_Class` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Water_StatusID_label | string | `Water_StatusID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| SHAPE_Leng | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Water_Clas | string |  |
| Sensor_Dat | date32[day] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence | string |  |
| Field_Vali | string |  |
| Water_Stat | string |  |
| SenorID_ol | string |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20230504rwa-water-extent.parquet | 9.5 MB | 12201a9335bb... |
| ./fl20230504rwa-water-extent.pmtiles | 1.1 MB | 122060f13313... |
| ./styles/default.json | 1.0 KB | 1220db91e02e... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20230504rwa-water-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/damage-assessment-along-the-mukungwa-river-western-northern-provinces-rwanda-as-of-10-may-](https://data.humdata.org/dataset/damage-assessment-along-the-mukungwa-river-western-northern-provinces-rwanda-as-of-10-may-)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `PHR_20230510_WaterExtent_NyabihuDistrict_WesternProvince_RWA`, `S1_20230503_FloodExtent_KigaliCity_Surrounding`, `S1_20230505_FloodExtent_KigaliCity_Surrounding`, `S2_20230507_LandslideExtent_Kibingo_Surrounding`.

## Attribution

UNITAR-UNOSAT

## License

[other](https://opendefinition.org/licenses/cc-by-sa/)

## Contact

Portolan Mirrors <nissim@radiant.earth>

## Known Issues

HDX states the license as "Creative Commons Attribution Share-Alike (CC BY-SA)" with no version, so the collection's license is `other`, linked to the license definition HDX gives. This is a preliminary assessment and has not yet been validated in the field. It is important to consider the characteristics of the source imagery used in the analyses when interpreting results. For damage assessments it should be noted that only significant damage to the structural integrity of the buildings analyzed can be seen in imagery, while minor damage such as cracks or holes may not be visible at all. For flood extractions using radar data it is important to note that urban areas and highly vegetated areas may mask the flood signature and result in underestimation of flood waters. Users with specific questions or concerns should contact unosat@unitar.org to seek clarification.

---

*Generated by [Portolan](https://github.com/portolan-sdi/portolan-cli) from STAC metadata and .portolan/metadata.yaml*

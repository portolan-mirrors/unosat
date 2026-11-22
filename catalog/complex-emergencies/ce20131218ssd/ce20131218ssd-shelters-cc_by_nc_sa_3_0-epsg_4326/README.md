# Shelters: Complex emergency, South Sudan, 18 December 2013 (CE20131218SSD)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20131218ssd/ce20131218ssd-shelters-cc_by_nc_sa_3_0-epsg_4326/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Shelters for Complex emergency, South Sudan, 18 December 2013 (CE20131218SSD): 379,044 features merged from 43 source layers. Point layers with shelter or camp columns, or whose names mention camps, shelters, IDPs, or settlements. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of Bentiu IDP Camp, Rubkona County, Unity State, South Sudan](https://data.humdata.org/dataset/geodata-of-bentiu-idp-camp-rubkona-county-unity-state-south-sudan-march-24-2015)
- [Geodata of Bentiu IDP Camp, Rubkona County, Unity State, South Sudan](https://data.humdata.org/dataset/geodata-of-bentiu-idp-camp-rubkona-county-unity-state-south-sudan-november-16-2015)
- [Geodata of Damage Assesment In The City Of Malakal, Upper Nile State, South Sudan](https://data.humdata.org/dataset/geodata-of-damage-assesment-in-the-city-of-malakal-upper-nile-state-south-sud-march-21-2014)
- [Geodata of Damage Assesment in the City of Malakal, Upper Nile State, South Sudan](https://data.humdata.org/dataset/geodata-of-damage-assesment-in-the-city-of-malakal-upper-nile-state-south-sud-january-24-2014)
- [Geodata of Damage Assessment in the City of Bentiu, Unity State, South Sudan](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-the-city-of-bentiu-unity-state-south-sudan-january-18-2014)
- [Geodata of Damage assesment in the city of Bor, Jonglei State, South Sudan](https://data.humdata.org/dataset/geodata-of-damage-assesment-in-the-city-of-bor-jonglei-state-south-sudan-january-21-2014)
- [Geodata of Delthoma IDP Camp, Melut District, Upper Nile State, South Sudan](https://data.humdata.org/dataset/geodata-of-delthoma-idp-camp-melut-district-upper-nile-state-south-sudan-december-03-2015)
- [Geodata of Destruction in Leer, Unity State, South Sudan](https://data.humdata.org/dataset/geodata-of-destruction-in-leer-unity-state-south-sudan-february-07-2014)
- [Geodata of Destruction in Mayom, Unity State, South Sudan](https://data.humdata.org/dataset/geodata-of-destruction-in-mayom-unity-state-south-sudan-january-21-2014)
- [Geodata of Destruction in Rubkona, Unity State, South Sudan](https://data.humdata.org/dataset/geodata-of-destruction-in-rubkona-unity-state-south-sudan-january-16-2014)
- [Geodata of Gendrasa Refugee Camp, Maban County, Upper Nile State, South Sudan](https://data.humdata.org/dataset/geodata-of-gendrasa-refugee-camp-maban-county-upper-nile-state-south-sudan-july-01-2015)
- [Geodata of IDP Camp in Melut, Upper Nile State, South Sudan](https://data.humdata.org/dataset/geodata-of-idp-camp-in-melut-upper-nile-state-south-sudan-december-23-2014)
- and 25 more; the event's [catalog page](../catalog.json) lists them all.

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [29.78319030700004, 4.805453453000041, 33.71798538300004, 10.45357361300006]

## Temporal Coverage

- **Start**: 2014-01-09T00:00:00Z
- **End**: 2016-08-19T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Site_ID | string | Coded value. The source geodatabase domain gives: 1 = Tent Shelter; 2 = Metal Structure; 3 = Improvised Shelter (Wood / Stone / Mud); 4 = Admin Building; 5 = Semi-Permanent Structure. The decoded text is in `Site_ID_label`. |
| Sensor_ID | string | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Sensor_ID_label`, which is decoded per source file. |
| Sensor_Date | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence_ID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `Confidence_ID_label`. |
| Field_Validation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `Field_Validation_label`. |
| CampStatusID | int32 | Coded value. The source geodatabase domain gives: 0 = Closed / Relocated; 1 = Open (Operational); 2 = Planned / Under Construction; 9 = Camp Destroyed. The decoded text is in `CampStatusID_label`. |
| CampName | string |  |
| Notes | string | Free-text notes by the analyst. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | string | Coded value. The 4 source files of this collection use 4 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| CampType | string | Coded value. The source geodatabase domain gives: 1 = Refugee Camp; 2 = IDP Camp. The decoded text is in `CampType_label`. |
| CampTrend | string | Coded value. The source geodatabase domain gives: 1 = Increase; 2 = Decrease. The decoded text is in `CampTrend_label`. |
| Shelter_Status | int32 | Coded value. The source geodatabase domain gives: 1 = Open; 2 = Closed. The decoded text is in `Shelter_Status_label`. |
| ShelterClose_Date | timestamp[us, tz=UTC] |  |
| Structure_Type | int32 | Coded value. The source geodatabase domain gives: 1 = Tent Shelter; 2 = Admin Building; 3 = Improvised Shelter (Wood / Stone / Mud); 4 = Semi-Permanent Structure; 5 = Metal Structure. The decoded text is in `Structure_Type_label`. |
| CampStatusID_label | string | `CampStatusID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| CampTrend_label | string | `CampTrend` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| CampType_label | string | `CampType` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Confidence_ID_label | string | `Confidence_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Field_Validation_label | string | `Field_Validation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Sensor_ID_label | string | `Sensor_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Shelter_Status_label | string | `Shelter_Status` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Site_ID_label | string | `Site_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Structure_Type_label | string | `Structure_Type` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| Structure_material | string |  |
| Sensor_Dat | date32[day] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence | string |  |
| Field_Vali | string |  |
| CampStatus | string |  |
| Shelter_St | string |  |
| ShelterClo | date32[day] |  |
| Structure_ | string |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20131218ssd-shelters-cc_by_nc_sa_3_0-epsg_4326.parquet | 10.7 MB | 1220cd53243a... |
| ./ce20131218ssd-shelters-cc_by_nc_sa_3_0-epsg_4326.pmtiles | 10.8 MB | 1220420b3967... |
| ./styles/default.json | 992 B | 12200ef103a6... |
| ./ce20131218ssd-shelters-cc_by_nc_sa_3_0-epsg_4326.thumb.jpg | 4.5 KB | 1220a2a9007c... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20131218ssd-shelters-cc_by_nc_sa_3_0-epsg_4326.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-bentiu-idp-camp-rubkona-county-unity-state-south-sudan-march-24-2015](https://data.humdata.org/dataset/geodata-of-bentiu-idp-camp-rubkona-county-unity-state-south-sudan-march-24-2015)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `IDP_Juba_Shelters`, `IDP_Leitchour_Shelters`, `IDP_Malakal_Shelters`, `IDP_Minkaman_Shelters`, `IDP_Minkaman_Shelters_1`, `IDP_Minkaman_Structures_Feb2015`, `IDP_Structures_Bentiu_20151031`, `IDP_Structures_Bor`, `IDP_Structures_Delthoma_20151129`, `IDP_Structures_Juba_20160818`, `IDP_Structures_Juba_20160905`, `IDP_Structures_minkaman012016`, `IDP_UNMISS_Rubkona_Structures_20150307`, `IDP_WauShilluk_Shelters`, `IDP_Wunthou_Shelters`, `Juba_Structures_20160627`, `Melut_Structure_20141202`, `Refugee_Camp_Gendrasa_Shelters_20150408`.

## Attribution

UNITAR-UNOSAT

## License

[CC-BY-NC-SA-3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/)

## Contact

Portolan Mirrors <nissim@radiant.earth>

## Known Issues

This is a preliminary assessment and has not yet been validated in the field. It is important to consider the characteristics of the source imagery used in the analyses when interpreting results. For damage assessments it should be noted that only significant damage to the structural integrity of the buildings analyzed can be seen in imagery, while minor damage such as cracks or holes may not be visible at all. For flood extractions using radar data it is important to note that urban areas and highly vegetated areas may mask the flood signature and result in underestimation of flood waters. Users with specific questions or concerns should contact unosat@unitar.org to seek clarification.

---

*Generated by [Portolan](https://github.com/portolan-sdi/portolan-cli) from STAC metadata and .portolan/metadata.yaml*

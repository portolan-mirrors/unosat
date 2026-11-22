# Shelters: Complex emergency, Somalia, 10 July 2013 (CE20130710SOM)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20130710som/ce20130710som-shelters-cc_by_nc_sa_3_0/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Shelters for Complex emergency, Somalia, 10 July 2013 (CE20130710SOM): 227,465 features merged from 35 source layers. Point layers with shelter or camp columns, or whose names mention camps, shelters, IDPs, or settlements. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of IDP Settlements and Shelters in Kismayo, Lower Juba, Somalia](https://data.humdata.org/dataset/geodata-of-idp-settlements-and-shelters-in-kismayo-lower-juba-somalia-april-30-2014)
- [Geodata of IDP Settlements and Shelters in Kismayo, Lower Juba, Somalia](https://data.humdata.org/dataset/geodata-of-idp-settlements-and-shelters-in-kismayo-lower-juba-somalia-july-03-2014)
- [Geodata of IDP Settlements and shelters in Luuq, Gedo Province, Somalia](https://data.humdata.org/dataset/geodata-of-idp-settlements-and-shelters-in-luuq-gedo-province-somalia-june-30-2014)
- [Geodata of IDP Shelter Changes in Baidoa, Somalia, Between 21 August 2013 and 08 February 2014](https://data.humdata.org/dataset/geodata-of-idp-shelter-changes-in-baidoa-somalia-between-21-august-2013-and-0-march-18-2014)
- [Geodata of IDP Shelter changes in Baidoa, Somalia, Between 08 February and 02 October 2014](https://data.humdata.org/dataset/geodata-of-idp-shelter-changes-in-baidoa-somalia-between-08-february-and-02-o-october-31-2014)
- [Geodata of IDP Shelter changes in Hargeisa, Somalia between 20 August 2012 and 02 November 2014](https://data.humdata.org/dataset/geodata-of-idp-shelter-changes-in-hargeisa-somalia-between-20-august-2012-and-december-17-2014)
- [Geodata of IDP Shelters Detected in Galkayo, Somalia](https://data.humdata.org/dataset/geodata-of-idp-shelters-detected-in-galkayo-somalia-april-09-2014)
- [Geodata of IDP Shelters Detected, North of Galkayo, Somalia](https://data.humdata.org/dataset/geodata-of-idp-shelters-detected-north-of-galkayo-somalia-may-27-2014)
- [Geodata of IDP shelter Changes in Kismayo, Somalia, Between 11 August 2013 - 05 March 2014](https://data.humdata.org/dataset/geodata-of-idp-shelter-changes-in-kismayo-somalia-between-11-august-2013-05-m-march-18-2014)
- [Geodata of Informal IDP shelters in border town of Doolow, Somalia](https://data.humdata.org/dataset/geodata-of-informal-idp-shelters-in-border-town-of-doolow-somalia-october-28-2014)
- [Geodata of UPDATE: IDP Shelter density in Daynile and Dharkenley District, Mogadishu, Somalia](https://data.humdata.org/dataset/geodata-of-idp-shelter-density-in-daynile-and-dharkenley-district-mogadishu-november-10-2014)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [42.06198845300008, -0.36957953699993595, 49.21329788600008, 11.289102686000092]

## Temporal Coverage

- **Start**: 2014-03-18T00:00:00Z
- **End**: 2014-12-17T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Site_ID | string | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Site_ID_label`, which is decoded per source file. |
| Sensor_ID | string | Coded value. The 6 source files of this collection use 6 different domains for it, so read `Sensor_ID_label`, which is decoded per source file. |
| Sensor_Date | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence_ID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `Confidence_ID_label`. |
| Field_Validation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `Field_Validation_label`. |
| CampStatusID | int32 | Coded value. The source geodatabase domain gives: 0 = Closed / Relocated; 1 = Open (Operational); 2 = Planned / Under Construction; 9 = Camp Destroyed. The decoded text is in `CampStatusID_label`. |
| CampName | string |  |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| CampQuicklook | int32 |  |
| Notes | string | Free-text notes by the analyst. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | string | Coded value. The 4 source files of this collection use 4 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| City_Town | string |  |
| CampStatusID_label | string | `CampStatusID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Confidence_ID_label | string | `Confidence_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Field_Validation_label | string | `Field_Validation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Sensor_ID_label | string | `Sensor_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Site_ID_label | string | `Site_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| Sensor_Dat | date32[day] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence | string |  |
| Field_Vali | string |  |
| CampStatus | string |  |
| CampType | int32 | Coded value. The source geodatabase domain gives: 1 = Refugee Camp; 2 = IDP Camp. The decoded text is in `CampType_label`. |
| CampTrend | int32 | Coded value. The source geodatabase domain gives: 1 = Increase; 2 = Decrease. The decoded text is in `CampTrend_label`. |
| Shelter_Status | int32 | Coded value. The source geodatabase domain gives: 1 = Open; 2 = Closed. The decoded text is in `Shelter_Status_label`. |
| ShelterClose_Date | timestamp[us, tz=UTC] |  |
| Structure_Type | int32 | Coded value. The source geodatabase domain gives: 1 = Tent Shelter; 2 = Admin Building; 3 = Improvised Shelter (Wood / Stone / Mud); 4 = Semi-Permanent Structure; 5 = Metal Structure. The decoded text is in `Structure_Type_label`. |
| CampTrend_label | string | `CampTrend` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| CampType_label | string | `CampType` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Shelter_Status_label | string | `Shelter_Status` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Structure_Type_label | string | `Structure_Type` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| MetalRoof | int16 |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20130710som-shelters-cc_by_nc_sa_3_0.parquet | 7.0 MB | 1220ce7ce39e... |
| ./ce20130710som-shelters-cc_by_nc_sa_3_0.pmtiles | 6.7 MB | 1220bedf1adb... |
| ./styles/default.json | 929 B | 12200f3328b9... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20130710som-shelters-cc_by_nc_sa_3_0.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-idp-settlements-and-shelters-in-kismayo-lower-juba-somalia-april-30-2014](https://data.humdata.org/dataset/geodata-of-idp-settlements-and-shelters-in-kismayo-lower-juba-somalia-april-30-2014)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Afgooye_corridor_k7k13_Structures`, `Baidoa_Structures_20130821`, `Baidoa_Structures_20140208`, `Baidoa_Structures_20140208_v2`, `Baidoa_Structures_20141002`, `BarigaBososo_Structure_20141020`, `DaynileDarkheneyStructures_20141009`, `Doolow_Structures`, `Galkayo_Structures`, `Hargeisa_Structures_20141102`, `IDP_Structures`, `Kismayo_Structures_20140305`, `Kismayo_Structures_20140503`, `Luuq_Shelters`, `Luuq_Structures_20140607`.

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

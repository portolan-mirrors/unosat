# Shelters: Complex emergency, Syrian Arab Republic, 4 June 2013 (CE20130604SYR)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20130604syr/ce20130604syr-shelters-cc_by_nc_sa_3_0-epsg_4326/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Shelters for Complex emergency, Syrian Arab Republic, 4 June 2013 (CE20130604SYR): 863,677 features merged from 36 source layers. Point layers with shelter or camp columns, or whose names mention camps, shelters, IDPs, or settlements. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of Bab Al Salame IDP Camp, A'Zaz District, Aleppo Governorate, Syria](https://data.humdata.org/dataset/geodata-of-bab-al-salame-idp-camp-azaz-district-aleppo-governorate-syria-june-12-2015)
- [Geodata of Domiz Refugee Camp,  Duhok Governorate, Iraq](https://data.humdata.org/dataset/geodata-of-domiz-refugee-camp-duhok-governorate-iraq-january-10-2014)
- [Geodata of Oncunipar Refugee Camp, Merkez District, Kilis Province, Turkey](https://data.humdata.org/dataset/geodata-of-oncunipar-refugee-camp-merkez-district-kilis-province-turkey-june-16-2015)
- [Geodata of Rubkan Border Crossing IDP Settlement, Homs Governorate, Syria](https://data.humdata.org/dataset/geodata-of-rubkan-border-crossing-idp-settlement-homs-governorate-syria-july-31-2014)
- [Geodata of Shelter Density Map at Rukban Border Crossing, Jordan-Syria Border](https://data.humdata.org/dataset/geodata-of-shelter-density-map-at-rukban-border-crossing-jordan-syria-border-april-29-2016)
- [Geodata of Shelter Density Map at Rukban Border Crossing, Jordan-Syria Border](https://data.humdata.org/dataset/geodata-of-shelter-density-map-at-rukban-border-crossing-jordan-syria-border-june-09-2016)
- [Geodata of Shelter Density Map at Rukban Border crossing, Jordan-Syria Border](https://data.humdata.org/dataset/geodata-of-shelter-density-map-at-rukban-border-crossing-jordan-syria-border-july-27-2016)
- [Geodata of Shelter Density map at Rukban Border crossing, Jordan-Syria Border](https://data.humdata.org/dataset/geodata-of-shelter-density-map-at-rukban-border-crossing-jordan-syria-border-june-28-2016)
- [Geodata of Shelters at Hadalat Border Crossing, Jordan-Syria Border](https://data.humdata.org/dataset/geodata-of-shelters-at-hadalat-border-crossing-jordan-syria-border)
- [Geodata of Shelters at Hadalat Border Crossing, Jordan-Syria Border](https://data.humdata.org/dataset/geodata-of-shelters-at-hadalat-border-crossing-jordan-syria-border-july-14-2016)
- [Geodata of Shelters at Hadalat Border Crossing, Jordan-Syria Border](https://data.humdata.org/dataset/geodata-of-shelters-at-hadalat-border-crossing-jordan-syria-border-june-09-2016)
- [Geodata of Shelters at Hadalat Border Crossing, Jordan-Syria Border](https://data.humdata.org/dataset/geodata-of-shelters-at-hadalat-border-crossing-jordan-syria-border-may-09-2016)
- and 13 more; the event's [catalog page](../catalog.json) lists them all.

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [36.310496432000036, 31.886418854000055, 42.89250750600007, 36.787830254000085]

## Temporal Coverage

- **Start**: 2014-01-10T00:00:00Z
- **End**: 2016-08-17T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Site_ID | string | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Site_ID_label`, which is decoded per source file. |
| Sensor_ID | string | Coded value. The 4 source files of this collection use 4 different domains for it, so read `Sensor_ID_label`, which is decoded per source file. |
| Sensor_Date | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence_ID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `Confidence_ID_label`. |
| Field_Validation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `Field_Validation_label`. |
| CampStatusID | int32 | Coded value. The source geodatabase domain gives: 0 = Closed / Relocated; 1 = Open (Operational); 2 = Planned / Under Construction; 9 = Camp Destroyed. The decoded text is in `CampStatusID_label`. |
| CampName | string |  |
| Notes | string | Free-text notes by the analyst. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | string | Coded value. The 5 source files of this collection use 5 different domains for it, so read `StaffID_label`, which is decoded per source file. |
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
| Sensor_Dat | date32[day] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence | string |  |
| Field_Vali | string |  |
| CampStatus | string |  |
| Shelter_St | string |  |
| ShelterClo | date32[day] |  |
| Structure_ | string |  |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| CampQuicklook | int32 |  |
| City_Town | string |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20130604syr-shelters-cc_by_nc_sa_3_0-epsg_4326.parquet | 20.8 MB | 1220ca08ccc0... |
| ./ce20130604syr-shelters-cc_by_nc_sa_3_0-epsg_4326.pmtiles | 10.2 MB | 1220ae1b8199... |
| ./styles/default.json | 1002 B | 1220fd259d96... |
| ./ce20130604syr-shelters-cc_by_nc_sa_3_0-epsg_4326.thumb.jpg | 4.8 KB | 122023983369... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20130604syr-shelters-cc_by_nc_sa_3_0-epsg_4326.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-2-al-azraq-refugee-camp-az-zarqa-governorate-jordan-january-17-2014](https://data.humdata.org/dataset/geodata-of-2-al-azraq-refugee-camp-az-zarqa-governorate-jordan-january-17-2014)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Al_Kamoune_Structures_20160416`, `Al_Zaatari_Shelters`, `Al_Zaatari_Shelters_1`, `Azraq_Shelters`, `Azraq_Shelters_20140426`, `BabAlSalame_Structure_20150605`, `Domiz_Shelters`, `Hadalat_Structures_20141202`, `Hadalat_Structures_20150421`, `Hadalat_Structures_20150830`, `Hadalat_Structures_20160129`, `Hadalat_Structures_20160429`, `Hadalat_Structures_20160514`, `Hadalat_Structures_20160713`, `Hadalat_Structures_20160905`, `Hadalat_Structures_20161018`, `Hadalat_Structures_20161112`, `Hadalat_Structures_20170124`, `Hadalat_Structures_20170304`, `Oncunipar_Structures_20150605`, `Rubkan_Shelters`, `Rukban_Structures_20160523`, `Rukban_Structures_20160624`, `Rukban_Structures_20160725`, `Sujjo_Structure_20150605`.

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

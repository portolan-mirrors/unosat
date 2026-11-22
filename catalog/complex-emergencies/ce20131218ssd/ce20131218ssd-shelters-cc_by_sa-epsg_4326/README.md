# Shelters: Complex emergency, South Sudan, 18 December 2013 (CE20131218SSD)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20131218ssd/ce20131218ssd-shelters-cc_by_sa-epsg_4326/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Shelters for Complex emergency, South Sudan, 18 December 2013 (CE20131218SSD): 118,279 features merged from 14 source layers. Point layers with shelter or camp columns, or whose names mention camps, shelters, IDPs, or settlements. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [South Sudan - IDP Shelters in UN House Compound, Juba, Central Equatoria](https://data.humdata.org/dataset/idp-shelters-in-un-house-compound-juba-central-equatoria-south-sudan)
- [Structures at the Doro settlement in South Sudan](https://data.humdata.org/dataset/structures-at-the-doro-settlement-in-south-sudan-2752)
- [Structures at the Yusuf Batil settlement in South Sudan.](https://data.humdata.org/dataset/structures-at-the-yusuf-batil-settlement-in-south-sudan-2751)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [27.959562831000028, 3.7316573420000623, 33.775181674000066, 10.128694832000065]

## Temporal Coverage

- **Start**: 2016-08-19T00:00:00Z
- **End**: 2018-01-03T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Site_ID | int16 | Coded value. The source geodatabase domain gives: 1 = Tent Shelter; 2 = Metal Structure; 3 = Improvised Shelter (Wood / Stone / Mud); 4 = Admin Building; 5 = Semi-Permanent Structure. The decoded text is in `Site_ID_label`. |
| Sensor_Date | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence_ID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `Confidence_ID_label`. |
| Field_Validation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `Field_Validation_label`. |
| CampStatusID | int32 | Coded value. The source geodatabase domain gives: 0 = Closed / Relocated; 1 = Open (Operational); 2 = Planned / Under Construction; 9 = Camp Destroyed. The decoded text is in `CampStatusID_label`. |
| CampName | string |  |
| Notes | string | Free-text notes by the analyst. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| CampType | int32 | Coded value. The source geodatabase domain gives: 1 = Refugee Camp; 2 = IDP Camp. The decoded text is in `CampType_label`. |
| CampTrend | int32 | Coded value. The source geodatabase domain gives: 1 = Increase; 2 = Decrease. The decoded text is in `CampTrend_label`. |
| Shelter_Status | int32 | Coded value. The source geodatabase domain gives: 1 = Open; 2 = Closed. The decoded text is in `Shelter_Status_label`. |
| ShelterClose_Date | timestamp[us, tz=UTC] |  |
| Structure_Type | int32 | Coded value. The source geodatabase domain gives: 1 = Tent Shelter; 2 = Admin Building; 3 = Improvised Shelter (Wood / Stone / Mud); 4 = Semi-Permanent Structure; 5 = Metal Structure. The decoded text is in `Structure_Type_label`. |
| StaffID | string | Coded value. The 3 source files of this collection use 3 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| Sensor_ID | string | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Sensor_ID_label`, which is decoded per source file. |
| CampStatusID_label | string | `CampStatusID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| CampTrend_label | string | `CampTrend` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| CampType_label | string | `CampType` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Confidence_ID_label | string | `Confidence_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Field_Validation_label | string | `Field_Validation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Shelter_Status_label | string | `Shelter_Status` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Site_ID_label | string | `Site_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Structure_Type_label | string | `Structure_Type` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| Sensor_ID_label | string | `Sensor_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20131218ssd-shelters-cc_by_sa-epsg_4326.parquet | 4.4 MB | 1220c82da2fb... |
| ./ce20131218ssd-shelters-cc_by_sa-epsg_4326.pmtiles | 2.5 MB | 12208d95fc21... |
| ./styles/default.json | 947 B | 1220e7875cd4... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20131218ssd-shelters-cc_by_sa-epsg_4326.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/idp-shelters-in-un-house-compound-juba-central-equatoria-south-sudan](https://data.humdata.org/dataset/idp-shelters-in-un-house-compound-juba-central-equatoria-south-sudan)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `IDP_Structures_AjuonThok_20170401_1`, `IDP_Structures_Batil_20171031`, `IDP_Structures_Doro_20171111`, `IDP_Structures_Ganyel_20170108`, `IDP_Structures_Gendrassa_20171031`, `IDP_Structures_Juba_20160905`, `IDP_Structures_Juba_20170208`, `IDP_Structures_Kaya_20170324`, `IDP_Structures_Kerwak_20170201`, `IDP_Structures_Logo_20170403`, `IDP_Structures_Nyal_20170108`, `IDP_Structures_Pamir_20170511`, `IDP_Structures_Wau_20161215`, `IDP_Structures_Yida_20170606_1`.

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

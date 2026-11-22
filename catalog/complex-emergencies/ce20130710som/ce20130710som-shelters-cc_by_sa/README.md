# Shelters: Complex emergency, Somalia, 10 July 2013 (CE20130710SOM)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20130710som/ce20130710som-shelters-cc_by_sa/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Shelters for Complex emergency, Somalia, 10 July 2013 (CE20130710SOM): 51,087 features merged from 3 source layers. Point layers with shelter or camp columns, or whose names mention camps, shelters, IDPs, or settlements. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Somalia - Displaced Persons' Shelters in Dalxiska](https://data.humdata.org/dataset/displaced-persons-shelters-in-dalxiska-somalia)
- [Somalia - Internally Displaced Persons Shelters in Baidoa Town](https://data.humdata.org/dataset/internally-displaced-persons-shelters-in-baidoa-town)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![geodata](https://img.shields.io/badge/geodata-blue) ![populated places-settlements](https://img.shields.io/badge/populated_places--settlements-blue)

## Spatial Coverage

- **Bounding Box**: [42.55892067100007, -0.34287225899993246, 43.678458387000035, 3.157742237000093]

## Temporal Coverage

- **Start**: 2016-10-06T00:00:00Z
- **End**: 2017-05-09T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Site_ID | int16 | Coded value. The source geodatabase domain gives: 1 = Tent Shelter; 2 = Metal Structure; 3 = Improvised Shelter (Wood / Stone / Mud); 4 = Admin Building; 5 = Semi-Permanent Structure. The decoded text is in `Site_ID_label`. |
| Sensor_ID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Sensor_ID_label`, which is decoded per source file. |
| Sensor_Date | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence_ID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `Confidence_ID_label`. |
| Field_Validation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `Field_Validation_label`. |
| CampStatusID | int32 | Coded value. The source geodatabase domain gives: 0 = Closed / Relocated; 1 = Open (Operational); 2 = Planned / Under Construction; 9 = Camp Destroyed. The decoded text is in `CampStatusID_label`. |
| CampName | string |  |
| Notes | string | Free-text notes by the analyst. |
| StaffID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| CampType | int32 | Coded value. The source geodatabase domain gives: 1 = Refugee Camp; 2 = IDP Camp. The decoded text is in `CampType_label`. |
| CampTrend | int32 | Coded value. The source geodatabase domain gives: 1 = Increase; 2 = Decrease. The decoded text is in `CampTrend_label`. |
| Shelter_Status | int32 | Coded value. The source geodatabase domain gives: 1 = Open; 2 = Closed. The decoded text is in `Shelter_Status_label`. |
| ShelterClose_Date | timestamp[us, tz=UTC] |  |
| Structure_Type | int32 | Coded value. The source geodatabase domain gives: 1 = Tent Shelter; 2 = Admin Building; 3 = Improvised Shelter (Wood / Stone / Mud); 4 = Semi-Permanent Structure; 5 = Metal Structure. The decoded text is in `Structure_Type_label`. |
| GlobalID | string | ArcGIS global identifier of the feature. |
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
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20130710som-shelters-cc_by_sa.parquet | 2.1 MB | 1220e4365b2e... |
| ./ce20130710som-shelters-cc_by_sa.pmtiles | 2.6 MB | 12207e2ffe8f... |
| ./styles/default.json | 901 B | 1220b02159b2... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20130710som-shelters-cc_by_sa.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/displaced-persons-shelters-in-dalxiska-somalia](https://data.humdata.org/dataset/displaced-persons-shelters-in-dalxiska-somalia)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Baidoa_Structures_20170122`, `Baidoa_Structures_20170421`, `Dalxiska_Structures_20160908`.

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

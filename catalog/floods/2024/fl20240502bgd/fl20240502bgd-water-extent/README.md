# Water extent: Flood, Bangladesh, 2 May 2024 (FL20240502BGD)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2024/fl20240502bgd/fl20240502bgd-water-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Water extent for Flood, Bangladesh, 2 May 2024 (FL20240502BGD): 2,128 features merged from 38 source layers. Polygon layers with a water class column (such as `Water_Class`), or whose names mention flood, water, or inundation: satellite-detected water. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Building Damage Assessment in Shyamnagar Upazila, Bagerhat District, Khulna Division, Bangladesh as of 10 June 2024](https://data.humdata.org/dataset/building-damage-assessment-in-shyamnagar-upazila-bagerhat-district-khulna-division-banglad)
- [Cumulative Satellite Detected Waters over Sylhet Division, Bangladesh as of 19 & 22 June 2024](https://data.humdata.org/dataset/cumulative-satellite-detected-waters-over-sylhet-division-bangladesh-as-of-19-22-june-2024)
- [Flood impact analysis in Chhatak Upazila, Sunamganj District, Sylhet Division, Bangladesh as of 26 June 2024](https://data.humdata.org/dataset/flood-impact-analysis-in-chhatak-upazila-sunamganj-district-sylhet-division-bangladesh-as-)
- [Flood impact analysis in Sunamganj Sadar and Bishwambarpur Upazilas, Sunamganj District, Sylhet Division, Bangladesh as of 26 June 2024](https://data.humdata.org/dataset/flood-impact-analysis-in-sunamganj-sadar-and-bishwambarpur-upazilas-sunamganj-district-syl)
- [Flood impact analysis in Sylhet District, Sylhet Division, Bangladesh as of 26 June 2024](https://data.humdata.org/dataset/flood-impact-analysis-in-sylhet-district-sylhet-division-bangladesh-as-of-26-june-2024)
- [Satellite detected water extent over Barisal, Dhaka and Khulna Divisions, Bangladesh as of 1 June 2024](https://data.humdata.org/dataset/water-extent-over-barisal-dhaka-and-khulna-divisions-bangladesh-as-of-1-june-2024)
- [Satellite detected water extent over Satkhira and Khulna Districts, Khulna Divisions, Bangladesh as of 1 June 2024](https://data.humdata.org/dataset/water-extent-over-satkhira-and-khulna-districts-khulna-divisions-bangladesh-as-of-1-june-2)
- [Satellite detected water extents between 16 & 23 July 2024 in Bangladesh](https://data.humdata.org/dataset/satellite-detected-water-extents-between-16-23-july-2024-in-bangladesh)
- [Satellite detected water extents between 4 & 11 July 2024 in Bangladesh](https://data.humdata.org/dataset/satellite-detected-water-extents-between-4-11-july-2024-in-bangladesh)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![cyclones-hurricanes-typhoons](https://img.shields.io/badge/cyclones--hurricanes--typhoons-blue) ![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [88.02133328300005, 20.627564711000048, 92.65130241817212, 26.63403860200009]

## Temporal Coverage

- **Start**: 2024-06-04T00:00:00Z
- **End**: 2024-07-31T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Water_Class | int16 | Coded value. The source geodatabase domain gives: 0 = Archive Water Extent / Pre-Flood Water; 1 = Flood Water; 2 = Satellite Detected Water / Possible Saturated Soil; 3 = Probable Flash Flood-Affected Land; 4 = Aquaculture; 5 = Possible Satuated, wet soil; 6 = Tsunami-Affected Land; 7 = Maximum Satellite Observed Water (Cumulative); 8 = Swamp / Marsh / Mangrove; 9 = Snow Cover. The decoded text is in `Water_Class_label`. |
| Sensor_ID | string | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Sensor_ID_label`, which is decoded per source file. |
| Sensor_Date | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence_ID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `Confidence_ID_label`. |
| Field_Validation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `Field_Validation_label`. |
| Water_StatusID | int32 | Coded value. The source geodatabase domain gives: 1 = New Water / Water Increase; 2 = No water change / Static Level; 3 = No water / Water levels decreased. The decoded text is in `Water_StatusID_label`. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| SenorID_old | int16 | Coded value. The source geodatabase domain gives: 1 = MODIS; 2 = ASAR WSM; 3 = ASAR IMP; 4 = Radarsat; 5 = DMC; 6 = SPOT5; 7 = ALOS Palsar WB1; 8 = ASAR APP. The decoded text is in `SenorID_old_label`. |
| StaffID | string | Coded value. The 3 source files of this collection use 3 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
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
| FID_S1_20240619_20240622_AnalysisExtent_Sylhet | int32 |  |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int64 |  |
| FID_S1_20240619_20240622_WaterExtent_Sylhet1 | int32 |  |
| Notes_1 | string |  |
| Area_m2_1 | double |  |
| Area_ha_1 | double |  |
| StaffID_1 | int64 |  |
| EventCode_1 | string |  |
| Water_Clas | string |  |
| Sensor_Dat | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence | string |  |
| Field_Vali | string |  |
| Water_Stat | string |  |
| SenorID_ol | string |  |
| SHAPE_Leng | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| FID_S1_202 | int64 |  |
| FID_S1_203 | int64 |  |
| EventCode_ | string |  |
| Water_Cl_1 | string |  |
| Sensor_D_1 | date32[day] |  |
| Confiden_1 | string |  |
| Field_Va_1 | string |  |
| Water_St_1 | string |  |
| SenorID__1 | string |  |
| FID_bgd_ad | int64 |  |
| ADM3_EN | string |  |
| ADM3_PCODE | string |  |
| ADM3_REF | string |  |
| ADM3ALT1EN | string |  |
| ADM3ALT2EN | string |  |
| ADM2_EN | string |  |
| ADM2_PCODE | string |  |
| ADM1_EN | string |  |
| ADM1_PCODE | string |  |
| ADM0_EN | string |  |
| ADM0_PCODE | string |  |
| Area | double |  |
| FL_Area | double |  |
| st1_31ma_5 | double |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20240502bgd-water-extent.parquet | 538.8 MB | 1220d7c46e2d... |
| ./fl20240502bgd-water-extent.pmtiles | 201.4 MB | 122068731894... |
| ./styles/default.json | 972 B | 12202e3f40b8... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20240502bgd-water-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/building-damage-assessment-in-shyamnagar-upazila-bagerhat-district-khulna-division-banglad](https://data.humdata.org/dataset/building-damage-assessment-in-shyamnagar-upazila-bagerhat-district-khulna-division-banglad)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `GLOBAL_20240626_FloodExtent_Sunamganj`, `PHR_20240626_FloodExtent_SunamganjSadar`, `S1_20240619_20240622_FloodExtent_Sylhet`, `S1_20240619_20240622_WaterExtent_Sylhet`, `SAOCOM_20240626_FloodExtent_Sylhet`, `ST1_20240601_FloodExtent_Bangladesh`, `ST1_20240622_20240629_FloodExtent_Bangladesh`, `ST1_20240704_20240711_FloodExtent_Bangladesh`, `ST1_20240716_20240723_FloodExtent_Bangladesh`, `TDX1_20240601_FloodWater_Satkhira`.

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

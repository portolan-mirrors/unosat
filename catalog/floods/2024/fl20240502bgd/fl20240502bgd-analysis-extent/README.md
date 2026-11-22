# Analysis extent: Flood, Bangladesh, 2 May 2024 (FL20240502BGD)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2024/fl20240502bgd/fl20240502bgd-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Analysis extent for Flood, Bangladesh, 2 May 2024 (FL20240502BGD): 67 features merged from 67 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Building Damage Assessment in Bagerhat District, Khulna Division, Bangladesh as of 4 June 2024](https://data.humdata.org/dataset/building-damage-assessment-in-bagerhat-district-khulna-division-bangladesh-as-of-4-june-20)
- [Building Damage Assessment in Paikgachha Upazila, Khulna District, Khulna Division, Bangladesh as of 4 June 2024](https://data.humdata.org/dataset/building-damage-assessment-in-paikgachha-upazila-khulna-district-khulna-division-banglades)
- [Building Damage Assessment in Rampal Upazila Bagerhat District, Khulna Division, Bangladesh as of 4 June 2024](https://data.humdata.org/dataset/building-damage-assessment-in-rampal-upazila-bagerhat-district-khulna-division-bangladesh-)
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

- **Bounding Box**: [88.00862798600008, 20.590609348000044, 92.68030687500004, 26.634513010000035]

## Temporal Coverage

- **Start**: 2024-06-04T00:00:00Z
- **End**: 2024-07-31T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Site_ID | int32 | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Stadium; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 42 = Military Facility; 45 = Suspected Mass Grave Site; 46 = Airport Facility; 47 = Church; 48 = Dam; 49 = Port. The decoded text is in `Site_ID_label`. |
| AgencyID | int64 |  |
| SiteName | string |  |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Site_ID_label | string | `Site_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int64 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `SensorID_label`, which is decoded per source file. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | string | Coded value. The 2 source files of this collection use 2 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Staff_ID | int64 |  |
| ConfidenceID_label | string | `ConfidenceID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| FieldValidation_label | string | `FieldValidation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SHAPE_Leng | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Confidence | int32 |  |
| FieldValid | int32 |  |
| Sensor_ID | string |  |
| ADM0_PCODE | string |  |
| Area | double |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20240502bgd-analysis-extent.parquet | 2.7 MB | 122020a2d965... |
| ./fl20240502bgd-analysis-extent.pmtiles | 3.0 MB | 12205abcafb4... |
| ./styles/default.json | 671 B | 12208c174564... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20240502bgd-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/building-damage-assessment-in-bagerhat-district-khulna-division-bangladesh-as-of-4-june-20](https://data.humdata.org/dataset/building-damage-assessment-in-bagerhat-district-khulna-division-bangladesh-as-of-4-june-20)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `PHR_20240604_AnalysisExtent_Morrelganj`, `PHR_20240604_AnalysisExtent_Paikgachha`, `PHR_20240604_AnalysisExtent_Rampal`, `PHR_20240626_CloudObstruction_SunamganjSadar`, `S1_20240619_20240622_AnalysisExtent_Sylhet`, `SAOCOM_20240626_AnalysisExtent_Sylhet_1`, `ST1_20240601_AnalysisExtent_Bangladesh`, `ST1_20240622_20240629_AnalysisExtent_Bangladesh`, `ST1_20240704_20240711_AnalysisExtent_Bangladesh`, `ST1_20240716_20240723_AnalysisExtent_Bangladesh`, `TDX1_20240601_AnalysisExtent_Satkhira`, `WV2_20240610_AnalysisExtent_Shyamnagar`.

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

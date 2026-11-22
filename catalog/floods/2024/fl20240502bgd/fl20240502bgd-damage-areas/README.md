# Damage areas: Flood, Bangladesh, 2 May 2024 (FL20240502BGD)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2024/fl20240502bgd/fl20240502bgd-damage-areas/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Damage areas for Flood, Bangladesh, 2 May 2024 (FL20240502BGD): 432,638 features merged from 12 source layers. Polygon layers with a damage class column: damaged areas, zones, or density cells. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Flood impact analysis in Chhatak Upazila, Sunamganj District, Sylhet Division, Bangladesh as of 26 June 2024](https://data.humdata.org/dataset/flood-impact-analysis-in-chhatak-upazila-sunamganj-district-sylhet-division-bangladesh-as-)
- [Flood impact analysis in Sunamganj Sadar and Bishwambarpur Upazilas, Sunamganj District, Sylhet Division, Bangladesh as of 26 June 2024](https://data.humdata.org/dataset/flood-impact-analysis-in-sunamganj-sadar-and-bishwambarpur-upazilas-sunamganj-district-syl)
- [Flood impact analysis in Sylhet District, Sylhet Division, Bangladesh as of 26 June 2024](https://data.humdata.org/dataset/flood-impact-analysis-in-sylhet-district-sylhet-division-bangladesh-as-of-26-june-2024)
- [Satellite detected water extents between 16 & 23 July 2024 in Bangladesh](https://data.humdata.org/dataset/satellite-detected-water-extents-between-16-23-july-2024-in-bangladesh)
- [Satellite detected water extents between 4 & 11 July 2024 in Bangladesh](https://data.humdata.org/dataset/satellite-detected-water-extents-between-4-11-july-2024-in-bangladesh)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [91.34024100000005, 24.846397255000056, 91.89434905000007, 25.149153333000072]

## Temporal Coverage

- **Start**: 2024-06-29T00:00:00Z
- **End**: 2024-07-31T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SiteID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `SiteID_label`, which is decoded per source file. |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int64 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `SensorID_label`, which is decoded per source file. |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Settlement_Name | string |  |
| Notes | string | Free-text notes by the analyst. |
| Main_Damage_Site_Class | int16 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Main_Damage_Site_Class_label`, which is decoded per source file. |
| Grouped_Damage_Classes | int16 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Grouped_Damage_Classes_label`, which is decoded per source file. |
| StaffID | string | Coded value. The 2 source files of this collection use 2 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| ImageID_Num | int32 |  |
| Shape_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Shape_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| ConfidenceID_label | string | `ConfidenceID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| FieldValidation_label | string | `FieldValidation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Grouped_Damage_Classes_label | string | `Grouped_Damage_Classes` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Main_Damage_Site_Class_label | string | `Main_Damage_Site_Class` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SiteID_label | string | `SiteID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| Confidence | string |  |
| FieldValid | int32 |  |
| Settlement | string |  |
| Main_Damag | int32 |  |
| Grouped_Da | int32 |  |
| ImageID_Nu | int64 |  |
| Shape_Leng | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Water_Clas | string |  |
| Sensor_ID | string |  |
| Sensor_Dat | date32[day] | Acquisition date of the satellite image the feature was mapped from. |
| Field_Vali | string |  |
| Water_Stat | string |  |
| SenorID_ol | string |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20240502bgd-damage-areas.parquet | 12.6 MB | 122076c55a00... |
| ./fl20240502bgd-damage-areas.pmtiles | 28.5 MB | 1220cde0296d... |
| ./styles/default.json | 913 B | 1220b9adeed1... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20240502bgd-damage-areas.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/flood-impact-analysis-in-chhatak-upazila-sunamganj-district-sylhet-division-bangladesh-as-](https://data.humdata.org/dataset/flood-impact-analysis-in-chhatak-upazila-sunamganj-district-sylhet-division-bangladesh-as-)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `GLOBAL_20240626_FloodedStructure_Sunamganj`, `PHR_20240626_FloodedStructure_SunamganjSadar`, `SAOCOM_20240626_FloodedStructure_Sylhet`.

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

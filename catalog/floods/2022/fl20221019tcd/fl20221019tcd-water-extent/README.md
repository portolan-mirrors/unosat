# Water extent: Flood, Chad, 19 October 2022 (FL20221019TCD)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2022/fl20221019tcd/fl20221019tcd-water-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Water extent for Flood, Chad, 19 October 2022 (FL20221019TCD): 49 features merged from 49 source layers. Polygon layers with a water class column (such as `Water_Class`), or whose names mention flood, water, or inundation: satellite-detected water. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Satellite detected water extent between 30 October 2022 and 31 October 2018 in Hadjer-Lamis & Lac Regions, Chad](https://data.humdata.org/dataset/water-extent-between-30-october-2022-and-31-october-2018-in-hadjer-lamis-lac-regions-chad)
- [Satellite detected water extent in N'Djamena and Chari Departments, Chad as of 30 October 2022](https://data.humdata.org/dataset/water-extent-in-n-djamena-and-chari-departments-chad-as-of-30-october-2022)
- [Satellite detected water extent in N'Djamena department, N'Djamena Region, Chad as of 20 October 2022](https://data.humdata.org/dataset/water-extent-in-n-djamena-department-n-djamena-region-chad-as-of-20-october-2022)
- [Satellite detected water extent in N'Djamena department, N'Djamena Region, Chad as of 21 October 2022](https://data.humdata.org/dataset/water-extent-in-n-djamena-department-n-djamena-region-chad-as-of-21-october-2022)
- [Satellite detected water extent in N'Djamena department, N'Djamena Region, Chad as of 24 October 2022](https://data.humdata.org/dataset/water-extent-in-n-djamena-department-n-djamena-region-chad-as-of-24-october-2022)
- [Satellite detected water extents between 14 and 18 October 2022 over Chad](https://data.humdata.org/dataset/satellite-detected-water-extents-between-14-and-18-october-2022-over-chad)
- [Satellite detected water extents between 30 October and 03 November 2022 over Chad](https://data.humdata.org/dataset/satellite-detected-water-extents-between-30-october-and-03-november-2022-over-chad)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [13.521720259000062, 7.517531856000062, 23.119776156000057, 22.25114385100005]

## Temporal Coverage

- **Start**: 2022-10-20T00:00:00Z
- **End**: 2022-11-04T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Water_Class | int16 | Coded value. The source geodatabase domain gives: 0 = Archive Water Extent / Pre-Flood Water; 1 = Flood Water; 2 = Satellite Detected Water / Possible Saturated Soil; 3 = Probable Flash Flood-Affected Land; 4 = Aquaculture; 5 = Possible Satuated, wet soil; 6 = Tsunami-Affected Land; 7 = Maximum Satellite Observed Water (Cumulative); 8 = Swamp / Marsh / Mangrove; 9 = Snow Cover. The decoded text is in `Water_Class_label`. |
| Sensor_ID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Sensor_ID_label`, which is decoded per source file. |
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
| StaffID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `StaffID_label`, which is decoded per source file. |
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
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20221019tcd-water-extent.parquet | 340.7 MB | 1220f39fa4a8... |
| ./fl20221019tcd-water-extent.pmtiles | 38.5 MB | 1220d9f72cd4... |
| ./styles/default.json | 1.1 KB | 12206f59663e... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20221019tcd-water-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/satellite-detected-water-extents-between-14-and-18-october-2022-over-chad](https://data.humdata.org/dataset/satellite-detected-water-extents-between-14-and-18-october-2022-over-chad)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `KV5_20221030_FloodExtent_NDjamenaDepartment_Chad`, `PHR_20221021_FloodExtent_NDjamenaDepartment_Chad`, `S2_20181031_WaterExtent_HadjerLamisLacRegions_Chad`, `S2_20191011_WaterExtent_HadjerLamisLacRegions_Chad`, `S2_20201010_WaterExtent_HadjerLamisLacRegions_Chad`, `S2_20211025_WaterExtent_HadjerLamisLacRegions_Chad`, `S2_20221015_FloodExtent_NDjamenaDepartment_Chad`, `S2_20221020_FloodExtent_NDjamenaDepartment_Chad`, `S2_20221020_PermanentWater_NDjamenaDepartment_Chad`, `S2_20221030_WaterExtent_HadjerLamisLacRegions_Chad`, `VIIRS_20221014_20221018_FloodExtent_Chad`, `VIIRS_20221030_20221103_MaximumFloodWaterExtent_Chad`, `VIIRS_20221030_20221103_PermanentWater_Chad`, `WV2_20221024_FloodExtent_NDjamenaDepartment_Chad`.

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

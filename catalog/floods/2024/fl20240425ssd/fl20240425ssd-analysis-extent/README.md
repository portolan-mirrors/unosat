# Analysis extent: Flood, South Sudan, 25 April 2024 (FL20240425SSD)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2024/fl20240425ssd/fl20240425ssd-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Analysis extent for Flood, South Sudan, 25 April 2024 (FL20240425SSD): 26,896 features merged from 749 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Satellite detected water extent over Juba County, Central Equatoria Province, South Sudan as of 06 May 2024](https://data.humdata.org/dataset/water-extent-over-juba-county-central-equatoria-province-south-sudan-as-of-06-may-2024)
- [Satellite detected water extents between 05 and 09 June 2024 over South Sudan](https://data.humdata.org/dataset/satellite-detected-water-extents-between-05-and-09-june-2024-over-south-sudan)
- [Satellite detected water extents between 05 and 09 October 2024 over South Sudan](https://data.humdata.org/dataset/satellite-detected-water-extents-between-05-and-09-october-2024-over-south-sudan)
- [Satellite detected water extents between 08 and 12 December 2024 over South Sudan](https://data.humdata.org/dataset/satellite-detected-water-extents-between-08-and-12-december-2024-over-south-sudan)
- [Satellite detected water extents between 10 and 14 August 2024 over South Sudan](https://data.humdata.org/dataset/satellite-detected-water-extents-between-10-and-14-august-2024-over-south-sudan)
- [Satellite detected water extents between 13 and 17 October 2024 over South Sudan](https://data.humdata.org/dataset/satellite-detected-water-extents-between-13-and-17-october-2024-over-south-sudan)
- [Satellite detected water extents between 13 and 17 September 2024 over South Sudan](https://data.humdata.org/dataset/satellite-detected-water-extents-between-13-and-17-september-2024-over-south-sudan)
- [Satellite detected water extents between 14 and 18 December 2024 over South Sudan](https://data.humdata.org/dataset/satellite-detected-water-extents-between-14-and-18-december-2024-over-south-sudan)
- [Satellite detected water extents between 15 and 19 August 2024 over South Sudan](https://data.humdata.org/dataset/satellite-detected-water-extents-between-15-and-19-august-2024-over-south-sudan)
- [Satellite detected water extents between 18 and 22 August 2024 over South Sudan](https://data.humdata.org/dataset/satellite-detected-water-extents-between-18-and-22-august-2024-over-south-sudan)
- [Satellite detected water extents between 20 and 24 April 2024 over South Sudan](https://data.humdata.org/dataset/satellite-detected-water-extents-between-20-and-24-april-2024-over-south-sudan)
- [Satellite detected water extents between 20 and 24 October 2024 over South Sudan](https://data.humdata.org/dataset/satellite-detected-water-extents-between-20-and-24-october-2024-over-south-sudan)
- and 2 more; the event's [catalog page](../catalog.json) lists them all.

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [24.15072456300004, 3.4860405740000715, 35.95192367100009, 12.236147519000042]

## Temporal Coverage

- **Start**: 2024-04-25T00:00:00Z
- **End**: 2024-12-20T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | string | Coded value. The 2 source files of this collection use 2 different domains for it, so read `SensorID_label`, which is decoded per source file. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | string | Coded value. The 2 source files of this collection use 2 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Staff_ID | int64 |  |
| Area_km2 | double | Area in square kilometres, as UNOSAT computed it. |
| Pop | double |  |
| Adm0 | string |  |
| Adm1 | string |  |
| Adm2 | string |  |
| ConfidenceID_label | string | `ConfidenceID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| FieldValidation_label | string | `FieldValidation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Shape_Leng | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Confidence | string |  |
| FieldValid | string |  |
| EventCod | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Confiden_1 | string |  |
| FieldVal_1 | string |  |
| Sensor_ID | string |  |
| d_Confiden | string |  |
| d_SensorID | string |  |
| d_FieldVal | string |  |
| d_StaffID | string |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20240425ssd-analysis-extent.parquet | 15.2 MB | 1220bd925269... |
| ./fl20240425ssd-analysis-extent.pmtiles | 152.8 MB | 122063449edf... |
| ./styles/default.json | 671 B | 12203302a09e... |
| ./fl20240425ssd-analysis-extent.thumb.jpg | 11.5 KB | 122087bc82be... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20240425ssd-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/satellite-detected-water-extents-between-05-and-09-june-2024-over-south-sudan](https://data.humdata.org/dataset/satellite-detected-water-extents-between-05-and-09-june-2024-over-south-sudan)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `S2_20240506_AnalysisExtent_Juba_CentralEquatoria`, `VIIRS_20190930_20191019_CloudObstruction_SouthSudan`, `VIIRS_20200920_20201019_CloudObstruction_SouthSudan`, `VIIRS_20210919_20211018_CloudObstruction_SouthSudan`, `VIIRS_20210926_20210930_CloudObstruction_SouthSudan`, `VIIRS_20211009_20211013_CloudObstruction_SouthSudan`, `VIIRS_20211015_20211019_CloudObstruction_SouthSudan`, `VIIRS_20211020_20211024_CloudObstruction_SouthSudan`, `VIIRS_20211103_20211107_CloudObstruction_SouthSudan`, `VIIRS_20211119_20211123_CloudObstruction_SouthSudan`, `VIIRS_20220110_20220114_CloudObstruction_SouthSudan`, `VIIRS_20220115_20220119_CloudObstruction_SouthSudan`, `VIIRS_20220223_20220227_CloudObstruction_SouthSudan`, `VIIRS_20220305_20220309_CloudObstruction_SouthSudan`, `VIIRS_20220310_20220314_CloudObstruction_SouthSudan`, `VIIRS_20220401_20220405_CloudObstruction_SouthSudan`, `VIIRS_20220401_20220424_AnalysisExtent_SouthSudan`, `VIIRS_20220420_20220424_CloudObstruction_SouthSudan`, `VIIRS_20220514_20220518_CloudObstruction_SouthSudan`, `VIIRS_20220525_20220529_CloudObstruction_SouthSudan`, `VIIRS_20220608_20220612_CloudObstruction_SouthSudan`, `VIIRS_20220719_20220723_CloudObstruction_SouthSudan`, `VIIRS_20220803_20220807_CloudObstruction_SouthSudan`, `VIIRS_20220830_20220903_CloudObstruction_SouthSudan`, `VIIRS_20220910_20220914_CloudObstruction_SouthSudan`, `VIIRS_20221004_20221008_CloudObstruction_SouthSudan`, `VIIRS_20221018_20221022_CloudObstruction_SouthSudan`, `VIIRS_20221026_20221030_CloudObstruction_SouthSudan`, `VIIRS_20221110_20221114_CloudObstruction_SouthSudan`, `VIIRS_20221224_20221228_CloudObstruction_SouthSudan`, `VIIRS_20230112_20230116_CloudObstruction_SouthSudan`, `VIIRS_20230117_20230121_CloudObstruction_SouthSudan`, `VIIRS_20230220_20230224_CloudObstruction_SouthSudan`, `VIIRS_20230301_20230305_CloudObstruction_SouthSudan`, `VIIRS_20230325_20230329_CloudObstruction_SouthSudan`, `VIIRS_20230427_20230501_CloudObstruction_SouthSudan`, `VIIRS_20230506_20230510_CloudObstruction_SouthSudan`, `VIIRS_20230601_20230605_CloudObstruction_SouthSudan`, `VIIRS_20230610_20230614_CloudObstruction_SouthSudan`, `VIIRS_20230710_20230714_CloudObstruction_SouthSudan` and 27 more.

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

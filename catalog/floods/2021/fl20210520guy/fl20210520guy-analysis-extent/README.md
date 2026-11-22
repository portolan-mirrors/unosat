# Analysis extent: Flood, Guyana, 20 May 2021 (FL20210520GUY)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2021/fl20210520guy/fl20210520guy-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Analysis extent for Flood, Guyana, 20 May 2021 (FL20210520GUY): 10 features merged from 10 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Satellite detected water extent along the Mazaruni river as of 09 June 2021, Region 7 - Cuyuni-Mazaruni, Guyana](https://data.humdata.org/dataset/water-extent-along-the-mazaruni-river-as-of-09-june-2021-region-7-cuyuni-mazaruni-guyana)
- [Satellite detected water extent along the Mazaruni river as of 23 June 2021, Region 7 - Cuyuni-Mazaruni, Guyana](https://data.humdata.org/dataset/water-extent-along-the-mazaruni-river-as-of-23-june-2021-region-7-cuyuni-mazaruni-guyana)
- [Satellite detected water extent as of 8 June 2021 in Guyana](https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-8-june-2021-in-guyana)
- [Satellite detected water extent between 2 & 6 June 2021 in Guyana](https://data.humdata.org/dataset/satellite-detected-water-extent-between-2-6-june-2021-in-guyana)
- [Satellite detected water extent in Region 9-Upper Takutu-Upper Essequibo, Guyana as of 12 June 2021](https://data.humdata.org/dataset/water-extent-in-region-9-upper-takutu-upper-essequibo-guyana-as-of-12-june-2021)
- [Satellite detected water extent over Kwakwani town along the Berbice river as of 07 June 2021, Region 10, Guyana](https://data.humdata.org/dataset/water-extent-over-kwakwani-town-along-the-berbice-river-as-of-07-june-2021-region-10-guyan)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [-61.392996129999915, 1.1713706800000523, -56.48079612999993, 8.557570680000083]

## Temporal Coverage

- **Start**: 2021-06-07T00:00:00Z
- **End**: 2021-06-24T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Notes | string | Free-text notes by the analyst. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| Shape_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Shape_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Confidence | string |  |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | string | Coded value. The 2 source files of this collection use 2 different domains for it, so read `SensorID_label`, which is decoded per source file. |
| FieldValid | string |  |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| StaffID | string | Coded value. The 2 source files of this collection use 2 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| EventCod | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Area_ha | float | Area in hectares, as UNOSAT computed it. |
| ConfidenceID_label | string | `ConfidenceID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| FieldValidation_label | string | `FieldValidation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Sensor_ID | string |  |
| Staff_ID | int32 |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20210520guy-analysis-extent.parquet | 29.5 MB | 1220cc4f5ebd... |
| ./fl20210520guy-analysis-extent.pmtiles | 13.3 MB | 12208dad1f00... |
| ./styles/default.json | 671 B | 12204fb828a0... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20210520guy-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-8-june-2021-in-guyana](https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-8-june-2021-in-guyana)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `RCM2_20210607_AnalysisExtent_Kwakwani`, `RCM2_20210609_AnalysisExtent_UpperMazaruni`, `ST1_20210519_AnalysisExtent_Rupununi`, `ST1_20210612_AnalysisExtent_Region9`, `ST1_20210623_AnalysisExtent_UpperMazaruni`, `ST2_20210520_AnalysisExtent_Rupununi`, `ST2_20210520_CloudObstruction_Rupununi`, `VIIRS_20210602_20210606_AnalysisExtent_Guyana`, `VIIRS_20210602_20210606_CloudObstruction_Guyana`, `VIIRS_ABI_20210608_CloudObstruction_Guyana`.

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

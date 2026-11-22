# Analysis extent: Flood, Sudan, 8 August 2016 (FL20160808SDN)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2016/fl20160808sdn/fl20160808sdn-analysis-extent-cc_by_nc_sa_3_0/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Analysis extent for Flood, Sudan, 8 August 2016 (FL20160808SDN): 7 features merged from 7 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of Evolution of Possible Flood Water & Saturated Soil Over Khartoum City, Khartoum State, Sudan](https://data.humdata.org/dataset/geodata-of-evolution-of-possible-flood-water-saturated-soil-over-khartoum-ci-august-18-2016)
- [Geodata of Possible Flood Water & Saturated Soil Over Khartoum Area, Khartoum State, Sudan](https://data.humdata.org/dataset/geodata-of-possible-flood-water-saturated-soil-over-khartoum-area-khartoum-s-august-17-2016)
- [Geodata of Possible Flood Water & Saturated Soil over Abu Hamad Area, River Nile State, Sudan](https://data.humdata.org/dataset/geodata-of-possible-flood-water-saturated-soil-over-abu-hamad-area-river-nil-august-19-2016)
- [Geodata of Satellite Detected Waters Over Khartoum Area, Khartoum State, Sudan](https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-over-khartoum-area-khartoum-state-sudan-august-12-2016)
- [Geodata of Satellite Detected Waters over central part of Kassala State, Sudan](https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-over-central-part-of-kassala-state-sudan-august-12-2016)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [32.287859397000034, 12.564594753000051, 37.28303798600007, 19.76978452800006]

## Temporal Coverage

- **Start**: 2016-08-12T00:00:00Z
- **End**: 2016-08-19T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `SensorID_label`, which is decoded per source file. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 18 = AM; 22 = WP; 33 = LB; 44 = JL; 55 = VG; 66 = CJ; 73 = RS; 77 = LD; 88 = HK; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 141 = KJP; 151 = MNY; 222 = CS; 1000 = Unknown. The decoded text is in `StaffID_label`. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Area_ha | float | Area in hectares, as UNOSAT computed it. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20160808sdn-analysis-extent-cc_by_nc_sa_3_0.parquet | 6.2 KB | 1220d7c39af2... |
| ./fl20160808sdn-analysis-extent-cc_by_nc_sa_3_0.pmtiles | 608.3 KB | 122034ac26ec... |
| ./styles/default.json | 687 B | 1220b3b19a10... |
| ./fl20160808sdn-analysis-extent-cc_by_nc_sa_3_0.thumb.jpg | 7.9 KB | 12201ab63067... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20160808sdn-analysis-extent-cc_by_nc_sa_3_0.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-evolution-of-possible-flood-water-saturated-soil-over-khartoum-ci-august-18-2016](https://data.humdata.org/dataset/geodata-of-evolution-of-possible-flood-water-saturated-soil-over-khartoum-ci-august-18-2016)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `LS_20160808_Kassala_Analysis_Extent`, `RS_20160808_WadMadani_Analysis_Extent`, `RS_20160812_Sennar_AnalysisExtent`, `RS_20160818_Al_Jazeera_Analysis_Extent`, `SP_20160814_AbuHamad_AnalysisExtent`, `SP_20160815_Khartoum_AnalysisExtent`, `TX_20160811_Kartoum_Analysis_Extent`.

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

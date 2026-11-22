# Water extent: Flood, Sudan, 8 August 2016 (FL20160808SDN)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2016/fl20160808sdn/fl20160808sdn-water-extent-cc_by_nc_sa_3_0/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Water extent for Flood, Sudan, 8 August 2016 (FL20160808SDN): 151,821 features merged from 8 source layers. Polygon layers with a water class column (such as `Water_Class`), or whose names mention flood, water, or inundation: satellite-detected water. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of Evolution of Possible Flood Water & Saturated Soil Over Khartoum City, Khartoum State, Sudan](https://data.humdata.org/dataset/geodata-of-evolution-of-possible-flood-water-saturated-soil-over-khartoum-ci-august-18-2016)
- [Geodata of Possible Flood Water & Saturated Soil Over Khartoum Area, Khartoum State, Sudan](https://data.humdata.org/dataset/geodata-of-possible-flood-water-saturated-soil-over-khartoum-area-khartoum-s-august-17-2016)
- [Geodata of Possible Flood Water & Saturated Soil over Abu Hamad Area, River Nile State, Sudan](https://data.humdata.org/dataset/geodata-of-possible-flood-water-saturated-soil-over-abu-hamad-area-river-nil-august-19-2016)
- [Geodata of Satellite Detected Waters Over Khartoum Area, Khartoum State, Sudan](https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-over-khartoum-area-khartoum-state-sudan-august-12-2016)
- [Geodata of Satellite Detected Waters over central part of Kassala State, Sudan](https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-over-central-part-of-kassala-state-sudan-august-12-2016)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [32.12356263600009, 12.568234430000075, 37.056721640000035, 19.767314463000048]

## Temporal Coverage

- **Start**: 2016-08-12T00:00:00Z
- **End**: 2016-08-19T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Water_Class | int16 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Water_Class_label`, which is decoded per source file. |
| Sensor_ID | int32 | Coded value. The 3 source files of this collection use 3 different domains for it, so read `Sensor_ID_label`, which is decoded per source file. |
| Sensor_Date | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence_ID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `Confidence_ID_label`. |
| Field_Validation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `Field_Validation_label`. |
| Water_StatusID | int32 | Coded value. The source geodatabase domain gives: 1 = New Water / Water Increase; 2 = No water change / Static Level; 3 = No water / Water levels decreased. The decoded text is in `Water_StatusID_label`. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| SenorID_old | int16 | Coded value. The source geodatabase domain gives: 1 = MODIS; 2 = ASAR WSM; 3 = ASAR IMP; 4 = Radarsat; 5 = DMC; 6 = SPOT5; 7 = ALOS Palsar WB1; 8 = ASAR APP. The decoded text is in `SenorID_old_label`. |
| StaffID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Shape_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Shape_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
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
| ./fl20160808sdn-water-extent-cc_by_nc_sa_3_0.parquet | 81.2 MB | 1220c656beea... |
| ./fl20160808sdn-water-extent-cc_by_nc_sa_3_0.pmtiles | 45.4 MB | 1220e636e246... |
| ./styles/default.json | 991 B | 1220233dceaf... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20160808sdn-water-extent-cc_by_nc_sa_3_0.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-evolution-of-possible-flood-water-saturated-soil-over-khartoum-ci-august-18-2016](https://data.humdata.org/dataset/geodata-of-evolution-of-possible-flood-water-saturated-soil-over-khartoum-ci-august-18-2016)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `LS_20160605_PreFlood_Kassala`, `LS_20160808_PostFlood_Kassala`, `RS_20160812_PostFlood_Sennar`, `RS_20160818_PostFlood_Al_Jazeera`, `SP_20160814_PostFlood_AbuHamad`, `SP_20160815_PostFlood_Khartoum`, `TX_20091010_PreFlood_Khartoum`, `TX_20160811_PostFlood_Khartoum`.

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

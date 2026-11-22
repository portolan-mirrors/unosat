# Water extent: Flood, Myanmar, 3 July 2015 (FL20150703MMR)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2015/fl20150703mmr/fl20150703mmr-water-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Water extent for Flood, Myanmar, 3 July 2015 (FL20150703MMR): 563,598 features merged from 22 source layers. Polygon layers with a water class column (such as `Water_Class`), or whose names mention flood, water, or inundation: satellite-detected water. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of Damage Assessment over Tuikhingzang, Tonzang Township, Chin Division, Myanmar](https://data.humdata.org/dataset/geodata-of-damage-assessment-over-tuikhingzang-tonzang-township-chin-division-september-17-2015)
- [Geodata of Flood Waters Near City of Yangon, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-near-city-of-yangon-myanmar-august-10-2015)
- [Geodata of Flood Waters Over Ann and Myebon area, Rakhine State, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-ann-and-myebon-area-rakhine-state-myanmar-august-17-2015)
- [Geodata of Flood Waters Over Ann area, Rakhine State, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-ann-area-rakhine-state-myanmar-august-14-2015)
- [Geodata of Flood Waters Over Central Magway State, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-central-magway-state-myanmar-august-07-2015)
- [Geodata of Flood Waters Over Central Sagaing Region, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-central-sagaing-region-myanmar-august-13-2015)
- [Geodata of Flood Waters Over Central Sagaing State, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-central-sagaing-state-myanmar-july-24-2015)
- [Geodata of Flood Waters Over Kayin and Mon State, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-kayin-and-mon-state-myanmar-august-14-2015)
- [Geodata of Flood Waters Over Kyautaw area, Rakhine State, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-kyautaw-area-rakhine-state-myanmar-august-19-2015)
- [Geodata of Flood Waters Over Northern Rakhine State, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-northern-rakhine-state-myanmar-august-11-2015)
- [Geodata of Flood Waters Over Northwest Rakhine State, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-northwest-rakhine-state-myanmar-july-13-2015)
- [Geodata of Flood Waters Over South Bago Division, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-south-bago-division-myanmar-august-13-2015)
- and 7 more; the event's [catalog page](../catalog.json) lists them all.

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [91.88788027100003, 14.823898829000086, 99.32187066700004, 25.520275883000068]

## Temporal Coverage

- **Start**: 2015-07-13T00:00:00Z
- **End**: 2015-10-21T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Water_Class | int16 | Coded value. The source geodatabase domain gives: 0 = Preflood Water; 1 = Flood Water; 2 = Flood-Affected Land / Possible Flood water; 3 = Probable Flash Flood-Affected Land; 4 = Satellite Detected Water; 6 = Possible Saturated, wet Soil/ possible Flood Water; 9 = Aquaculture (Wet Rice); 14 = Tsunami-Affected Land; 88 = Swamp/Marsh/Mangrove; 99 = Maximum Flood Water Extent (Cumulative). The decoded text is in `Water_Class_label`. |
| Sensor_ID | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT 6; 42 = Sentinel-1; 43 = Komsat-2; 999 = Combination of Sensors. The decoded text is in `Sensor_ID_label`. |
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
| ./fl20150703mmr-water-extent.parquet | 245.2 MB | 1220255221fd... |
| ./fl20150703mmr-water-extent.pmtiles | 203.3 MB | 1220753ce3b6... |
| ./styles/default.json | 995 B | 122065ea0df6... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20150703mmr-water-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-damage-assessment-over-tuikhingzang-tonzang-township-chin-division-september-17-2015](https://data.humdata.org/dataset/geodata-of-damage-assessment-over-tuikhingzang-tonzang-township-chin-division-september-17-2015)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `LS20150130_PreFlood`, `LS20150429_PreFlood`, `PL20150916_Flood`, `RS20150710_PostFlood`, `RS20150730_PostFlood`, `RS20150806_PostFlood`, `RS20150809_Flood`, `RS20150817_PostFlood`, `ST20150207_Preflood`, `ST20150228_Preflood`, `ST20150315_Preflood`, `ST20150320_PreFlood`, `ST20150511_Preflood`, `ST20150711_PostFlood`, `ST20150718_PostFlood`, `ST20150806_Flood`, `ST20150806_Water`, `ST20150811_Flood`, `ST20150904_PostFlood`, `TX20150806_PostFlood`, `TX20150810_PostFlood`, `WV20151017_Flood`.

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

# Shelters: Flood, Myanmar, 3 July 2015 (FL20150703MMR)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2015/fl20150703mmr/fl20150703mmr-shelters/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Shelters for Flood, Myanmar, 3 July 2015 (FL20150703MMR): 260 features merged from 1 source layer. Point layers with shelter or camp columns, or whose names mention camps, shelters, IDPs, or settlements. The `source_layer` and `source_file` columns name the layer and file each row came from.

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

- **Bounding Box**: [94.0253812, 23.5576206, 94.0434104, 23.5606087]

## Temporal Coverage

- **Start**: 2015-07-13T00:00:00Z
- **End**: 2015-10-21T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Site_ID | int16 | Coded value. The source geodatabase domain gives: 1 = Tent Shelter; 2 = Metal Structure; 3 = Improvised Shelter (Wood / Stone / Mud); 4 = Admin Building; 5 = Semi-Permanent Structure. The decoded text is in `Site_ID_label`. |
| Sensor_ID | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT 6; 42 = Sentinel-1; 43 = Komsat-2; 999 = Combination of Sensors. The decoded text is in `Sensor_ID_label`. |
| Sensor_Date | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence_ID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `Confidence_ID_label`. |
| Field_Validation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `Field_Validation_label`. |
| CampStatusID | int32 | Coded value. The source geodatabase domain gives: 0 = Closed / Relocated; 1 = Open (Operational); 2 = Planned / Under Construction; 9 = Camp Destroyed. The decoded text is in `CampStatusID_label`. |
| CampName | string |  |
| Notes | string | Free-text notes by the analyst. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 22 = WP; 33 = LB; 44 = JL; 55 = VG; 66 = CJ; 73 = RS; 77 = LD; 88 = HK; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 222 = CS; 1000 = Unknown. The decoded text is in `StaffID_label`. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| CampType | int32 | Coded value. The source geodatabase domain gives: 1 = Refugee Camp; 2 = IDP Camp. The decoded text is in `CampType_label`. |
| CampTrend | int32 | Coded value. The source geodatabase domain gives: 1 = Increase; 2 = Decrease. The decoded text is in `CampTrend_label`. |
| Shelter_Status | int32 | Coded value. The source geodatabase domain gives: 1 = Open; 2 = Closed. The decoded text is in `Shelter_Status_label`. |
| ShelterClose_Date | timestamp[us, tz=UTC] |  |
| Structure_Type | int32 | Coded value. The source geodatabase domain gives: 1 = Tent Shelter; 2 = Admin Building; 3 = Improvised Shelter (Wood / Stone / Mud); 4 = Semi-Permanent Structure; 5 = Metal Structure. The decoded text is in `Structure_Type_label`. |
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
| ./fl20150703mmr-shelters.parquet | 22.7 KB | 12200cd77521... |
| ./fl20150703mmr-shelters.pmtiles | 56.3 KB | 1220bb9fc652... |
| ./styles/default.json | 892 B | 1220227530b8... |
| ./fl20150703mmr-shelters.thumb.jpg | 3.9 KB | 1220df58a573... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20150703mmr-shelters.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-damage-assessment-over-tuikhingzang-tonzang-township-chin-division-september-17-2015](https://data.humdata.org/dataset/geodata-of-damage-assessment-over-tuikhingzang-tonzang-township-chin-division-september-17-2015)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `PL_20150916_IDP_Structures`.

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

# Damage areas: Complex emergency, Ukraine, 23 February 2022 (CE20220223UKR)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20220223ukr/ce20220223ukr-damage-areas-cc_by_igo_3_0/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Damage areas for Complex emergency, Ukraine, 23 February 2022 (CE20220223UKR): 26,971 features merged from 12 source layers. Polygon layers with a damage class column: damaged areas, zones, or density cells. The `source_layer` and `source_file` columns name the layer and file each row came from. The geometry is in EPSG:3857, the CRS of the source layers; the PMTiles copy is in Web Mercator.

From these HDX datasets:

- [UNOSAT Damage Assessment Overview Map - Livoberezhnyi and Zhovtnevyi Districts, Mariupol City, Ukraine](https://data.humdata.org/dataset/unosat-damage-assessment-overview-map-livoberezhnyi-district-mariupol-city-ukraine)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [30.1593406022197, 47.00029244482142, 38.18531484566269, 51.55525156514055]

## Temporal Coverage

- **Start**: 2022-03-18T00:00:00Z
- **End**: 2022-03-18T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Shape_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Shape_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The source geodatabase domain gives: 1 = Worldview-1; 2 = Worldview-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = Komsat-2; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 27 = ASAR IMM; 28 = WorldView-3; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 999 = Combination of Sensors. The decoded text is in `SensorID_label`. |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| Main_Damage_Site_Class | int16 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Main_Damage_Site_Class_label`, which is decoded per source file. |
| SensorDate_2 | timestamp[us, tz=UTC] |  |
| SensorID_2 | int32 | Coded value. The source geodatabase domain gives: 1 = Worldview-1; 2 = Worldview-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = Komsat-2; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 27 = ASAR IMM; 28 = WorldView-3; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 999 = Combination of Sensors. The decoded text is in `SensorID_2_label`. |
| ConfidenceID_2 | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_2_label`. |
| Main_Damage_Site_Class_2 | int16 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Main_Damage_Site_Class_2_label`, which is decoded per source file. |
| Damage_Status_2 | int16 | Coded value. The source geodatabase domain gives: 0 = No change; 1 = Increase - damage; 2 = Decrease - damage; 3 = New - damage; 4 = Demolished; 5 = Rebuilt; 6 = Reconstructed. The decoded text is in `Damage_Status_2_label`. |
| SensorDate_3 | timestamp[us, tz=UTC] |  |
| SensorID_3 | int32 | Coded value. The source geodatabase domain gives: 1 = Worldview-1; 2 = Worldview-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = Komsat-2; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 27 = ASAR IMM; 28 = WorldView-3; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 999 = Combination of Sensors. The decoded text is in `SensorID_3_label`. |
| ConfidenceID_3 | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_3_label`. |
| Main_Damage_Site_Clas3 | int16 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Main_Damage_Site_Clas3_label`, which is decoded per source file. |
| Damage_Status_3 | int16 | Coded value. The source geodatabase domain gives: 0 = No change; 1 = Increase - damage; 2 = Decrease - damage; 3 = New - damage; 4 = Demolished; 5 = Rebuilt; 6 = Reconstructed. The decoded text is in `Damage_Status_3_label`. |
| SensorDate_4 | timestamp[us, tz=UTC] |  |
| SensorID_4 | int32 | Coded value. The source geodatabase domain gives: 1 = Worldview-1; 2 = Worldview-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = Komsat-2; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 27 = ASAR IMM; 28 = WorldView-3; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 999 = Combination of Sensors. The decoded text is in `SensorID_4_label`. |
| ConfidenceID_4 | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_4_label`. |
| Main_Damage_Site_Class_4 | int16 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Main_Damage_Site_Class_4_label`, which is decoded per source file. |
| Damage_Status_4 | int16 | Coded value. The source geodatabase domain gives: 0 = No change; 1 = Increase - damage; 2 = Decrease - damage; 3 = New - damage; 4 = Demolished; 5 = Rebuilt; 6 = Reconstructed. The decoded text is in `Damage_Status_4_label`. |
| SensorDate_5 | timestamp[us, tz=UTC] |  |
| SensorID_5 | int32 | Coded value. The source geodatabase domain gives: 1 = Worldview-1; 2 = Worldview-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = Komsat-2; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 27 = ASAR IMM; 28 = WorldView-3; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 999 = Combination of Sensors. The decoded text is in `SensorID_5_label`. |
| ConfidenceID_5 | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_5_label`. |
| Main_Damage_Site_Class_5 | int16 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Main_Damage_Site_Class_5_label`, which is decoded per source file. |
| Damage_Status_5 | int16 | Coded value. The source geodatabase domain gives: 0 = No change; 1 = Increase - damage; 2 = Decrease - damage; 3 = New - damage; 4 = Demolished; 5 = Rebuilt; 6 = Reconstructed. The decoded text is in `Damage_Status_5_label`. |
| SensorDate_6 | timestamp[us, tz=UTC] |  |
| SensorID_6 | int32 | Coded value. The source geodatabase domain gives: 1 = Worldview-1; 2 = Worldview-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = Komsat-2; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 27 = ASAR IMM; 28 = WorldView-3; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 999 = Combination of Sensors. The decoded text is in `SensorID_6_label`. |
| ConfidenceID_6 | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_6_label`. |
| Main_Damage_Site_Class_6 | int16 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Main_Damage_Site_Class_6_label`, which is decoded per source file. |
| Damage_Status_6 | int16 | Coded value. The source geodatabase domain gives: 0 = No change; 1 = Increase - damage; 2 = Decrease - damage; 3 = New - damage; 4 = Demolished; 5 = Rebuilt; 6 = Reconstructed. The decoded text is in `Damage_Status_6_label`. |
| Grouped_Damage_Classes | int16 | Coded value. The source geodatabase domain gives: 1 = Damaged Buildings; 2 = Damaged Greenhouses; 3 = Impacts on Roads / Bridges; 4 = Impacts in Fields; 5 = Damaged Road segments. The decoded text is in `Grouped_Damage_Classes_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Notes | string | Free-text notes by the analyst. |
| Settlement_Name | string |  |
| Neighborhood | string |  |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Analyst | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Analyst_label`, which is decoded per source file. |
| Analyst_label | string | `Analyst` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| ConfidenceID_label | string | `ConfidenceID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| ConfidenceID_2_label | string | `ConfidenceID_2` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| ConfidenceID_3_label | string | `ConfidenceID_3` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| ConfidenceID_4_label | string | `ConfidenceID_4` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| ConfidenceID_5_label | string | `ConfidenceID_5` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| ConfidenceID_6_label | string | `ConfidenceID_6` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Damage_Status_2_label | string | `Damage_Status_2` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Damage_Status_3_label | string | `Damage_Status_3` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Damage_Status_4_label | string | `Damage_Status_4` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Damage_Status_5_label | string | `Damage_Status_5` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Damage_Status_6_label | string | `Damage_Status_6` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| FieldValidation_label | string | `FieldValidation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Grouped_Damage_Classes_label | string | `Grouped_Damage_Classes` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Main_Damage_Site_Clas3_label | string | `Main_Damage_Site_Clas3` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Main_Damage_Site_Class_label | string | `Main_Damage_Site_Class` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Main_Damage_Site_Class_2_label | string | `Main_Damage_Site_Class_2` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Main_Damage_Site_Class_4_label | string | `Main_Damage_Site_Class_4` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Main_Damage_Site_Class_5_label | string | `Main_Damage_Site_Class_5` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Main_Damage_Site_Class_6_label | string | `Main_Damage_Site_Class_6` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_2_label | string | `SensorID_2` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_3_label | string | `SensorID_3` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_4_label | string | `SensorID_4` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_5_label | string | `SensorID_5` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_6_label | string | `SensorID_6` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| PageName | string |  |
| PageNumber | int32 |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20220223ukr-damage-areas-cc_by_igo_3_0.parquet | 462.4 KB | 1220fee5fb2c... |
| ./ce20220223ukr-damage-areas-cc_by_igo_3_0.pmtiles | 7.0 MB | 122038b92e5f... |
| ./styles/default.json | 1014 B | 1220750defad... |
| ./ce20220223ukr-damage-areas-cc_by_igo_3_0.thumb.jpg | 5.7 KB | 1220549c6e3a... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20220223ukr-damage-areas-cc_by_igo_3_0.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/unosat-damage-assessment-overview-map-livoberezhnyi-district-mariupol-city-ukraine](https://data.humdata.org/dataset/unosat-damage-assessment-overview-map-livoberezhnyi-district-mariupol-city-ukraine)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Bucha_31March2022_RDA`, `Chernihiv_22March2022_RDA`, `Donetsk_26March2022_RDA`, `Horenka_31March2022_RDA`, `Hostomel_31March2022_RDA`, `Irpin_31March2022_RDA`, `Kharkiv_23March2022_RDA`, `MariupolDonesk_26March2022_RDA`, `Mariupol_26March2022_RDA`, `Mariupol_3April2022_RDA`, `Sumy_22March2022_RDA`, `WestKyiv_31March2022_RDA`.

## Attribution

UNITAR-UNOSAT

## License

[CC-BY-3.0-IGO](https://creativecommons.org/licenses/by/3.0/igo/legalcode)

## Contact

Portolan Mirrors <nissim@radiant.earth>

## Known Issues

This is a preliminary assessment and has not yet been validated in the field. It is important to consider the characteristics of the source imagery used in the analyses when interpreting results. For damage assessments it should be noted that only significant damage to the structural integrity of the buildings analyzed can be seen in imagery, while minor damage such as cracks or holes may not be visible at all. For flood extractions using radar data it is important to note that urban areas and highly vegetated areas may mask the flood signature and result in underestimation of flood waters. Users with specific questions or concerns should contact unosat@unitar.org to seek clarification.

---

*Generated by [Portolan](https://github.com/portolan-sdi/portolan-cli) from STAC metadata and .portolan/metadata.yaml*

# Damage sites: Complex emergency, Ukraine, 23 February 2022 (CE20220223UKR)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20220223ukr/ce20220223ukr-damage-sites-cc_by_igo_3_0/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Damage sites for Complex emergency, Ukraine, 23 February 2022 (CE20220223UKR): 5,034 features merged from 9 source layers. Point layers with a damage class column (such as `Main_Damage_Site_Class`): one point per assessed structure or site. The `source_layer` and `source_file` columns name the layer and file each row came from. The geometry is in EPSG:3857, the CRS of the source layers; the PMTiles copy is in Web Mercator.

From these HDX datasets:

- [UNOSAT Damage Assessment Overview Map - Livoberezhnyi and Zhovtnevyi Districts, Mariupol City, Ukraine](https://data.humdata.org/dataset/unosat-damage-assessment-overview-map-livoberezhnyi-district-mariupol-city-ukraine)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [29.870764504080206, 47.08582856967705, 37.693624281773516, 51.5510821771955]

## Temporal Coverage

- **Start**: 2022-03-18T00:00:00Z
- **End**: 2022-03-18T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SiteID | int16 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `SiteID_label`, which is decoded per source file. |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `SensorID_label`, which is decoded per source file. |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| Main_Damage_Site_Class | int16 | Coded value. The 3 source files of this collection use 3 different domains for it, so read `Main_Damage_Site_Class_label`, which is decoded per source file. |
| SensorDate_2 | timestamp[us, tz=UTC] |  |
| SensorID_2 | int32 | Coded value. The source geodatabase domain gives: 1 = Worldview-1; 2 = Worldview-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = Komsat-2; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 27 = ASAR IMM; 28 = WorldView-3; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 999 = Combination of Sensors. The decoded text is in `SensorID_2_label`. |
| ConfidenceID_2 | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_2_label`. |
| Main_Damage_Site_Class_2 | int16 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Main_Damage_Site_Class_2_label`, which is decoded per source file. |
| Damage_Status_2 | int16 | Coded value. The source geodatabase domain gives: 0 = No change; 1 = Increase - damage; 2 = Decrease - damage; 3 = New - damage; 4 = Demolished; 5 = Rebuilt; 6 = Reconstructed. The decoded text is in `Damage_Status_2_label`. |
| SensorDate_3 | timestamp[us, tz=UTC] |  |
| SensorID_3 | int32 | Coded value. The source geodatabase domain gives: 1 = Worldview-1; 2 = Worldview-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = Komsat-2; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 27 = ASAR IMM; 28 = WorldView-3; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 999 = Combination of Sensors. The decoded text is in `SensorID_3_label`. |
| ConfidenceID_3 | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_3_label`. |
| Damage_Status_3 | int16 | Coded value. The source geodatabase domain gives: 0 = No change; 1 = Increase - damage; 2 = Decrease - damage; 3 = New - damage; 4 = Demolished; 5 = Rebuilt; 6 = Reconstructed. The decoded text is in `Damage_Status_3_label`. |
| SensorDate_4 | timestamp[us, tz=UTC] |  |
| SensorID_4 | int32 | Coded value. The source geodatabase domain gives: 1 = Worldview-1; 2 = Worldview-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = Komsat-2; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 27 = ASAR IMM; 28 = WorldView-3; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 999 = Combination of Sensors. The decoded text is in `SensorID_4_label`. |
| ConfidenceID_4 | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_4_label`. |
| Main_Damage_Site_Class_4 | int16 | Coded value. The source geodatabase domain gives: 1 = Destroyed; 2 = Severe Damage; 3 = Moderate Damage; 4 = Possible Damage; 5 = Impact Crater (Damage to Road); 6 = No Visible Damage; 7 = Impact Crater (Damage to Field); 8 = Destroyed (Demolition Zone); 9 = Suspected Phosphorus shell Attack Zone; 10 = Road Damage from Tank Passage; 11 = Possible Damage from adjacent impact, debris. The decoded text is in `Main_Damage_Site_Class_4_label`. |
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
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Notes | string | Free-text notes by the analyst. |
| Settlement_Name | string |  |
| Neighborhood | string |  |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Analyst | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Analyst_label`, which is decoded per source file. |
| Main_Damage_Site_Clas3 | int16 | Coded value. The source geodatabase domain gives: 1 = Destroyed; 2 = Severe Damage; 3 = Moderate Damage; 4 = Possible Damage; 5 = Impact Crater (Damage to Road); 6 = No Visible Damage; 7 = Impact Crater (Damage to Field); 8 = Destroyed (Demolition Zone); 9 = Suspected Phosphorus shell Attack Zone; 10 = Road Damage from Tank Passage; 11 = Possible Damage from adjacent impact, debris. The decoded text is in `Main_Damage_Site_Clas3_label`. |
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
| SiteID_label | string | `SiteID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| Grouped_Damage_Classes | int16 | Coded value. The source geodatabase domain gives: 1 = Damaged Buildings; 2 = Damaged Greenhouses; 3 = Impacts on Roads / Bridges; 4 = Impacts in Fields; 5 = Damaged Road segments. The decoded text is in `Grouped_Damage_Classes_label`. |
| Grouped_Damage_Classes_label | string | `Grouped_Damage_Classes` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 18 = TH; 22 = WP; 33 = LB; 44 = JL; 45 = MD; 54 = HP; 55 = VG; 57 = PG; 66 = CJ; 70 = SG; 73 = RS; 77 = LD; 88 = HK; 91 = KA; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 141 = KJP; 151 = MNY; 161 = DC; 171 = SR; 181 = NL; 191 = DH; 212 = MH; 213 = JT; 214 = ES; 215 = KB; 216 = JY; 218 = PA; 219 = SS; 220 = YM; 222 = CS; 900 = SU; 1000 = Unknown. The decoded text is in `StaffID_label`. |
| ImageID_Num | int32 |  |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20220223ukr-damage-sites-cc_by_igo_3_0.parquet | 208.6 KB | 1220f95d5662... |
| ./ce20220223ukr-damage-sites-cc_by_igo_3_0.pmtiles | 499.5 KB | 12201518b8b1... |
| ./styles/default.json | 1.2 KB | 122095c20701... |
| ./ce20220223ukr-damage-sites-cc_by_igo_3_0.thumb.jpg | 4.9 KB | 1220fa59cf89... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20220223ukr-damage-sites-cc_by_igo_3_0.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/unosat-damage-assessment-overview-map-livoberezhnyi-district-mariupol-city-ukraine](https://data.humdata.org/dataset/unosat-damage-assessment-overview-map-livoberezhnyi-district-mariupol-city-ukraine)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Azovstal_25April2022_CDA`, `Borodyanka_CDA_20220502`, `Bucha_31March2022_CDA`, `Chernihiv_28April2022_CDA`, `Hostomel_31March2022_CDA`, `Irpin_31March2022_CDA`, `Kharkiv_CDA_20220424`, `Mariupol_14March2021_CDA_All_No_Military_V2`, `Vorzel_20220331_CDA`.

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

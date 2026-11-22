# Damage sites: Flood, Somalia, 5 November 2023 (FL20231105SOM)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2023/fl20231105som/fl20231105som-damage-sites/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Damage sites for Flood, Somalia, 5 November 2023 (FL20231105SOM): 2,105,124 features merged from 186 source layers. Point layers with a damage class column (such as `Main_Damage_Site_Class`): one point per assessed structure or site. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Satellite detected water extent in Bardere City, Baardheere District, Gedo Region, Somalia, 13 November 2023](https://data.humdata.org/dataset/water-extent-in-bardere-city-baardheere-district-gedo-region-somalia-13-november-2023)
- [Satellite detected water extent in Bardere City, Baardheere District, Gedo Region, Somalia, 22 November 2023](https://data.humdata.org/dataset/water-extent-in-bardere-city-baardheere-district-gedo-region-somalia-22-november-2023)
- [Satellite detected water extent in Bardere City, Baardheere District, Gedo Region, Somalia, 29 November 2023](https://data.humdata.org/dataset/water-extent-in-bardere-city-baardheere-district-gedo-region-somalia-29-november-2023)
- [Satellite detected water extent in Beledweyne City, Beledweyne District, Hiraan Region, Somalia, 12 November 2023](https://data.humdata.org/dataset/water-extent-in-beledweyne-city-beledweyne-district-hiraan-region-somalia-12-november-2023)
- [Satellite detected water extent in Bu'aale City, Bu'aale District, Middle Juba Region, Somalia, 13 November 2023](https://data.humdata.org/dataset/water-extent-in-bu-aale-city-bu-aale-district-middle-juba-region-somalia-13-november-2023)
- [Satellite detected water extent in Bu'aale City, Bu'aale District, Middle Juba Region, Somalia, 22 November 2023](https://data.humdata.org/dataset/water-extent-in-bu-aale-city-bu-aale-district-middle-juba-region-somalia-22-november-2023)
- [Satellite detected water extent in Buloburto City and surroundings, Buloburto District, Hiraan Region, Somalia, 30 November 2023](https://data.humdata.org/dataset/water-extent-in-buloburto-city-and-surroundings-buloburto-district-hiraan-region-somalia-3)
- [Satellite detected water extent in Jilib City, Jilib District, Middle Juba Region, Somalia, 15 November 2023](https://data.humdata.org/dataset/water-extent-in-jilib-city-jilib-district-middle-juba-region-somalia-15-november-2023)
- [Satellite detected water extent in Jowhar City, Jowhar District, Middle Shabelle Region, Somalia as of 20 November 2023](https://data.humdata.org/dataset/water-extent-in-jowhar-city-jowhar-district-middle-shabelle-region-somalia-as-of-20-novemb)
- [Satellite detected water extent in Jowhar City, Jowhar District, Middle Shabelle Region, Somalia as of 22 November 2023](https://data.humdata.org/dataset/water-extent-in-jowhar-city-jowhar-district-middle-shabelle-region-somalia-as-of-22-novemb)
- [Satellite detected water extent in Jowhar City, Jowhar District, Middle Shabelle Region, Somalia, 22 November 2023](https://data.humdata.org/dataset/water-extent-in-jowhar-city-jowhar-district-middle-shabelle-region-somalia-22-november-202)
- [Satellite detected water extent in Juba Hoose and Juba Dhexe Region, Somalia, 3 December 2023](https://data.humdata.org/dataset/water-extent-in-juba-hoose-and-juba-dhexe-region-somalia-3-december-2023)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [42.27506835000008, 0.4125755430000595, 45.59669995000007, 4.994503980000047]

## Temporal Coverage

- **Start**: 2023-11-13T00:00:00Z
- **End**: 2023-12-05T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SiteID | int16 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `SiteID_label`, which is decoded per source file. |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT-4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT-6; 42 = Sentinel-1; 43 = Kompsat-2; 44 = Sentinel-2; 45 = Sentinel-3; 46 = Kompsat-3; 47 = Deimos-2; 48 = TripleSat; 49 = PlanetLabs; 50 = RapidEye; 51 = WorldView-4; 52 = SPOT-7; 53 = Jilin-1; 54 = GaoFen-2; 55 = SkySat; 56 = ICEYE; 57 = Landsat-9; 58 = VIIRS-NOAA; 59 = RCM-1; 60 = RCM-2; 61 = RCM-3; 62 = TanDEM-X; 63 = BlackSky; …. The decoded text is in `SensorID_label`. |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Settlement_Name | string |  |
| Notes | string | Free-text notes by the analyst. |
| Main_Damage_Site_Class | int16 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Main_Damage_Site_Class_label`, which is decoded per source file. |
| Grouped_Damage_Classes | int16 | Coded value. The source geodatabase domain gives: 1 = Damaged Buildings; 2 = Damaged Greenhouses; 3 = Impacts on Roads / Bridges; 4 = Impacts in Fields; 5 = Damaged Road segments; 6 = Damaged Port. The decoded text is in `Grouped_Damage_Classes_label`. |
| StaffID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| ImageID_Num | int32 |  |
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
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20231105som-damage-sites.parquet | 12.7 MB | 122002d6de37... |
| ./fl20231105som-damage-sites.pmtiles | 4.0 MB | 12207960993a... |
| ./styles/default.json | 1.0 KB | 1220fd70eab3... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20231105som-damage-sites.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/water-extent-in-bardere-city-baardheere-district-gedo-region-somalia-13-november-2023](https://data.humdata.org/dataset/water-extent-in-bardere-city-baardheere-district-gedo-region-somalia-13-november-2023)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `GF2_20231123_AffectedStructures_BeledweyneCity_HiraanRegion`, `PHR_20231112_AffectedStructure_BeledweyneCity_MiddleShabelleRegion`, `PHR_20231113_AffectedStructures_BaardhereCity_GedoRegion`, `PHR_20231113_AffectedStructures_BuaaleCity_MiddleJubaRegion`, `PHR_20231115_AffectedBuildings_JilibCity_MiddleJubaRegion`, `PHR_20231116_AffectedStructures_LuuqCity_GedoRegion`, `S2_20231115_BuildingAffectAssessment_AlongWebiShabelleRiver`, `S2_20231120_BuildingAffectAssessment_AlongWebiShabelleRiver`, `WV2_20231122_AffectedStructure_JowharCity_MiddleShabelleRegion`, `WV2_20231124_AffectedStructures_Jilib_Somalia`, `WV2_20231130_AffectedStructures_BeledweyneCity_HiraanRegion`, `WV2_20231130_AffectedStructures_BuloBurto_HiraanRegion`, `WV3_20231122_AffectedStructures_BaardhereCity_GedoRegion`, `WV3_20231122_AffectedStructures_BuaaleCity_MiddleJubaRegion`, `WV3_20231129SOM_AffectedStructure_Baardhere_GedoRegion`, `WV3_20231129_AffectedStructures_LuuqCity_GedoRegion`.

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

# Analysis extent: Flood, Somalia, 5 November 2023 (FL20231105SOM)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2023/fl20231105som/fl20231105som-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Analysis extent for Flood, Somalia, 5 November 2023 (FL20231105SOM): 1,568 features merged from 404 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Floods in Somalia, November 2023](https://data.humdata.org/dataset/floods-in-somalia-november-2023)
- [Preliminary satellite-derived flood assessment - Bu’aale District, Middle Juba Region, Somalia - 09 November 2023](https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-buaale-district-middle-juba-region-somalia-)
- [Preliminary satellite-derived flood assessment - Jowhar District, Middle Shabelle Region, Somalia - 09 November 2023](https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-jowhar-district-middle-shabelle-region-soma)
- [Preliminary satellite-derived flood assessment -Bardere City, Baardheere District, Gedo Region, Somalia](https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-bardere-city-baardheere-district-gedo-regio)
- [Satellite detected water extent in Bardere City, Baardheere District, Gedo Region, Somalia, 13 November 2023](https://data.humdata.org/dataset/water-extent-in-bardere-city-baardheere-district-gedo-region-somalia-13-november-2023)
- [Satellite detected water extent in Bardere City, Baardheere District, Gedo Region, Somalia, 22 November 2023](https://data.humdata.org/dataset/water-extent-in-bardere-city-baardheere-district-gedo-region-somalia-22-november-2023)
- [Satellite detected water extent in Bardere City, Baardheere District, Gedo Region, Somalia, 29 November 2023](https://data.humdata.org/dataset/water-extent-in-bardere-city-baardheere-district-gedo-region-somalia-29-november-2023)
- [Satellite detected water extent in Beledweyne City, Beledweyne District, Hiraan Region, Somalia, 12 November 2023](https://data.humdata.org/dataset/water-extent-in-beledweyne-city-beledweyne-district-hiraan-region-somalia-12-november-2023)
- [Satellite detected water extent in Bu'aale City, Bu'aale District, Middle Juba Region, Somalia, 13 November 2023](https://data.humdata.org/dataset/water-extent-in-bu-aale-city-bu-aale-district-middle-juba-region-somalia-13-november-2023)
- [Satellite detected water extent in Bu'aale City, Bu'aale District, Middle Juba Region, Somalia, 22 November 2023](https://data.humdata.org/dataset/water-extent-in-bu-aale-city-bu-aale-district-middle-juba-region-somalia-22-november-2023)
- [Satellite detected water extent in Buloburto City and surroundings, Buloburto District, Hiraan Region, Somalia, 30 November 2023](https://data.humdata.org/dataset/water-extent-in-buloburto-city-and-surroundings-buloburto-district-hiraan-region-somalia-3)
- [Satellite detected water extent in Gedo & Juba Dhexe Region, Somalia as of 07 November 2023](https://data.humdata.org/dataset/satellite-detected-water-extent-in-gedo-juba-dhexe-region-somalia-as-of-07-november-2023)
- and 8 more; the event's [catalog page](../catalog.json) lists them all.

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [40.99487507500004, -1.664897400999962, 51.413032532000045, 11.985202789000084]

## Temporal Coverage

- **Start**: 2023-11-07T00:00:00Z
- **End**: 2023-12-05T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | string | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT-4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT-6; 42 = Sentinel-1; 43 = Kompsat-2; 44 = Sentinel-2; 45 = Sentinel-3; 46 = Kompsat-3; 47 = Deimos-2; 48 = TripleSat; 49 = PlanetLabs; 50 = RapidEye; 51 = WorldView-4; 52 = SPOT-7; 53 = Jilin-1; 54 = GaoFen-2; 55 = SkySat; 56 = ICEYE; 57 = Landsat-9; 58 = VIIRS-NOAA; 59 = RCM-1; 60 = RCM-2; 61 = RCM-3; 62 = TanDEM-X; 63 = BlackSky; …. The decoded text is in `SensorID_label`. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | string | Coded value. The 2 source files of this collection use 2 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Area_ha | float | Area in hectares, as UNOSAT computed it. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Staff_ID | int32 |  |
| ConfidenceID_label | string | `ConfidenceID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| FieldValidation_label | string | `FieldValidation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Sensor_ID | string |  |
| EventCod | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Confidence | string |  |
| FieldValid | string |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20231105som-analysis-extent.parquet | 3.6 MB | 122011bb442d... |
| ./fl20231105som-analysis-extent.pmtiles | 10.1 MB | 12204878f6af... |
| ./styles/default.json | 671 B | 12208562dc5c... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20231105som-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/floods-in-somalia-november-2023](https://data.humdata.org/dataset/floods-in-somalia-november-2023)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `GF2_20231123_AnalysisExtent_BeledweyneCity_HiraanRegion`, `PHR_20231112_AnalysisExtent_BeledweyneCity_ShabelleRegion`, `PHR_20231112_CloudObstruction_BeledweyneCity_ShabelleRegion`, `PHR_20231113_AnalysisExtent_Baardhere_GedoRegion`, `PHR_20231113_AnalysisExtent_BuaaleCity_MiddleJubaRegion`, `PHR_20231113_CloudObstruction_Baardhere_GedoRegion`, `PHR_20231115_AnalysisExtent_JilibCity_MiddleJubaRegion`, `PHR_20231116_AnalysisExtent_LuuqCity_GedoRegion`, `PHR_20231116_CloudObstruction_LuuqCity_GedoRegion`, `RCM_20231122_AnalysisExtent_Jowhar_MiddleShabelleRegion`, `S1_20231105_AnalysisExtent_Gedo_JubaRegion`, `S1_20231107_AnalysisExtent_Doolow_LuuqDistrict_GedoRegion`, `S1_20231107_AnalysisExtent_Gedo_JubaRegion`, `S1_20231109_AnalysisExtent_Jowhar_MiddleShabelleRegion`, `S2_20231115_AnalysisExtent_AlongWebiShabelleRiver`, `S2_20231115_CloudObstruction_AlongWebiShabelleRiver`, `S2_20231120_AnalysisExtent_Along_AlongWebiShabelleRiver`, `S2_20231120_AnalysisExtent_Jowhar_MiddleShabelleRegion`, `S2_20231120_CloudObstruction_AlongWebiShabelleRiver`, `S2_20231120_CloudObstruction_Jowhar_MiddleShabelleRegion`, `S2_20231203_AnalysisExtent_JubaHoose_JubaDhexeRegion`, `VIIRS_20231101_20231105_AnalysisExtent_SouthSomalia`, `VIIRS_20231128_20231202_AnalysisExtent_SouthSomalia`, `WV2_20231122_AnalysisExtent_JowharCity_MiddleShabelleRegion`, `WV2_20231122_CloudObstruction_JowharCity_MiddleShabelleRegion`, `WV2_20231124_AnalysisExtent_Jilib_Somalia`, `WV2_20231130_AnalysisExtent_BeledweyneCity_HiraanRegion`, `WV2_20231130_AnalysisExtent_BuloBurto_HiraanRegion`, `WV3_20231122_AnalysisExtent_Baardhere_GedoRegion`, `WV3_20231122_AnalysisExtent_BuaaleCity_MiddleJubaRegion`, `WV3_20231129_AnalysisExtent_Baardhere_GedoRegion`, `WV3_20231129_AnalysisExtent_LuuqCity_GedoRegion`.

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

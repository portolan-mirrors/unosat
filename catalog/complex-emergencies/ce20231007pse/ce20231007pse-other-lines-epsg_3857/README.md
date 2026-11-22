# Other lines: Complex emergency, State of Palestine, 7 October 2023 (CE20231007PSE)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20231007pse/ce20231007pse-other-lines-epsg_3857/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Other lines for Complex emergency, State of Palestine, 7 October 2023 (CE20231007PSE): 187,625 features merged from 4 source layers. Lines layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from. The geometry is in EPSG:3857, the CRS of the source layers; the PMTiles copy is in Web Mercator.

From these HDX datasets:

- [UNOSAT Gaza Strip Road Network Comprehensive Damage Assessment](https://data.humdata.org/dataset/unosat-gaza-strip-road-network-comprehensive-damage-assessment)
- [UNOSAT Gaza Strip Road Network Comprehensive Damage Assessment - August 2024](https://data.humdata.org/dataset/unosat-gaza-strip-road-network-comprehensive-damage-assessment-august-2024)
- [UNOSAT Gaza Strip Road Network Comprehensive Damage Assessment - July 2025](https://data.humdata.org/dataset/unosat-gaza-strip-road-network-comprehensive-damage-assessment-july-2025)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![crisis-opt-israel-hostilities](https://img.shields.io/badge/crisis--opt--israel--hostilities-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [34.219768930439415, 31.22697776049942, 34.567661938429545, 31.59212964761192]

## Temporal Coverage

- **Start**: 2024-06-14T00:00:00Z
- **End**: 2025-09-12T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| RoadType | string |  |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT-4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT-6; 42 = Sentinel-1; 43 = Kompsat-2; 44 = Sentinel-2; 45 = Sentinel-3; 46 = Kompsat-3; 47 = Deimos-2; 48 = TripleSat; 49 = PlanetLabs; 50 = RapidEye; 51 = WorldView-4; 52 = SPOT-7; 53 = Jilin-1; 54 = GaoFen-2; 55 = SkySat; 56 = ICEYE; 57 = Landsat-9; 58 = VIIRS-NOAA; 59 = RCM-1; 60 = RCM-2; 61 = RCM-3; 62 = TanDEM-X; 63 = BlackSky; …. The decoded text is in `SensorID_label`. |
| Classification | int16 | Coded value. The source geodatabase domain gives: 1 = Impact crater; 2 = Debris (moderate); 3 = Debris (severe); 4 = Bulldozed; 5 = Destroyed; 6 = Obstacles. The decoded text is in `Classification_label`. |
| UNHabitat_DL | string |  |
| Length_km | double |  |
| Length_m | double |  |
| Governorate | string |  |
| Notes | string | Free-text notes by the analyst. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Shape_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Classification_label | string | `Classification` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| Name | string |  |
| Classification1 | int16 | Coded value. The source geodatabase domain gives: 1 = Destroyed; 2 = Severely affected; 3 = Moderately affected; 4 = Obstacles; 5 = No visible damage. The decoded text is in `Classification1_label`. |
| SensorDate2 | timestamp[us, tz=UTC] |  |
| SensorID2 | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT-4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT-6; 42 = Sentinel-1; 43 = Kompsat-2; 44 = Sentinel-2; 45 = Sentinel-3; 46 = Kompsat-3; 47 = Deimos-2; 48 = TripleSat; 49 = PlanetLabs; 50 = RapidEye; 51 = WorldView-4; 52 = SPOT-7; 53 = Jilin-1; 54 = GaoFen-2; 55 = SkySat; 56 = ICEYE; 57 = Landsat-9; 58 = VIIRS-NOAA; 59 = RCM-1; 60 = RCM-2; 61 = RCM-3; 62 = TanDEM-X; 63 = BlackSky; …. The decoded text is in `SensorID2_label`. |
| Classification2 | int16 | Coded value. The source geodatabase domain gives: 1 = Destroyed; 2 = Severely affected; 3 = Moderately affected; 4 = Obstacles; 5 = No visible damage. The decoded text is in `Classification2_label`. |
| DamageStatus | int16 | Coded value. The source geodatabase domain gives: 0 = No change; 1 = Increase - damage; 2 = Decrease - damage; 3 = New - damage; 4 = Demolished; 5 = Rebuilt; 6 = Reconstructed. The decoded text is in `DamageStatus_label`. |
| Field | int32 |  |
| Classification1_label | string | `Classification1` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Classification2_label | string | `Classification2` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| DamageStatus_label | string | `DamageStatus` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID2_label | string | `SensorID2` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorDate3 | timestamp[us, tz=UTC] |  |
| SensorID3 | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT-4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT-6; 42 = Sentinel-1; 43 = Kompsat-2; 44 = Sentinel-2; 45 = Sentinel-3; 46 = Kompsat-3; 47 = Deimos-2; 48 = TripleSat; 49 = PlanetLabs; 50 = RapidEye; 51 = WorldView-4; 52 = SPOT-7; 53 = Jilin-1; 54 = GaoFen-2; 55 = SkySat; 56 = ICEYE; 57 = Landsat-9; 58 = VIIRS-NOAA; 59 = RCM-1; 60 = RCM-2; 61 = RCM-3; 62 = TanDEM-X; 63 = BlackSky; …. The decoded text is in `SensorID3_label`. |
| Classification3 | int16 | Coded value. The source geodatabase domain gives: 1 = Destroyed; 2 = Severely affected; 3 = Moderately affected; 4 = Obstacles; 5 = No visible damage. The decoded text is in `Classification3_label`. |
| DamageStatus3 | int16 | Coded value. The source geodatabase domain gives: 0 = No change; 1 = Increase - damage; 2 = Decrease - damage; 3 = New - damage; 4 = Demolished; 5 = Rebuilt; 6 = Reconstructed. The decoded text is in `DamageStatus3_label`. |
| Classification3_label | string | `Classification3` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| DamageStatus3_label | string | `DamageStatus3` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID3_label | string | `SensorID3` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20231007pse-other-lines-epsg_3857.parquet | 5.5 MB | 1220f97694c8... |
| ./ce20231007pse-other-lines-epsg_3857.pmtiles | 11.1 MB | 1220aa64ef64... |
| ./styles/default.json | 411 B | 12200c93a529... |
| ./ce20231007pse-other-lines-epsg_3857.thumb.jpg | 27.9 KB | 122090e53dcf... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20231007pse-other-lines-epsg_3857.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/unosat-gaza-strip-road-network-comprehensive-damage-assessment](https://data.humdata.org/dataset/unosat-gaza-strip-road-network-comprehensive-damage-assessment)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `CE20231007PSE_UNOSAT_UNHABITAT_GazaStrip_RoadAssessment_20240529`, `Gaza_NewRoadCorridor_18082024`, `UNOSAT_Gaza_RoadCDA_18082024`, `UNOSAT_Gaza_RoadCDA_OCHA_Road_Assessment_20250708`.

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

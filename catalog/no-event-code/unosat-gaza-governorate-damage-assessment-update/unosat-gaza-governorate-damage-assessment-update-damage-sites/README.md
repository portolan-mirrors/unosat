# Damage sites: UNOSAT Gaza Governorate Damage Assessment Update
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/no-event-code/unosat-gaza-governorate-damage-assessment-update/unosat-gaza-governorate-damage-assessment-update-damage-sites/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Damage sites for UNOSAT Gaza Governorate Damage Assessment Update: 9,138 features merged from 4 source layers. Point layers with a damage class column (such as `Main_Damage_Site_Class`): one point per assessed structure or site. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [UNOSAT Gaza Governorate Damage Assessment Update](https://data.humdata.org/dataset/unosat-gaza-governorate-damage-assessment-update)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![crisis-opt-israel-hostilities](https://img.shields.io/badge/crisis--opt--israel--hostilities-blue) ![dataset](https://img.shields.io/badge/dataset-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [34.38461386200004, 31.431923048000044, 34.56456913400007, 31.589428619000046]

## Temporal Coverage

- **Start**: 2023-10-20T00:00:00Z
- **End**: 2023-10-20T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SiteID | int16 | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Stadium; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 42 = Military Facility; 45 = Suspected Mass Grave Site; 46 = Airport Facility; 47 = Church; 48 = Dam; 49 = Port. The decoded text is in `SiteID_label`. |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT-4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT-6; 42 = Sentinel-1; 43 = Kompsat-2; 44 = Sentinel-2; 45 = Sentinel-3; 46 = Kompsat-3; 47 = Deimos-2; 48 = TripleSat; 49 = PlanetLabs; 50 = RapidEye; 51 = WorldView-4; 52 = SPOT-7; 53 = Jilin-1; 54 = GaoFen-2; 55 = SkySat; 56 = ICEYE; 57 = Landsat-9; 58 = VIIRS-NOAA; 59 = RCM-1; 60 = RCM-2; 61 = RCM-3; 62 = TanDEM-X; 63 = BlackSky; …. The decoded text is in `SensorID_label`. |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| Main_Damage_Site_Class | int16 | Coded value. The source geodatabase domain gives: 1 = Destroyed; 2 = Severe Damage; 3 = Moderate Damage; 4 = Possible Damage; 5 = Impact Crater (Damage to Road); 6 = No Visible Damage; 7 = Impact Crater (Damage to Field); 8 = Destroyed (Demolition Zone); 9 = Suspected Phosphorus shell Attack Zone; 10 = Road Damage from Tank Passage; 11 = Possible Damage from adjacent impact, debris; 12 = Lava Flow; 13 = Damage. The decoded text is in `Main_Damage_Site_Class_label`. |
| Grouped_Damage_Classes | int16 | Coded value. The source geodatabase domain gives: 1 = Damaged Buildings; 2 = Damaged Greenhouses; 3 = Impacts on Roads / Bridges; 4 = Impacts in Fields; 5 = Damaged Road segments; 6 = Damaged Port. The decoded text is in `Grouped_Damage_Classes_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Notes | string | Free-text notes by the analyst. |
| Settlement_Name | string |  |
| Neighborhood | string |  |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| ConfidenceID_label | string | `ConfidenceID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| FieldValidation_label | string | `FieldValidation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Grouped_Damage_Classes_label | string | `Grouped_Damage_Classes` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Main_Damage_Site_Class_label | string | `Main_Damage_Site_Class` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SiteID_label | string | `SiteID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| SensorDate_2 | timestamp[us, tz=UTC] |  |
| SensorID_2 | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT-4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT-6; 42 = Sentinel-1; 43 = Kompsat-2; 44 = Sentinel-2; 45 = Sentinel-3; 46 = Kompsat-3; 47 = Deimos-2; 48 = TripleSat; 49 = PlanetLabs; 50 = RapidEye; 51 = WorldView-4; 52 = SPOT-7; 53 = Jilin-1; 54 = GaoFen-2; 55 = SkySat; 56 = ICEYE; 57 = Landsat-9; 58 = VIIRS-NOAA; 59 = RCM-1; 60 = RCM-2; 61 = RCM-3; 62 = TanDEM-X; 63 = BlackSky; …. The decoded text is in `SensorID_2_label`. |
| ConfidenceID_2 | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_2_label`. |
| Main_Damage_Site_Class_2 | int16 | Coded value. The source geodatabase domain gives: 1 = Destroyed; 2 = Severe Damage; 3 = Moderate Damage; 4 = Possible Damage; 5 = Impact Crater (Damage to Road); 6 = No Visible Damage; 7 = Impact Crater (Damage to Field); 8 = Destroyed (Demolition Zone); 9 = Suspected Phosphorus shell Attack Zone; 10 = Road Damage from Tank Passage; 11 = Possible Damage from adjacent impact, debris; 12 = Lava Flow; 13 = Damage. The decoded text is in `Main_Damage_Site_Class_2_label`. |
| Damage_Status_2 | int16 |  |
| SensorDate_3 | timestamp[us, tz=UTC] |  |
| SensorID_3 | int32 |  |
| ConfidenceID_3 | int16 |  |
| Main_Damage_Site_Class_3 | int16 |  |
| Damage_Status_3 | int16 |  |
| SensorDate_4 | timestamp[us, tz=UTC] |  |
| SensorID_4 | int32 |  |
| ConfidenceID_4 | int16 |  |
| Main_Damage_Site_Class_4 | int16 |  |
| Damage_Status_4 | int16 |  |
| SensorDate_5 | timestamp[us, tz=UTC] |  |
| SensorID_5 | int32 |  |
| ConfidenceID_5 | int16 |  |
| Main_Damage_Site_Class_5 | int16 |  |
| Damage_Status_5 | int16 |  |
| SensorDate_6 | timestamp[us, tz=UTC] |  |
| SensorID_6 | int32 |  |
| ConfidenceID_6 | int16 |  |
| Main_Damage_Site_Class_6 | int16 |  |
| Damage_Status_6 | int16 |  |
| SensorDate_7 | timestamp[us, tz=UTC] |  |
| SensorID_7 | int32 |  |
| ConfidenceID_7 | int16 |  |
| Main_Damage_Site_Class_7 | int16 |  |
| Damage_Status_7 | int16 |  |
| SensorDate_8 | timestamp[us, tz=UTC] |  |
| SensorID_8 | int32 |  |
| ConfidenceID_8 | int16 |  |
| Main_Damage_Site_Class_8 | int16 |  |
| Damage_Status_8 | int16 |  |
| SensorDate_9 | timestamp[us, tz=UTC] |  |
| SensorID_9 | int32 |  |
| ConfidenceID_9 | int16 |  |
| Main_Damage_Site_Class_9 | int16 |  |
| Damage_Status_9 | int16 |  |
| SensorDate_10 | timestamp[us, tz=UTC] |  |
| SensorID_10 | int32 |  |
| ConfidenceID_10 | int16 |  |
| Main_Damage_Site_Class_10 | int16 |  |
| Damage_Status_10 | int16 |  |
| Construction_Status | int16 |  |
| StaffID | int32 |  |
| ConfidenceID_2_label | string | `ConfidenceID_2` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Main_Damage_Site_Class_2_label | string | `Main_Damage_Site_Class_2` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_2_label | string | `SensorID_2` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./unosat-gaza-governorate-damage-assessment-update-damage-sites.parquet | 369.2 KB | 1220a7be2eb7... |
| ./unosat-gaza-governorate-damage-assessment-update-damage-sites.pmtiles | 342.0 KB | 122096f83dca... |
| ./styles/default.json | 1.1 KB | 1220498eefb2... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./unosat-gaza-governorate-damage-assessment-update-damage-sites.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/unosat-gaza-governorate-damage-assessment-update](https://data.humdata.org/dataset/unosat-gaza-governorate-damage-assessment-update)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Damage_Sites_Agriculture_NorthGazaGov_20231015`, `Damage_Sites_GazaGov_20231010`, `Damage_Sites_GazaGov_20231015`, `Damage_Sites_NorthGazaGov_20231015`.

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

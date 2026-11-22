# Damage sites: Tropical cyclone, Philippines, 16 December 2021 (TC20211216PHL)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/tropical-cyclones/2021/tc20211216phl/tc20211216phl-damage-sites/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Damage sites for Tropical cyclone, Philippines, 16 December 2021 (TC20211216PHL): 20,547 features merged from 28 source layers. Point layers with a damage class column (such as `Main_Damage_Site_Class`): one point per assessed structure or site. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [16th of December 2021 Tropical Cyclone RAI-21, Philippines. Preliminary Satellite-Based Comprehensive Damage Assessment](https://data.humdata.org/dataset/16th-of-december-2021-tropical-cyclone-rai-21-philippines-preliminary-satellite-based-comp)
- [Damage assessment  in Roxas town, Palawan province, Region IV-B (Mimaropa), Philippines  as of 21 December 2021](https://data.humdata.org/dataset/damage-assessment-in-roxas-town-palawan-province-region-iv-b-mimaropa-philippines-as-of-21)
- [Damage assessment in Bien Unido, Trinidad & Ubay municipalities, Bohol Province, Philippines as of 23 December 2021](https://data.humdata.org/dataset/damage-assessment-in-bien-unido-trinidad-ubay-municipalities-bohol-province-philippines-as)
- [Damage assessment in Bucas Grande Island, Socorro, Surigao del Norte of Philippines as of 17 December 2021](https://data.humdata.org/dataset/damage-assessment-in-bucas-grande-island-socorro-surigao-del-norte-of-philippines-as-of-17)
- [Damage assessment in City of Carcar and San Fernando municipalities, Cebu Province, Region VII, Philippines](https://data.humdata.org/dataset/damage-assessment-in-city-of-carcar-and-san-fernando-municipalities-cebu-province-region-v)
- [Damage assessment in City of Naga Municipality, Cebu Province, Region VII, Philippines as of 21 December 2021](https://data.humdata.org/dataset/damage-assessment-in-city-of-naga-municipality-cebu-province-region-vii-philippines-as-of-)
- [Damage assessment in City of Talisay municipality, Cebu Province, Region VII, Philippines as of 21 December 2021](https://data.humdata.org/dataset/damage-assessment-in-city-of-talisay-municipality-cebu-province-region-vii-philippines-as-)
- [Damage assessment in Dinagat Island, Region XIII of Philippines as of 23 December 2021](https://data.humdata.org/dataset/damage-assessment-in-dinagat-island-region-xiii-of-philippines-as-of-23-december-2021)
- [Damage assessment in Jimalalud and La Libertad municipalities, Negros Oriental Province, Region VII, Philippines](https://data.humdata.org/dataset/damage-assessment-in-jimalalud-and-la-libertad-municipalities-negros-oriental-province-reg)
- [Damage assessment in Siargao Island, General Luna, Surigao del Norte of Philippines as of 26 December 2021](https://data.humdata.org/dataset/damage-assessment-in-siargao-island-general-luna-surigao-del-norte-of-philippines-as-of-26)
- [Damage assessment in Talibon municipality, Bohol Province, Region VII, Philippines as of 23 December 2021](https://data.humdata.org/dataset/damage-assessment-in-talibon-municipality-bohol-province-region-vii-philippines-as-of-23-d)
- [Damage assessment in Ubay municipality, Bohol Province, Region VII (Central Visayas), Philippines as of 23 December 2021](https://data.humdata.org/dataset/damage-assessment-in-ubay-municipality-bohol-province-region-vii-central-visayas-philippin)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![cyclones-hurricanes-typhoons](https://img.shields.io/badge/cyclones--hurricanes--typhoons-blue) ![geodata](https://img.shields.io/badge/geodata-blue) ![tropical cyclone](https://img.shields.io/badge/tropical_cyclone-blue)

## Spatial Coverage

- **Bounding Box**: [119.32228563600006, 9.645493492000071, 126.16827328400007, 10.530319981000048]

## Temporal Coverage

- **Start**: 2021-12-23T00:00:00Z
- **End**: 2022-01-14T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SiteID | int16 | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Staduim; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 42 = Military Facility; 45 = Suspected Mass Grave Site; 46 = Airport Facility; 47 = Church. The decoded text is in `SiteID_label`. |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT-4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT-6; 42 = Sentinel-1; 43 = Kompsat-2; 44 = Sentinel-2; 45 = Sentinel-3; 46 = Kompsat-3; 47 = Deimos-2; 48 = TripleSat; 49 = PlanetLabs; 50 = RapidEye; 51 = WorldView-4; 52 = SPOT-7; 999 = Combination of Sensors. The decoded text is in `SensorID_label`. |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Settlement_Name | string |  |
| Notes | string | Free-text notes by the analyst. |
| Main_Damage_Site_Class | int16 | Coded value. The source geodatabase domain gives: 1 = Destroyed; 2 = Severe Damage; 3 = Moderate Damage; 4 = Possible Damage; 5 = Impact Crater (Damage to Road); 6 = No Visible Damage; 7 = Impact Crater (Damage to Field); 8 = Destroyed (Demolition Zone); 9 = Suspected Phosphorus shell Attack Zone; 10 = Road Damage from Tank Passage; 11 = Possible Damage from adjacent impact, debris; 12 = Lava Flow. The decoded text is in `Main_Damage_Site_Class_label`. |
| Grouped_Damage_Classes | int16 | Coded value. The source geodatabase domain gives: 1 = Damaged Buildings; 2 = Damaged Greenhouses; 3 = Impacts on Roads / Bridges; 4 = Impacts in Fields; 5 = Damaged Road segments. The decoded text is in `Grouped_Damage_Classes_label`. |
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
| ./tc20211216phl-damage-sites.parquet | 773.6 KB | 1220a7e6fbbc... |
| ./tc20211216phl-damage-sites.pmtiles | 783.7 KB | 12206768008b... |
| ./styles/default.json | 1.1 KB | 12206555514a... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./tc20211216phl-damage-sites.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/16th-of-december-2021-tropical-cyclone-rai-21-philippines-preliminary-satellite-based-comp](https://data.humdata.org/dataset/16th-of-december-2021-tropical-cyclone-rai-21-philippines-preliminary-satellite-based-comp)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `PHR_20211221_DamagedSchoolHospital_PalawanIsland`, `PHR_20211221_Damaged_CityofNaga`, `PHR_20211221_Damaged_CityofTalisay_Cebu`, `PHR_20211221_Damaged_PalawanIsland`, `PHR_20211221_PotentiallyDamaged_CityofNaga`, `PHR_20211221_PotentiallyDamaged_CityofTalisay_Cebu`, `PHR_20211221_PotentiallyDamaged_PalawanIsland`, `PHR_20211222_Damaged_LaLibertad_NegrosIsland`, `PHR_20211222_PotentiallyDamaged_LaLibertad_NegrosIsland`, `PHR_20211223_DamagedPort_DinagatIsland`, `PHR_20211223_Damaged_CarcarCity_SanFernando`, `PHR_20211223_Damaged_DinagatIsland`, `PHR_20211223_Damaged_NorthernBoholIsland_Center`, `PHR_20211223_Damaged_NorthernBoholIsland_NW`, `PHR_20211223_Damaged_NorthernBoholIsland_SE`, `PHR_20211223_Damaged_SouthernLeyteProvince`, `PHR_20211223_PotentiallyDamaged_CarcarCity_SanFernando`, `PHR_20211223_PotentiallyDamaged_DinagatIsland`, `PHR_20211223_PotentiallyDamaged_Dumaran`, `PHR_20211223_PotentiallyDamaged_NorthernBoholIsland_Center`, `PHR_20211223_PotentiallyDamaged_NorthernBoholIsland_NW`, `PHR_20211223_PotentiallyDamaged_NorthernBoholIsland_SE`, `PHR_20211226_Damaged_GeneralLuna`, `PHR_20211226_PotentiallyDamaged_GeneralLuna`, `WV3_20211217_DamagedBridge_Socorro`, `WV3_20211217_Damaged_Socorro`, `WV3_20211217_PotentiallyDamaged_Socorro`, `WV3_20211217_Road_Obstacle_Socorro`.

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

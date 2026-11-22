# Other points: Tropical cyclone, Fiji, 19 February 2016 (TC20160219FJI)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/tropical-cyclones/2016/tc20160219fji/tc20160219fji-other-points/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Other points for Tropical cyclone, Fiji, 19 February 2016 (TC20160219FJI): 299 features merged from 1 source layer. Points layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of Damage Assessment in Greater Lautoka Area, Ba Province, Western Division, Fiji](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-greater-lautoka-area-ba-province-western-divi-february-25-2016)
- [Geodata of Damage Assessment in Sasa Area, Ba Province, Western Division, Fiji](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-sasa-area-ba-province-western-division-fiji-march-03-2016)
- [Geodata of Damage Assessment in Vatukoula Area, Ba Province, Western Division, Fiji](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-vatukoula-area-ba-province-western-division-f-march-02-2016)
- [Geodata of Damage Assessment over north and west of Ba Town, Ba Province, Western Division, Fiji](https://data.humdata.org/dataset/geodata-of-damage-assessment-over-north-and-west-of-ba-town-ba-province-weste-march-03-2016)
- [Geodata of Population Exposure Analysis - Tropical Cyclone Winston - 19 February 2016](https://data.humdata.org/dataset/geodata-of-population-exposure-analysis-tropical-cyclone-winston-19-february-march-09-2016)
- [Geodata of Population Exposure Analysis - Tropical Cyclone Winston - 22 February 2016](https://data.humdata.org/dataset/geodata-of-population-exposure-analysis-tropical-cyclone-winston-22-february-march-09-2016)
- [Geodata of Satellite Detected Waters in Savu Area, Naitasiri Province, Central Division, Fiji](https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-in-savu-area-naitasiri-province-central-february-22-2016)
- [Geodata of UNOSAT Damage Assessment Activities in Viti Levu Island, Fiji](https://data.humdata.org/dataset/geodata-of-unosat-damage-assessment-activities-in-viti-levu-island-fiji-march-10-2016)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![cyclones-hurricanes-typhoons](https://img.shields.io/badge/cyclones--hurricanes--typhoons-blue) ![geodata](https://img.shields.io/badge/geodata-blue) ![tropical cyclone](https://img.shields.io/badge/tropical_cyclone-blue)

## Spatial Coverage

- **Bounding Box**: [177.8293119, -17.513954747999946, 177.90300688600007, -17.48182596299995]

## Temporal Coverage

- **Start**: 2016-02-22T00:00:00Z
- **End**: 2016-03-10T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SiteID | int16 | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Staduim; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 45 = Suspected Mass Grave Site. The decoded text is in `SiteID_label`. |
| DamageID1 | int16 | Coded value. The source geodatabase domain gives: 1 = Destroyed; 2 = Severe Damage; 3 = Moderate Damage; 4 = Possible Damage; 5 = Impact Crater (Damage to Road); 6 = No Visible Damage; 7 = Impact Crater (Damage to Field); 8 = Destroyed (Demolition Zone); 9 = Suspected Phosphorus shell Attack Zone; 10 = Road Damage from Tank Passage; 11 = Possible Damage from adjacent impact, debris. The decoded text is in `DamageID1_label`. |
| DamageID2 | int16 | Coded value. The source geodatabase domain gives: 1 = Damaged Buildings; 2 = Damaged Greenhouses; 3 = Impacts on Roads / Bridges; 4 = Impacts in Fields; 5 = Damaged Road segments. The decoded text is in `DamageID2_label`. |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The source geodatabase domain gives: 1 = Worldview-1; 2 = Worldview-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = Komsat-2; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleadies; 999 = Combination of Sensors. The decoded text is in `SensorID_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Settlement_Name | string |  |
| Notes | string | Free-text notes by the analyst. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 22 = WP; 33 = LB; 44 = JL; 55 = MF; 66 = RS; 77 = LD; 88 = HK. The decoded text is in `StaffID_label`. |
| ConfidenceID_label | string | `ConfidenceID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| DamageID1_label | string | `DamageID1` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| DamageID2_label | string | `DamageID2` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| FieldValidation_label | string | `FieldValidation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
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
| ./tc20160219fji-other-points.parquet | 24.7 KB | 12209c07b313... |
| ./tc20160219fji-other-points.pmtiles | 72.1 KB | 1220f1a2a74e... |
| ./styles/default.json | 695 B | 1220043677bc... |
| ./tc20160219fji-other-points.thumb.jpg | 8.9 KB | 122024de41a8... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./tc20160219fji-other-points.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-damage-assessment-in-greater-lautoka-area-ba-province-western-divi-february-25-2016](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-greater-lautoka-area-ba-province-western-divi-february-25-2016)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `PL_20160226_Vatukoula_Damge`.

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

# Damage sites: Complex emergency, Syrian Arab Republic, 4 June 2013 (CE20130604SYR)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20130604syr/ce20130604syr-damage-sites-cc_by_sa-epsg_4326/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Damage sites for Complex emergency, Syrian Arab Republic, 4 June 2013 (CE20130604SYR): 313,512 features merged from 26 source layers. Point layers with a damage class column (such as `Main_Damage_Site_Class`): one point per assessed structure or site. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Damage Density in the City of Aleppo, Syria](https://data.humdata.org/dataset/damage-density-in-the-city-of-aleppo-syria)
- [Damage assessment of Deir Ez Zor, Deir Ez Zor Governorate, Syria](https://data.humdata.org/dataset/damage-assessment-of-deir-ez-zor-deir-ez-zor-governorate-syria-2741)
- [Damage density of Ar Raqqa, Ar Raqqa Governorate, Syria](https://data.humdata.org/dataset/damage-density-of-ar-raqqa-ar-raqqa-governorate-syria-2742)
- [Damage density of Deir Ez Zor, Deir Ez Zor Governorate, Syria](https://data.humdata.org/dataset/damage-density-of-deir-ez-zor-deir-ez-zor-governorate-syria-2740)
- [Infrastructure and roads damage assessment of Ar Raqqa, Ar Raqqa Governorate, Syria](https://data.humdata.org/dataset/infrastructure-and-roads-damage-assessment-of-ar-raqqa-ar-raqqa-governorate-syria-2747)
- [Infrastructure and roads damage assessment of Deir Ez Zor, Deir Ez Zor Governorate, Syria](https://data.humdata.org/dataset/infrastructure-and-roads-damage-assessment-of-deir-ez-zor-deir-ez-zor-governorate-syria-2748)
- [Percentage damage in residential area of Aleppo City](https://data.humdata.org/dataset/percentage-damage-in-residential-area-of-aleppo-city)
- [Percentage of buildings damaged in the city of Aleppo](https://data.humdata.org/dataset/neighborhood-shelter-damage-percentages-in-aleppo-city)
- [Syria - 2014  Damage density  in Hama, Hama Governorate](https://data.humdata.org/dataset/damage-density-2014-of-hama-hama-governorate-syria)
- [Syria - 2016 Damage density in Hama, Hama Governorate](https://data.humdata.org/dataset/damage-density-2016-of-hama-hama-governorate-syria)
- [Syria - Damage assessement in Hama, Hama Governorate.](https://data.humdata.org/dataset/damage-assessement-of-hama-hama-governorate-syria)
- [Syria - Damage assessment of Deir Ez Zor, Deir Ez Zor Governorate](https://data.humdata.org/dataset/damage-assessment-of-deir-ez-zor-deir-ez-zor-governorate-syria)
- and 9 more; the event's [catalog page](../catalog.json) lists them all.

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![damage assessment](https://img.shields.io/badge/damage_assessment-blue) ![education](https://img.shields.io/badge/education-blue) ![education facilities-schools](https://img.shields.io/badge/education_facilities--schools-blue) ![geodata](https://img.shields.io/badge/geodata-blue) ![health](https://img.shields.io/badge/health-blue) ![health facilities](https://img.shields.io/badge/health_facilities-blue)

## Spatial Coverage

- **Bounding Box**: [36.070346500000085, 32.58670491400005, 40.17991499800007, 36.28290321700007]

## Temporal Coverage

- **Start**: 2016-12-16T00:00:00Z
- **End**: 2017-12-11T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SiteID | int16 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `SiteID_label`, which is decoded per source file. |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The 3 source files of this collection use 3 different domains for it, so read `SensorID_label`, which is decoded per source file. |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| Main_Damage_Site_Class | int16 | Coded value. The source geodatabase domain gives: 1 = Destroyed; 2 = Severe Damage; 3 = Moderate Damage; 4 = Possible Damage; 5 = Impact Crater (Damage to Road); 6 = No Visible Damage; 7 = Impact Crater (Damage to Field); 8 = Destroyed (Demolition Zone); 9 = Suspected Phosphorus shell Attack Zone; 10 = Road Damage from Tank Passage; 11 = Possible Damage from adjacent impact, debris. The decoded text is in `Main_Damage_Site_Class_label`. |
| SensorDate_2 | timestamp[us, tz=UTC] |  |
| SensorID_2 | int32 | Coded value. The 3 source files of this collection use 3 different domains for it, so read `SensorID_2_label`, which is decoded per source file. |
| ConfidenceID_2 | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_2_label`. |
| Main_Damage_Site_Class_2 | int16 | Coded value. The source geodatabase domain gives: 1 = Destroyed; 2 = Severe Damage; 3 = Moderate Damage; 4 = Possible Damage; 5 = Impact Crater (Damage to Road); 6 = No Visible Damage; 7 = Impact Crater (Damage to Field); 8 = Destroyed (Demolition Zone); 9 = Suspected Phosphorus shell Attack Zone; 10 = Road Damage from Tank Passage; 11 = Possible Damage from adjacent impact, debris. The decoded text is in `Main_Damage_Site_Class_2_label`. |
| Damage_Status_2 | int16 | Coded value. The source geodatabase domain gives: 0 = No change; 1 = Increase - damage; 2 = Decrease - damage; 3 = New - damage. The decoded text is in `Damage_Status_2_label`. |
| SensorDate_3 | timestamp[us, tz=UTC] |  |
| SensorID_3 | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `SensorID_3_label`, which is decoded per source file. |
| ConfidenceID_3 | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_3_label`. |
| Main_Damage_Site_Class_3 | int32 | Coded value. The source geodatabase domain gives: 1 = Destroyed; 2 = Severe Damage; 3 = Moderate Damage; 4 = Possible Damage; 5 = Impact Crater (Damage to Road); 6 = No Visible Damage; 7 = Impact Crater (Damage to Field); 8 = Destroyed (Demolition Zone); 9 = Suspected Phosphorus shell Attack Zone; 10 = Road Damage from Tank Passage; 11 = Possible Damage from adjacent impact, debris. The decoded text is in `Main_Damage_Site_Class_3_label`. |
| Damage_Status_3 | int16 | Coded value. The source geodatabase domain gives: 0 = No change; 1 = Increase - damage; 2 = Decrease - damage; 3 = New - damage. The decoded text is in `Damage_Status_3_label`. |
| Grouped_Damage_Classes | int16 | Coded value. The source geodatabase domain gives: 1 = Damaged Buildings; 2 = Damaged Greenhouses; 3 = Impacts on Roads / Bridges; 4 = Impacts in Fields; 5 = Damaged Road segments. The decoded text is in `Grouped_Damage_Classes_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Notes | string | Free-text notes by the analyst. |
| Settlement_Name | string |  |
| Neighborhood | string |  |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| ConfidenceID_label | string | `ConfidenceID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| ConfidenceID_2_label | string | `ConfidenceID_2` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| ConfidenceID_3_label | string | `ConfidenceID_3` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Damage_Status_2_label | string | `Damage_Status_2` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Damage_Status_3_label | string | `Damage_Status_3` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| FieldValidation_label | string | `FieldValidation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Grouped_Damage_Classes_label | string | `Grouped_Damage_Classes` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Main_Damage_Site_Class_label | string | `Main_Damage_Site_Class` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Main_Damage_Site_Class_2_label | string | `Main_Damage_Site_Class_2` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Main_Damage_Site_Class_3_label | string | `Main_Damage_Site_Class_3` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_2_label | string | `SensorID_2` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_3_label | string | `SensorID_3` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SiteID_label | string | `SiteID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| SensorDate_4 | timestamp[us, tz=UTC] |  |
| SensorID_4 | int32 | Coded value. The source geodatabase domain gives: 1 = Worldview-1; 2 = Worldview-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = Komsat-2; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 27 = ASAR IMM; 28 = WorldView-3; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 999 = Combination of Sensors. The decoded text is in `SensorID_4_label`. |
| ConfidenceID_4 | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_4_label`. |
| Main_Damage_Site_Class_4 | int16 | Coded value. The source geodatabase domain gives: 1 = Destroyed; 2 = Severe Damage; 3 = Moderate Damage; 4 = Possible Damage; 5 = Impact Crater (Damage to Road); 6 = No Visible Damage; 7 = Impact Crater (Damage to Field); 8 = Destroyed (Demolition Zone); 9 = Suspected Phosphorus shell Attack Zone; 10 = Road Damage from Tank Passage; 11 = Possible Damage from adjacent impact, debris. The decoded text is in `Main_Damage_Site_Class_4_label`. |
| Damage_Status_4 | int16 | Coded value. The source geodatabase domain gives: 0 = No change; 1 = Increase - damage; 2 = Decrease - damage; 3 = New - damage. The decoded text is in `Damage_Status_4_label`. |
| StaffID_4 | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 22 = WP; 33 = LB; 44 = JL; 55 = VG; 66 = CJ; 77 = LD; 88 = HK; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 222 = CS; 1000 = Unknown. The decoded text is in `StaffID_4_label`. |
| ConfidenceID_4_label | string | `ConfidenceID_4` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Damage_Status_4_label | string | `Damage_Status_4` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Main_Damage_Site_Class_4_label | string | `Main_Damage_Site_Class_4` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_4_label | string | `SensorID_4` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_4_label | string | `StaffID_4` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_3 | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 22 = WP; 33 = LB; 44 = JL; 55 = VG; 66 = CJ; 77 = LD; 88 = HK; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 222 = CS; 1000 = Unknown. The decoded text is in `StaffID_3_label`. |
| StaffID_3_label | string | `StaffID_3` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorDate_5 | timestamp[us, tz=UTC] |  |
| SensorID_5 | int32 | Coded value. The source geodatabase domain gives: 1 = Worldview-1; 2 = Worldview-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = Komsat-2; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 27 = ASAR IMM; 28 = WorldView-3; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 999 = Combination of Sensors. The decoded text is in `SensorID_5_label`. |
| ConfidenceID_5 | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_5_label`. |
| Main_Damage_Site_Class_5 | int16 | Coded value. The source geodatabase domain gives: 1 = Destroyed; 2 = Severe Damage; 3 = Moderate Damage; 4 = Possible Damage; 5 = Impact Crater (Damage to Road); 6 = No Visible Damage; 7 = Impact Crater (Damage to Field); 8 = Destroyed (Demolition Zone); 9 = Suspected Phosphorus shell Attack Zone; 10 = Road Damage from Tank Passage; 11 = Possible Damage from adjacent impact, debris. The decoded text is in `Main_Damage_Site_Class_5_label`. |
| Damage_Status_5 | int16 | Coded value. The source geodatabase domain gives: 0 = No change; 1 = Increase - damage; 2 = Decrease - damage; 3 = New - damage. The decoded text is in `Damage_Status_5_label`. |
| ConfidenceID_5_label | string | `ConfidenceID_5` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Damage_Status_5_label | string | `Damage_Status_5` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Main_Damage_Site_Class_5_label | string | `Main_Damage_Site_Class_5` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_5_label | string | `SensorID_5` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20130604syr-damage-sites-cc_by_sa-epsg_4326.parquet | 4.6 MB | 12204f6c4598... |
| ./ce20130604syr-damage-sites-cc_by_sa-epsg_4326.pmtiles | 4.9 MB | 12207951a3aa... |
| ./styles/default.json | 1.0 KB | 1220742a797a... |
| ./ce20130604syr-damage-sites-cc_by_sa-epsg_4326.thumb.jpg | 6.2 KB | 122059dc6ab5... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20130604syr-damage-sites-cc_by_sa-epsg_4326.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/damage-assessement-of-hama-hama-governorate-syria](https://data.humdata.org/dataset/damage-assessement-of-hama-hama-governorate-syria)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Damage_Sites_Aleppo_SDA`, `Damage_Sites_Damascus_CDA`, `Damage_Sites_Daraa_CDA`, `Damage_Sites_Deir_ez_Zor`, `Damage_Sites_Deir_ez_Zor_CDA`, `Damage_Sites_Hama_CDA`, `Damage_Sites_Homs_CDA`, `Damage_Sites_Idlib_CDA`, `Damage_Sites_Raqqa_CDA`, `Damage_Sites_Raqqa_CDA_Ex_wroads`.

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

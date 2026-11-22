# Damage sites: Complex emergency, Syrian Arab Republic, 4 June 2013 (CE20130604SYR)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20130604syr/ce20130604syr-damage-sites-cc_by_nc_sa_3_0-epsg_4326/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Damage sites for Complex emergency, Syrian Arab Republic, 4 June 2013 (CE20130604SYR): 111,608 features merged from 21 source layers. Point layers with a damage class column (such as `Main_Damage_Site_Class`): one point per assessed structure or site. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of Damage Assessment for Ancient City of Palmyra, Syria](https://data.humdata.org/dataset/geodata-of-damage-assessment-for-ancient-city-of-palmyra-syria-april-06-2016)
- [Geodata of Damage Assessment of Aleppo, Aleppo Governorate, Syria](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-aleppo-aleppo-governorate-syria-july-21-2015)
- [Geodata of Damage Assessment of Aleppo, Aleppo Governorate, Syria](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-aleppo-aleppo-governorate-syria-november-06-2014)
- [Geodata of Damage Assessment of Ar Raqqa, Ar Raqqa Governorate, Syria](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-ar-raqqa-ar-raqqa-governorate-syria-july-21-2015)
- [Geodata of Damage Assessment of Ar Raqqa, Ar Raqqa Governorate, Syria](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-ar-raqqa-ar-raqqa-governorate-syria-november-07-2014)
- [Geodata of Damage Assessment of Daraa, Daraa Governorate, Syria](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-daraa-daraa-governorate-syria-july-21-2015)
- [Geodata of Damage Assessment of Daraa, Daraa Governorate, Syria](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-daraa-daraa-governorate-syria-november-07-2014)
- [Geodata of Damage Assessment of Deir Ez Zor, Deir Ez Zor Governorate, Syria](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-deir-ez-zor-deir-ez-zor-governorate-syria-july-21-2015)
- [Geodata of Damage Assessment of Deir Ez Zor, Deir Ez Zor Governorate, Syria](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-deir-ez-zor-deir-ez-zor-governorate-syria-november-06-2014)
- [Geodata of Damage Assessment of Hama, Hama Governorate, Syria](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-hama-hama-governorate-syria-november-06-2014)
- [Geodata of Damage Assessment of Homs, Homs Governorate, Syria](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-homs-homs-governorate-syria-november-06-2014)
- [Geodata of Damage Assessment of Idlib, Idlib Governorate, Syria](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-idlib-idlib-governorate-syria-july-21-2015)
- and 10 more; the event's [catalog page](../catalog.json) lists them all.

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [36.08352847200007, 32.59776136100004, 40.178343089000066, 36.902268579000065]

## Temporal Coverage

- **Start**: 2014-11-06T00:00:00Z
- **End**: 2016-06-09T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SiteID | string | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Staduim; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 45 = Suspected Mass Grave Site. The decoded text is in `SiteID_label`. |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | string | Coded value. The 3 source files of this collection use 3 different domains for it, so read `SensorID_label`, which is decoded per source file. |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Settlement_Name | string |  |
| Notes | string | Free-text notes by the analyst. |
| Main_Damage_Site_Class | int16 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Main_Damage_Site_Class_label`, which is decoded per source file. |
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
| Confidence | string |  |
| Main_Damag | string |  |
| SensorDa_1 | date32[day] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID_2 | string | Coded value. The 2 source files of this collection use 2 different domains for it, so read `SensorID_2_label`, which is decoded per source file. |
| Confiden_1 | string |  |
| Main_Dam_1 | string |  |
| Damage_Sta | string |  |
| SensorDa_2 | date32[day] |  |
| SensorID_3 | string | Coded value. The source geodatabase domain gives: 1 = Worldview-1; 2 = Worldview-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = Komsat-2; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 27 = ASAR IMM; 28 = WorldView-3; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 999 = Combination of Sensors. The decoded text is in `SensorID_3_label`. |
| Confiden_2 | string |  |
| Main_Dam_2 | string |  |
| Damage_S_1 | string |  |
| Grouped_Da | string |  |
| FieldValid | string |  |
| Settlement | string |  |
| Neighborho | string |  |
| SensorDate_2 | timestamp[us, tz=UTC] |  |
| ConfidenceID_2 | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_2_label`. |
| Main_Damage_Site_Class_2 | int16 | Coded value. The source geodatabase domain gives: 1 = Destroyed; 2 = Severe Damage; 3 = Moderate Damage; 4 = Possible Damage; 5 = Impact Crater (Damage to Road); 6 = No Visible Damage; 7 = Impact Crater (Damage to Field); 8 = Destroyed (Demolition Zone); 9 = Suspected Phosphorus shell Attack Zone; 10 = Road Damage from Tank Passage; 11 = Possible Damage from adjacent impact, debris. The decoded text is in `Main_Damage_Site_Class_2_label`. |
| Damage_Status_2 | int16 | Coded value. The source geodatabase domain gives: 0 = No change; 1 = Increase - damage; 2 = Decrease - damage; 3 = New - damage. The decoded text is in `Damage_Status_2_label`. |
| SensorDate_3 | timestamp[us, tz=UTC] |  |
| ConfidenceID_3 | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_3_label`. |
| Main_Damage_Site_Class_3 | int32 | Coded value. The source geodatabase domain gives: 1 = Destroyed; 2 = Severe Damage; 3 = Moderate Damage; 4 = Possible Damage; 5 = Impact Crater (Damage to Road); 6 = No Visible Damage; 7 = Impact Crater (Damage to Field); 8 = Destroyed (Demolition Zone); 9 = Suspected Phosphorus shell Attack Zone; 10 = Road Damage from Tank Passage; 11 = Possible Damage from adjacent impact, debris. The decoded text is in `Main_Damage_Site_Class_3_label`. |
| Damage_Status_3 | int16 | Coded value. The source geodatabase domain gives: 0 = No change; 1 = Increase - damage; 2 = Decrease - damage; 3 = New - damage. The decoded text is in `Damage_Status_3_label`. |
| Neighborhood | string |  |
| ConfidenceID_2_label | string | `ConfidenceID_2` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| ConfidenceID_3_label | string | `ConfidenceID_3` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Damage_Status_2_label | string | `Damage_Status_2` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Damage_Status_3_label | string | `Damage_Status_3` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Main_Damage_Site_Class_2_label | string | `Main_Damage_Site_Class_2` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Main_Damage_Site_Class_3_label | string | `Main_Damage_Site_Class_3` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_2_label | string | `SensorID_2` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_3_label | string | `SensorID_3` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Damage_Status | int16 | Coded value. The source geodatabase domain gives: 0 = No change; 1 = Increase - damage; 2 = Decrease - damage; 3 = New - damage. The decoded text is in `Damage_Status_label`. |
| Damage_Status_label | string | `Damage_Status` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20130604syr-damage-sites-cc_by_nc_sa_3_0-epsg_4326.parquet | 2.3 MB | 1220b9592373... |
| ./ce20130604syr-damage-sites-cc_by_nc_sa_3_0-epsg_4326.pmtiles | 3.0 MB | 12209c107ec6... |
| ./styles/default.json | 1.2 KB | 122075e56345... |
| ./ce20130604syr-damage-sites-cc_by_nc_sa_3_0-epsg_4326.thumb.jpg | 5.2 KB | 1220b117f519... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20130604syr-damage-sites-cc_by_nc_sa_3_0-epsg_4326.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-damage-assessment-al-quaryatayn-homs-governorate-syria-june-09-2016](https://data.humdata.org/dataset/geodata-of-damage-assessment-al-quaryatayn-homs-governorate-syria-june-09-2016)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Damage_Sites_Al_Quaryatayn_20160507`, `Damage_Sites_Palmyra_Tadmur_20160330`, `Damage_sites_Update3_Aleppo_20150426`, `Damage_sites_Update3_Daraa_20150604`, `Damage_sites_Update3_Deir_Ez_Zor_20150510`, `Damage_sites_Update3_Idlib_20150406`, `Damage_sites_Update3_Raqqa_20150529`, `Damage_sites_Update_Aleppo_20140523`, `Damage_sites_Update_Daraa_20140501`, `Damage_sites_Update_Deir_Ez_Zor_20140513`, `Damage_sites_Update_Hama_20140305`, `Damage_sites_Update_Homs_20140421`, `Damage_sites_Update_Idlib_20140502`, `Damage_sites_Update_Raqqa_20140212`, `Damage_sites_Update_all`, `Kobane_Damage_Sites`.

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

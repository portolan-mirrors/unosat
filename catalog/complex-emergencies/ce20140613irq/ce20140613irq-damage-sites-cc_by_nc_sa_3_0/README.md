# Damage sites: Complex emergency, Iraq, 13 June 2014 (CE20140613IRQ)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20140613irq/ce20140613irq-damage-sites-cc_by_nc_sa_3_0/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Damage sites for Complex emergency, Iraq, 13 June 2014 (CE20140613IRQ): 15,712 features merged from 9 source layers. Point layers with a damage class column (such as `Main_Damage_Site_Class`): one point per assessed structure or site. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of Damage Assessment for Ramadi, Al Anbar Province, Iraq](https://data.humdata.org/dataset/geodata-of-damage-assessment-for-ramadi-al-anbar-province-iraq-january-15-2016)
- [Geodata of Damage Assessment in Central Ramadi, Al Anbar Province, Iraq](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-central-ramadi-al-anbar-province-iraq-january-15-2016)
- [Geodata of Damage Assessment of Al-Sabbahiya (Hamadan) Village, Sinjar District, Nineveh Province, Iraq](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-al-sabbahiya-hamadan-village-sinjar-district-december-12-2015)
- [Geodata of Damage Assessment of Baiji, Salah ad Din Governorate, Iraq](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-baiji-salah-ad-din-governorate-iraq-february-20-2015)
- [Geodata of Damage Assessment of Fallujah, Al Anbar Province, Iraq](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-fallujah-al-anbar-province-iraq-january-22-2015)
- [Geodata of Damage Assessment of Gundy Hamy Village, Sinjar District, Nineveh Province, Iraq](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-gundy-hamy-village-sinjar-district-nineveh-pr-december-11-2015)
- [Geodata of Damage Assessment of Jalawla, Diyala Governorate, Iraq](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-jalawla-diyala-governorate-iraq-february-06-2015)
- [Geodata of Damage Assessment of Kany Sark Village, Sinjar District, Nineveh Province, Iraq](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-kany-sark-village-sinjar-district-nineveh-pro-december-12-2015)
- [Geodata of Damage Assessment of Ramadi, Al Anbar Province, Iraq](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-ramadi-al-anbar-province-iraq-january-22-2015)
- [Geodata of Damage Assessment of Ramboosi Sharqi Village, Sinjar District, Nineveh Province, Iraq](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-ramboosi-sharqi-village-sinjar-district-ninev-december-12-2015)
- [Geodata of Damage Assessment of Shkaftat Gharby Village, Sinjar District, Nineveh Province, Iraq](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-shkaftat-gharby-village-sinjar-district-ninev-december-11-2015)
- [Geodata of Damage Assessment of Shkaftat Sharqy Village, Sinjar District, Nineveh Province, Iraq](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-shkaftat-sharqy-village-sinjar-district-ninev-december-11-2015)
- and 7 more; the event's [catalog page](../catalog.json) lists them all.

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [41.77031190800005, 33.302121094000086, 45.18480025300005, 36.673786877000055]

## Temporal Coverage

- **Start**: 2015-01-22T00:00:00Z
- **End**: 2016-07-11T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SiteID | int16 | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Staduim; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 45 = Suspected Mass Grave Site. The decoded text is in `SiteID_label`. |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `SensorID_label`, which is decoded per source file. |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Settlement_Name | string |  |
| Notes | string | Free-text notes by the analyst. |
| Main_Damage_Site_Class | int16 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Main_Damage_Site_Class_label`, which is decoded per source file. |
| Grouped_Damage_Classes | int16 | Coded value. The source geodatabase domain gives: 1 = Damaged Buildings; 2 = Damaged Greenhouses; 3 = Impacts on Roads / Bridges; 4 = Impacts in Fields; 5 = Damaged Road segments. The decoded text is in `Grouped_Damage_Classes_label`. |
| StaffID | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 22 = WP; 33 = LB; 44 = JL; 55 = VG; 66 = CJ; 77 = LD; 88 = HK; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 222 = CS; 1000 = Unknown. The decoded text is in `StaffID_label`. |
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
| ./ce20140613irq-damage-sites-cc_by_nc_sa_3_0.parquet | 660.1 KB | 1220f7386c94... |
| ./ce20140613irq-damage-sites-cc_by_nc_sa_3_0.pmtiles | 736.9 KB | 12205be138c7... |
| ./styles/default.json | 1.3 KB | 1220c7ce1005... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20140613irq-damage-sites-cc_by_nc_sa_3_0.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-damage-assessment-for-ramadi-al-anbar-province-iraq-january-15-2016](https://data.humdata.org/dataset/geodata-of-damage-assessment-for-ramadi-al-anbar-province-iraq-january-15-2016)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Baiji_Damage_Sites`, `Fallujah_Damage_Sites`, `Fallujah_Damage_Sites_June2016`, `Jalawla_Damage_Sites`, `Ramadi_Damage_Sites`, `Ramadi_Damage_Sites_20160129`, `Sinjar_Damage_Sites`, `Tikrit_Damage_Sites`, `Zumar_Damage_Sites`.

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

# Damage sites: Earthquake, Syrian Arab Republic, Türkiye, 6 February 2023 (EQ20230206SYR)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/earthquakes/2023/eq20230206syr/eq20230206syr-damage-sites/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Damage sites for Earthquake, Syrian Arab Republic, Türkiye, 6 February 2023 (EQ20230206SYR): 34,633 features merged from 358 source layers. Point layers with a damage class column (such as `Main_Damage_Site_Class`): one point per assessed structure or site. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [6 February 2023 M 7.8 Marash/Antep (Kehramanmarash) Earthquake, Preliminary Satellite-Based Comprehensive Damage Assessment Report](https://data.humdata.org/dataset/6-february-2023-m-7-8-marash-antep-kehramanmarash-earthquake-preliminary-satellite-based-c)
- [Damage Assessment  in Jableh City, Jableh District, Latakia Province, Syria as of 9 February 2023](https://data.humdata.org/dataset/damage-assessment-in-jableh-city-jableh-district-latakia-province-syria-as-of-9-february-2)
- [Damage Assessment Istamo (Latakia) as of 9 February 2023](https://data.humdata.org/dataset/damage-assessment-istamo-latakia-as-of-9-february-2023)
- [Damage Assessment in A'zaz City, Aleppo Governorate, Syria as of 9 February 2023](https://data.humdata.org/dataset/damage-assessment-in-a-zaz-city-aleppo-governorate-syria-as-of-9-february-2023)
- [Damage Assessment in Al Bab, Qabasin and Bza'a towns, Syria as of 11 February 2023](https://data.humdata.org/dataset/damage-assessment-in-al-bab-qabasin-and-bza-a-towns-syria-as-of-11-february-2023)
- [Damage Assessment in Al Bab, Syria as of 11 February 2023](https://data.humdata.org/dataset/damage-assessment-in-al-bab-syria-as-of-11-february-2023)
- [Damage Assessment in Idlib City, Syria as of 9 February 2023](https://data.humdata.org/dataset/damage-assessment-in-idlib-city-syria-as-of-9-february-2023)
- [Damage Assessment in Jindires and the surrounding area, Syria as of 10 February 2023](https://data.humdata.org/dataset/damage-assessment-in-jindires-and-the-surrounding-area-syria-as-of-10-february-2023)
- [Damage Assessment in Jindires, Afrin District, Aleppo Governorate, Syria as of 11 February 2023](https://data.humdata.org/dataset/damage-assessment-in-jindires-afrin-district-aleppo-governorate-syria-as-of-11-february-20)
- [Damage Assessment in Jisr al-Shughur City (Idleb) as of 9 February 2023](https://data.humdata.org/dataset/damage-assessment-in-jisr-al-shughur-city-idleb-as-of-9-february-2023)
- [Damage Assessment in Killi (Idlib District), Syria as of 16 February 2023](https://data.humdata.org/dataset/damage-assessment-in-killi-idlib-district-syria-as-of-16-february-2023)
- [Damage Assessment in Lilawa Village, Jarablus District, Aleppo Governorate, Syria as of 7 February 2023](https://data.humdata.org/dataset/damage-assessment-in-lilawa-village-jarablus-district-aleppo-governorate-syria-as-of-7-feb)
- and 5 more; the event's [catalog page](../catalog.json) lists them all.

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![earthquake](https://img.shields.io/badge/earthquake-blue) ![earthquake-tsunami](https://img.shields.io/badge/earthquake--tsunami-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [35.743395502000055, 35.32816693400008, 37.747518134000074, 36.70797662500007]

## Temporal Coverage

- **Start**: 2023-02-08T00:00:00Z
- **End**: 2023-03-16T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SiteID | int16 | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Staduim; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 42 = Military Facility; 45 = Suspected Mass Grave Site; 46 = Airport Facility; 47 = Church. The decoded text is in `SiteID_label`. |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `SensorID_label`, which is decoded per source file. |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Settlement_Name | string |  |
| Notes | string | Free-text notes by the analyst. |
| Main_Damage_Site_Class | int16 | Coded value. The source geodatabase domain gives: 1 = Destroyed; 2 = Severe Damage; 3 = Moderate Damage; 4 = Possible Damage; 5 = Impact Crater (Damage to Road); 6 = No Visible Damage; 7 = Impact Crater (Damage to Field); 8 = Destroyed (Demolition Zone); 9 = Suspected Phosphorus shell Attack Zone; 10 = Road Damage from Tank Passage; 11 = Possible Damage from adjacent impact, debris; 12 = Lava Flow; 13 = Damage. The decoded text is in `Main_Damage_Site_Class_label`. |
| Grouped_Damage_Classes | int16 | Coded value. The source geodatabase domain gives: 1 = Damaged Buildings; 2 = Damaged Greenhouses; 3 = Impacts on Roads / Bridges; 4 = Impacts in Fields; 5 = Damaged Road segments. The decoded text is in `Grouped_Damage_Classes_label`. |
| StaffID | int32 | Coded value. The 3 source files of this collection use 3 different domains for it, so read `StaffID_label`, which is decoded per source file. |
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
| ./eq20230206syr-damage-sites.parquet | 141.5 KB | 12201d8c8af4... |
| ./eq20230206syr-damage-sites.pmtiles | 527.7 KB | 1220223dd52c... |
| ./styles/default.json | 997 B | 1220954083f0... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./eq20230206syr-damage-sites.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/6-february-2023-m-7-8-marash-antep-kehramanmarash-earthquake-preliminary-satellite-based-c](https://data.humdata.org/dataset/6-february-2023-m-7-8-marash-antep-kehramanmarash-earthquake-preliminary-satellite-based-c)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `GF2_20230209_DamageStructure_Sarmada`, `PHR_20230207_DamageStructure_Salqin`, `PHR_20230209_DamageStructure_Azaz`, `PHR_20230209_DamageStructure_EinElsoda`, `PHR_20230209_DamageStructure_Idlip`, `PHR_20230209_DamageStructure_Istamo`, `PHR_20230209_DamageStructure_Jableh`, `PHR_20230209_DamageStructure_Jableh_North`, `PHR_20230209_DamageStructure_JisrChoughour`, `PHR_20230209_DamageStructure_Latakia`, `PHR_20230210_DamageStructure_Jindires`, `PHR_20230211_DamageStructure_Albab`, `PHR_20230215_DamageStructure_AlAtaarib`, `PHR_20230216_DamageStructure_Killi`, `WV02_20230217_DamageStructure_Rajo`, `WV2_20230217_DamageStructure_AdDana`, `WV3_20230207_DamageStructure_Lilawa_Jarablus_Aleppo`, `WV3_20230207_DamageStructure_Zayzafun_Azaz_Aleppo`, `WV3_20230211_DamageStructure_Yazibaxe`, `WV3_20230212_DamageStructure_Afrin`, `WV3_20230212_DamageStructure_SgoeNiyarah`, `WV3_20230324_DamageStructure_EinElkoroum`.

## Attribution

UNITAR-UNOSAT

## License

[other](https://opendefinition.org/licenses/cc-by-sa/)

## Contact

Portolan Mirrors <nissim@radiant.earth>

## Known Issues

HDX states the license as "Creative Commons Attribution Share-Alike (CC BY-SA)" with no version, so the collection's license is `other`, linked to the license definition HDX gives. This is a preliminary assessment and has not yet been validated in the field. It is important to consider the characteristics of the source imagery used in the analyses when interpreting results. For damage assessments it should be noted that only significant damage to the structural integrity of the buildings analyzed can be seen in imagery, while minor damage such as cracks or holes may not be visible at all. For flood extractions using radar data it is important to note that urban areas and highly vegetated areas may mask the flood signature and result in underestimation of flood waters. Users with specific questions or concerns should contact unosat@unitar.org to seek clarification. This is a preliminary assessment and has not yet been validated in the field. It is important to consider the characteristics of the source imagery used in the analyses when interpreting results. For damage assessments it should be noted that only significant damage to the structural integrity of the buildings analyzed can be seen in imagery, while minor damage such as cracks or holes may not be visible at all. For flood extractions using radar data it is important to note that urban areas and highly vegetated areas may mask the flood signature and result in underestimation of flood waters. Users with specific questions or concerns should contact unosat@unitar.org to seek clarification.
Glide: EQ-2023-000015-TUR

---

*Generated by [Portolan](https://github.com/portolan-sdi/portolan-cli) from STAC metadata and .portolan/metadata.yaml*

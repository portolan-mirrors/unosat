# Damage sites: Flood, Libya, 12 September 2023 (FL20230912LBY)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2023/fl20230912lby/fl20230912lby-damage-sites/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Damage sites for Flood, Libya, 12 September 2023 (FL20230912LBY): 49,907 features merged from 55 source layers. Point layers with a damage class column (such as `Main_Damage_Site_Class`): one point per assessed structure or site. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [10 September 2023 Mediterranean Sea Storm Daniel in Libya, Preliminary Satellite-Based Comprehensive Damage Assessment Report](https://data.humdata.org/dataset/10-september-2023-mediterranean-sea-storm-daniel-in-libya-preliminary-satellite-based-comp)
- [Flood impact assessment in Al Tamimi Town, Derna Governorate, East Province, Libya](https://data.humdata.org/dataset/flood-impact-assessment-in-al-tamimi-town-derna-governorate-east-province-libya)
- [Flood impact assessment in Dams over Benghazi and Almarj Governorates, East Province, Libya](https://data.humdata.org/dataset/flood-impact-assessment-in-dams-over-benghazi-and-almarj-governorates-east-province-libya)
- [Flood impact assessment in Derna City centre, East Province, Libya](https://data.humdata.org/dataset/flood-impact-assessment-in-derna-city-centre-east-province-libya)
- [Flood impact assessment in Derna City, East Province, Libya](https://data.humdata.org/dataset/flood-impact-assessment-in-derna-city-east-province-libya)
- [Flood impact assessment in Derna dams, East Province, Libya](https://data.humdata.org/dataset/flood-impact-assessment-in-derna-dams-east-province-libya)
- [Night-Time Light Loss Assessment in Derna & Al Bayda (Libya) using Night-time Light Imagery](https://data.humdata.org/dataset/night-time-light-loss-assessment-in-derna-al-bayda-libya-using-night-time-light-imagery)
- [Power Supply Assessment in Benghazi (Libya) using Night-time Light Imagery](https://data.humdata.org/dataset/power-supply-assessment-in-benghazi-libya-using-night-time-light-imagery)
- [Power Supply Assessment in Derna & Al Bayda (Libya) using Night-time Light Imagery](https://data.humdata.org/dataset/power-supply-assessment-in-derna-al-bayda-libya-using-night-time-light-imagery)
- [Preliminary satellite-derived reservoir assessment, Benghazi, Almarj & Derna governorates, East province, Libya - 19 September 2023](https://data.humdata.org/dataset/preliminary-satellite-derived-reservoir-assessment-benghazi-almarj-derna-governorates-east)
- [Storm Daniel in Libya, September 2023 - UNOSAT Live Web Map](https://data.humdata.org/dataset/storm-daniel-in-libya-september-2023-unosat-live-web-map)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue) ![libya-floods](https://img.shields.io/badge/libya--floods-blue)

## Spatial Coverage

- **Bounding Box**: [20.557677505000072, 32.32312748700008, 23.100592133000077, 32.77373683600007]

## Temporal Coverage

- **Start**: 2023-09-12T00:00:00Z
- **End**: 2023-10-11T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SiteID | int16 | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Stadium; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 42 = Military Facility; 45 = Suspected Mass Grave Site; 46 = Airport Facility; 47 = Church; 48 = Dam; 49 = Port. The decoded text is in `SiteID_label`. |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `SensorID_label`, which is decoded per source file. |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Settlement_Name | string |  |
| Notes | string | Free-text notes by the analyst. |
| Main_Damage_Site_Class | int16 | Coded value. The source geodatabase domain gives: 1 = Destroyed; 2 = Severe Damage; 3 = Moderate Damage; 4 = Possible Damage; 5 = Impact Crater (Damage to Road); 6 = No Visible Damage; 7 = Impact Crater (Damage to Field); 8 = Destroyed (Demolition Zone); 9 = Suspected Phosphorus shell Attack Zone; 10 = Road Damage from Tank Passage; 11 = Possible Damage from adjacent impact, debris; 12 = Lava Flow; 13 = Damage. The decoded text is in `Main_Damage_Site_Class_label`. |
| Grouped_Damage_Classes | int16 | Coded value. The source geodatabase domain gives: 1 = Damaged Buildings; 2 = Damaged Greenhouses; 3 = Impacts on Roads / Bridges; 4 = Impacts in Fields; 5 = Damaged Road segments; 6 = Damaged Port. The decoded text is in `Grouped_Damage_Classes_label`. |
| StaffID | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 18 = TH; 22 = WP; 33 = LB; 44 = JL; 45 = MD; 54 = HP; 55 = VG; 57 = PG; 66 = CJ; 70 = SG; 73 = RS; 77 = LD; 88 = HK; 91 = KA; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 141 = KJP; 151 = MNY; 161 = DC; 171 = SR; 181 = NL; 191 = DH; 212 = MH; 213 = JT; 214 = ES; 215 = KB; 216 = JY; 218 = PA; 219 = SS; 220 = YM; 221 = IS; 222 = LD; 1000 = Unknown. The decoded text is in `StaffID_label`. |
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
| ./fl20230912lby-damage-sites.parquet | 188.4 KB | 12208e6b3ddc... |
| ./fl20230912lby-damage-sites.pmtiles | 214.1 KB | 12205706e1f3... |
| ./styles/default.json | 1.0 KB | 12206dea49d4... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20230912lby-damage-sites.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/10-september-2023-mediterranean-sea-storm-daniel-in-libya-preliminary-satellite-based-comp](https://data.humdata.org/dataset/10-september-2023-mediterranean-sea-storm-daniel-in-libya-preliminary-satellite-based-comp)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `PHR_20230913_AffectedStructure_Derna`, `PHR_20230913_DamagedStructure_Al_Tamimi`, `PT_20230917_DamageSites_Tocra`, `S2_20230912_AffectedInfrastructure_Derna`, `S2_20230912_AffectedStructure_Derna`.

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

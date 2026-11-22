# Damage sites: Flood, Myanmar, 3 July 2015 (FL20150703MMR)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2015/fl20150703mmr/fl20150703mmr-damage-sites/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Damage sites for Flood, Myanmar, 3 July 2015 (FL20150703MMR): 189 features merged from 1 source layer. Point layers with a damage class column (such as `Main_Damage_Site_Class`): one point per assessed structure or site. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of Damage Assessment over Tuikhingzang, Tonzang Township, Chin Division, Myanmar](https://data.humdata.org/dataset/geodata-of-damage-assessment-over-tuikhingzang-tonzang-township-chin-division-september-17-2015)
- [Geodata of Flood Waters Near City of Yangon, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-near-city-of-yangon-myanmar-august-10-2015)
- [Geodata of Flood Waters Over Ann and Myebon area, Rakhine State, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-ann-and-myebon-area-rakhine-state-myanmar-august-17-2015)
- [Geodata of Flood Waters Over Ann area, Rakhine State, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-ann-area-rakhine-state-myanmar-august-14-2015)
- [Geodata of Flood Waters Over Central Magway State, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-central-magway-state-myanmar-august-07-2015)
- [Geodata of Flood Waters Over Central Sagaing Region, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-central-sagaing-region-myanmar-august-13-2015)
- [Geodata of Flood Waters Over Central Sagaing State, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-central-sagaing-state-myanmar-july-24-2015)
- [Geodata of Flood Waters Over Kayin and Mon State, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-kayin-and-mon-state-myanmar-august-14-2015)
- [Geodata of Flood Waters Over Kyautaw area, Rakhine State, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-kyautaw-area-rakhine-state-myanmar-august-19-2015)
- [Geodata of Flood Waters Over Northern Rakhine State, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-northern-rakhine-state-myanmar-august-11-2015)
- [Geodata of Flood Waters Over Northwest Rakhine State, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-northwest-rakhine-state-myanmar-july-13-2015)
- [Geodata of Flood Waters Over South Bago Division, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-south-bago-division-myanmar-august-13-2015)
- and 7 more; the event's [catalog page](../catalog.json) lists them all.

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [94.00745676400004, 23.496399920000044, 94.06775440700005, 23.55691883600008]

## Temporal Coverage

- **Start**: 2015-07-13T00:00:00Z
- **End**: 2015-10-21T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SiteID | int16 | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Staduim; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 45 = Suspected Mass Grave Site. The decoded text is in `SiteID_label`. |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT 6; 42 = Sentinel-1; 43 = Komsat-2; 999 = Combination of Sensors. The decoded text is in `SensorID_label`. |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Settlement_Name | string |  |
| Notes | string | Free-text notes by the analyst. |
| Main_Damage_Site_Class | int16 | Coded value. The source geodatabase domain gives: 1 = Destroyed; 2 = Severe Damage; 3 = Moderate Damage; 4 = Possible Damage; 5 = Impact Crater (Damage to Road); 6 = No Visible Damage; 7 = Impact Crater (Damage to Field); 8 = Destroyed (Demolition Zone); 9 = Suspected Phosphorus shell Attack Zone; 10 = Road Damage from Tank Passage; 11 = Possible Damage from adjacent impact, debris; 12 = Lava Flow. The decoded text is in `Main_Damage_Site_Class_label`. |
| Grouped_Damage_Classes | int16 | Coded value. The source geodatabase domain gives: 1 = Damaged Buildings; 2 = Damaged Greenhouses; 3 = Impacts on Roads / Bridges; 4 = Impacts in Fields; 5 = Damaged Road segments. The decoded text is in `Grouped_Damage_Classes_label`. |
| StaffID | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 22 = WP; 33 = LB; 44 = JL; 55 = VG; 66 = CJ; 73 = RS; 77 = LD; 88 = HK; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 222 = CS; 1000 = Unknown. The decoded text is in `StaffID_label`. |
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
| ./fl20150703mmr-damage-sites.parquet | 15.1 KB | 1220052b1799... |
| ./fl20150703mmr-damage-sites.pmtiles | 51.1 KB | 1220af70da4c... |
| ./styles/default.json | 998 B | 122036a7a5b7... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20150703mmr-damage-sites.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-damage-assessment-over-tuikhingzang-tonzang-township-chin-division-september-17-2015](https://data.humdata.org/dataset/geodata-of-damage-assessment-over-tuikhingzang-tonzang-township-chin-division-september-17-2015)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `PL20150916_DamageSites`.

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

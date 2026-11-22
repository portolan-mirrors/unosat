# Damage sites: Volcano, Democratic Republic of the Congo, 23 May 2021 (VO20210523COD)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/volcanoes/vo20210523cod/vo20210523cod-damage-sites/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Damage sites for Volcano, Democratic Republic of the Congo, 23 May 2021 (VO20210523COD): 3 features merged from 1 source layer. Point layers with a damage class column (such as `Main_Damage_Site_Class`): one point per assessed structure or site. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Coulée de lave et structures affectées suite à l'éruption volcanique du Nyiragongo, Province du Nord-Kivu, RD Congo](https://data.humdata.org/dataset/coulee-de-lave-et-structures-affectees-suite-a-l-eruption-volcanique-du-nyiragongo-provinc)
- [Lava flow and affected structures caused by  the volcanic eruption of the 22 May 2021 in Kanyanza village, DR Congo](https://data.humdata.org/dataset/lava-flow-and-affected-structures-caused-by-the-volcanic-eruption-of-the-22-may-2021-in-ka)
- [Lava flow and affected structures caused by Nyiragongo volcanic eruption, Nord-Kivu Province, DR Congo](https://data.humdata.org/dataset/lava-flow-and-affected-structures-caused-by-nyiragongo-volcanic-eruption-nord-kivu-provinc)
- [Lava flow and affected structures caused by the volcanic eruption of the 22 May 2021 in north of Goma airport, DR Congo](https://data.humdata.org/dataset/lava-flow-and-affected-structures-caused-by-the-volcanic-eruption-of-the-22-may-2021-in-no)
- [Lava flow and geological information in NordKivu Province, DR Congo and Western Province, Rwanda as of 01 June 2021](https://data.humdata.org/dataset/lava-flow-and-geological-information-in-nordkivu-province-dr-congo-and-western-province-rw)
- [Lava flow and geological information related to the volcanic eruption in DR Congo and Rwanda as of 27 May 2021](https://data.humdata.org/dataset/lava-flow-and-geological-information-related-to-the-volcanic-eruption-in-dr-congo-and-rwan)
- [Lava flow extent and affected structures caused by the 22 May 2021 Nyiragongo volcanic eruption in Goma, DR Congo](https://data.humdata.org/dataset/lava-flow-extent-and-affected-structures-caused-by-the-22-may-2021-nyiragongo-volcanic-eru)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![geodata](https://img.shields.io/badge/geodata-blue) ![natural disasters](https://img.shields.io/badge/natural_disasters-blue) ![volcano](https://img.shields.io/badge/volcano-blue)

## Spatial Coverage

- **Bounding Box**: [29.25428000000005, -1.5822099999999182, 29.259340000000066, -1.5496799999999098]

## Temporal Coverage

- **Start**: 2021-05-25T00:00:00Z
- **End**: 2021-06-03T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SiteID | int16 | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Staduim; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 42 = Military Facility; 45 = Suspected Mass Grave Site; 46 = Airport Facility; 47 = Church. The decoded text is in `SiteID_label`. |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 |  |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Settlement_Name | string |  |
| Notes | string | Free-text notes by the analyst. |
| Main_Damage_Site_Class | int16 | Coded value. The source geodatabase domain gives: 1 = Destroyed; 2 = Severe Damage; 3 = Moderate Damage; 4 = Possible Damage; 5 = Impact Crater (Damage to Road); 6 = No Visible Damage; 7 = Impact Crater (Damage to Field); 8 = Destroyed (Demolition Zone); 9 = Suspected Phosphorus shell Attack Zone; 10 = Road Damage from Tank Passage; 11 = Possible Damage from adjacent impact, debris; 12 = Lava Flow. The decoded text is in `Main_Damage_Site_Class_label`. |
| Grouped_Damage_Classes | int16 | Coded value. The source geodatabase domain gives: 1 = Damaged Buildings; 2 = Damaged Greenhouses; 3 = Impacts on Roads / Bridges; 4 = Impacts in Fields; 5 = Damaged Road segments. The decoded text is in `Grouped_Damage_Classes_label`. |
| StaffID | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 18 = TH; 22 = WP; 33 = LB; 44 = JL; 45 = MD; 54 = HP; 55 = VG; 57 = PG; 66 = CJ; 70 = SG; 73 = RS; 77 = LD; 88 = HK; 91 = KA; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 141 = KJP; 151 = MNY; 161 = DC; 171 = SR; 181 = NL; 191 = DH; 212 = MH; 213 = JT; 214 = ES; 215 = KB; 216 = JY; 218 = PA; 219 = SS; 222 = CS; 1000 = Unknown. The decoded text is in `StaffID_label`. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| ImageID_Num | int32 |  |
| ConfidenceID_label | string | `ConfidenceID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| FieldValidation_label | string | `FieldValidation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Grouped_Damage_Classes_label | string | `Grouped_Damage_Classes` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Main_Damage_Site_Class_label | string | `Main_Damage_Site_Class` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SiteID_label | string | `SiteID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./vo20210523cod-damage-sites.parquet | 5.0 KB | 1220dcd8b3dc... |
| ./vo20210523cod-damage-sites.pmtiles | 21.0 KB | 1220b171bb4e... |
| ./styles/default.json | 695 B | 12205f53b9c8... |
| ./vo20210523cod-damage-sites.thumb.jpg | 2.4 KB | 12200fd192f0... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./vo20210523cod-damage-sites.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/coulee-de-lave-et-structures-affectees-suite-a-l-eruption-volcanique-du-nyiragongo-provinc](https://data.humdata.org/dataset/coulee-de-lave-et-structures-affectees-suite-a-l-eruption-volcanique-du-nyiragongo-provinc)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `USGS_VentLocation`.

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

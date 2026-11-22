# Damage sites: Complex emergency, State of Palestine, 15 July 2014 (CE20140715PSE)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20140715pse/ce20140715pse-damage-sites/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Damage sites for Complex emergency, State of Palestine, 15 July 2014 (CE20140715PSE): 71,230 features merged from 6 source layers. Point layers with a damage class column (such as `Main_Damage_Site_Class`): one point per assessed structure or site. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of 2009-2014 Density Comparison of Destroyed and Severely Damaged Structures in Gaza Strip, Occupied Palestinian Territory](https://data.humdata.org/dataset/geodata-of-2009-2014-density-comparison-of-destroyed-and-severely-damaged-str-september-19-2014)
- [Geodata of Damage Assessment In Central Gaza Strip - Occupied Palestinian Territory - 12 July 2014](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-central-gaza-strip-occupied-palestinian-terri-july-21-2014)
- [Geodata of Damage Assessment in Atatra, Gaza Strip - Occupied Palestinian Territory](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-atatra-gaza-strip-occupied-palestinian-territ-august-04-2014)
- [Geodata of Damage Assessment in Beit Hanun, Gaza Strip - Occupied Palestinian Territory](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-beit-hanun-gaza-strip-occupied-palestinian-te-july-28-2014)
- [Geodata of Damage Assessment in Beit Lahia, Gaza Strip - Occupied Palestinian Territory](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-beit-lahia-gaza-strip-occupied-palestinian-te-july-30-2014)
- [Geodata of Damage Assessment in Gaza City, Gaza Strip - Occupied Palestinian Territory](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-gaza-city-gaza-strip-occupied-palestinian-ter-july-31-2014)
- [Geodata of Damage Assessment in Gaza Strip, Occupied Palestinian Territory](https://data.humdata.org/dataset/geodata-of-health-facilities-damage-assessment-in-gaza-strip-occupied-palesti-september-26-2014)
- [Geodata of Damage Assessment in Jarara Area, Gaza Strip - Occupied Palestinian Territory](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-jarara-area-gaza-strip-occupied-palestinian-t-august-07-2014)
- [Geodata of Damage Assessment in Khuza'a and Al Qararra, Gaza Strip, Occupied Palestinian Territory](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-khuzaa-and-al-qararra-gaza-strip-occupied-pal-august-08-2014)
- [Geodata of Damage Assessment in Northeastern Gaza Strip - Occupied Palestinian Territory](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-northeastern-gaza-strip-occupied-palestinian-july-27-2014)
- [Geodata of Damage Assessment in Rafah, Gaza Strip - Occupied Palestinian Territory](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-rafah-gaza-strip-occupied-palestinian-territo-august-07-2014)
- [Geodata of Damage to Agricultural Areas and Greenhouses, Gaza Strip - Occupied Palestinian Territory](https://data.humdata.org/dataset/geodata-of-damage-to-agricultural-areas-and-greenhouses-gaza-strip-occupied-p-september-23-2014)
- and 5 more; the event's [catalog page](../catalog.json) lists them all.

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![damage assessment](https://img.shields.io/badge/damage_assessment-blue) ![education](https://img.shields.io/badge/education-blue) ![education facilities-schools](https://img.shields.io/badge/education_facilities--schools-blue) ![geodata](https://img.shields.io/badge/geodata-blue) ![health](https://img.shields.io/badge/health-blue) ![health facilities](https://img.shields.io/badge/health_facilities-blue)

## Spatial Coverage

- **Bounding Box**: [34.22027435600006, 31.23267754400007, 34.55516213100009, 31.58725198400009]

## Temporal Coverage

- **Start**: 2014-07-21T00:00:00Z
- **End**: 2014-10-02T23:59:59Z

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
| Main_Damage_Site_Class | int16 | Coded value. The source geodatabase domain gives: 1 = Destroyed; 2 = Severe Damage; 3 = Moderate Damage; 4 = Possible Damage; 5 = Impact Crater (Damage to Road); 6 = No Visible Damage; 7 = Impact Crater (Damage to Field); 8 = Destroyed (Demolition Zone); 9 = Suspected Phosphorus shell Attack Zone; 10 = Road Damage from Tank Passage; 11 = Possible Damage from adjacent impact, debris. The decoded text is in `Main_Damage_Site_Class_label`. |
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
| Name | string |  |
| Source | string |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20140715pse-damage-sites.parquet | 1003.6 KB | 12207c3f3c82... |
| ./ce20140715pse-damage-sites.pmtiles | 1.4 MB | 12201c18487c... |
| ./styles/default.json | 1.3 KB | 122033fb9c0d... |
| ./ce20140715pse-damage-sites.thumb.jpg | 30.7 KB | 1220354e7cae... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20140715pse-damage-sites.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-2009-2014-density-comparison-of-destroyed-and-severely-damaged-str-september-19-2014](https://data.humdata.org/dataset/geodata-of-2009-2014-density-comparison-of-destroyed-and-severely-damaged-str-september-19-2014)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Damage_Analysis_Schools`, `Gaza_Strip_Damage_Sites_Final_Update1`, `Gaza_Strip_Damage_Sites_Final_Update3`.

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

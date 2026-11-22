# Damage areas: Complex emergency, Central African Republic, 12 December 2013 (CE20131212CAF)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20131212caf/ce20131212caf-damage-areas/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Damage areas for Complex emergency, Central African Republic, 12 December 2013 (CE20131212CAF): 32 features merged from 6 source layers. Polygon layers with a damage class column: damaged areas, zones, or density cells. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of Damage Assesment in Bangui, Central African Republic](https://data.humdata.org/dataset/geodata-of-damage-assesment-in-bangui-central-african-republic-july-02-2014)
- [Geodata of Damage Assesment in Bangui, Central African Republic](https://data.humdata.org/dataset/geodata-of-damage-assesment-in-bangui-central-african-republic-march-07-2014)
- [Geodata of Damage Assesment in Bouar, Nana Membere Province, Central African republic](https://data.humdata.org/dataset/geodata-of-damage-assesment-in-bouar-nana-membere-province-central-african-re-march-14-2014)
- [Geodata of Damage Assessment in Marcounda Sub-Prefecture, Central African Republic](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-marcounda-sub-prefecture-central-african-repu-july-08-2014)
- [Geodata of Damage Assessment in Paoua, OuhamPende, Central African Republic](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-paoua-ouhampende-central-african-republic-june-23-2014)
- [Geodata of Destruction in Bossangoa Area, Ouham, Central African Republic](https://data.humdata.org/dataset/geodata-of-destruction-in-bossangoa-area-ouham-central-african-republic-march-14-2014)
- [Geodata of IDP Settlement, M Poko Airport, Bangui, Central African Republic](https://data.humdata.org/dataset/geodata-of-idp-settlement-m-poko-airport-bangui-central-african-republic-january-24-2014)
- [Geodata of IDP Settlement, M'Poko Airport, Bangui, Central African Republic](https://data.humdata.org/dataset/geodata-of-idp-settlement-mpoko-airport-bangui-central-african-republic-june-26-2014)
- [Geodata of IDP Settlement, M'Poko Airport, Bangui, Central African Republic](https://data.humdata.org/dataset/geodata-of-idp-settlement-mpoko-airport-bangui-central-african-republic-october-21-2015)
- [Geodata of Sido Refugee Camp, Moyen - Chari Region, Republic of Chad](https://data.humdata.org/dataset/geodata-of-sido-refugee-camp-moyen-chari-region-republic-of-chad-june-03-2014)
- [Geodata of Sido Refugee Camp, Moyen - Chari Region, Republic of Chad](https://data.humdata.org/dataset/geodata-of-sido-refugee-camp-moyen-chari-region-republic-of-chad-june-19-2014)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [16.416914449000046, 4.3233940710000525, 18.644155841000043, 7.275715466000065]

## Temporal Coverage

- **Start**: 2014-01-24T00:00:00Z
- **End**: 2015-10-21T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SiteID | int16 | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Staduim; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 45 = Suspected Mass Grave Site. The decoded text is in `SiteID_label`. |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The source geodatabase domain gives: 1 = Worldview-1; 2 = Worldview-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = Komsat-2; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 999 = Combination of Sensors. The decoded text is in `SensorID_label`. |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Settlement_Name | string |  |
| Notes | string | Free-text notes by the analyst. |
| Main_Damage_Site_Class | int16 | Coded value. The source geodatabase domain gives: 1 = Destroyed; 2 = Severe Damage; 3 = Moderate Damage; 4 = Possible Damage; 5 = Impact Crater (Damage to Road); 6 = No Visible Damage; 7 = Impact Crater (Damage to Field); 8 = Destroyed (Demolition Zone); 9 = Suspected Phosphorus shell Attack Zone; 10 = Road Damage from Tank Passage; 11 = Possible Damage from adjacent impact, debris. The decoded text is in `Main_Damage_Site_Class_label`. |
| Grouped_Damage_Classes | int16 | Coded value. The source geodatabase domain gives: 1 = Damaged Buildings; 2 = Damaged Greenhouses; 3 = Impacts on Roads / Bridges; 4 = Impacts in Fields; 5 = Damaged Road segments. The decoded text is in `Grouped_Damage_Classes_label`. |
| StaffID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| ImageID_Num | int32 |  |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| Area_m2 | float | Area in square metres, as UNOSAT computed it. |
| Area_ha | float | Area in hectares, as UNOSAT computed it. |
| Shape_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Shape_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Name | string |  |
| AbbName | string |  |
| ConfidenceID_label | string | `ConfidenceID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| FieldValidation_label | string | `FieldValidation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Grouped_Damage_Classes_label | string | `Grouped_Damage_Classes` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Main_Damage_Site_Class_label | string | `Main_Damage_Site_Class` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SiteID_label | string | `SiteID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20131212caf-damage-areas.parquet | 16.0 KB | 1220b0c2d5f9... |
| ./ce20131212caf-damage-areas.pmtiles | 115.2 KB | 122037b24f56... |
| ./styles/default.json | 907 B | 12208be9150a... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20131212caf-damage-areas.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-damage-assesment-in-bangui-central-african-republic-july-02-2014](https://data.humdata.org/dataset/geodata-of-damage-assesment-in-bangui-central-african-republic-july-02-2014)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Bangui_Arrondissement`, `BossangoaCathedralIDP_Camp_Extent_20140106`, `Paoua_Damage_Zones`.

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

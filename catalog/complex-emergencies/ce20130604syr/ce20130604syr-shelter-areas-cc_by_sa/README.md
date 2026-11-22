# Shelter areas: Complex emergency, Syrian Arab Republic, 4 June 2013 (CE20130604SYR)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20130604syr/ce20130604syr-shelter-areas-cc_by_sa/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Shelter areas for Complex emergency, Syrian Arab Republic, 4 June 2013 (CE20130604SYR): 402 features merged from 7 source layers. Polygon layers with shelter or camp columns, or whose names mention camps, shelters, IDPs, or settlements. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Damage Density in the City of Aleppo, Syria](https://data.humdata.org/dataset/damage-density-in-the-city-of-aleppo-syria)
- [Internally Displaced Persons Shelters in Daraa and Quneitra Governorate](https://data.humdata.org/dataset/internally-displaced-persons-shelters-in-daraa-and-quneitra-governorate)
- [Internally Displaced Persons Shelters in Idlib, Lattakia and Aleppo Governorate](https://data.humdata.org/dataset/internally-displaced-persons-shelters-in-idlib-lattakia-and-aleppo-governorate)
- [Percentage damage in residential area of Aleppo City](https://data.humdata.org/dataset/percentage-damage-in-residential-area-of-aleppo-city)
- [Percentage of buildings damaged in the city of Aleppo](https://data.humdata.org/dataset/neighborhood-shelter-damage-percentages-in-aleppo-city)
- [Syria - 2014  Damage density  in Hama, Hama Governorate](https://data.humdata.org/dataset/damage-density-2014-of-hama-hama-governorate-syria)
- [Syria - 2016 Damage density in Hama, Hama Governorate](https://data.humdata.org/dataset/damage-density-2016-of-hama-hama-governorate-syria)
- [Syria - Damage assessement in Hama, Hama Governorate.](https://data.humdata.org/dataset/damage-assessement-of-hama-hama-governorate-syria)
- [Syria - Damage assessment of Deir Ez Zor, Deir Ez Zor Governorate](https://data.humdata.org/dataset/damage-assessment-of-deir-ez-zor-deir-ez-zor-governorate-syria)
- [Syria - Damage assessment of Idlib, Idlib Governorate](https://data.humdata.org/dataset/damage-assessment-of-idlib-idlib-governorate-syria)
- [Syria - Damage assessment of Jobar neighborhood and Irbin city, Damascus governorate.](https://data.humdata.org/dataset/damage-assessment-of-jobar-neighborhood-and-irbin-city-damascus-governorate-syria)
- [Syria - Damage density 2015 of Daraa, Daraa Governorate,](https://data.humdata.org/dataset/damage-density-2015-of-daraa-daraa-governorate-syria)
- and 7 more; the event's [catalog page](../catalog.json) lists them all.

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![damage assessment](https://img.shields.io/badge/damage_assessment-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [35.61393928487013, 32.28055284700008, 42.38504219144403, 37.31913947990313]

## Temporal Coverage

- **Start**: 2016-08-17T00:00:00Z
- **End**: 2017-06-21T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Name | string |  |
| Source | string |  |
| Shape_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Shape_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| OBJECTID_1 | int64 |  |
| Mohafaza_p | string |  |
| Mohafaza_A | string |  |
| Mohafaza_E | string |  |
| Mantika_pc | string |  |
| Mantika_AR | string |  |
| Mantika_EN | string |  |
| Nahya_pcod | string |  |
| Nahya_AR | string |  |
| Nahya_EN | string |  |
| Nahya_refn | string |  |
| Area_sqkm_ | double |  |
| SHAPE_Leng | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| IDPS_SETTL | int32 |  |
| N_SHELTERS | int32 |  |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `SensorID_label`, which is decoded per source file. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| StaffID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Site_ID | int16 | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Staduim; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 45 = Suspected Mass Grave Site; 50 = UNESCO World Heritage Site. The decoded text is in `Site_ID_label`. |
| Sensor_ID | int32 | Coded value. The source geodatabase domain gives: 1 = Worldview-1; 2 = Worldview-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = Komsat-2; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleadies; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 40 = WorldView-3; 999 = Combination of Sensors. The decoded text is in `Sensor_ID_label`. |
| Sensor_Date | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence_ID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `Confidence_ID_label`. |
| Field_Validation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `Field_Validation_label`. |
| CampStatusID | int32 | Coded value. The source geodatabase domain gives: 0 = Closed / Relocated; 1 = Open (Operational); 2 = Planned / Under Construction; 9 = Camp Destroyed. The decoded text is in `CampStatusID_label`. |
| CampName | string |  |
| CampQuicklook | int32 |  |
| GlobalID | string | ArcGIS global identifier of the feature. |
| CampType | int32 | Coded value. The source geodatabase domain gives: 1 = Refugee Camp; 2 = IDP Camp. The decoded text is in `CampType_label`. |
| CampStatusID_label | string | `CampStatusID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| CampType_label | string | `CampType` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Confidence_ID_label | string | `Confidence_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Field_Validation_label | string | `Field_Validation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Sensor_ID_label | string | `Sensor_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Site_ID_label | string | `Site_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20130604syr-shelter-areas-cc_by_sa.parquet | 1.1 MB | 1220269aefb6... |
| ./ce20130604syr-shelter-areas-cc_by_sa.pmtiles | 25.0 MB | 1220c6928491... |
| ./styles/default.json | 880 B | 1220a13061f8... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20130604syr-shelter-areas-cc_by_sa.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/damage-assessement-of-hama-hama-governorate-syria](https://data.humdata.org/dataset/damage-assessement-of-hama-hama-governorate-syria)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Al_Zaatari_Camp_Extent`, `IDP_Idlib_Lattakia_Aleppo_Extent`, `IDP_Quneitra_Daraa_Extent`, `Settlements`, `Sub_district_IDP_population`.

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

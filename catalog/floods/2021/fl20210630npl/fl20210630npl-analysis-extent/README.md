# Analysis extent: Flood, Nepal, 30 June 2021 (FL20210630NPL)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2021/fl20210630npl/fl20210630npl-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Analysis extent for Flood, Nepal, 30 June 2021 (FL20210630NPL): 8 features merged from 8 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Landslides impact analysis in Melamchi Municipality, Bagmati province, Nepal as of 24 June 2021](https://data.humdata.org/dataset/landslides-impact-analysis-in-melamchi-municipality-bagmati-province-nepal-as-of-24-june-2)
- [Satellite detected water extent over Kaski and Syangja districts, Gandaki province, Nepal as of 4 July 2021](https://data.humdata.org/dataset/water-extent-over-kaski-and-syangja-districts-gandaki-province-nepal-as-of-4-july-2021)
- [Satellite detected water extent over Nawalparasi West, Rupandehi and Kapilbastu districts, Nepal as of 7 July 2021](https://data.humdata.org/dataset/water-extent-over-nawalparasi-west-rupandehi-and-kapilbastu-districts-nepal-as-of-7-july-2)
- [Satellite detected water extent over Province 1 and 2 , Nepal as of 1 of July 2021](https://data.humdata.org/dataset/satellite-detected-water-extent-over-province-1-and-2-nepal-as-of-1-of-july-2021)
- [Satellite detected water extent over Province 1, Nepal as of 4 July 2021](https://data.humdata.org/dataset/satellite-detected-water-extent-over-province-1-nepal-as-of-4-july-2021)
- [Satellite detected water extent over Province 2, Lumbini, Gandaki,and Bagmati provinces , Nepal  as of 3 of July 2021](https://data.humdata.org/dataset/water-extent-over-province-2-lumbini-gandaki-and-bagmati-provinces-nepal-as-of-3-of-july-2)
- [Satellite detected water extent over Sudurpaschim and Lumbini provinces, Nepal as of 4 July 2021](https://data.humdata.org/dataset/water-extent-over-sudurpaschim-and-lumbini-provinces-nepal-as-of-4-july-2021)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [79.78629844500006, 25.805045375000077, 88.10474762900003, 28.95065747500007]

## Temporal Coverage

- **Start**: 2021-07-02T00:00:00Z
- **End**: 2021-07-08T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT-4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT-6; 42 = Sentinel-1; 43 = Kompsat-2; 44 = Sentinel-2; 45 = Sentinel-3; 46 = Kompsat-3; 47 = Deimos-2; 48 = TripleSat; 49 = PlanetLabs; 50 = RapidEye; 51 = WorldView-4; 52 = SPOT-7; 999 = Combination of Sensors. The decoded text is in `SensorID_label`. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | string | Coded value. The 2 source files of this collection use 2 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| Site_ID | int16 | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Staduim; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 42 = Military Facility; 45 = Suspected Mass Grave Site; 46 = Airport Facility; 47 = Church. The decoded text is in `Site_ID_label`. |
| AgencyID | int32 |  |
| SiteName | string |  |
| Site_ID_label | string | `Site_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Sensor_ID | string |  |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Staff_ID | int32 |  |
| ConfidenceID_label | string | `ConfidenceID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| FieldValidation_label | string | `FieldValidation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20210630npl-analysis-extent.parquet | 312.0 KB | 122053c46b53... |
| ./fl20210630npl-analysis-extent.pmtiles | 753.8 KB | 12204850e746... |
| ./styles/default.json | 671 B | 1220eed13089... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20210630npl-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/landslides-impact-analysis-in-melamchi-municipality-bagmati-province-nepal-as-of-24-june-2](https://data.humdata.org/dataset/landslides-impact-analysis-in-melamchi-municipality-bagmati-province-nepal-as-of-24-june-2)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `S1_20210701_AnalysisExtent_Province1_2`, `S1_20210702_AnalysisExtent_Lumbini_Gandaki_Bagmati_Province2`, `S1_20210704_AnalysisExtent_Province1`, `S1_20210704_AnalysisExtent_Sudurpaschim_Lumbini`, `S1_20210707_AnalysisExtent_Lumbini`, `S2_20210624_AnalysisExtent_Melamchi`, `S2_20210704_AnalysisExtent_Kaski_Syangja`, `S2_20210704_Cloudobstruction_Kaski_Syangja`.

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

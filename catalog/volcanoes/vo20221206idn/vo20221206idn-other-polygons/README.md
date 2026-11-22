# Other polygons: Volcano, Indonesia, 6 December 2022 (VO20221206IDN)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/volcanoes/vo20221206idn/vo20221206idn-other-polygons/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Other polygons for Volcano, Indonesia, 6 December 2022 (VO20221206IDN): 12 features merged from 12 source layers. Polygons layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Mount Semeru volcanic eruption, Jawa Timur Province, Indonesia - UNOSAT Live Web Map](https://data.humdata.org/dataset/mount-semeru-volcanic-eruption-jawa-timur-province-indonesia-unosat-live-web-map)
- [Potentially affected areas  by pyroclastic flow/deposits after the December 2022 Mount Semeru volcanic eruption in East Java.](https://data.humdata.org/dataset/potentially-affected-areas-by-pyroclastic-flow-deposits-after-the-december-2022-mount-seme)
- [Potentially affected areas SE Semeru mount in East Java, Indonesia](https://data.humdata.org/dataset/potentially-affected-areas-se-semeru-mount-in-east-java-indonesia)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![geodata](https://img.shields.io/badge/geodata-blue) ![natural disasters](https://img.shields.io/badge/natural_disasters-blue) ![volcano](https://img.shields.io/badge/volcano-blue)

## Spatial Coverage

- **Bounding Box**: [112.89470314700009, -8.35646202299995, 113.12796116900006, -8.097065894999957]

## Temporal Coverage

- **Start**: 2022-12-12T00:00:00Z
- **End**: 2022-12-13T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| Site_ID | int32 | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Staduim; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 42 = Military Facility; 45 = Suspected Mass Grave Site; 46 = Airport Facility; 47 = Church. The decoded text is in `Site_ID_label`. |
| AgencyID | int64 |  |
| SiteName | string |  |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| SHAPE_Leng | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Sensor_ID | string |  |
| StaffID | string |  |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| SiteID | int32 |  |
| SensorDate | date32[day] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence | int32 |  |
| Settlement | string |  |
| ImageID_Nu | int64 |  |
| SensorID | string |  |
| FieldValid | string |  |
| OBJECTID | int64 |  |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Site_ID_label | string | `Site_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./vo20221206idn-other-polygons.parquet | 401.7 KB | 1220120995d6... |
| ./vo20221206idn-other-polygons.pmtiles | 103.9 KB | 1220954f37d9... |
| ./styles/default.json | 664 B | 1220db5f62e6... |
| ./vo20221206idn-other-polygons.thumb.jpg | 15.4 KB | 122099c38fb1... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./vo20221206idn-other-polygons.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/mount-semeru-volcanic-eruption-jawa-timur-province-indonesia-unosat-live-web-map](https://data.humdata.org/dataset/mount-semeru-volcanic-eruption-jawa-timur-province-indonesia-unosat-live-web-map)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `WV3_20221209_S2_20221211_Spot6_20221212_AnalysisArea`, `WV3_20221209_S2_20221211_Spot6_20221212_AnalysisArea_Semeru`, `WV3_20221209_S2_20221211_Spot6_20221212_Pyroclasticflow`.

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

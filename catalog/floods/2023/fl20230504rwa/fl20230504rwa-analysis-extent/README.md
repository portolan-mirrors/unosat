# Analysis extent: Flood, Rwanda, 4 May 2023 (FL20230504RWA)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2023/fl20230504rwa/fl20230504rwa-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Analysis extent for Flood, Rwanda, 4 May 2023 (FL20230504RWA): 20 features merged from 20 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Damage assessment along the Mukungwa river, Western & Northern Provinces, Rwanda as of 10 May 2023](https://data.humdata.org/dataset/damage-assessment-along-the-mukungwa-river-western-northern-provinces-rwanda-as-of-10-may-)
- [Damage assessment along the Sebaya River, Rubavu and Karongi Districts, Western Province, Rwanda. - 6 May 2023](https://data.humdata.org/dataset/damage-assessment-along-the-sebaya-river-rubavu-and-karongi-districts-western-province-rwa)
- [Preliminary satellite flood and landslide assessment report, Along Sebaya River, Rubavu District, Karongi Districtn Western Province, Rwanda](https://data.humdata.org/dataset/preliminary-satellite-flood-and-landslide-assessment-report-along-sebaya-river-rubavu-dist)
- [Satellite detected landslides / mudslides over Kibingo, Congonil, Kagana and Ghanga Villages, Rutsiro District, Western Province, Rwanda  as of 7 May 2023](https://data.humdata.org/dataset/landslides-mudslides-over-kibingo-congonil-kagana-and-ghanga-villages-rutsiro-district-wes)
- [Satellite detected water extent along the Nyabarongo river West and South of Kigali City in Southern and Eastern Provinces, Rwanda as of 5 May 2023](https://data.humdata.org/dataset/water-extent-along-the-nyabarongo-river-west-and-south-of-kigali-city-in-southern-and-east)
- [Satellite detected water extent over Kigali City, Southern, Northern, Western, and Eastern Provinces, Rwanda  as of 3 May 2023](https://data.humdata.org/dataset/water-extent-over-kigali-city-southern-northern-western-and-eastern-provinces-rwanda-as-of)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [29.302987346000066, -2.345914867999909, 30.288783228000057, -1.6190118319999556]

## Temporal Coverage

- **Start**: 2023-05-05T00:00:00Z
- **End**: 2023-05-15T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The 3 source files of this collection use 3 different domains for it, so read `SensorID_label`, which is decoded per source file. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | string | Coded value. The 3 source files of this collection use 3 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| Site_ID | int16 | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Stadium; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 42 = Military Facility; 45 = Suspected Mass Grave Site; 46 = Airport Facility; 47 = Church. The decoded text is in `Site_ID_label`. |
| AgencyID | int32 |  |
| SiteName | string |  |
| Site_ID_label | string | `Site_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SHAPE_Leng | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Sensor_ID | string |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20230504rwa-analysis-extent.parquet | 8.3 KB | 1220591d8b57... |
| ./fl20230504rwa-analysis-extent.pmtiles | 120.1 KB | 1220e59e4654... |
| ./styles/default.json | 671 B | 1220a52a09b2... |
| ./fl20230504rwa-analysis-extent.thumb.jpg | 8.4 KB | 122084e9c921... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20230504rwa-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/damage-assessment-along-the-mukungwa-river-western-northern-provinces-rwanda-as-of-10-may-](https://data.humdata.org/dataset/damage-assessment-along-the-mukungwa-river-western-northern-provinces-rwanda-as-of-10-may-)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `PHR_20230506_AnalysisExtent_Nyundo_NorthernProvince_RWA`, `PHR_20230510_AnalysisExtent_NyabihuDistrict_WesternProvince_RWA`, `S1_20230503_AnalysisExtent_KigaliCity_Surrounding`, `S1_20230505_AnalysisExtent_KigaliCity_Surrounding`, `S2_20230507_AnalysisExtent_Kibingo_Surrounding`.

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

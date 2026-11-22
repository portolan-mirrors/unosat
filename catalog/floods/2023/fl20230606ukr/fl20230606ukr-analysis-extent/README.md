# Analysis extent: Flood, Ukraine, 6 June 2023 (FL20230606UKR)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2023/fl20230606ukr/fl20230606ukr-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Analysis extent for Flood, Ukraine, 6 June 2023 (FL20230606UKR): 193 features merged from 193 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Cumulative Satellite Detected Waters and Impact over Khersonska Oblast in Ukraine between 06 and 09 June 2023](https://data.humdata.org/dataset/cumulative-waters-and-impact-over-khersonska-oblast-in-ukraine-between-06-and-09-june-2023)
- [Damage assessment around the Nova Kakhova Dam, Ukraine as of 06 June 2023; 08:07 UTC](https://data.humdata.org/dataset/damage-assessment-around-the-nova-kakhova-dam-ukraine-as-of-06-june-2023-08-07-utc)
- [Damage assessment over Antonivka City and Dachi City, Khersonskyi Region, Khersonska Oblast, Ukraine as of 07 June 2023](https://data.humdata.org/dataset/damage-assessment-over-antonivka-city-and-dachi-city-khersonskyi-region-khersonska-oblast-)
- [Damage assessment over Kardashynka Village, Kokhany Village and surroundings, Khersonskyi Region, Khersonska Oblast, Ukraine as of 07 June 2023](https://data.humdata.org/dataset/damage-assessment-over-kardashynka-village-kokhany-village-and-surroundings-khersonskyi-re)
- [Damage assessment over Kherson City, Khersonskyi Region, Kehersonska Oblast, Ukraine as of 07 June 2023; 08:19 UTC](https://data.humdata.org/dataset/damage-assessment-over-kherson-city-khersonskyi-region-kehersonska-oblast-ukraine-as-of-07)
- [Damage assessment over Kherson City, Khersonskyi Region, Khersonska Oblast, Ukraine as of 17 June 2023.](https://data.humdata.org/dataset/damage-assessment-over-kherson-city-khersonskyi-region-khersonska-oblast-ukraine-as-of-17-)
- [Damage assessment over Oleshky City, Khersonskyi Region, Khersonska Oblast, Ukraine as of 07 June 2023](https://data.humdata.org/dataset/damage-assessment-over-oleshky-city-khersonskyi-region-khersonska-oblast-ukraine-as-of-07-)
- [Damage assessment over Solontsi Village and Pidlisne Village, Khersonskyi Region, Khersonska Oblast, Ukraine as of 07 June 2023](https://data.humdata.org/dataset/damage-assessment-over-solontsi-village-and-pidlisne-village-khersonskyi-region-khersonska)
- [Flood water extent evolution over Oleshky City in the east bank of the Dnipro (Dnieper) in Khersonska Oblast, Ukraine as of 09 June 2023; 08:37 UTC](https://data.humdata.org/dataset/flood-water-extent-evolution-over-oleshky-city-in-the-east-bank-of-the-dnipro-dnieper-in-k)
- [Flood water extent over Hola Prystan City in the east bank of the Dnipro (Dnieper) in Khersonska Oblast, Ukraine as of 17 June 2023; 09:13 UTC](https://data.humdata.org/dataset/flood-water-extent-over-hola-prystan-city-in-the-east-bank-of-the-dnipro-dnieper-in-kherso)
- [Floods along the Dnipro River, Ukraine - UNOSAT Live Web Map](https://data.humdata.org/dataset/floods-along-the-dnipro-river-ukraine-unosat-live-web-map)
- [Satellite Detected Waters Evolution over Khersonska, Dnipropetrovska, Mykolaivska,Odeska and Zaporizka Oblasts in Ukraine  as of 15 July 2023](https://data.humdata.org/dataset/waters-evolution-over-khersonska-dnipropetrovska-mykolaivska-odeska-and-zaporizka-oblasts-)
- and 7 more; the event's [catalog page](../catalog.json) lists them all.

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [31.150201585000048, 46.211581445000036, 35.40320585000006, 47.79427157400005]

## Temporal Coverage

- **Start**: 2023-06-07T00:00:00Z
- **End**: 2023-07-20T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `SensorID_label`, which is decoded per source file. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | string | Coded value. The 2 source files of this collection use 2 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Shape_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Shape_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| Staff_ID | int32 |  |
| ConfidenceID_label | string | `ConfidenceID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| FieldValidation_label | string | `FieldValidation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
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
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20230606ukr-analysis-extent.parquet | 14.3 MB | 1220f7d24bda... |
| ./fl20230606ukr-analysis-extent.pmtiles | 8.8 MB | 122077439b2b... |
| ./styles/default.json | 671 B | 12201206911f... |
| ./fl20230606ukr-analysis-extent.thumb.jpg | 22.9 KB | 1220b1edf4bd... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20230606ukr-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/cumulative-waters-and-impact-over-khersonska-oblast-in-ukraine-between-06-and-09-june-2023](https://data.humdata.org/dataset/cumulative-waters-and-impact-over-khersonska-oblast-in-ukraine-between-06-and-09-june-2023)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `ICEYE_20230607_AnalysisExtent`, `ICEYE_20230607_AnalysisExtent_KhersonskaOblast_UKR`, `ST1_20230609_AnalysisExtent_KhersonskarOblast_UKR`, `ST1_20230621_AnalysisExtent_KhersonskarOblast_UKR`, `ST1_20230715_AnalysisExtent`, `ST1_20230715_CloudObstruction`, `ST2_20230613_AnalysisExtent_KhersonskaOblast_UKR`, `ST2_20230613_CloudObstruction_KhersonskaOblast_UKR`, `ST2_20230703_20230705_AnalysisExtent`, `ST3_20230606_AnalysisExtent_KhersonskaOblast_UKR`, `ST3_20230606_CloudObstructionKhersonskaOblast_UKR`, `ST3_20230609_ST2_20230608_AnalysisExtent_KhersonskaOblast_UKR`, `SkySat_20230606_AnalysisExtent_NK_Dam`, `WV03_20230608_AnalysisExtent_HolaPrystanCity_UKR`.

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

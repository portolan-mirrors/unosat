# Water extent: Flood, Ukraine, 6 June 2023 (FL20230606UKR)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2023/fl20230606ukr/fl20230606ukr-water-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Water extent for Flood, Ukraine, 6 June 2023 (FL20230606UKR): 531 features merged from 531 source layers. Polygon layers with a water class column (such as `Water_Class`), or whose names mention flood, water, or inundation: satellite-detected water. The `source_layer` and `source_file` columns name the layer and file each row came from.

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

- **Bounding Box**: [31.134267212000054, 45.68273624400007, 35.51350817800005, 47.83549447200005]

## Temporal Coverage

- **Start**: 2023-06-07T00:00:00Z
- **End**: 2023-07-20T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Water_Class | int16 | Coded value. The source geodatabase domain gives: 0 = Archive Water Extent / Pre-Flood Water; 1 = Flood Water; 2 = Satellite Detected Water / Possible Saturated Soil; 3 = Probable Flash Flood-Affected Land; 4 = Aquaculture; 5 = Possible Satuated, wet soil; 6 = Tsunami-Affected Land; 7 = Maximum Satellite Observed Water (Cumulative); 8 = Swamp / Marsh / Mangrove; 9 = Snow Cover. The decoded text is in `Water_Class_label`. |
| Sensor_ID | string | Coded value. The 3 source files of this collection use 3 different domains for it, so read `Sensor_ID_label`, which is decoded per source file. |
| Sensor_Date | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence_ID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `Confidence_ID_label`. |
| Field_Validation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `Field_Validation_label`. |
| Water_StatusID | int32 | Coded value. The source geodatabase domain gives: 1 = New Water / Water Increase; 2 = No water change / Static Level; 3 = No water / Water levels decreased. The decoded text is in `Water_StatusID_label`. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| SenorID_old | int16 | Coded value. The source geodatabase domain gives: 1 = MODIS; 2 = ASAR WSM; 3 = ASAR IMP; 4 = Radarsat; 5 = DMC; 6 = SPOT5; 7 = ALOS Palsar WB1; 8 = ASAR APP. The decoded text is in `SenorID_old_label`. |
| StaffID | string | Coded value. The 3 source files of this collection use 3 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Confidence_ID_label | string | `Confidence_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Field_Validation_label | string | `Field_Validation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SenorID_old_label | string | `SenorID_old` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Sensor_ID_label | string | `Sensor_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Water_Class_label | string | `Water_Class` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Water_StatusID_label | string | `Water_StatusID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| Water_Clas | string |  |
| Sensor_Dat | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence | string |  |
| Field_Vali | string |  |
| Water_Stat | string |  |
| SenorID_ol | string |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20230606ukr-water-extent.parquet | 64.6 MB | 12208352a1cf... |
| ./fl20230606ukr-water-extent.pmtiles | 19.6 MB | 1220e11061ab... |
| ./styles/default.json | 1.1 KB | 1220ea5e6808... |
| ./fl20230606ukr-water-extent.thumb.jpg | 22.8 KB | 122010087d8f... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20230606ukr-water-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/cumulative-waters-and-impact-over-khersonska-oblast-in-ukraine-between-06-and-09-june-2023](https://data.humdata.org/dataset/cumulative-waters-and-impact-over-khersonska-oblast-in-ukraine-between-06-and-09-june-2023)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `ICEYE_20230607_FloodExtent_KhersonskaOblast_UKR`, `ICEYE_20230607_WaterExtentOutsideRiverBed_KhersonskaOblast_UKR`, `ICEYE_20230607_WaterExtent_KhersonskaOblast_UKR`, `L9_20230609_WaterExtent_KhersonskaOblast_UKR`, `MODIS_AquaTerra_20230607_FloodExtent_NK_Dam`, `MultiSensors_20230606_20230609_MaximumWaterExtent`, `ST1_20230609_WaterExtent_KhersonskarOblast_UKR`, `ST1_20230621_FloodExtent_KhersonskarOblast_UKR`, `ST1_20230621_WaterExtent_KhersonskarOblast_UKR`, `ST1_20230715_WaterExtent`, `ST2_20230603_20230605_RiverBanks_DniproRiver`, `ST2_20230603_20230605_WaterExtent_KhersonskaOblast_UKR`, `ST2_20230608_FloodExtent_KhersonskarOblast_UKR`, `ST2_20230608_WaterExtent_KhersonskarOblast_UKR`, `ST2_20230613_FloodExtent_KhersonskaOblast_UKR`, `ST2_20230613_WaterExtent_KhersonskaOblast_UKR`, `ST2_20230703_20230705_FloodExtent`, `ST2_20230703_20230705_WaterExtent`, `ST3_20230605_WaterExtent_KhersonskaOblast_UKR`, `ST3_20230606_20230607_20230609_ST2_20230608_ICEYE_20230607_FloodExtent_KhersonskaOblast`, `ST3_20230606_FloodExtent_KhersonskaOblast_UKR`, `ST3_20230606_WaterExtent_KhersonskaOblast_UKR`, `ST3_20230609_FloodExtent_KhersonskaOblast_UKR`, `ST3_20230609_WaterExtent_KhersonskaOblast_UKR`, `SkySat_20230606_FloodExtent_NK_Dam`, `SkySat_20230606_WaterExtent_NK_Dam`, `WV03_20230608_FloodExtent_HolaPrystanCity_UKR`, `WV3_20230617_FloodExtent_HolaPrystan`, `WV3_20230617_FloodExtent_Kherson`, `WV3_20230617_FloodExtent_Oleshky`, `WV3_20230617_WaterExtent_Kherson`, `WV3_20230617_WaterExtent_Oleshky`.

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

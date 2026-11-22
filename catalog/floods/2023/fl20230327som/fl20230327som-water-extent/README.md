# Water extent: Flood, Ethiopia, Somalia, 27 March 2023 (FL20230327SOM)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2023/fl20230327som/fl20230327som-water-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Water extent for Flood, Ethiopia, Somalia, 27 March 2023 (FL20230327SOM): 277 features merged from 172 source layers. Polygon layers with a water class column (such as `Water_Class`), or whose names mention flood, water, or inundation: satellite-detected water. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Satellite detected cumulative water over Beledweyne City, Hiraan Region of Somalia between 12 and 25 May 2023](https://data.humdata.org/dataset/cumulative-water-over-beledweyne-city-hiraan-region-of-somalia-between-12-and-25-may-2023)
- [Satellite detected water extent  over southern Hiraan Region and Jowhar CIty, Middle Shabelle Region, Somalia as of 24 May 2023](https://data.humdata.org/dataset/water-extent-over-southern-hiraan-region-and-jowhar-city-middle-shabelle-region-somalia-as)
- [Satellite detected water extent - Beledweyne City, Beledweyne District, Hiraan Region of Somalia as of 19 May 2023](https://data.humdata.org/dataset/water-extent-beledweyne-city-beledweyne-district-hiraan-region-of-somalia-as-of-19-may-202)
- [Satellite detected water extent over Belet Weyne and Bulo Burto Zones, Hiraan Region, Somalia as of 29 April 2023](https://data.humdata.org/dataset/water-extent-over-belet-weyne-and-bulo-burto-zones-hiraan-region-somalia-as-of-29-april-20)
- [Satellite detected water extent over Bulo Burto City, Bulo Burto District, Hiraan Region of Somalia as of 3 June 2023](https://data.humdata.org/dataset/water-extent-over-bulo-burto-city-bulo-burto-district-hiraan-region-of-somalia-as-of-3-jun)
- [Satellite detected water extent over Bulo Burto City, Bulo Burto District, Hiraan Region of Somalia as of 30 May 2023](https://data.humdata.org/dataset/water-extent-over-bulo-burto-city-bulo-burto-district-hiraan-region-of-somalia-as-of-30-ma)
- [Satellite detected water extent over Ferfer Woreda, Shabelle District, Shabelle Region, Ethiopia as of 30 March 2023](https://data.humdata.org/dataset/water-extent-over-ferfer-woreda-shabelle-district-shabelle-region-ethiopia-as-of-30-march-)
- [Satellite detected water extent over Hiraan, Lower Shabelle, and Middle Shabelle Regions, Somalia as of 29 April 2023](https://data.humdata.org/dataset/water-extent-over-hiraan-lower-shabelle-and-middle-shabelle-regions-somalia-as-of-29-april)
- [Satellite detected water extent over Shabelle District, Shabelle Region, Ethiopia as of 28 March 2023](https://data.humdata.org/dataset/water-extent-over-shabelle-district-shabelle-region-ethiopia-as-of-28-march-2023)
- [Satellite detected water extent over Shabelle Zone, Somali Region, Ethiopia and Beledweyne District, Hiraan Region of Somalia as of 29 April 2023](https://data.humdata.org/dataset/water-extent-over-shabelle-zone-somali-region-ethiopia-and-beledweyne-district-hiraan-regi)
- [Satellite detected water extent over Shabelle Zone, Somali Region, Ethiopia and Beledweyne and Northern Bulo Burto District, Hiraan Region of Somalia as of 14 May 2023](https://data.humdata.org/dataset/water-extent-over-shabelle-zone-somali-region-ethiopia-and-beledweyne-and-northern-bulo-bu)
- [Satellite detected water extent over Shabelle Zone, Somali Region, Ethiopia as of 2 April 2023](https://data.humdata.org/dataset/water-extent-over-shabelle-zone-somali-region-ethiopia-as-of-2-april-2023)
- and 2 more; the event's [catalog page](../catalog.json) lists them all.

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [42.29537852200008, 2.3347677570000656, 45.71823601400007, 6.774914210000077]

## Temporal Coverage

- **Start**: 2023-03-29T00:00:00Z
- **End**: 2023-06-05T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Water_Class | int16 | Coded value. The source geodatabase domain gives: 0 = Archive Water Extent / Pre-Flood Water; 1 = Flood Water; 2 = Satellite Detected Water / Possible Saturated Soil; 3 = Probable Flash Flood-Affected Land; 4 = Aquaculture; 5 = Possible Satuated, wet soil; 6 = Tsunami-Affected Land; 7 = Maximum Satellite Observed Water (Cumulative); 8 = Swamp / Marsh / Mangrove; 9 = Snow Cover. The decoded text is in `Water_Class_label`. |
| Sensor_ID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Sensor_ID_label`, which is decoded per source file. |
| Sensor_Date | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence_ID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `Confidence_ID_label`. |
| Field_Validation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `Field_Validation_label`. |
| Water_StatusID | int32 | Coded value. The source geodatabase domain gives: 1 = New Water / Water Increase; 2 = No water change / Static Level; 3 = No water / Water levels decreased. The decoded text is in `Water_StatusID_label`. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| SenorID_old | int16 | Coded value. The source geodatabase domain gives: 1 = MODIS; 2 = ASAR WSM; 3 = ASAR IMP; 4 = Radarsat; 5 = DMC; 6 = SPOT5; 7 = ALOS Palsar WB1; 8 = ASAR APP. The decoded text is in `SenorID_old_label`. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| StaffID | int32 | Coded value. The 3 source files of this collection use 3 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
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
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20230327som-water-extent.parquet | 20.2 MB | 1220b6ccad09... |
| ./fl20230327som-water-extent.pmtiles | 13.6 MB | 12206cd679ba... |
| ./styles/default.json | 972 B | 12206908eb10... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20230327som-water-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/cumulative-water-over-beledweyne-city-hiraan-region-of-somalia-between-12-and-25-may-2023](https://data.humdata.org/dataset/cumulative-water-over-beledweyne-city-hiraan-region-of-somalia-between-12-and-25-may-2023)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `JL_PHR_20230513_20230525_FloodExtent_Beledweyne_SOM`, `JL_PHR_20230525_FloodExtent_Beledweyne_SOM`, `PHR_20230529_20230530_WaterExtent_BuloBurto_SOM`, `PHR_20230603_WaterExtent_BuloBurto_SOM`, `S2_20230328_WaterExtent_ShabelleDistrict_ETH`, `S2_20230402_FloodExtent_ShabelleDistrict_ETH`, `S2_20230404_FloodExtent_Border_ETH_SOM`, `S2_20230409_FloodExtent_Border_ETH_SOM`, `S2_20230414_FloodExtent_Border_ETH_SOM`, `S2_20230419_FloodExtent_Booco`, `S2_20230419_FloodExtent_Border_ETH_SOM`, `S2_20230419_FloodExtent_Jowhar`, `S2_20230429_FloodExtent_Booco`, `S2_20230429_FloodExtent_Border_ETH_SOM`, `S2_20230429_FloodExtent_Jowhar`, `S2_20230514_WaterExtent_Border_ETH_SOM_Bocco`, `S2_20230519_WaterExtent_BeledweyneCity_Somalia`, `SP_20230330_WaterExtent_SouthernShabelleDistrict_ETH`, `VIIRS_20230523_FloodExtent_SOM`, `VIIRS_20230528_FloodExtent_SOM`.

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

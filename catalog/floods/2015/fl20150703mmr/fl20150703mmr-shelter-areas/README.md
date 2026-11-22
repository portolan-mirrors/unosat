# Shelter areas: Flood, Myanmar, 3 July 2015 (FL20150703MMR)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2015/fl20150703mmr/fl20150703mmr-shelter-areas/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Shelter areas for Flood, Myanmar, 3 July 2015 (FL20150703MMR): 2 features merged from 1 source layer. Polygon layers with shelter or camp columns, or whose names mention camps, shelters, IDPs, or settlements. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of Damage Assessment over Tuikhingzang, Tonzang Township, Chin Division, Myanmar](https://data.humdata.org/dataset/geodata-of-damage-assessment-over-tuikhingzang-tonzang-township-chin-division-september-17-2015)
- [Geodata of Flood Waters Near City of Yangon, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-near-city-of-yangon-myanmar-august-10-2015)
- [Geodata of Flood Waters Over Ann and Myebon area, Rakhine State, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-ann-and-myebon-area-rakhine-state-myanmar-august-17-2015)
- [Geodata of Flood Waters Over Ann area, Rakhine State, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-ann-area-rakhine-state-myanmar-august-14-2015)
- [Geodata of Flood Waters Over Central Magway State, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-central-magway-state-myanmar-august-07-2015)
- [Geodata of Flood Waters Over Central Sagaing Region, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-central-sagaing-region-myanmar-august-13-2015)
- [Geodata of Flood Waters Over Central Sagaing State, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-central-sagaing-state-myanmar-july-24-2015)
- [Geodata of Flood Waters Over Kayin and Mon State, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-kayin-and-mon-state-myanmar-august-14-2015)
- [Geodata of Flood Waters Over Kyautaw area, Rakhine State, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-kyautaw-area-rakhine-state-myanmar-august-19-2015)
- [Geodata of Flood Waters Over Northern Rakhine State, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-northern-rakhine-state-myanmar-august-11-2015)
- [Geodata of Flood Waters Over Northwest Rakhine State, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-northwest-rakhine-state-myanmar-july-13-2015)
- [Geodata of Flood Waters Over South Bago Division, Myanmar](https://data.humdata.org/dataset/geodata-of-flood-waters-over-south-bago-division-myanmar-august-13-2015)
- and 7 more; the event's [catalog page](../catalog.json) lists them all.

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [94.02528064000006, 23.55748751200008, 94.04360513800003, 23.560732104000067]

## Temporal Coverage

- **Start**: 2015-07-13T00:00:00Z
- **End**: 2015-10-21T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Site_ID | int16 | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Staduim; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 45 = Suspected Mass Grave Site. The decoded text is in `Site_ID_label`. |
| Sensor_ID | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT 6; 42 = Sentinel-1; 43 = Komsat-2; 999 = Combination of Sensors. The decoded text is in `Sensor_ID_label`. |
| Sensor_Date | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence_ID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `Confidence_ID_label`. |
| Field_Validation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `Field_Validation_label`. |
| CampStatusID | int32 | Coded value. The source geodatabase domain gives: 0 = Closed / Relocated; 1 = Open (Operational); 2 = Planned / Under Construction; 9 = Camp Destroyed. The decoded text is in `CampStatusID_label`. |
| CampName | string |  |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| CampQuicklook | int32 |  |
| Notes | string | Free-text notes by the analyst. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 22 = WP; 33 = LB; 44 = JL; 55 = VG; 66 = CJ; 73 = RS; 77 = LD; 88 = HK; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 222 = CS; 1000 = Unknown. The decoded text is in `StaffID_label`. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| CampType | int32 | Coded value. The source geodatabase domain gives: 1 = Refugee Camp; 2 = IDP Camp. The decoded text is in `CampType_label`. |
| City_District | string |  |
| Date_Opened | int32 |  |
| ShelterCount | int32 |  |
| ShelterEstimate | int32 |  |
| FormaltentID | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Yes; 2 = No. The decoded text is in `FormaltentID_label`. |
| CampStatID_L2 | int32 | Coded value. The source geodatabase domain gives: 10 = Open - New; 20 = Open - Reopened; 30 = Open - Expanded; 40 = Open - Contracted; 50 = Open - No Change; 60 = Open - Unknown (clouded / no coverage); 70 = Closed - New (no further indication of resident status); 80 = Closed - Relocated / Aggregated to adjacent camp site; 90 = Closed - Absorbed (site absorbed by other camp expansion); 100 = Closed - Unchanged; 110 = Planned (opening within next days, grounds prepared); 120 = Planned (grounds not prepared, opening date undefined). The decoded text is in `CampStatID_L2_label`. |
| Date_Opened_OLD | int32 | Coded value. The source geodatabase domain gives: 1 = Before 2009; 2 = Before 30 March 2011; 3 = Before 15 April 2011; 4 = Between 30 March - 15 April 2011; 5 = Between 15 April -28 July 2011; 6 = Between 28 July / 18 Aug 2011; 7 = Between 28 July - 21 August 2011; 8 = Between 18 -21 August 2011; 9 = Before 31 October 2010; 10 = Between 21 August - 4 Sept. 2011; 20 = Before 1 April 2011; 21 = Between 1 April - 12 September 2011; 22 = Between 21 August - 18 October 2011; 23 = Between 12 Sept. -18 October 2011; 30 = Between 21 August - 12 September 2011; 40 = Between 12 September - 18 October 2011; 41 = Between 18 October 2011 - 16 January 2012; 42 = Between 18 October 2011 - 2 May 2012; 43 = Between 18 October 2011 - 10 May 2012; 44 = Between 14 September 2011 - 10 May 2012. The decoded text is in `Date_Opened_OLD_label`. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| CampStatID_L2_label | string | `CampStatID_L2` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| CampStatusID_label | string | `CampStatusID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| CampType_label | string | `CampType` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Confidence_ID_label | string | `Confidence_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Date_Opened_OLD_label | string | `Date_Opened_OLD` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Field_Validation_label | string | `Field_Validation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| FormaltentID_label | string | `FormaltentID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Sensor_ID_label | string | `Sensor_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Site_ID_label | string | `Site_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20150703mmr-shelter-areas.parquet | 8.1 KB | 1220438fd28a... |
| ./fl20150703mmr-shelter-areas.pmtiles | 26.5 KB | 12200a31c8cd... |
| ./styles/default.json | 871 B | 122068f541d5... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20150703mmr-shelter-areas.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-damage-assessment-over-tuikhingzang-tonzang-township-chin-division-september-17-2015](https://data.humdata.org/dataset/geodata-of-damage-assessment-over-tuikhingzang-tonzang-township-chin-division-september-17-2015)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `PL20150916_Camp_Extent`.

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

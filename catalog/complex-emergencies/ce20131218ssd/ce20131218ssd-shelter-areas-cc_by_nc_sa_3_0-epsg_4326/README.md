# Shelter areas: Complex emergency, South Sudan, 18 December 2013 (CE20131218SSD)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20131218ssd/ce20131218ssd-shelter-areas-cc_by_nc_sa_3_0-epsg_4326/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Shelter areas for Complex emergency, South Sudan, 18 December 2013 (CE20131218SSD): 1,166 features merged from 29 source layers. Polygon layers with shelter or camp columns, or whose names mention camps, shelters, IDPs, or settlements. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of Bentiu IDP Camp, Rubkona County, Unity State, South Sudan](https://data.humdata.org/dataset/geodata-of-bentiu-idp-camp-rubkona-county-unity-state-south-sudan-november-16-2015)
- [Geodata of Damage Assesment In The City Of Malakal, Upper Nile State, South Sudan](https://data.humdata.org/dataset/geodata-of-damage-assesment-in-the-city-of-malakal-upper-nile-state-south-sud-march-21-2014)
- [Geodata of Damage Assesment in the City of Malakal, Upper Nile State, South Sudan](https://data.humdata.org/dataset/geodata-of-damage-assesment-in-the-city-of-malakal-upper-nile-state-south-sud-january-24-2014)
- [Geodata of Damage Assessment in the City of Bentiu, Unity State, South Sudan](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-the-city-of-bentiu-unity-state-south-sudan-january-18-2014)
- [Geodata of Damage assesment in the city of Bor, Jonglei State, South Sudan](https://data.humdata.org/dataset/geodata-of-damage-assesment-in-the-city-of-bor-jonglei-state-south-sudan-january-21-2014)
- [Geodata of Delthoma IDP Camp, Melut District, Upper Nile State, South Sudan](https://data.humdata.org/dataset/geodata-of-delthoma-idp-camp-melut-district-upper-nile-state-south-sudan-december-03-2015)
- [Geodata of Destruction in Leer, Unity State, South Sudan](https://data.humdata.org/dataset/geodata-of-destruction-in-leer-unity-state-south-sudan-february-07-2014)
- [Geodata of Destruction in Mayom, Unity State, South Sudan](https://data.humdata.org/dataset/geodata-of-destruction-in-mayom-unity-state-south-sudan-january-21-2014)
- [Geodata of Destruction in Rubkona, Unity State, South Sudan](https://data.humdata.org/dataset/geodata-of-destruction-in-rubkona-unity-state-south-sudan-january-16-2014)
- [Geodata of IDP Camp in Melut, Upper Nile State, South Sudan](https://data.humdata.org/dataset/geodata-of-idp-camp-in-melut-upper-nile-state-south-sudan-december-23-2014)
- [Geodata of IDP Camp in UNMISS Malakal Base, Malakal, South Sudan](https://data.humdata.org/dataset/geodata-of-idp-camp-in-unmiss-malakal-base-malakal-south-sudan-january-20-2014)
- [Geodata of IDP Camp in UNMISS Malakal Base, Malakal, South Sudan](https://data.humdata.org/dataset/geodata-of-idp-camp-in-unmiss-malakal-base-malakal-south-sudan-october-22-2015)
- and 16 more; the event's [catalog page](../catalog.json) lists them all.

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [29.78278208100005, 4.80541222700009, 32.26310040800007, 10.453688043000056]

## Temporal Coverage

- **Start**: 2014-01-09T00:00:00Z
- **End**: 2016-08-19T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Site_ID | string | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Staduim; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 45 = Suspected Mass Grave Site. The decoded text is in `Site_ID_label`. |
| Sensor_ID | string | Coded value. The 3 source files of this collection use 3 different domains for it, so read `Sensor_ID_label`, which is decoded per source file. |
| Sensor_Date | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence_ID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `Confidence_ID_label`. |
| Field_Validation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `Field_Validation_label`. |
| CampStatusID | int32 | Coded value. The source geodatabase domain gives: 0 = Closed / Relocated; 1 = Open (Operational); 2 = Planned / Under Construction; 9 = Camp Destroyed. The decoded text is in `CampStatusID_label`. |
| CampName | string |  |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| CampQuicklook | int32 |  |
| Notes | string | Free-text notes by the analyst. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | string | Coded value. The 5 source files of this collection use 5 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| CampType | string | Coded value. The source geodatabase domain gives: 1 = Refugee Camp; 2 = IDP Camp. The decoded text is in `CampType_label`. |
| City_District | string |  |
| Date_Opened | int32 |  |
| ShelterCount | int32 |  |
| ShelterEstimate | int32 |  |
| FormaltentID | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Yes; 2 = No. The decoded text is in `FormaltentID_label`. |
| CampStatID_L2 | int32 | Coded value. The source geodatabase domain gives: 10 = Open - New; 20 = Open - Reopened; 30 = Open - Expanded; 40 = Open - Contracted; 50 = Open - No Change; 60 = Open - Unknown (clouded / no coverage); 70 = Closed - New (no further indication of resident status); 80 = Closed - Relocated / Aggregated to adjacent camp site; 90 = Closed - Absorbed (site absorbed by other camp expansion); 100 = Closed - Unchanged; 110 = Planned (opening within next days, grounds prepared); 120 = Planned (grounds not prepared, opening date undefined). The decoded text is in `CampStatID_L2_label`. |
| Date_Opened_OLD | int32 | Coded value. The source geodatabase domain gives: 1 = Before 2009; 2 = Before 30 March 2011; 3 = Before 15 April 2011; 4 = Between 30 March - 15 April 2011; 5 = Between 15 April -28 July 2011; 6 = Between 28 July / 18 Aug 2011; 7 = Between 28 July - 21 August 2011; 8 = Between 18 -21 August 2011; 9 = Before 31 October 2010; 10 = Between 21 August - 4 Sept. 2011; 20 = Before 1 April 2011; 21 = Between 1 April - 12 September 2011; 22 = Between 21 August - 18 October 2011; 23 = Between 12 Sept. -18 October 2011; 30 = Between 21 August - 12 September 2011; 40 = Between 12 September - 18 October 2011; 41 = Between 18 October 2011 - 16 January 2012; 42 = Between 18 October 2011 - 2 May 2012; 43 = Between 18 October 2011 - 10 May 2012; 44 = Between 14 September 2011 - 10 May 2012. The decoded text is in `Date_Opened_OLD_label`. |
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
| Sensor_Dat | date32[day] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence | string |  |
| Field_Vali | string |  |
| CampStatus | string |  |
| City_Distr | string |  |
| Date_Opene | int64 |  |
| ShelterCou | int64 |  |
| ShelterEst | int64 |  |
| Formaltent | string |  |
| CampStatID | string |  |
| Date_Ope_1 | string |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20131218ssd-shelter-areas-cc_by_nc_sa_3_0-epsg_4326.parquet | 150.9 KB | 12207cf5a52b... |
| ./ce20131218ssd-shelter-areas-cc_by_nc_sa_3_0-epsg_4326.pmtiles | 349.2 KB | 12208b8a98d3... |
| ./styles/default.json | 971 B | 1220e86a6592... |
| ./ce20131218ssd-shelter-areas-cc_by_nc_sa_3_0-epsg_4326.thumb.jpg | 2.6 KB | 12205acd62f9... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20131218ssd-shelter-areas-cc_by_nc_sa_3_0-epsg_4326.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-bentiu-idp-camp-rubkona-county-unity-state-south-sudan-november-16-2015](https://data.humdata.org/dataset/geodata-of-bentiu-idp-camp-rubkona-county-unity-state-south-sudan-november-16-2015)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `IDP_Camp_Extent`, `IDP_Camp_Extent_Bentiu`, `IDP_Camp_Extent_Bor`, `IDP_Camp_Extent_Delthoma_201551129`, `IDP_Camp_Extent_Juba`, `IDP_Camp_Extent_Juba_PoC`, `IDP_Camp_Extent_Malakal`, `IDP_Camp_Extent_Malakal_1`, `IDP_Camp_Extent_Rubkona`, `IDP_Camp_Extent_WauShilluk`, `Melut_Camp_Extent_20141202`, `Protection_of_Civilians_Area`.

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

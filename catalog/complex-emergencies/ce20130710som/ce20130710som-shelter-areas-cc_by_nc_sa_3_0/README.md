# Shelter areas: Complex emergency, Somalia, 10 July 2013 (CE20130710SOM)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20130710som/ce20130710som-shelter-areas-cc_by_nc_sa_3_0/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Shelter areas for Complex emergency, Somalia, 10 July 2013 (CE20130710SOM): 9,667 features merged from 54 source layers. Polygon layers with shelter or camp columns, or whose names mention camps, shelters, IDPs, or settlements. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of IDP Settlements and Shelters in Kismayo, Lower Juba, Somalia](https://data.humdata.org/dataset/geodata-of-idp-settlements-and-shelters-in-kismayo-lower-juba-somalia-april-30-2014)
- [Geodata of IDP Settlements and Shelters in Kismayo, Lower Juba, Somalia](https://data.humdata.org/dataset/geodata-of-idp-settlements-and-shelters-in-kismayo-lower-juba-somalia-july-03-2014)
- [Geodata of IDP Settlements and shelters in Luuq, Gedo Province, Somalia](https://data.humdata.org/dataset/geodata-of-idp-settlements-and-shelters-in-luuq-gedo-province-somalia-june-30-2014)
- [Geodata of IDP Shelter Changes in Baidoa, Somalia, Between 21 August 2013 and 08 February 2014](https://data.humdata.org/dataset/geodata-of-idp-shelter-changes-in-baidoa-somalia-between-21-august-2013-and-0-march-18-2014)
- [Geodata of IDP Shelter changes in Baidoa, Somalia, Between 08 February and 02 October 2014](https://data.humdata.org/dataset/geodata-of-idp-shelter-changes-in-baidoa-somalia-between-08-february-and-02-o-october-31-2014)
- [Geodata of IDP Shelter changes in Hargeisa, Somalia between 20 August 2012 and 02 November 2014](https://data.humdata.org/dataset/geodata-of-idp-shelter-changes-in-hargeisa-somalia-between-20-august-2012-and-december-17-2014)
- [Geodata of IDP Shelters Detected, North of Galkayo, Somalia](https://data.humdata.org/dataset/geodata-of-idp-shelters-detected-north-of-galkayo-somalia-may-27-2014)
- [Geodata of IDP shelter Changes in Kismayo, Somalia, Between 11 August 2013 - 05 March 2014](https://data.humdata.org/dataset/geodata-of-idp-shelter-changes-in-kismayo-somalia-between-11-august-2013-05-m-march-18-2014)
- [Geodata of Informal IDP shelters in border town of Doolow, Somalia](https://data.humdata.org/dataset/geodata-of-informal-idp-shelters-in-border-town-of-doolow-somalia-october-28-2014)
- [Geodata of UPDATE: IDP Shelter density in Daynile and Dharkenley District, Mogadishu, Somalia](https://data.humdata.org/dataset/geodata-of-idp-shelter-density-in-daynile-and-dharkenley-district-mogadishu-november-10-2014)
- [Geodata of Update 6: Reduction of Somali IDP Shelter Concentrations in Mogadishu, Somalia  (3 June 2013 - 24 November 2013)](https://data.humdata.org/dataset/geodata-of-6-reduction-of-somali-idp-shelter-concentrations-in-mogadishu-som-january-02-2014)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [40.275299000000075, -0.3697252889999163, 49.21341787100005, 11.289194687000077]

## Temporal Coverage

- **Start**: 2014-01-02T00:00:00Z
- **End**: 2014-12-17T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Site_ID | string | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Staduim; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 45 = Suspected Mass Grave Site. The decoded text is in `Site_ID_label`. |
| Sensor_ID | string | Coded value. The 4 source files of this collection use 4 different domains for it, so read `Sensor_ID_label`, which is decoded per source file. |
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
| StaffID | string | Coded value. The 6 source files of this collection use 6 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| CampType | string | Coded value. The source geodatabase domain gives: 1 = Refugee Camp; 2 = IDP Camp. The decoded text is in `CampType_label`. |
| City_District | string |  |
| Date_Opened | int32 |  |
| ShelterCount | int32 |  |
| ShelterEstimate | int32 |  |
| FormaltentID | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Yes; 2 = No. The decoded text is in `FormaltentID_label`. |
| CampStatID_L2 | int32 | Coded value. The source geodatabase domain gives: 10 = Open - New; 20 = Open - Reopened; 30 = Open - Expanded; 40 = Open - Contracted; 50 = Open - No Change; 60 = Open - Unknown (clouded / no coverage); 70 = Closed - New (no further indication of resident status); 80 = Closed - Relocated / Aggregated to adjacent camp site; 90 = Closed - Absorbed (site absorbed by other camp expansion); 100 = Closed - Unchanged; 110 = Planned (opening within next days, grounds prepared); 120 = Planned (grounds not prepared, opening date undefined). The decoded text is in `CampStatID_L2_label`. |
| Date_Opened_OLD | int32 | Coded value. The source geodatabase domain gives: 1 = Before 2009; 2 = Before 30 March 2011; 3 = Before 15 April 2011; 4 = Between 30 March - 15 April 2011; 5 = Between 15 April -28 July 2011; 6 = Between 28 July / 18 Aug 2011; 7 = Between 28 July - 21 August 2011; 8 = Between 18 -21 August 2011; 9 = Before 31 October 2010; 10 = Between 21 August - 4 Sept. 2011; 20 = Before 1 April 2011; 21 = Between 1 April - 12 September 2011; 22 = Between 21 August - 18 October 2011; 23 = Between 12 Sept. -18 October 2011; 30 = Between 21 August - 12 September 2011; 40 = Between 12 September - 18 October 2011; 41 = Between 18 October 2011 - 16 January 2012; 42 = Between 18 October 2011 - 2 May 2012; 43 = Between 18 October 2011 - 10 May 2012; 44 = Between 14 September 2011 - 10 May 2012. The decoded text is in `Date_Opened_OLD_label`. |
| Date_Closed_OLD | int32 | Coded value. The source geodatabase domain gives: 1 = Before 2009; 2 = Before 30 March 2011; 3 = Before 15 April 2011; 4 = Between 30 March - 15 April 2011; 5 = Between 15 April -28 July 2011; 6 = Between 28 July / 18 Aug 2011; 7 = Between 28 July - 21 August 2011; 8 = Between 18 -21 August 2011; 9 = Before 31 October 2010; 10 = Between 21 August - 4 Sept. 2011; 20 = Before 1 April 2011; 21 = Between 1 April - 12 September 2011; 22 = Between 21 August - 18 October 2011; 23 = Between 12 Sept. -18 October 2011; 30 = Between 21 August - 12 September 2011; 40 = Between 12 September - 18 October 2011; 41 = Between 18 October 2011 - 16 January 2012; 42 = Between 18 October 2011 - 2 May 2012; 43 = Between 18 October 2011 - 10 May 2012; 44 = Between 14 September 2011 - 10 May 2012. The decoded text is in `Date_Closed_OLD_label`. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| CampStatID_L2_label | string | `CampStatID_L2` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| CampStatusID_label | string | `CampStatusID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| CampType_label | string | `CampType` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Confidence_ID_label | string | `Confidence_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Date_Closed_OLD_label | string | `Date_Closed_OLD` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
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
| Date_Opene | int32 |  |
| ShelterCou | int32 |  |
| ShelterEst | int32 |  |
| Formaltent | string |  |
| CampStatID | string |  |
| Date_Ope_1 | string |  |
| Site_ID_txt | string |  |
| SensorID_v2_txt | string |  |
| Confidence_ID_txt | string |  |
| Field_Validation_txt | string |  |
| Camp_StatusID_txt | string |  |
| StaffID_txt | string |  |
| Moga_District_txt | string |  |
| Date_Moga_txt | string |  |
| Camp_statusID_L2_txt | string |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20130710som-shelter-areas-cc_by_nc_sa_3_0.parquet | 735.4 KB | 1220187882a3... |
| ./ce20130710som-shelter-areas-cc_by_nc_sa_3_0.pmtiles | 3.2 MB | 12207c92542d... |
| ./styles/default.json | 961 B | 122096495f61... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20130710som-shelter-areas-cc_by_nc_sa_3_0.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-6-reduction-of-somali-idp-shelter-concentrations-in-mogadishu-som-january-02-2014](https://data.humdata.org/dataset/geodata-of-6-reduction-of-somali-idp-shelter-concentrations-in-mogadishu-som-january-02-2014)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Baidoa_Camp_Extent_20130821`, `Baidoa_Camp_Extent_20140208`, `Baidoa_Camp_Extent_20141002`, `Bariga_Bososo_Camp_Extent_20141020`, `Camp_Extent_20110818`, `Camp_Extent_20110821`, `Camp_Extent_20110904`, `Camp_Extent_20111018`, `Camp_Extent_20120116`, `Camp_Extent_20120123`, `Camp_Extent_20120502`, `Camp_Extent_20120502_update`, `Camp_Extent_20120515`, `Camp_Extent_20130603`, `Camp_Extent_20131124`, `Doolow_Camp_Extent`, `Galkayo_Camp_Extent`, `Galkayo_Camp_Extent_20140420`, `Hargeisa_Camp_Extent_20141102`, `Kismayo_Camp_Extent_20110904`, `Kismayo_Camp_Extent_20120116`, `Kismayo_Camp_Extent_20120510`, `Kismayo_Camp_Extent_20120510_atributes`, `Kismayo_Camp_Extent_20121209`, `Kismayo_Camp_Extent_20130811`, `Kismayo_Camp_Extent_20140305`, `Kismayo_Camp_Extent_20140503`, `Luuq_Camp_Extent_20121219`, `Luuq_Camp_Extent_20140607`, `Mogadishu_Camp_Extent_20131125`.

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

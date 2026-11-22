# Shelter areas: Complex emergency, Syrian Arab Republic, 4 June 2013 (CE20130604SYR)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20130604syr/ce20130604syr-shelter-areas-cc_by_nc_sa_3_0/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Shelter areas for Complex emergency, Syrian Arab Republic, 4 June 2013 (CE20130604SYR): 307 features merged from 15 source layers. Polygon layers with shelter or camp columns, or whose names mention camps, shelters, IDPs, or settlements. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of Bab Al Salame IDP Camp, A'Zaz District, Aleppo Governorate, Syria](https://data.humdata.org/dataset/geodata-of-bab-al-salame-idp-camp-azaz-district-aleppo-governorate-syria-june-12-2015)
- [Geodata of Domiz Refugee Camp,  Duhok Governorate, Iraq](https://data.humdata.org/dataset/geodata-of-domiz-refugee-camp-duhok-governorate-iraq-january-10-2014)
- [Geodata of Oncunipar Refugee Camp, Merkez District, Kilis Province, Turkey](https://data.humdata.org/dataset/geodata-of-oncunipar-refugee-camp-merkez-district-kilis-province-turkey-june-16-2015)
- [Geodata of Sujjo IDP Camp, A'Zaz District, Aleppo Governorate, Syria](https://data.humdata.org/dataset/geodata-of-sujjo-idp-camp-azaz-district-aleppo-governorate-syria-june-19-2015)
- [Geodata of UPDATE: AL ZAATARI REFUGEE CAMP, MAFRAQ GOVERNORATE, JORDAN](https://data.humdata.org/dataset/geodata-of-al-zaatari-refugee-camp-mafraq-governorate-jordan-july-21-2014)
- [Geodata of UPDATE: AL Zaatari Refugee camp, Mafraq Governorate, Jordan](https://data.humdata.org/dataset/geodata-of-al-zaatari-refugee-camp-mafraq-governorate-jordan-november-19-2014)
- [Geodata of Update 2: Al Azraq Refugee Camp,  Az Zarqa Governorate, Jordan](https://data.humdata.org/dataset/geodata-of-2-al-azraq-refugee-camp-az-zarqa-governorate-jordan-january-17-2014)
- [Geodata of Update: Al Azraq Refugee Camp,  Az Zarqa Governorate, Jordan](https://data.humdata.org/dataset/geodata-of-al-azraq-refugee-camp-az-zarqa-governorate-jordan-may-02-2014)
- [Geodata of Update: Al Azraq Refugee Camp, Az Zarqa Governorate, Jordan](https://data.humdata.org/dataset/geodata-of-al-azraq-refugee-camp-az-zarqa-governorate-jordan-november-03-2015)
- [Geodata of Update: Al Azraq Refugee Camp, Az Zarqa Governorate, Jordan](https://data.humdata.org/dataset/geodata-of-al-azraq-refugee-camp-az-zarqa-governorate-jordan-november-28-2014)
- [Geodata of Update: Al Zaatari Refugee Camp, Mafraq Governorate, Jordan](https://data.humdata.org/dataset/geodata-of-al-zaatari-refugee-camp-mafraq-governorate-jordan-august-17-2016)
- [Geodata of Update: Al Zaatari Refugee Camp, Mafraq Governorate, Jordan](https://data.humdata.org/dataset/geodata-of-al-zaatari-refugee-camp-mafraq-governorate-jordan-december-08-2015)
- and 3 more; the event's [catalog page](../catalog.json) lists them all.

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [36.31172729200006, 31.887434085000052, 42.89257999100005, 36.787972281000066]

## Temporal Coverage

- **Start**: 2014-01-10T00:00:00Z
- **End**: 2016-08-17T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Site_ID | int16 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Site_ID_label`, which is decoded per source file. |
| Sensor_ID | int32 | Coded value. The 3 source files of this collection use 3 different domains for it, so read `Sensor_ID_label`, which is decoded per source file. |
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
| StaffID | int32 | Coded value. The 4 source files of this collection use 4 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| CampType | int32 | Coded value. The source geodatabase domain gives: 1 = Refugee Camp; 2 = IDP Camp. The decoded text is in `CampType_label`. |
| City_District | string |  |
| Date_Opened | int32 |  |
| ShelterCount | int32 |  |
| ShelterEstimate | int32 |  |
| FormaltentID | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Yes; 2 = No. The decoded text is in `FormaltentID_label`. |
| CampStatID_L2 | int32 | Coded value. The source geodatabase domain gives: 10 = Open - New; 20 = Open - Reopened; 30 = Open - Expanded; 40 = Open - Contracted; 50 = Open - No Change; 60 = Open - Unknown (clouded / no coverage); 70 = Closed - New (no further indication of resident status); 80 = Closed - Relocated / Aggregated to adjacent camp site; 90 = Closed - Absorbed (site absorbed by other camp expansion); 100 = Closed - Unchanged; 110 = Planned (opening within next days, grounds prepared); 120 = Planned (grounds not prepared, opening date undefined). The decoded text is in `CampStatID_L2_label`. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| CampStatID_L2_label | string | `CampStatID_L2` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| CampStatusID_label | string | `CampStatusID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| CampType_label | string | `CampType` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Confidence_ID_label | string | `Confidence_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Field_Validation_label | string | `Field_Validation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| FormaltentID_label | string | `FormaltentID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Sensor_ID_label | string | `Sensor_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Site_ID_label | string | `Site_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| Date_Opened_OLD | int32 | Coded value. The source geodatabase domain gives: 1 = Before 2009; 2 = Before 30 March 2011; 3 = Before 15 April 2011; 4 = Between 30 March - 15 April 2011; 5 = Between 15 April -28 July 2011; 6 = Between 28 July / 18 Aug 2011; 7 = Between 28 July - 21 August 2011; 8 = Between 18 -21 August 2011; 9 = Before 31 October 2010; 10 = Between 21 August - 4 Sept. 2011; 20 = Before 1 April 2011; 21 = Between 1 April - 12 September 2011; 22 = Between 21 August - 18 October 2011; 23 = Between 12 Sept. -18 October 2011; 30 = Between 21 August - 12 September 2011; 40 = Between 12 September - 18 October 2011; 41 = Between 18 October 2011 - 16 January 2012; 42 = Between 18 October 2011 - 2 May 2012; 43 = Between 18 October 2011 - 10 May 2012; 44 = Between 14 September 2011 - 10 May 2012. The decoded text is in `Date_Opened_OLD_label`. |
| Date_Opened_OLD_label | string | `Date_Opened_OLD` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20130604syr-shelter-areas-cc_by_nc_sa_3_0.parquet | 44.7 KB | 12203acf1a07... |
| ./ce20130604syr-shelter-areas-cc_by_nc_sa_3_0.pmtiles | 257.9 KB | 1220712d64ee... |
| ./styles/default.json | 923 B | 12205c43013e... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20130604syr-shelter-areas-cc_by_nc_sa_3_0.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-2-al-azraq-refugee-camp-az-zarqa-governorate-jordan-january-17-2014](https://data.humdata.org/dataset/geodata-of-2-al-azraq-refugee-camp-az-zarqa-governorate-jordan-january-17-2014)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Al_Zaatari_Camp_Extent`, `Azraq_Camp_Extent`, `BabAlSalame_Extent_20150605`, `Domiz_Camp_Extent`, `Oncunipar_Extent_20150605`, `Sujjo_Extent_20150605`.

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

# Shelters: Complex emergency, Iraq, 13 June 2014 (CE20140613IRQ)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20140613irq/ce20140613irq-shelters-cc_by_sa/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Shelters for Complex emergency, Iraq, 13 June 2014 (CE20140613IRQ): 9,915 features merged from 7 source layers. Point layers with shelter or camp columns, or whose names mention camps, shelters, IDPs, or settlements. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Fires at the Al Qayyarah oil field, Nineveh Governorate, between 18 July 2016 and 24 January 2017](https://data.humdata.org/dataset/fires-at-the-al-qayyarah-oil-field-nineveh-governorate-between-18-july-2016-and-24-january-2017)
- [Fires at the Al Qayyarah oil field, Nineveh Governorate, between 18 July 2016 and 7 January 2017](https://data.humdata.org/dataset/fires-at-the-al-qayyarah-oil-field-nineveh-governorate-between-18-july-2016-and-7-january-2017)
- [Iraq - Environmental damage in Al Qayyarah](https://data.humdata.org/dataset/environmental-damage-in-al-qayyarah-iraq)
- [Iraq - Fires at the Al Qayyarah oil field, Nineveh Governorate](https://data.humdata.org/dataset/fires-at-the-al-qayyarah-oil-field-nineveh-governorate-between-18-july-2016-and-13-march-2017)
- [Iraq - Gawilan IDP Settlement, Al - Hamdaniya, Ninawa Province](https://data.humdata.org/dataset/gawilan-idp-settlement-al-hamdaniya-ninawa-province-iraq)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![climate hazards](https://img.shields.io/badge/climate_hazards-blue) ![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [42.02000000029983, 34.150000000199896, 44.960000000000036, 36.93000000039973]

## Temporal Coverage

- **Start**: 2016-07-18T00:00:00Z
- **End**: 2017-03-13T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID_1 | int64 |  |
| FID_1 | int32 |  |
| PCode | string |  |
| PNameEn | string |  |
| PNameAr | string |  |
| Longitude | double |  |
| Latitude | double |  |
| PCodeAlt1 | double |  |
| PNameAlt1 | string |  |
| A1Code | string |  |
| A1NameEn | string |  |
| A2Code | string |  |
| A2NameEn | string |  |
| OBJECTID | int64 |  |
| Id | int32 |  |
| SmokeFreqD | int32 |  |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| Shape_Leng | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Structure_material | string |  |
| Sensor_ID | string |  |
| Sensor_date | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence_ID | string |  |
| Field_Validation | string |  |
| Camp_SatusID | string |  |
| CampName | string |  |
| StaffID | string |  |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| CampType | string |  |
| CampTrend | string |  |
| Shelter_Status | string |  |
| ShelterClose_Date | string |  |
| Structure_Type | string |  |
| City_District | string |  |
| SectorID | string |  |
| GlobalID | string | ArcGIS global identifier of the feature. |
| Note | string | Free-text notes by the analyst. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20140613irq-shelters-cc_by_sa.parquet | 422.1 KB | 122089274cb4... |
| ./ce20140613irq-shelters-cc_by_sa.pmtiles | 2.9 MB | 1220cc32da76... |
| ./styles/default.json | 908 B | 1220837a00f8... |
| ./ce20140613irq-shelters-cc_by_sa.thumb.jpg | 32.0 KB | 122024f556b9... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20140613irq-shelters-cc_by_sa.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/environmental-damage-in-al-qayyarah-iraq](https://data.humdata.org/dataset/environmental-damage-in-al-qayyarah-iraq)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Affected_settlements_20160718_20161025`, `Affected_settlements_20160718_20161125`, `Affected_settlements_20160718_20161214`, `Affected_settlements_20160718_20170107`, `Affected_settlements_20160718_20170124`, `Affected_settlements_20160718_20170313`, `IDP_GawilanCamp_Structures_28June2016`.

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

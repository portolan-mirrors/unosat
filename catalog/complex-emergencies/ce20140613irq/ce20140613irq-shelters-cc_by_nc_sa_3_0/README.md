# Shelters: Complex emergency, Iraq, 13 June 2014 (CE20140613IRQ)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20140613irq/ce20140613irq-shelters-cc_by_nc_sa_3_0/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Shelters for Complex emergency, Iraq, 13 June 2014 (CE20140613IRQ): 3,193 features merged from 1 source layer. Point layers with shelter or camp columns, or whose names mention camps, shelters, IDPs, or settlements. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of Gawilan IDP Settlement, Al - Hamdaniya, Ninawa Province, Iraq](https://data.humdata.org/dataset/geodata-of-gawilan-idp-settlement-al-hamdaniya-ninawa-province-iraq-august-17-2016)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [43.59610452800007, 36.331382586000075, 43.62176583000007, 36.34667103700008]

## Temporal Coverage

- **Start**: 2016-08-17T00:00:00Z
- **End**: 2016-08-17T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
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
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20140613irq-shelters-cc_by_nc_sa_3_0.parquet | 194.0 KB | 1220bf5684e4... |
| ./ce20140613irq-shelters-cc_by_nc_sa_3_0.pmtiles | 237.9 KB | 122093a5464e... |
| ./styles/default.json | 915 B | 12203b30d00d... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20140613irq-shelters-cc_by_nc_sa_3_0.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-gawilan-idp-settlement-al-hamdaniya-ninawa-province-iraq-august-17-2016](https://data.humdata.org/dataset/geodata-of-gawilan-idp-settlement-al-hamdaniya-ninawa-province-iraq-august-17-2016)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `IDP_GawilanCamp_Structures_28June2016`.

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

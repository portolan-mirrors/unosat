# Shelter areas: Complex emergency, South Sudan, 18 December 2013 (CE20131218SSD)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20131218ssd/ce20131218ssd-shelter-areas-cc_by_nc_sa_3_0-epsg_3857/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Shelter areas for Complex emergency, South Sudan, 18 December 2013 (CE20131218SSD): 3,897 features merged from 1 source layer. Polygon layers with shelter or camp columns, or whose names mention camps, shelters, IDPs, or settlements. The `source_layer` and `source_file` columns name the layer and file each row came from. The geometry is in EPSG:3857, the CRS of the source layers; the PMTiles copy is in Web Mercator.

From these HDX datasets:

- [Geodata of Rapid Satellite Imagery Assessment and IDP Shelter Analysis - South Sudan](https://data.humdata.org/dataset/geodata-of-rapid-satellite-imagery-assessment-and-idp-shelter-analysis-south-december-08-2015)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [29.463157878531927, 7.291856964544586, 30.488385069086895, 8.908923799956392]

## Temporal Coverage

- **Start**: 2015-12-08T00:00:00Z
- **End**: 2015-12-08T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| PageName | string |  |
| PageNumber | int32 |  |
| SensorID | int16 | Coded value. The source geodatabase domain gives: 0 = Geoeye-1; 1 = Worldview-1; 2 = Worldview-2; 3 = Worldview-3; 4 = QuickBird. The decoded text is in `SensorID_label`. |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| Analyzed | int16 | Coded value. The source geodatabase domain gives: 0 = No Analyzed; 1 = Analyzed. The decoded text is in `Analyzed_label`. |
| Cloud | int16 | Coded value. The source geodatabase domain gives: 0 = No clouds; 1 = Clouds > 50%. The decoded text is in `Cloud_label`. |
| Destroyed | int16 | Coded value. The source geodatabase domain gives: 0 = No Destruction; 1 = Medium Destruction; 2 = Devastation. The decoded text is in `Destroyed_label`. |
| Looting | int16 | Coded value. The source geodatabase domain gives: 0 = No looting; 1 = Visible Looting. The decoded text is in `Looting_label`. |
| IDPs | int16 | Coded value. The source geodatabase domain gives: 0 = No IDPs; 1 = Visible IDPs. The decoded text is in `IDPs_label`. |
| Cows | int16 | Coded value. The source geodatabase domain gives: 0 = No cows; 1 = Visible cows. The decoded text is in `Cows_label`. |
| Shape_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Shape_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Analyzed_label | string | `Analyzed` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Cloud_label | string | `Cloud` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Cows_label | string | `Cows` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Destroyed_label | string | `Destroyed` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| IDPs_label | string | `IDPs` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Looting_label | string | `Looting` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20131218ssd-shelter-areas-cc_by_nc_sa_3_0-epsg_3857.parquet | 105.2 KB | 12207834982b... |
| ./ce20131218ssd-shelter-areas-cc_by_nc_sa_3_0-epsg_3857.pmtiles | 5.8 MB | 1220af882840... |
| ./styles/default.json | 684 B | 12201f76302d... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20131218ssd-shelter-areas-cc_by_nc_sa_3_0-epsg_3857.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-rapid-satellite-imagery-assessment-and-idp-shelter-analysis-south-december-08-2015](https://data.humdata.org/dataset/geodata-of-rapid-satellite-imagery-assessment-and-idp-shelter-analysis-south-december-08-2015)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `UNOSAT_Rapid_Assessment_Results`.

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

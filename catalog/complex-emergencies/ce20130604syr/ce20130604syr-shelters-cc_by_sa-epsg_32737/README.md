# Shelters: Complex emergency, Syrian Arab Republic, 4 June 2013 (CE20130604SYR)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20130604syr/ce20130604syr-shelters-cc_by_sa-epsg_32737/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Shelters for Complex emergency, Syrian Arab Republic, 4 June 2013 (CE20130604SYR): 11,702 features merged from 1 source layer. Point layers with shelter or camp columns, or whose names mention camps, shelters, IDPs, or settlements. The `source_layer` and `source_file` columns name the layer and file each row came from. The geometry is in EPSG:32737, the CRS of the source layers; the PMTiles copy is in Web Mercator.

From these HDX datasets:

- [Shelter density map at Rukban border crossing](https://data.humdata.org/dataset/shelter-density-map-at-rukban-border-crossing-2824)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [38.482998870965616, 33.30153541005107, 38.68408444291797, 33.431131616353404]

## Temporal Coverage

- **Start**: 2018-07-13T00:00:00Z
- **End**: 2018-07-13T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| Site_ID | string |  |
| Sensor_ID | string |  |
| Sensor_Dat | date32[day] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence | string |  |
| Field_Vali | string |  |
| CampStatus | string |  |
| CampName | string |  |
| Notes | string | Free-text notes by the analyst. |
| StaffID | string |  |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| CampType | string |  |
| CampTrend | string |  |
| Shelter_St | string |  |
| ShelterClo | date32[day] |  |
| Structure_ | string |  |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20130604syr-shelters-cc_by_sa-epsg_32737.parquet | 363.8 KB | 122077ba5b41... |
| ./ce20130604syr-shelters-cc_by_sa-epsg_32737.pmtiles | 172.8 KB | 12209797d7b4... |
| ./styles/default.json | 699 B | 12204068af60... |
| ./ce20130604syr-shelters-cc_by_sa-epsg_32737.thumb.jpg | 22.8 KB | 1220b68f464a... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20130604syr-shelters-cc_by_sa-epsg_32737.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/shelter-density-map-at-rukban-border-crossing-2824](https://data.humdata.org/dataset/shelter-density-map-at-rukban-border-crossing-2824)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Rukban_IDPs_20180623_WGS`.

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

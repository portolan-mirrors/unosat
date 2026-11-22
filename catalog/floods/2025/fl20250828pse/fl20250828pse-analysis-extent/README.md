# Analysis extent: Flood, State of Palestine, 28 August 2025 (FL20250828PSE)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2025/fl20250828pse/fl20250828pse-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Analysis extent for Flood, State of Palestine, 28 August 2025 (FL20250828PSE): 2 features merged from 2 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from. The geometry is in EPSG:32636, the CRS of the source layers; the PMTiles copy is in Web Mercator.

From these HDX datasets:

- [Sea Surge risk & flood impact assessment in the Coastal Area of Gaza city (Occupied Palestinian Territory) as of 29 August 2025](https://data.humdata.org/dataset/sea-surge-risk-flood-impact-assessment-in-the-coastal-area-of-gaza-city-occupied-palestini)
- [Sea Surge risk & flood impact assessment in the Coastal Area of Southern Gaza Strip (Occupied Palestinian Territory) as of 29 August 2025](https://data.humdata.org/dataset/sea-surge-risk-flood-impact-assessment-in-the-coastal-area-of-southern-gaza-strip-occupied)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![crisis-opt-israel-hostilities](https://img.shields.io/badge/crisis--opt--israel--hostilities-blue) ![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [34.21494905972737, 31.322914587578236, 34.496598912385615, 31.60005822575948]

## Temporal Coverage

- **Start**: 2025-09-09T00:00:00Z
- **End**: 2025-09-10T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Shape_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Shape_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20250828pse-analysis-extent.parquet | 11.6 KB | 1220875e6416... |
| ./fl20250828pse-analysis-extent.pmtiles | 26.9 KB | 1220434e496e... |
| ./styles/default.json | 671 B | 1220c78f530d... |
| ./fl20250828pse-analysis-extent.thumb.jpg | 9.4 KB | 1220707367fa... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20250828pse-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/sea-surge-risk-flood-impact-assessment-in-the-coastal-area-of-gaza-city-occupied-palestini](https://data.humdata.org/dataset/sea-surge-risk-flood-impact-assessment-in-the-coastal-area-of-gaza-city-occupied-palestini)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Gaza_IDP_AnalysisExtent_20250829`.

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

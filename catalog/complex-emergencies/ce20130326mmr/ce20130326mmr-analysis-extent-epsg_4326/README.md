# Analysis extent: Complex emergency, Myanmar, 26 March 2013 (CE20130326MMR)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20130326mmr/ce20130326mmr-analysis-extent-epsg_4326/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Analysis extent for Complex emergency, Myanmar, 26 March 2013 (CE20130326MMR): 5 features merged from 5 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Destroyed areas in Buthidaung, Maungdaw, and Rathedaung Townships of Rakhine State in Myanmar](https://data.humdata.org/dataset/destroyed-areas-in-buthidaung-maungdaw-and-rathedaung-townships-of-rakhine-state-in-myanmar-2727)
- [Destroyed buildings in Maungdaw and Buthindaung townships, Maungdaw District, Myanmar](https://data.humdata.org/dataset/destroyed-buildings-in-maungdaw-and-buthindaung-townships-maungdaw-district-myanmar)
- [Fire Detections in Buthidaung, Maungdaw, and Rathedaung Townships of Rakhine State in Myanmar](https://data.humdata.org/dataset/fire-detections-in-buthidaung-maungdaw-and-rathedaung-townships-of-rakhine-state-in-myanmar-2746)
- [Update: Destroyed buildings in Maungdaw and Buthindaung townships, Maungdaw District, Myanmar](https://data.humdata.org/dataset/destroyed-buildings-in-maungdaw-and-buthindaung-townships-maungdaw-district-myanmar-2697)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [92.16648645700008, 20.260321687000044, 92.87008246700003, 21.42269275600006]

## Temporal Coverage

- **Start**: 2017-09-27T00:00:00Z
- **End**: 2017-11-30T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Id | int32 |  |
| Area_Km | float |  |
| Shape_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Shape_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| Name | string |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20130326mmr-analysis-extent-epsg_4326.parquet | 5.4 KB | 12204a404078... |
| ./ce20130326mmr-analysis-extent-epsg_4326.pmtiles | 100.9 KB | 122058fbb924... |
| ./styles/default.json | 681 B | 1220415fc25d... |
| ./ce20130326mmr-analysis-extent-epsg_4326.thumb.jpg | 8.9 KB | 12201b91458d... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20130326mmr-analysis-extent-epsg_4326.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/destroyed-areas-in-buthidaung-maungdaw-and-rathedaung-townships-of-rakhine-state-in-myanmar-2727](https://data.humdata.org/dataset/destroyed-areas-in-buthidaung-maungdaw-and-rathedaung-townships-of-rakhine-state-in-myanmar-2727)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Analysis_extent_Maungdaw_20170925`, `Analysis_extent_Maungdaw_20171001`, `Analysis_extent_Maungdaw_20171011`.

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

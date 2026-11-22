# Water extent: Flood, Bolivia (Plurinational State of), 9 February 2018 (FL20180209BOL)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2018/fl20180209bol/fl20180209bol-water-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Water extent for Flood, Bolivia (Plurinational State of), 9 February 2018 (FL20180209BOL): 22,499 features merged from 2 source layers. Polygon layers with a water class column (such as `Water_Class`), or whose names mention flood, water, or inundation: satellite-detected water. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Satellite detected waters over Cochabamba department, Bolivia](https://data.humdata.org/dataset/satellite-detected-waters-over-cochabamba-department-bolivia)
- [Satellite detected waters over El Beni department, Bolivia](https://data.humdata.org/dataset/satellite-detected-waters-over-el-beni-department-bolivia)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [-66.44421478299995, -17.99460683199993, -64.63329986999992, -14.503411782999933]

## Temporal Coverage

- **Start**: 2018-02-13T00:00:00Z
- **End**: 2018-02-14T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| Water_Clas | string |  |
| Sensor_ID | string |  |
| Sensor_Dat | date32[day] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence | string |  |
| Field_Vali | string |  |
| Water_Stat | string |  |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| SenorID_ol | string |  |
| StaffID | string |  |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20180209bol-water-extent.parquet | 6.0 MB | 1220adbc5412... |
| ./fl20180209bol-water-extent.pmtiles | 5.4 MB | 1220e4f23909... |
| ./styles/default.json | 977 B | 12203c3822b2... |
| ./fl20180209bol-water-extent.thumb.jpg | 5.3 KB | 122049e41cb4... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20180209bol-water-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/satellite-detected-waters-over-cochabamba-department-bolivia](https://data.humdata.org/dataset/satellite-detected-waters-over-cochabamba-department-bolivia)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `RS20180209_FloodExtent_Trinidad`, `ST20180210_FloodExtent_Cochabamba`.

## Attribution

UNITAR-UNOSAT

## License

[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

## Contact

Portolan Mirrors <nissim@radiant.earth>

## Known Issues

This is a preliminary assessment and has not yet been validated in the field. It is important to consider the characteristics of the source imagery used in the analyses when interpreting results. For damage assessments it should be noted that only significant damage to the structural integrity of the buildings analyzed can be seen in imagery, while minor damage such as cracks or holes may not be visible at all. For flood extractions using radar data it is important to note that urban areas and highly vegetated areas may mask the flood signature and result in underestimation of flood waters. Users with specific questions or concerns should contact unosat@unitar.org to seek clarification.

---

*Generated by [Portolan](https://github.com/portolan-sdi/portolan-cli) from STAC metadata and .portolan/metadata.yaml*

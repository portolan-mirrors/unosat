# Landslides: Flood, Afghanistan, 30 April 2014 (FL20140430AFG)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2014/fl20140430afg/fl20140430afg-landslides/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Landslides for Flood, Afghanistan, 30 April 2014 (FL20140430AFG): 1 features merged from 1 source layer. Polygon layers whose names mention landslides, mudflows, or debris. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of Estimated Rainfall Accumulation from 30 April to 06 May 2014, Afghanistan](https://data.humdata.org/dataset/geodata-of-estimated-rainfall-accumulation-from-30-april-to-06-may-2014-afgha-may-06-2014)
- [Geodata of Flood Waters Over Khwaja Du Koh, Jawzjan Province, Afghanistan](https://data.humdata.org/dataset/geodata-of-flood-waters-over-khwaja-du-koh-jawzjan-province-afghanistan-may-01-2014)
- [Geodata of Flood Waters Over Khwaja Du Koh, Jawzjan Province, Afghanistan](https://data.humdata.org/dataset/geodata-of-flood-waters-over-khwaja-du-koh-jawzjan-province-afghanistan-may-07-2014)
- [Geodata of Flood Waters Over Kulukh Tapah, Kunduz Province, Afghanistan](https://data.humdata.org/dataset/geodata-of-flood-waters-over-kulukh-tapah-kunduz-province-afghanistan-may-13-2014)
- [Geodata of Flood Waters and Inundation Near Khwaja Du Koh, Jawzjan Province, Afghanistan](https://data.humdata.org/dataset/geodata-of-flood-waters-and-inundation-near-khwaja-du-koh-jawzjan-province-af-may-01-2014)
- [Geodata of Inundation Near Sar-E Pol, Sar-E Pol Province, Afghanistan](https://data.humdata.org/dataset/geodata-of-inundation-near-sar-e-pol-sar-e-pol-province-afghanistan-may-02-2014)
- [Geodata of Inundation Near Sar-E Pol, Sar-E Pol Province, Afghanistan](https://data.humdata.org/dataset/geodata-of-inundation-near-sar-e-pol-sar-e-pol-province-afghanistan-may-07-2014)
- [Geodata of Landslide in Ab Barek, Badakshan Province, Afghanistan](https://data.humdata.org/dataset/geodata-of-landslide-in-ab-barek-badakshan-province-afghanistan-may-04-2014)
- [Geodata of Update: Landslide in Ab Barek, Badakshan Province, Afghanistan](https://data.humdata.org/dataset/geodata-of-landslide-in-ab-barek-badakshan-province-afghanistan-may-08-2014)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [70.35534790300005, 37.00974071500008, 70.36688353000005, 37.018382917000054]

## Temporal Coverage

- **Start**: 2014-05-01T00:00:00Z
- **End**: 2014-05-13T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OID | int64 |  |
| Name | string |  |
| Shape_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Shape_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20140430afg-landslides.parquet | 3.4 KB | 1220762dcafa... |
| ./fl20140430afg-landslides.pmtiles | 18.4 KB | 1220b946298b... |
| ./styles/default.json | 640 B | 1220dd5ca337... |
| ./fl20140430afg-landslides.thumb.jpg | 8.8 KB | 1220a42ca59c... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20140430afg-landslides.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-estimated-rainfall-accumulation-from-30-april-to-06-may-2014-afgha-may-06-2014](https://data.humdata.org/dataset/geodata-of-estimated-rainfall-accumulation-from-30-april-to-06-may-2014-afgha-may-06-2014)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Landslide_20140503_Extent`.

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

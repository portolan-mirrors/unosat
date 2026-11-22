# Landslides: Earthquake, Nepal, 25 April 2015 (EQ20150425NPL)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/earthquakes/2015/eq20150425npl/eq20150425npl-landslides/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Landslides for Earthquake, Nepal, 25 April 2015 (EQ20150425NPL): 51 features merged from 1 source layer. Polygon layers whose names mention landslides, mudflows, or debris. The `source_layer` and `source_file` columns name the layer and file each row came from. The geometry is in EPSG:32645, the CRS of the source layers; the PMTiles copy is in Web Mercator.

From these HDX datasets:

- [Geodata of Damage Assessment of Banepa, Kathmandu Valley, Nepal](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-banepa-kathmandu-valley-nepal-april-30-2015)
- [Geodata of Damage Assessment of Bhaktapur, Kathmandu Valley, Nepal](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-bhaktapur-kathmandu-valley-nepal-april-30-2015)
- [Geodata of Damage Assessment of Daraudi Valley, Western Region, Nepal](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-daraudi-valley-western-region-nepal-may-05-2015)
- [Geodata of Damage Assessment of Hansapur Area, Western Region, Nepal](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-hansapur-area-western-region-nepal-may-05-2015)
- [Geodata of Damage Assessment of Manbu Area, Western Region, Nepal](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-manbu-area-western-region-nepal-may-07-2015)
- [Geodata of Damage Assessment of Muchok Area, Western Region, Nepal](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-muchok-area-western-region-nepal-may-05-2015)
- [Geodata of Damage Assessment of Sankhu, Kathmandu Valley, Nepal](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-sankhu-kathmandu-valley-nepal-april-30-2015)
- [Geodata of Damage Assessment of Tuhure Pasal Area, Western Region, Nepal](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-tuhure-pasal-area-western-region-nepal-may-08-2015)
- [Geodata of Damage Assessment of West Sundar Bazar Area, Western Region, Nepal](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-west-sundar-bazar-area-western-region-nepal-may-08-2015)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![earthquake](https://img.shields.io/badge/earthquake-blue) ![earthquake-tsunami](https://img.shields.io/badge/earthquake--tsunami-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [84.72084505175005, 27.466287987593173, 86.22290888459455, 28.557516156292525]

## Temporal Coverage

- **Start**: 2015-04-30T00:00:00Z
- **End**: 2015-05-08T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Damage | string |  |
| Damage_Int | string |  |
| Production | timestamp[us, tz=UTC] |  |
| Remote_Sen | timestamp[us, tz=UTC] |  |
| Shape_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Shape_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./eq20150425npl-landslides.parquet | 42.2 KB | 12209d030e76... |
| ./eq20150425npl-landslides.pmtiles | 58.5 KB | 122087103822... |
| ./styles/default.json | 640 B | 122078209e9f... |
| ./eq20150425npl-landslides.thumb.jpg | 4.8 KB | 122085731f09... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./eq20150425npl-landslides.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-damage-assessment-of-banepa-kathmandu-valley-nepal-april-30-2015](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-banepa-kathmandu-valley-nepal-april-30-2015)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `NGA_Landslides_Nepal_May_7th_2015`.

## Attribution

UNITAR-UNOSAT

## License

[CC-BY-NC-SA-3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/)

## Contact

Portolan Mirrors <nissim@radiant.earth>

## Known Issues

When the layers were merged, M values were dropped from 1 layer(s) that mix Z and ZM geometry: NGA_Landslides_Nepal_May_7th_2015. This is a preliminary assessment and has not yet been validated in the field. It is important to consider the characteristics of the source imagery used in the analyses when interpreting results. For damage assessments it should be noted that only significant damage to the structural integrity of the buildings analyzed can be seen in imagery, while minor damage such as cracks or holes may not be visible at all. For flood extractions using radar data it is important to note that urban areas and highly vegetated areas may mask the flood signature and result in underestimation of flood waters. Users with specific questions or concerns should contact unosat@unitar.org to seek clarification.

---

*Generated by [Portolan](https://github.com/portolan-sdi/portolan-cli) from STAC metadata and .portolan/metadata.yaml*

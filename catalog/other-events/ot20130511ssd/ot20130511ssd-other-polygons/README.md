# Other polygons: Event, South Sudan, 11 May 2013 (OT20130511SSD)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/other-events/ot20130511ssd/ot20130511ssd-other-polygons/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Other polygons for Event, South Sudan, 11 May 2013 (OT20130511SSD): 2 features merged from 1 source layer. Polygons layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of Ajuong Thok Refugee Camp, Pariang County, Unity State, South Sudan](https://data.humdata.org/dataset/geodata-of-ajuong-thok-refugee-camp-pariang-county-unity-state-south-sudan-january-13-2014)
- [Geodata of Batil Refugee Camp, Maban County, Upper Nile State, South Sudan](https://data.humdata.org/dataset/geodata-of-batil-refugee-camp-maban-county-upper-nile-state-south-sudan-january-13-2014)
- [Geodata of Doro Refugee Camp, Maban County, Upper Nile State, South Sudan](https://data.humdata.org/dataset/geodata-of-doro-refugee-camp-maban-county-upper-nile-state-south-sudan-january-15-2014)
- [Geodata of Gendrasa Refugee Camp, Maban County, Upper Nile State, South Sudan](https://data.humdata.org/dataset/geodata-of-gendrasa-refugee-camp-maban-county-upper-nile-state-south-sudan-january-13-2014)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![event](https://img.shields.io/badge/event-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [30.26650420900006, 9.945435511000028, 33.752859467000064, 9.983551810000051]

## Temporal Coverage

- **Start**: 2014-01-13T00:00:00Z
- **End**: 2014-01-15T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Name | string |  |
| Ha | double |  |
| Shape_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Shape_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ot20130511ssd-other-polygons.parquet | 4.6 KB | 1220d71d564e... |
| ./ot20130511ssd-other-polygons.pmtiles | 21.4 KB | 1220dd8640e3... |
| ./styles/default.json | 664 B | 122042005197... |
| ./ot20130511ssd-other-polygons.thumb.jpg | 2.3 KB | 122078266bd5... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ot20130511ssd-other-polygons.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-ajuong-thok-refugee-camp-pariang-county-unity-state-south-sudan-january-13-2014](https://data.humdata.org/dataset/geodata-of-ajuong-thok-refugee-camp-pariang-county-unity-state-south-sudan-january-13-2014)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Runway`.

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

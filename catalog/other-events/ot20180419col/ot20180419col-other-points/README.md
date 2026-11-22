# Other points: Event, Colombia, 19 April 2018 (OT20180419COL)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/other-events/ot20180419col/ot20180419col-other-points/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Other points for Event, Colombia, 19 April 2018 (OT20180419COL): 27 features merged from 2 source layers. Points layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Análisis en terreno: Visitas de control y reconocimiento a lo largo de la quebrada Lizama y Caño Muerto, Barrancabermeja](https://data.humdata.org/dataset/analisis-en-terreno-visitas-de-control-y-reconocimiento-a-lo-largo-de-la-quebrada-lizama-y-cano-)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![event](https://img.shields.io/badge/event-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [-73.64491660443117, 7.129944209181958, -73.54345579673985, 7.210369982304179]

## Temporal Coverage

- **Start**: 2018-04-20T00:00:00Z
- **End**: 2018-04-20T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| FID_1 | int64 |  |
| FID_1_1 | int64 |  |
| Path | string |  |
| Name | string |  |
| DateTime | string |  |
| Direction | double |  |
| Angle | string |  |
| Caption | string |  |
| Number | int64 |  |
| Path_1 | string |  |
| FID_2 | int64 |  |
| title | string |  |
| photo | string |  |
| descriptio | string |  |
| recDate | string |  |
| pubDate | string |  |
| author | string |  |
| caption_1 | string |  |
| notes | string | Free-text notes by the analyst. |
| priority | int64 |  |
| category | string |  |
| mission | string |  |
| lat | double |  |
| lon | double |  |
| directio_1 | double |  |
| asignlink | string |  |
| viewlink | string |  |
| Distance | double |  |
| FID_3 | int64 |  |
| caption_2 | string |  |
| recDate_1 | string |  |
| pubDate_1 | string |  |
| author_1 | string |  |
| lat_1 | double |  |
| lon_1 | double |  |
| Distance_1 | double |  |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ot20180419col-other-points.parquet | 20.1 KB | 12205b20f823... |
| ./ot20180419col-other-points.pmtiles | 73.9 KB | 12205a2f78a5... |
| ./styles/default.json | 695 B | 1220e8431060... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ot20180419col-other-points.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/analisis-en-terreno-visitas-de-control-y-reconocimiento-a-lo-largo-de-la-quebrada-lizama-y-cano-](https://data.humdata.org/dataset/analisis-en-terreno-visitas-de-control-y-reconocimiento-a-lo-largo-de-la-quebrada-lizama-y-cano-)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Join_Crowd_ASIGN_Colombia_15abril_text`, `Join_Crowd_ASIGN_Colombia_18abril_text`.

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

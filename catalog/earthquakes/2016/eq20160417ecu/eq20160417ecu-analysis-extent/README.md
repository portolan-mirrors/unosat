# Analysis extent: Earthquake, Ecuador, 17 April 2016 (EQ20160417ECU)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/earthquakes/2016/eq20160417ecu/eq20160417ecu-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Analysis extent for Earthquake, Ecuador, 17 April 2016 (EQ20160417ECU): 54 features merged from 2 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of Damage Assessment of Atacames area, Esmeraldas Province, Ecuador](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-atacames-area-esmeraldas-province-ecuador-april-20-2016)
- [Geodata of Damage Assessment of Bahia de Caraquez, Manabi Province, Ecuador](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-bahia-de-caraquez-manabi-province-ecuador-april-21-2016)
- [Geodata of Damage Assessment of Chone area, Manabi Province, Ecuador](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-chone-area-manabi-province-ecuador-april-25-2016)
- [Geodata of Damage Assessment of Crucita Area, Manabi Province, Ecuador](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-crucita-area-manabi-province-ecuador-april-20-2016)
- [Geodata of Damage Assessment of Muisne, Esmeraldas Province, Ecuador](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-muisne-esmeraldas-province-ecuador-april-22-2016)
- [Geodata of Damage Assessment of Salinas and La Libertad Areas, Santa Elena Province, Ecuador](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-salinas-and-la-libertad-areas-santa-elena-pro-april-20-2016)
- [Geodata of Damage Assessment of San Vicente, Manabi Province, Ecuador](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-san-vicente-manabi-province-ecuador-april-21-2016)
- [Geodata of Damage Density in The City of Jama, Manabi Province, Ecuador](https://data.humdata.org/dataset/geodata-of-damage-density-in-the-city-of-jama-manabi-province-ecuador-may-18-2016)
- [Geodata of Damage assessment of Montecristi, Manabi province, Ecuador](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-montecristi-manabi-province-ecuador-april-27-2016)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![earthquake](https://img.shields.io/badge/earthquake-blue) ![earthquake-tsunami](https://img.shields.io/badge/earthquake--tsunami-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [-80.44384384199992, -0.7148914339999237, -79.7280610059999, 0.9042868480000834]

## Temporal Coverage

- **Start**: 2016-04-20T00:00:00Z
- **End**: 2016-05-18T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Id | int32 |  |
| Shape_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Shape_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./eq20160417ecu-analysis-extent.parquet | 3.5 MB | 1220ab6f04c4... |
| ./eq20160417ecu-analysis-extent.pmtiles | 447.7 KB | 1220f666c702... |
| ./styles/default.json | 671 B | 12201a0a2aba... |
| ./eq20160417ecu-analysis-extent.thumb.jpg | 4.2 KB | 12204447a068... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./eq20160417ecu-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-damage-assessment-of-atacames-area-esmeraldas-province-ecuador-april-20-2016](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-atacames-area-esmeraldas-province-ecuador-april-20-2016)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `PL_20160418_Atacames_CloudMask`, `PL_20160419_SanVicente_CloudMask`.

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

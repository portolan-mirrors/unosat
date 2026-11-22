# Other points: Landslide, Indonesia, 18 November 2025 (LS20251118IDN)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/landslides/ls20251118idn/ls20251118idn-other-points/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Other points for Landslide, Indonesia, 18 November 2025 (LS20251118IDN): 8,529 features merged from 6 source layers. Points layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Landslide impact analysis in Majenang Sub-district, Cilacap District, Jawa Tengah Province, Indonesia as of 18 November 2025](https://data.humdata.org/dataset/landslide-impact-analysis-in-majenang-sub-district-cilacap-district-jawa-tengah-province-i)
- [Landslide impact analysis in Pandanarum Sub-district, Banjarnegara Regency, Jawa Tengah Province, Indonesia as of 18 & 19 November 2025](https://data.humdata.org/dataset/landslide-impact-analysis-in-pandanarum-sub-district-banjarnegara-regency-jawa-tengah-prov)
- [UNOSAT Live web map - Landslides in Central Java, Indonesia](https://data.humdata.org/dataset/unosat-live-web-map-landslides-in-central-java-indonesia)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![geodata](https://img.shields.io/badge/geodata-blue) ![landslide](https://img.shields.io/badge/landslide-blue) ![natural disasters](https://img.shields.io/badge/natural_disasters-blue)

## Spatial Coverage

- **Bounding Box**: [108.72972740009948, -7.297709553253242, 109.61145744970162, -7.258272999998894]

## Temporal Coverage

- **Start**: 2025-11-20T00:00:00Z
- **End**: 2025-11-24T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| osm_id | string |  |
| code | int16 |  |
| fclass | string |  |
| name | string |  |
| type | string |  |
| ORIG_FID | int32 |  |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ls20251118idn-other-points.parquet | 117.2 KB | 1220dc2b0b78... |
| ./ls20251118idn-other-points.pmtiles | 106.9 KB | 122021c91a25... |
| ./styles/default.json | 695 B | 1220ab8042f3... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ls20251118idn-other-points.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/landslide-impact-analysis-in-majenang-sub-district-cilacap-district-jawa-tengah-province-i](https://data.humdata.org/dataset/landslide-impact-analysis-in-majenang-sub-district-cilacap-district-jawa-tengah-province-i)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `DAPoint_Banja`, `DAPoint_Clilacap`.

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

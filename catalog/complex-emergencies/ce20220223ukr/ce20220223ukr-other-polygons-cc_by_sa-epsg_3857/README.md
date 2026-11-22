# Other polygons: Complex emergency, Ukraine, 23 February 2022 (CE20220223UKR)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20220223ukr/ce20220223ukr-other-polygons-cc_by_sa-epsg_3857/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Other polygons for Complex emergency, Ukraine, 23 February 2022 (CE20220223UKR): 2 features merged from 1 source layer. Polygons layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from. The geometry is in EPSG:3857, the CRS of the source layers; the PMTiles copy is in Web Mercator.

From these HDX datasets:

- [Mariupol Updated Building Damage Assessment Overview Map - Livoberezhnyi and Zhovtnevyi Districts](https://data.humdata.org/dataset/mariupol-updated-building-damage-assessment-overview-map-livoberezhnyi-and-zhovtnevyi-dist)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [37.49334158697207, 47.0836587795166, 37.69578700726106, 47.14620558461433]

## Temporal Coverage

- **Start**: 2022-06-15T00:00:00Z
- **End**: 2022-06-15T23:59:59Z

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
| ./ce20220223ukr-other-polygons-cc_by_sa-epsg_3857.parquet | 11.5 KB | 12200d1cd0ee... |
| ./ce20220223ukr-other-polygons-cc_by_sa-epsg_3857.pmtiles | 26.3 KB | 12203c867587... |
| ./styles/default.json | 683 B | 1220089d43b0... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20220223ukr-other-polygons-cc_by_sa-epsg_3857.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/mariupol-updated-building-damage-assessment-overview-map-livoberezhnyi-and-zhovtnevyi-dist](https://data.humdata.org/dataset/mariupol-updated-building-damage-assessment-overview-map-livoberezhnyi-and-zhovtnevyi-dist)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `UNOSAT_Mariupol_Livoberezhyny_AOI_12May2022`.

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

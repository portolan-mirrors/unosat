# Other polygons: Earthquake, Thailand, 28 March 2025 (EQ20250328THA)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/earthquakes/2025/eq20250328tha/eq20250328tha-other-polygons/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Other polygons for Earthquake, Thailand, 28 March 2025 (EQ20250328THA): 315 features merged from 7 source layers. Polygons layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Satellite-detected Damage the UNESCO Tentative List component Chiang Mai as of 29 March 2025](https://data.humdata.org/dataset/damage-the-unesco-tentative-list-component-chiang-mai-as-of-29-march-2025)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![crisis-myanmar-earthquake](https://img.shields.io/badge/crisis--myanmar--earthquake-blue) ![earthquake](https://img.shields.io/badge/earthquake-blue) ![earthquake-tsunami](https://img.shields.io/badge/earthquake--tsunami-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [95.1719889534275, 18.909272022086213, 97.10628481259408, 23.784816122865834]

## Temporal Coverage

- **Start**: 2025-04-17T00:00:00Z
- **End**: 2025-04-17T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| event_type | string |  |
| obj_desc | string |  |
| det_method | string |  |
| notation | string |  |
| dmg_src_id | int32 |  |
| area | double |  |
| Shape_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Shape_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| emsr_id | string |  |
| glide_no | string |  |
| area_id | string |  |
| locality | string |  |
| map_type | string |  |
| obj_type | string |  |
| name | string |  |
| info | string |  |
| simplified | string |  |
| damage_gra | string |  |
| or_src_id | int32 |  |
| cd_value | string |  |
| SRC_DATE | string |  |
| FRAMEWORK | string |  |
| AREA_HA | double | Area in hectares, as UNOSAT computed it. |
| TYPE | string |  |
| SOURCE | string |  |
| PROCESSING | string |  |
| COPYRIGHT | string |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./eq20250328tha-other-polygons.parquet | 785.1 KB | 1220121d4bea... |
| ./eq20250328tha-other-polygons.pmtiles | 387.0 KB | 12208d4cf41d... |
| ./styles/default.json | 664 B | 12206d363317... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./eq20250328tha-other-polygons.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/damage-the-unesco-tentative-list-component-chiang-mai-as-of-29-march-2025](https://data.humdata.org/dataset/damage-the-unesco-tentative-list-component-chiang-mai-as-of-29-march-2025)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `EMSR798_DEL_PRODUCT_observedEventA_MERGED`, `EMSR798_GRA_PRODUCT_areaOfInterestA_MERGED`, `EMSR798_GRA_PRODUCT_facilitiesA_MERGED`, `EMSR798_GRA_PRODUCT_notAnalysedA_MERGED`, `ICube_SERTIT_en_AreaOfInterest_MERGED`, `ICube_SERTIT_en_HydrographyA_MERGED`, `ICube_SERTIT_en_ObservedEventA_MERGED`.

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

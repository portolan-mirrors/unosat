# Other polygons: Complex emergency, Ukraine, 23 February 2022 (CE20220223UKR)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20220223ukr/ce20220223ukr-other-polygons-cc_by_sa-epsg_4326/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Other polygons for Complex emergency, Ukraine, 23 February 2022 (CE20220223UKR): 5 features merged from 2 source layers. Polygons layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Kremenchuk Damage Assessment Overview](https://data.humdata.org/dataset/kremenchuk-damage-assessment-overview)
- [Mariupol Rapid Damage Assessment Overview Map](https://data.humdata.org/dataset/mariupol-rapid-damage-assessment-overview-map)
- [North Kharkiv Rapid Damage Assessment Overview Map](https://data.humdata.org/dataset/north-kharkiv-rapid-damage-assessment-overview-map)
- [Sumy Rapid Damage Assessment Overview Map](https://data.humdata.org/dataset/sumy-rapid-damage-assessment-overview-map)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [33.37343403475296, 47.083658779229324, 37.6957870074645, 50.96376423173393]

## Temporal Coverage

- **Start**: 2022-03-30T00:00:00Z
- **End**: 2023-02-09T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Shape_Leng | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| ADM4_EN | string |  |
| ADM4_UA | string |  |
| ADM4_RU | string |  |
| ADM4_PCODE | string |  |
| ADM4_REF | string |  |
| ADM4ALT1EN | string |  |
| ADM4ALT2EN | string |  |
| ADM4ALT1UA | string |  |
| ADM4ALT2UA | string |  |
| ADM4ALT1RU | string |  |
| ADM4ALT2RU | string |  |
| ADM3_EN | string |  |
| ADM3_UA | string |  |
| ADM3_RU | string |  |
| ADM3_PCODE | string |  |
| ADM2_EN | string |  |
| ADM2_UA | string |  |
| ADM2_RU | string |  |
| ADM2_PCODE | string |  |
| ADM1_EN | string |  |
| ADM1_UA | string |  |
| ADM1_RU | string |  |
| ADM1_PCODE | string |  |
| ADM0_EN | string |  |
| ADM0_UA | string |  |
| ADM0_RU | string |  |
| ADM0_PCODE | string |  |
| date | timestamp[us, tz=UTC] |  |
| validOn | timestamp[us, tz=UTC] |  |
| validTo | timestamp[us, tz=UTC] |  |
| Shape_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Shape_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| Settlement | string |  |
| Dsitrict | string |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20220223ukr-other-polygons-cc_by_sa-epsg_4326.parquet | 60.4 KB | 1220b372f875... |
| ./ce20220223ukr-other-polygons-cc_by_sa-epsg_4326.pmtiles | 107.1 KB | 12207908ffe6... |
| ./styles/default.json | 683 B | 1220741c1d47... |
| ./ce20220223ukr-other-polygons-cc_by_sa-epsg_4326.thumb.jpg | 4.5 KB | 1220768f5b4a... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20220223ukr-other-polygons-cc_by_sa-epsg_4326.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/kremenchuk-damage-assessment-overview](https://data.humdata.org/dataset/kremenchuk-damage-assessment-overview)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Areas_of_Interest`, `Kremenchuk_boundaries`.

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

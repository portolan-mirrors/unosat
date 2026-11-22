# Other points: Complex emergency, Iraq, 13 June 2014 (CE20140613IRQ)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20140613irq/ce20140613irq-other-points-epsg_4326/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Other points for Complex emergency, Iraq, 13 June 2014 (CE20140613IRQ): 69 features merged from 4 source layers. Points layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Fires at the Al Qayyarah oil field, Nineveh Governorate, between 18 July and 14 December, 2016](https://data.humdata.org/dataset/fires-at-the-al-qayyarah-oil-field-nineveh-governorate-between-18-july-and-14-december-2016)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [43.21000000000009, 34.8300000000001, 44.02999999999997, 36.83000000000004]

## Temporal Coverage

- **Start**: 2016-12-21T00:00:00Z
- **End**: 2016-12-21T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| pointid | int32 |  |
| precip_mm | float |  |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| OBJECTID_1 | int64 |  |
| FID_1 | int32 |  |
| PCode | string |  |
| PNameEn | string |  |
| PNameAr | string |  |
| Longitude | double |  |
| Latitude | double |  |
| PCodeAlt1 | double |  |
| PNameAlt1 | string |  |
| A1Code | string |  |
| A1NameEn | string |  |
| A2Code | string |  |
| A2NameEn | string |  |
| Id | int32 |  |
| SmokeFreqDays | int32 |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20140613irq-other-points-epsg_4326.parquet | 9.7 KB | 1220e12cf7f3... |
| ./ce20140613irq-other-points-epsg_4326.pmtiles | 60.9 KB | 12207edf0b58... |
| ./styles/default.json | 705 B | 12200ae03cb7... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20140613irq-other-points-epsg_4326.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/fires-at-the-al-qayyarah-oil-field-nineveh-governorate-between-18-july-and-14-december-2016](https://data.humdata.org/dataset/fires-at-the-al-qayyarah-oil-field-nineveh-governorate-between-18-july-and-14-december-2016)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Most_affected_towns_20160718_20161025`, `Most_affected_towns_20160718_20161125`, `Most_affected_towns_20160718_20161214`, `rain_over_smoke_20160718_20161025`.

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

# Water extent: Flood, Mozambique, 12 January 2015 (FL20150112MOZ)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2015/fl20150112moz/fl20150112moz-water-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Water extent for Flood, Mozambique, 12 January 2015 (FL20150112MOZ): 118,991 features merged from 10 source layers. Polygon layers with a water class column (such as `Water_Class`), or whose names mention flood, water, or inundation: satellite-detected water. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of Flood Water over Namacura and Maganja Da Costa District, Zambezia Province, Mozambique](https://data.humdata.org/dataset/geodata-of-flood-water-over-namacura-and-maganja-da-costa-district-zambezia-p-february-10-2015)
- [Geodata of Flood Waters In Zambezia, Tete and Sofala, Mozambique, and Southern Region, Malawi](https://data.humdata.org/dataset/geodata-of-flood-waters-in-zambezia-tete-and-sofala-mozambique-and-southern-r-february-02-2015)
- [Geodata of Flood Waters In Zambezia, Tete and Sofala, Mozambique, and Southern Region, Malawi](https://data.humdata.org/dataset/geodata-of-flood-waters-in-zambezia-tete-and-sofala-mozambique-and-southern-r-february-04-2015)
- [Geodata of Flood Waters In Zambezia, Tete and Sofala, Mozambique, and Southern Region, Malawi](https://data.humdata.org/dataset/geodata-of-flood-waters-in-zambezia-tete-and-sofala-mozambique-and-southern-r-february-16-2015)
- [Geodata of Flood Waters Over Zambezia Province, Mozambique](https://data.humdata.org/dataset/geodata-of-flood-waters-over-zambezia-province-mozambique-january-19-2015)
- [Geodata of Flood Waters Over Zambezia, Tete and Sofala Provinces, Mozambique](https://data.humdata.org/dataset/geodata-of-flood-waters-over-zambezia-tete-and-sofala-provinces-mozambique-january-21-2015)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [33.503900000000044, -22.201143749999915, 38.70263041000004, -13.798800095999923]

## Temporal Coverage

- **Start**: 2015-01-19T00:00:00Z
- **End**: 2015-02-16T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| Water_Clas | string |  |
| Sensor_ID | string |  |
| Sensor_Dat | date32[day] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence | string |  |
| Field_Vali | string |  |
| Water_Stat | string |  |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| SenorID_ol | string |  |
| StaffID | string |  |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20150112moz-water-extent.parquet | 44.8 MB | 12202fc67e75... |
| ./fl20150112moz-water-extent.pmtiles | 27.3 MB | 122068cf5ee8... |
| ./styles/default.json | 941 B | 122052d2e285... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20150112moz-water-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-flood-water-over-namacura-and-maganja-da-costa-district-zambezia-p-february-10-2015](https://data.humdata.org/dataset/geodata-of-flood-water-over-namacura-and-maganja-da-costa-district-zambezia-p-february-10-2015)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `CM_20150213_Flood`, `LS_20150207_Flood`, `MO_20150210_Flood`, `RS2_0150118_Flood`, `RS2_20150121_Flood`, `RS2_20150130_Flood`, `RS2_20150203_Flood`, `RS2_20150204_Flood`, `S1_20141211_PreFlood`, `S1_20150111_PreFlood`.

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

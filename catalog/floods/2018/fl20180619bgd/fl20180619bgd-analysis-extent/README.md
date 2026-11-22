# Analysis extent: Flood, Bangladesh, 19 June 2018 (FL20180619BGD)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2018/fl20180619bgd/fl20180619bgd-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Analysis extent for Flood, Bangladesh, 19 June 2018 (FL20180619BGD): 2 features merged from 2 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Satellite Detected Waters in NE Bangladesh & NE India](https://data.humdata.org/dataset/satellite-detected-waters-in-ne-bangladesh-ne-india-2821)
- [Satellite Detected Waters in Sylhet Division, Bangladesh](https://data.humdata.org/dataset/satellite-detected-waters-in-sylhet-division-bangladesh-2819)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [90.92964399000005, 23.734730005000074, 93.54610479100006, 25.604868902000078]

## Temporal Coverage

- **Start**: 2018-06-19T00:00:00Z
- **End**: 2018-06-25T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| SensorDate | date32[day] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | string |  |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| StaffID | string |  |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20180619bgd-analysis-extent.parquet | 672.3 KB | 1220471ab600... |
| ./fl20180619bgd-analysis-extent.pmtiles | 365.3 KB | 1220238f2bd8... |
| ./styles/default.json | 671 B | 1220c0947326... |
| ./fl20180619bgd-analysis-extent.thumb.jpg | 11.2 KB | 1220d7bc1676... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20180619bgd-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/satellite-detected-waters-in-ne-bangladesh-ne-india-2821](https://data.humdata.org/dataset/satellite-detected-waters-in-ne-bangladesh-ne-india-2821)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `ST20180615_Assam_Analysis_Extent`, `ST20180615_Sylhet_Analysis_Extent`.

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

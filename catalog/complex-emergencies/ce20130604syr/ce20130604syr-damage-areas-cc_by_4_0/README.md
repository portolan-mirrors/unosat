# Damage areas: Complex emergency, Syrian Arab Republic, 4 June 2013 (CE20130604SYR)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20130604syr/ce20130604syr-damage-areas-cc_by_4_0/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Damage areas for Complex emergency, Syrian Arab Republic, 4 June 2013 (CE20130604SYR): 2,630 features merged from 4 source layers. Polygon layers with a damage class column: damaged areas, zones, or density cells. The `source_layer` and `source_file` columns name the layer and file each row came from. The geometry is in EPSG:32637, the CRS of the source layers; the PMTiles copy is in Web Mercator.

From these HDX datasets:

- [Rapidly assessed damage occurring between 23 February 2018 and 2 March 2018 in Douma, Eastern Ghouta Area, Syria](https://data.humdata.org/dataset/rapidly-assessed-damage-occurring-february-march-douma-eastern-ghouta-area-syria)
- [Rapidly assessed damage occurring between 23 February 2018 and 6 March 2018 in Eastern Ghouta Area, Damascus Governorate](https://data.humdata.org/dataset/rapidly-assessed-damage-occurring-february-march-eastern-ghouta-area-damascus-governorate-2782)
- [Rapidly assessed damage occurring between 3 December 2017 and 23 February 2018 in Eastern Ghouta Area, Syria](https://data.humdata.org/dataset/rapidly-assessed-damage-occurring-december-february-eastern-ghouta-area-syria)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [36.30659189027761, 33.45954825378029, 36.43250474111506, 33.589197124256636]

## Temporal Coverage

- **Start**: 2018-03-01T00:00:00Z
- **End**: 2018-03-08T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| SiteID | string |  |
| SensorDate | date32[day] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | string |  |
| Confidence | string |  |
| Notes | string | Free-text notes by the analyst. |
| Main_Damag | string |  |
| StaffID | string |  |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20130604syr-damage-areas-cc_by_4_0.parquet | 40.2 KB | 1220283e8037... |
| ./ce20130604syr-damage-areas-cc_by_4_0.pmtiles | 246.1 KB | 12201f7b258c... |
| ./styles/default.json | 989 B | 12202ac873e4... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20130604syr-damage-areas-cc_by_4_0.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/rapidly-assessed-damage-occurring-december-february-eastern-ghouta-area-syria](https://data.humdata.org/dataset/rapidly-assessed-damage-occurring-december-february-eastern-ghouta-area-syria)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `RDA_Damascus_20180223`, `RDA_Damascus_20180306`, `RDA_Douma_20180302`.

## Attribution

UNITAR-UNOSAT

## License

[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

## Contact

Portolan Mirrors <nissim@radiant.earth>

## Known Issues

This is a preliminary assessment and has not yet been validated in the field. It is important to consider the characteristics of the source imagery used in the analyses when interpreting results. For damage assessments it should be noted that only significant damage to the structural integrity of the buildings analyzed can be seen in imagery, while minor damage such as cracks or holes may not be visible at all. For flood extractions using radar data it is important to note that urban areas and highly vegetated areas may mask the flood signature and result in underestimation of flood waters. Users with specific questions or concerns should contact unosat@unitar.org to seek clarification.

---

*Generated by [Portolan](https://github.com/portolan-sdi/portolan-cli) from STAC metadata and .portolan/metadata.yaml*

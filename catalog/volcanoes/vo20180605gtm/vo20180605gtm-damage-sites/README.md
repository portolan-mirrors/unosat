# Damage sites: Volcano, Guatemala, 5 June 2018 (VO20180605GTM)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/volcanoes/vo20180605gtm/vo20180605gtm-damage-sites/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Damage sites for Volcano, Guatemala, 5 June 2018 (VO20180605GTM): 901 features merged from 2 source layers. Point layers with a damage class column (such as `Main_Damage_Site_Class`): one point per assessed structure or site. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Estimación del número de viviendas y estructuras dañadas en la aldea de San Miguel de Los Lotes y los alreadedores](https://data.humdata.org/dataset/estimacion-del-numero-de-viviendas-y-estructuras-danadas-en-la-aldea-de-san-miguel-de-los-lotes-y-)
- [Volcano de Fuego: Estimation of damaged buildings in San Miguel de Los Lotes and surrouding area, Guatemala](https://data.humdata.org/dataset/volcano-de-fuego-estimation-of-damaged-buildings-in-san-miguel-de-los-lotes-and-surrouding-area-)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![geodata](https://img.shields.io/badge/geodata-blue) ![natural disasters](https://img.shields.io/badge/natural_disasters-blue) ![volcano](https://img.shields.io/badge/volcano-blue)

## Spatial Coverage

- **Bounding Box**: [-90.84075420399995, 14.384929757000066, -90.81282561799992, 14.448485598000048]

## Temporal Coverage

- **Start**: 2018-06-07T00:00:00Z
- **End**: 2018-06-07T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| SiteID | string |  |
| SensorDate | date32[day] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | string |  |
| Confidence | string |  |
| FieldValid | string |  |
| Settlement | string |  |
| Notes | string | Free-text notes by the analyst. |
| Main_Damag | string |  |
| Grouped_Da | string |  |
| StaffID | string |  |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| ImageID_Nu | int64 |  |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./vo20180605gtm-damage-sites.parquet | 23.1 KB | 12208f0e7061... |
| ./vo20180605gtm-damage-sites.pmtiles | 44.1 KB | 12208f2eb2fb... |
| ./styles/default.json | 968 B | 1220cfe5be56... |
| ./vo20180605gtm-damage-sites.thumb.jpg | 4.9 KB | 122008fceabe... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./vo20180605gtm-damage-sites.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/estimacion-del-numero-de-viviendas-y-estructuras-danadas-en-la-aldea-de-san-miguel-de-los-lotes-y-](https://data.humdata.org/dataset/estimacion-del-numero-de-viviendas-y-estructuras-danadas-en-la-aldea-de-san-miguel-de-los-lotes-y-)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `ST20180604_Damage_Structures`, `WV20180606_Damage_Structures`.

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

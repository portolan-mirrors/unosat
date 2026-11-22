# Analysis extent: Tropical cyclone, Mozambique, 11 March 2022 (TC20220311MOZ)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/tropical-cyclones/2022/tc20220311moz/tc20220311moz-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Analysis extent for Tropical cyclone, Mozambique, 11 March 2022 (TC20220311MOZ): 6 features merged from 6 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Extensões de água superficias detectadas por satélite na Província de Nampula, Moçambique, no dia 13 de março de 2022](https://data.humdata.org/dataset/extensoes-de-agua-superficias-detectadas-por-satelite-na-provincia-de-nampula-mocambique-n)
- [Extensões de água superficias detectadas por satélite na Província de Zambezia Moçambique, no dia 15 de março de 2022](https://data.humdata.org/dataset/extensoes-de-agua-superficias-detectadas-por-satelite-na-provincia-de-zambezia-mocambique-)
- [Satellite detected water extents in Maganja Da Costa & Namacurra Districts, Mozambique as of 16 March 2022](https://data.humdata.org/dataset/water-extents-in-maganja-da-costa-namacurra-districts-mozambique-as-of-16-march-2022)
- [Satellite detected water extents in Maganja Da Costa, Namacurra & Nicoadala Districts, Mozambique as of 17 March 2022](https://data.humdata.org/dataset/water-extents-in-maganja-da-costa-namacurra-nicoadala-districts-mozambique-as-of-17-march-)
- [Satellite detected water extents in Maganja Da Costa, Namacurra & Nicoadala Districts, Mozambique as of 22 March 2022](https://data.humdata.org/dataset/water-extents-in-maganja-da-costa-namacurra-nicoadala-districts-mozambique-as-of-22-march-)
- [Satellite detected water extents in Nampula Province, Mozambique as of 13 March 2022](https://data.humdata.org/dataset/satellite-detected-water-extents-in-nampula-province-mozambique-as-of-13-march-2022)
- [Satellite detected water extents in Zambezia Province, Mozambique as of 15 March 2022](https://data.humdata.org/dataset/satellite-detected-water-extents-in-zambezia-province-mozambique-as-of-15-march-2022)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![cyclones-hurricanes-typhoons](https://img.shields.io/badge/cyclones--hurricanes--typhoons-blue) ![geodata](https://img.shields.io/badge/geodata-blue) ![tropical cyclone](https://img.shields.io/badge/tropical_cyclone-blue)

## Spatial Coverage

- **Bounding Box**: [36.64853463800006, -17.836493014999917, 40.84040923100008, -14.311195526999938]

## Temporal Coverage

- **Start**: 2022-03-14T00:00:00Z
- **End**: 2022-03-23T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `SensorID_label`, which is decoded per source file. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Area_ha | float | Area in hectares, as UNOSAT computed it. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./tc20220311moz-analysis-extent.parquet | 96.5 KB | 12209274b89c... |
| ./tc20220311moz-analysis-extent.pmtiles | 531.9 KB | 1220165be9dc... |
| ./styles/default.json | 671 B | 122003399876... |
| ./tc20220311moz-analysis-extent.thumb.jpg | 9.7 KB | 12206e3cec2b... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./tc20220311moz-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/extensoes-de-agua-superficias-detectadas-por-satelite-na-provincia-de-nampula-mocambique-n](https://data.humdata.org/dataset/extensoes-de-agua-superficias-detectadas-por-satelite-na-provincia-de-nampula-mocambique-n)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `RCM1_20220315_AnalysisExtent_ZambeziaProvince`, `S1_20220312_AnalysisExtent_NampulaProvince`, `S1_20220313_AnalysisExtent_NampulaProvince`, `S1_20220317_AnalysisExtent_Namacurra_MaganjaDaCosta_Districts`, `TSX_20220316_AnalysisExtent_Namacurra_MaganjaDaCosta_Districts`, `TSX_20220322_AnalysisExtent_Namacurra_MaganjaDaCosta_Districts`.

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

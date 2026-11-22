# Analysis extent: Landslide, United Republic of Tanzania, 8 December 2023 (LS20231208TZA)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/landslides/ls20231208tza/ls20231208tza-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Analysis extent for Landslide, United Republic of Tanzania, 8 December 2023 (LS20231208TZA): 3 features merged from 3 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Satellite detected landslide extent in Hanang District, Manyara Region, Tanzania as of 07 December 2023](https://data.humdata.org/dataset/landslide-extent-in-hanang-district-manyara-region-tanzania-as-of-07-december-2023)
- [Satellite detected landslide extent in Mogitu & Ganana Ward, Hanang District, Tanzania as of 19 December 2023](https://data.humdata.org/dataset/landslide-extent-in-mogitu-ganana-ward-hanang-district-tanzania-as-of-19-december-2023)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![geodata](https://img.shields.io/badge/geodata-blue) ![landslide](https://img.shields.io/badge/landslide-blue) ![natural disasters](https://img.shields.io/badge/natural_disasters-blue)

## Spatial Coverage

- **Bounding Box**: [35.315655105000076, -4.539442491999921, 35.41894100300004, -4.393137581999952]

## Temporal Coverage

- **Start**: 2023-12-12T00:00:00Z
- **End**: 2023-12-20T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Site_ID | int16 | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Stadium; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 42 = Military Facility; 45 = Suspected Mass Grave Site; 46 = Airport Facility; 47 = Church; 48 = Dam; 49 = Port; 50 = Power station; 51 = Power tower; 52 = Railway. The decoded text is in `Site_ID_label`. |
| AgencyID | int32 |  |
| SiteName | string |  |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Site_ID_label | string | `Site_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ls20231208tza-analysis-extent.parquet | 4.5 KB | 12201e553c44... |
| ./ls20231208tza-analysis-extent.pmtiles | 24.7 KB | 1220729e2b8b... |
| ./styles/default.json | 671 B | 1220b4fd1b0c... |
| ./ls20231208tza-analysis-extent.thumb.jpg | 7.7 KB | 12205b798852... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ls20231208tza-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/landslide-extent-in-hanang-district-manyara-region-tanzania-as-of-07-december-2023](https://data.humdata.org/dataset/landslide-extent-in-hanang-district-manyara-region-tanzania-as-of-07-december-2023)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `S2_20231207_AnalysisExtent_HanangDistrict`, `S2_20231219_AnalysisExtent_Katesh`.

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

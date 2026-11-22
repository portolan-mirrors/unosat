# Analysis extent: Earthquake, Afghanistan, 8 October 2023 (EQ20231008AFG)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/earthquakes/2023/eq20231008afg/eq20231008afg-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Analysis extent for Earthquake, Afghanistan, 8 October 2023 (EQ20231008AFG): 2,244,215 features merged from 35 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [7 October 2023 M6.3 Western Afghanistan Herat, Preliminary Satellite-Based Comprehensive Damage Assessment Report](https://data.humdata.org/dataset/7-october-2023-m6-3-western-afghanistan-herat-preliminary-satellite-based-comprehensive-da)
- [Building Damage Assessment in Koshkak village, Zindajan District, Hirat Province, Afghanistan as of 16 October 2023](https://data.humdata.org/dataset/building-damage-assessment-in-koshkak-village-zindajan-district-hirat-province-afghanistan)
- [Damage analysis by settlement and surface displacement of the 7th October 2023 Hirat earthquake](https://data.humdata.org/dataset/damage-analysis-by-settlement-and-surface-displacement-of-the-7th-october-2023-hirat-earth)
- [Damage analysis by settlement of the 11th October 2023 Hirat earthquake](https://data.humdata.org/dataset/damage-analysis-by-settlement-of-the-11th-october-2023-hirat-earthquake)
- [Preliminary satellite-derived damage assessment - 6.3M earthquake of 15 October 2023 03:36 UTC - Zindajan & Hinjil Districts, Hirat Province, Afghanistan](https://data.humdata.org/dataset/preliminary-satellite-derived-damage-assessment-6-3m-earthquake-of-15-october-2023-03-36-u)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![earthquake](https://img.shields.io/badge/earthquake-blue) ![earthquake-tsunami](https://img.shields.io/badge/earthquake--tsunami-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [60.471977233000075, 33.685452490000046, 63.304202158000066, 35.625492852000036]

## Temporal Coverage

- **Start**: 2023-10-10T00:00:00Z
- **End**: 2023-11-27T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Site_ID | int16 | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Stadium; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 42 = Military Facility; 45 = Suspected Mass Grave Site; 46 = Airport Facility; 47 = Church; 48 = Dam; 49 = Port. The decoded text is in `Site_ID_label`. |
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
| ./eq20231008afg-analysis-extent.parquet | 60.1 MB | 12201242d02f... |
| ./eq20231008afg-analysis-extent.pmtiles | 61.0 MB | 122061958750... |
| ./styles/default.json | 671 B | 122008d44760... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./eq20231008afg-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/7-october-2023-m6-3-western-afghanistan-herat-preliminary-satellite-based-comprehensive-da](https://data.humdata.org/dataset/7-october-2023-m6-3-western-afghanistan-herat-preliminary-satellite-based-comprehensive-da)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `MS_AnalysisExtent_BuildingFootprint_HeratProvince`, `MS_BuildingFootprintPolygon_HeratProvince`, `PL20231009_AnalysisExtent_HeratProvince`, `PNEO_20231016_AnalysisExtent_Injil_KarukhDistricts`, `PNEO_20231016_AnalysisExtent_ZindajanDistrict`, `WV01_WV03_20231011_AnalysisExtent_HeratProvince`, `WV1_20231015_AnalysisExtent_HeratProvince`.

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

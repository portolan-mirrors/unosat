# Analysis extent: Earthquake, Myanmar, 28 March 2025 (EQ20250328MMR)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/earthquakes/2025/eq20250328mmr/eq20250328mmr-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Analysis extent for Earthquake, Myanmar, 28 March 2025 (EQ20250328MMR): 23 features merged from 22 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Damage Assessment in Mahaaungmyay, Chanmyathazi and Chanayethazan Townships, Mandalay District, Mandalay Region, Myanmar as of 30 March 2025](https://data.humdata.org/dataset/damage-assessment-in-mahaaungmyay-chanmyathazi-and-chanayethazan-townships-mandalay-distri)
- [Damage Assessment in Mandalay & Sagaing Districts, Myanmar as of 03 April 2025](https://data.humdata.org/dataset/damage-assessment-in-mandalay-sagaing-districts-myanmar-as-of-03-april-2025)
- [Damage Assessment in Monywa Township, Monywa District, Sagaing Region, Myanmar as of 25 April 2025](https://data.humdata.org/dataset/damage-assessment-in-monywa-township-monywa-district-sagaing-region-myanmar-as-of-25-april)
- [Damage Assessment in Sagaing Township, Sagaing District, Sagaing Region, Myanmar as of 30 March 2025](https://data.humdata.org/dataset/damage-assessment-in-sagaing-township-sagaing-district-sagaing-region-myanmar-as-of-30-mar)
- [Damage Assessment in Sagaing and Mandalay, Myanmar as of 30 March 2025](https://data.humdata.org/dataset/damage-assessment-in-sagaing-and-mandalay-myanmar-as-of-30-march-2025)
- [Damage Assessment in Wundwin Township, Meiktila District Mandalay Region, Myanmar as of 01 April 2025](https://data.humdata.org/dataset/damage-assessment-in-wundwin-township-meiktila-district-mandalay-region-myanmar-as-of-01-a)
- [M7.7 28 March 2025 Sagaing Earthquake, Satellite-Based Comprehensive Damage Assessment Report](https://data.humdata.org/dataset/m7-7-28-march-2025-sagaing-earthquake-satellite-based-comprehensive-damage-assessment-repo)
- [Satellite-detected Damage in the Cultural Property Mahamuni Pagoda as of 30 March 2025](https://data.humdata.org/dataset/satellite-detected-damage-in-the-cultural-property-mahamuni-pagoda-as-of-30-march-2025)
- [Satellite-detected Damage to Cultural Heritage in Tada-U as of 03 April 2025](https://data.humdata.org/dataset/satellite-detected-damage-to-cultural-heritage-in-tada-u-as-of-03-april-2025)
- [Satellite-detected damage in the UNESCO Tentative List Site, Ancient Cities of Upper Myanmar: Innwa as of 30 March 2025](https://data.humdata.org/dataset/damage-in-the-unesco-tentative-list-site-ancient-cities-of-upper-myanmar-innwa-as-of-30-ma)
- [Satellite-detected damage in the UNESCO Tentative List Site, Ancient Cities of Upper Myanmar: Mandalay as of 30 March 2025](https://data.humdata.org/dataset/damage-in-the-unesco-tentative-list-site-ancient-cities-of-upper-myanmar-mandalay-as-of-30)
- [Satellite-detected damage in the UNESCO World Heritage Site, Bagan: Component 7 as of 03 April 2025](https://data.humdata.org/dataset/damage-in-the-unesco-world-heritage-site-bagan-component-7-as-of-03-april-2025)
- and 3 more; the event's [catalog page](../catalog.json) lists them all.

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![crisis-myanmar-earthquake](https://img.shields.io/badge/crisis--myanmar--earthquake-blue) ![earthquake](https://img.shields.io/badge/earthquake-blue) ![earthquake-tsunami](https://img.shields.io/badge/earthquake--tsunami-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [94.72263930000008, 21.04112886300004, 96.15033466000006, 22.698393666000072]

## Temporal Coverage

- **Start**: 2025-04-02T00:00:00Z
- **End**: 2025-06-13T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Site_ID | int16 | Coded value. The 3 source files of this collection use 3 different domains for it, so read `Site_ID_label`, which is decoded per source file. |
| AgencyID | int32 |  |
| SiteName | string |  |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Site_ID_label | string | `Site_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./eq20250328mmr-analysis-extent.parquet | 13.7 KB | 122030bd3c19... |
| ./eq20250328mmr-analysis-extent.pmtiles | 182.0 KB | 12207c67acd9... |
| ./styles/default.json | 671 B | 1220cf667a29... |
| ./eq20250328mmr-analysis-extent.thumb.jpg | 9.4 KB | 122068cca1df... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./eq20250328mmr-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/damage-assessment-in-mahaaungmyay-chanmyathazi-and-chanayethazan-townships-mandalay-distri](https://data.humdata.org/dataset/damage-assessment-in-mahaaungmyay-chanmyathazi-and-chanayethazan-townships-mandalay-distri)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `MultiSensors_Analysisextent`, `PHR_20250328_AnalysisExtent_Building_Mandalay`, `PHR_20250328_AnalysisExtent_Building_NorthMandalay`, `PHR_20250328_AnalysisExtent_Building_SouthMondalay`, `PHR_20250330_AnalysisExtent_CenterMandalay`, `PHR_20250330_AnalysisExtent_WestSagaing`, `PHR_20250401_AnalysisExtent_Shwetaung`, `THEOS2_20250329_AnalysisExtent_Northwest_Kyaukse`, `WV03_20250330_AnalysisExtent_Building_Sagaing`.

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

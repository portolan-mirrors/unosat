# Other points: Earthquake, Myanmar, 28 March 2025 (EQ20250328MMR)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/earthquakes/2025/eq20250328mmr/eq20250328mmr-other-points/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Other points for Earthquake, Myanmar, 28 March 2025 (EQ20250328MMR): 211,244 features merged from 55 source layers. Points layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Damage Assessment in Mandalay & Sagaing Districts, Myanmar as of 03 April 2025](https://data.humdata.org/dataset/damage-assessment-in-mandalay-sagaing-districts-myanmar-as-of-03-april-2025)
- [Damage Assessment in Monywa Township, Monywa District, Sagaing Region, Myanmar as of 25 April 2025](https://data.humdata.org/dataset/damage-assessment-in-monywa-township-monywa-district-sagaing-region-myanmar-as-of-25-april)
- [Damage Assessment in Wundwin Township, Meiktila District Mandalay Region, Myanmar as of 01 April 2025](https://data.humdata.org/dataset/damage-assessment-in-wundwin-township-meiktila-district-mandalay-region-myanmar-as-of-01-a)
- [Satellite-detected Damage in the Cultural Property Mahamuni Pagoda as of 30 March 2025](https://data.humdata.org/dataset/satellite-detected-damage-in-the-cultural-property-mahamuni-pagoda-as-of-30-march-2025)
- [Satellite-detected Damage to Cultural Heritage in Tada-U as of 03 April 2025](https://data.humdata.org/dataset/satellite-detected-damage-to-cultural-heritage-in-tada-u-as-of-03-april-2025)
- [Satellite-detected damage in the UNESCO Tentative List Site, Ancient Cities of Upper Myanmar: Innwa as of 30 March 2025](https://data.humdata.org/dataset/damage-in-the-unesco-tentative-list-site-ancient-cities-of-upper-myanmar-innwa-as-of-30-ma)
- [Satellite-detected damage in the UNESCO Tentative List Site, Ancient Cities of Upper Myanmar: Mandalay as of 30 March 2025](https://data.humdata.org/dataset/damage-in-the-unesco-tentative-list-site-ancient-cities-of-upper-myanmar-mandalay-as-of-30)
- [Satellite-detected damage in the UNESCO World Heritage Site, Bagan: Component 7 as of 03 April 2025](https://data.humdata.org/dataset/damage-in-the-unesco-world-heritage-site-bagan-component-7-as-of-03-april-2025)
- [Satellite-detected damage in the cultural property Pinya as of 30 March 2025](https://data.humdata.org/dataset/satellite-detected-damage-in-the-cultural-property-pinya-as-of-30-march-2025)
- [Satellite-detected damage to cultural heritage in Min Kun as of 03 April 2025](https://data.humdata.org/dataset/satellite-detected-damage-to-cultural-heritage-in-min-kun-as-of-03-april-2025)
- [UNOSAT Live Web Map - M 7.7 Sagaing Earthquake in Myanmar & Thailand](https://data.humdata.org/dataset/unosat-live-web-map-m-7-7-sagaing-earthquake-in-myanmar-thailand)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![crisis-myanmar-earthquake](https://img.shields.io/badge/crisis--myanmar--earthquake-blue) ![earthquake](https://img.shields.io/badge/earthquake-blue) ![earthquake-tsunami](https://img.shields.io/badge/earthquake--tsunami-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [95.18481175066182, 18.910241942711536, 97.10604189581687, 23.783159128291175]

## Temporal Coverage

- **Start**: 2025-04-06T00:00:00Z
- **End**: 2025-05-12T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| obj_type | string |  |
| name | string |  |
| info | string |  |
| simplified | string |  |
| damage_gra | string |  |
| det_method | string |  |
| notation | string |  |
| or_src_id | int32 |  |
| dmg_src_id | int32 |  |
| cd_value | string |  |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| obj_desc | string |  |
| elem_count | string |  |
| SRC_DATE | string |  |
| FRAMEWORK | string |  |
| TYPE | string |  |
| SOURCE | string |  |
| PROCESSING | string |  |
| COPYRIGHT | string |  |
| DAMAGE | string |  |
| DAMAGE_SRC | string |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./eq20250328mmr-other-points.parquet | 1.4 MB | 122011f6f85b... |
| ./eq20250328mmr-other-points.pmtiles | 696.7 KB | 12207b3392cb... |
| ./styles/default.json | 695 B | 1220ec52c6b9... |
| ./eq20250328mmr-other-points.thumb.jpg | 5.8 KB | 122033183390... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./eq20250328mmr-other-points.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/damage-assessment-in-mandalay-sagaing-districts-myanmar-as-of-03-april-2025](https://data.humdata.org/dataset/damage-assessment-in-mandalay-sagaing-districts-myanmar-as-of-03-april-2025)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `EMSR798_GRA_PRODUCT_ancillaryCrisisInfoP_MERGED`, `EMSR798_GRA_PRODUCT_builtUpP_MERGED`, `EMSR798_GRA_PRODUCT_transportationP_MERGED`, `ICube_SERTIT_en_ObservedEventP_MERGED`, `ICube_SERTIT_en_UrbanP_MERGED`.

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

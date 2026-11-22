# Damage sites: Earthquake, Indonesia, 5 August 2018 (EQ20180805IDN)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/earthquakes/2018/eq20180805idn/eq20180805idn-damage-sites/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Damage sites for Earthquake, Indonesia, 5 August 2018 (EQ20180805IDN): 1,509 features merged from 2 source layers. Point layers with a damage class column (such as `Main_Damage_Site_Class`): one point per assessed structure or site. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Damage assessment of Gumantar and Dangiang Desa, Kagayan District, Lombok Island, Indonesia](https://data.humdata.org/dataset/damage-assessment-of-gumantar-and-dangiang-desa-kagayan-district-lombok-island-indonesia-2836)
- [Potential Informal Gathering Sites over Tanjung & Pemenang Districts, Indonesia](https://data.humdata.org/dataset/potential-informal-gathering-sites-over-tanjung-pemenang-districts-indonesia-2838)
- [Potentially Damaged Buildings & Gathering Sites over Gili Islands, Lombok Utara District, Indonesia](https://data.humdata.org/dataset/potentially-damaged-buildings-gathering-sites-over-gili-islands-lombok-utara-district-indonesia-2837)
- [Potentially affected settlements over Tanjung and Pemenang Districts, Lombok Utara Regency, Nusa Tenggara Barat Province](https://data.humdata.org/dataset/potentially-affected-settlements-over-tanjung-and-pemenang-districts-lombok-utara-regency-nusa-)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![earthquake](https://img.shields.io/badge/earthquake-blue) ![earthquake-tsunami](https://img.shields.io/badge/earthquake--tsunami-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [116.03376548800009, -8.451923491999935, 116.29466654400005, -8.239909244999922]

## Temporal Coverage

- **Start**: 2018-08-07T00:00:00Z
- **End**: 2018-08-10T23:59:59Z

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
| ./eq20180805idn-damage-sites.parquet | 57.7 KB | 1220a348f67e... |
| ./eq20180805idn-damage-sites.pmtiles | 102.1 KB | 1220d6c20c3e... |
| ./styles/default.json | 1.0 KB | 1220a820d59c... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./eq20180805idn-damage-sites.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/damage-assessment-of-gumantar-and-dangiang-desa-kagayan-district-lombok-island-indonesia-2836](https://data.humdata.org/dataset/damage-assessment-of-gumantar-and-dangiang-desa-kagayan-district-lombok-island-indonesia-2836)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `PL20180807_DamageSettlementEstimation_NorthWestLombok`, `PL20180807_DamageSites_Gumantar_Desa`.

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

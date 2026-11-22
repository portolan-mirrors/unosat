# Shelters: Earthquake, Indonesia, 5 August 2018 (EQ20180805IDN)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/earthquakes/2018/eq20180805idn/eq20180805idn-shelters/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Shelters for Earthquake, Indonesia, 5 August 2018 (EQ20180805IDN): 176 features merged from 1 source layer. Point layers with shelter or camp columns, or whose names mention camps, shelters, IDPs, or settlements. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Damage assessment of Gumantar and Dangiang Desa, Kagayan District, Lombok Island, Indonesia](https://data.humdata.org/dataset/damage-assessment-of-gumantar-and-dangiang-desa-kagayan-district-lombok-island-indonesia-2836)
- [Potential Informal Gathering Sites over Tanjung & Pemenang Districts, Indonesia](https://data.humdata.org/dataset/potential-informal-gathering-sites-over-tanjung-pemenang-districts-indonesia-2838)
- [Potentially Damaged Buildings & Gathering Sites over Gili Islands, Lombok Utara District, Indonesia](https://data.humdata.org/dataset/potentially-damaged-buildings-gathering-sites-over-gili-islands-lombok-utara-district-indonesia-2837)
- [Potentially affected settlements over Tanjung and Pemenang Districts, Lombok Utara Regency, Nusa Tenggara Barat Province](https://data.humdata.org/dataset/potentially-affected-settlements-over-tanjung-and-pemenang-districts-lombok-utara-regency-nusa-)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![earthquake](https://img.shields.io/badge/earthquake-blue) ![earthquake-tsunami](https://img.shields.io/badge/earthquake--tsunami-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [116.02860216300007, -8.44503173399994, 116.16216668900006, -8.34145450899996]

## Temporal Coverage

- **Start**: 2018-08-07T00:00:00Z
- **End**: 2018-08-10T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| Site_ID | string |  |
| Sensor_ID | string |  |
| Sensor_Dat | date32[day] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence | string |  |
| Field_Vali | string |  |
| CampStatus | string |  |
| CampName | string |  |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| Notes | string | Free-text notes by the analyst. |
| StaffID | string |  |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| City_Town | string |  |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./eq20180805idn-shelters.parquet | 13.2 KB | 1220350a8b88... |
| ./eq20180805idn-shelters.pmtiles | 69.8 KB | 1220948c9c5d... |
| ./styles/default.json | 913 B | 1220df3395ee... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./eq20180805idn-shelters.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/damage-assessment-of-gumantar-and-dangiang-desa-kagayan-district-lombok-island-indonesia-2836](https://data.humdata.org/dataset/damage-assessment-of-gumantar-and-dangiang-desa-kagayan-district-lombok-island-indonesia-2836)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `PL20180808_IDPSite_Tandjung`.

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

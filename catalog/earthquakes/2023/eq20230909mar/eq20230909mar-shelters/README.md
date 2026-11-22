# Shelters: Earthquake, Morocco, 9 September 2023 (EQ20230909MAR)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/earthquakes/2023/eq20230909mar/eq20230909mar-shelters/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Shelters for Earthquake, Morocco, 9 September 2023 (EQ20230909MAR): 580 features merged from 35 source layers. Point layers with shelter or camp columns, or whose names mention camps, shelters, IDPs, or settlements. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Damage Assessment in Chichaoua, Marrakech-Safi Region, Morocco as of 10 September 2023](https://data.humdata.org/dataset/damage-assessment-in-chichaoua-marrakech-safi-region-morocco-as-of-10-september-2023)
- [Damage Assessment in Douar Tagadirte (Igermane), Chichaoua Province, Marrakech-Safi Region, Morocco as of 10 September 2023](https://data.humdata.org/dataset/damage-assessment-in-douar-tagadirte-igermane-chichaoua-province-marrakech-safi-region-mor)
- [Power Supply Assessment Following the Adassil/Al Haouz Earthquake (8 September 2023, M6.8) using High-resolution Night-time Light Images​ - 18 September 2023](https://data.humdata.org/dataset/power-supply-assessment-following-the-adassil-al-haouz-earthquake-8-september-2023-m6-8-us)
- [Évaluation des dégats à Adassil, région de  Chichaoua, province de Marrakech-Safi, Maroc, au 10 Septembre 2023](https://data.humdata.org/dataset/evaluation-des-degats-a-adassil-region-de-chichaoua-province-de-marrakech-safi-maroc-au-10)
- [Évaluation des dégats à Taroudant, région de  Taroudant, province de Souss Massa, Maroc, au 10 Septembre 2023](https://data.humdata.org/dataset/evaluation-des-degats-a-taroudant-region-de-taroudant-province-de-souss-massa-maroc-au-10-)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![earthquake](https://img.shields.io/badge/earthquake-blue) ![earthquake-tsunami](https://img.shields.io/badge/earthquake--tsunami-blue) ![geodata](https://img.shields.io/badge/geodata-blue) ![morocco-earthquake](https://img.shields.io/badge/morocco--earthquake-blue)

## Spatial Coverage

- **Bounding Box**: [-8.903250382999943, 30.440336028000047, -7.993991911999956, 31.612564125000063]

## Temporal Coverage

- **Start**: 2023-09-11T00:00:00Z
- **End**: 2023-09-18T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Site_ID | int16 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Site_ID_label`, which is decoded per source file. |
| AgencyID | int32 |  |
| SiteName | string |  |
| Lat | double |  |
| Lon | double |  |
| Notes | string | Free-text notes by the analyst. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Site_ID_label | string | `Site_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./eq20230909mar-shelters.parquet | 12.3 KB | 12207eac9dcd... |
| ./eq20230909mar-shelters.pmtiles | 64.3 KB | 122028b00852... |
| ./styles/default.json | 679 B | 122027d0a870... |
| ./eq20230909mar-shelters.thumb.jpg | 5.1 KB | 12209d921398... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./eq20230909mar-shelters.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/damage-assessment-in-chichaoua-marrakech-safi-region-morocco-as-of-10-september-2023](https://data.humdata.org/dataset/damage-assessment-in-chichaoua-marrakech-safi-region-morocco-as-of-10-september-2023)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `PL_20230910_IDP_Adassil`, `PL_20230910_IDP_Adebdi`, `PL_20230910_IDP_AitOthmane`, `PL_20230910_IDP_Chichaoua`, `PL_20230910_IDP_Marrakech`, `PL_20230910_IDP_Taroudant`, `WV2_20230909_IDP_LallaAaziza`.

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

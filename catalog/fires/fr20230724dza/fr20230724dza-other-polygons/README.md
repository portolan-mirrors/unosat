# Other polygons: Fire, Algeria, 24 July 2023 (FR20230724DZA)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/fires/fr20230724dza/fr20230724dza-other-polygons/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Other polygons for Fire, Algeria, 24 July 2023 (FR20230724DZA): 12 features merged from 12 source layers. Polygons layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Densité des foyers d'incendies dans les wilayas de Bouira, Tizi Ouzou et Bejaia le 24 juillet 2023](https://data.humdata.org/dataset/densite-des-foyers-d-incendies-dans-les-wilayas-de-bouira-tizi-ouzou-et-bejaia-le-24-juill)
- [Fire in Algeria - UNOSAT Live Web Map](https://data.humdata.org/dataset/fire-in-algeria-unosat-live-web-map)
- [Zones incendiées le 25 juillet 2023 dans la Wilaya de Bejaia, Algérie](https://data.humdata.org/dataset/zones-incendiees-le-25-juillet-2023-dans-la-wilaya-de-bejaia-algerie)
- [Zones incendiées le 25 juillet 2023 dans les communes de Melbou et Ziama Mansouria, Wilayas de Bejaia et Jijel, Algérie](https://data.humdata.org/dataset/zones-incendiees-le-25-juillet-2023-dans-les-communes-de-melbou-et-ziama-mansouria-wilayas)
- [Zones incendiées le 27 juillet 2023 dans les communes de Melbou et Ziama Mansouria, Wilayas de Bejaia et Jijel, Algérie](https://data.humdata.org/dataset/zones-incendiees-le-27-juillet-2023-dans-les-communes-de-melbou-et-ziama-mansouria-wilayas)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![disaster risk reduction-drr](https://img.shields.io/badge/disaster_risk_reduction--drr-blue) ![fire](https://img.shields.io/badge/fire-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [2.478785753000068, 35.85242462200006, 7.407449722000081, 37.09346920000007]

## Temporal Coverage

- **Start**: 2023-07-24T00:00:00Z
- **End**: 2023-07-28T23:59:59Z

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
| ./fr20230724dza-other-polygons.parquet | 162.2 KB | 1220df266861... |
| ./fr20230724dza-other-polygons.pmtiles | 425.9 KB | 12208251cc94... |
| ./styles/default.json | 664 B | 122032dfe985... |
| ./fr20230724dza-other-polygons.thumb.jpg | 8.7 KB | 1220acb568c4... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fr20230724dza-other-polygons.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/densite-des-foyers-d-incendies-dans-les-wilayas-de-bouira-tizi-ouzou-et-bejaia-le-24-juill](https://data.humdata.org/dataset/densite-des-foyers-d-incendies-dans-les-wilayas-de-bouira-tizi-ouzou-et-bejaia-le-24-juill)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `PL_20220726_AnalysisArea_Bejaja`, `PL_20230726_AnalysisArea_Bejaja`, `S2_20220725_AnalysisArea_Bejaja`, `S2_20220725_AnalysisArea_SoukElTenine`, `S2_20230725_AnalysisArea_Bejaja`, `S2_20230725_AnalysisArea_SoukElTenine`, `VIIRS_20230724_20230725_AreaOfInterest_Algjers_Bejaia_Skikda`.

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

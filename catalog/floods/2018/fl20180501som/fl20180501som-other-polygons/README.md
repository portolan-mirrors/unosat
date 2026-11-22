# Other polygons: Flood, Somalia, 1 May 2018 (FL20180501SOM)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2018/fl20180501som/fl20180501som-other-polygons/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Other polygons for Flood, Somalia, 1 May 2018 (FL20180501SOM): 1 features merged from 1 source layer. Polygons layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Satellite Detected Water Over Shabelle & Afder Zones, Ethiopia](https://data.humdata.org/dataset/satellite-detected-water-over-shabelle-afder-zones-ethiopia-2790)
- [Satellite Detected Water Over Shabelle & Afder Zones, Somali Region, Ethiopia](https://data.humdata.org/dataset/satellite-detected-water-over-shabelle-afder-zones-somali-region-ethiopia-2795)
- [Satellite Detected Water over Belet Weyne & Bulo Burto Districts, Hiraan Region, Somalia](https://data.humdata.org/dataset/satellite-detected-water-over-belet-weyne-bulo-burto-districts-hiraan-region-somalia-2793)
- [Satellite detected Water Over Saakow and Buaale Districts, Middle Juba, Somalia](https://data.humdata.org/dataset/satellite-detected-water-over-saakow-and-buaale-districts-middle-juba-somalia-2787)
- [Satellite detected water & IDP distribution over  Belet Weyne Town](https://data.humdata.org/dataset/satellite-detected-water-idp-distribution-over-belet-weyne-town-2792)
- [Satellite detected water & building damage assessment over  Belet Weyne Town, Somalia](https://data.humdata.org/dataset/satellite-detected-water-building-damage-assessment-over-belet-weyne-town-somalia-2806)
- [Satellite detected water over  Belet Weyne Town, Belet Weyne District](https://data.humdata.org/dataset/satellite-detected-water-over-belet-weyne-town-belet-weyne-district-2789)
- [Satellite detected water over  Middle Juba and Lower Juba Region, Somalia](https://data.humdata.org/dataset/satellite-detected-water-over-middle-juba-and-lower-juba-region-somalia-2788)
- [Satellite detected water over Belet Weyne District,Hiraan Region, Somalia](https://data.humdata.org/dataset/satellite-detected-water-over-belet-weyne-district-hiraan-region-somalia-2791)
- [Satellite detected water over Dinsoor, Baardheere, Bu'aale & Saakow district, Gedo, Middle Juba & Bay Region, Somalia](https://data.humdata.org/dataset/satellite-detected-water-over-dinsoor-baardheere-bu-aale-saakow-district-gedo-middle-juba-bay-)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [44.11664882600007, 4.716915524000058, 45.59370529900008, 6.0416929200000595]

## Temporal Coverage

- **Start**: 2018-05-02T00:00:00Z
- **End**: 2018-05-17T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| Site_ID | string |  |
| AgencyID | int64 |  |
| SiteName | string |  |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20180501som-other-polygons.parquet | 3.9 KB | 1220e31e2289... |
| ./fl20180501som-other-polygons.pmtiles | 82.7 KB | 12205b5acf9b... |
| ./styles/default.json | 664 B | 1220e3b895e2... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20180501som-other-polygons.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/satellite-detected-water-building-damage-assessment-over-belet-weyne-town-somalia-2806](https://data.humdata.org/dataset/satellite-detected-water-building-damage-assessment-over-belet-weyne-town-somalia-2806)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `ST20180507_Moibalo_Somalis_Extent`.

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

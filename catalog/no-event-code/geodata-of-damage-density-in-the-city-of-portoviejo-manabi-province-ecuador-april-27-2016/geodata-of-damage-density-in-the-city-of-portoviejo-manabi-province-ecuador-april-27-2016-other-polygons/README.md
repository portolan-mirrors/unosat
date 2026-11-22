# Other polygons: Geodata of Damage Density in the City of Portoviejo, Manabi Province, Ecuador
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/no-event-code/geodata-of-damage-density-in-the-city-of-portoviejo-manabi-province-ecuador-april-27-2016/geodata-of-damage-density-in-the-city-of-portoviejo-manabi-province-ecuador-april-27-2016-other-polygons/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Other polygons for Geodata of Damage Density in the City of Portoviejo, Manabi Province, Ecuador: 9 features merged from 9 source layers. Polygons layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of Damage Density in the City of Portoviejo, Manabi Province, Ecuador](https://data.humdata.org/dataset/geodata-of-damage-density-in-the-city-of-portoviejo-manabi-province-ecuador-april-27-2016)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![dataset](https://img.shields.io/badge/dataset-blue) ![earthquake-tsunami](https://img.shields.io/badge/earthquake--tsunami-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [-80.97864516499993, -2.3282569939999576, -79.7389700729999, 0.9409273180000923]

## Temporal Coverage

- **Start**: 2016-04-27T00:00:00Z
- **End**: 2016-04-27T23:59:59Z

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
| ./geodata-of-damage-density-in-the-city-of-portoviejo-manabi-province-ecuador-april-27-2016-other-polygons.parquet | 6.1 KB | 1220a46a9ffa... |
| ./geodata-of-damage-density-in-the-city-of-portoviejo-manabi-province-ecuador-april-27-2016-other-polygons.pmtiles | 62.9 KB | 1220a15720fb... |
| ./styles/default.json | 740 B | 1220128f9495... |
| ./geodata-of-damage-density-in-the-city-of-portoviejo-manabi-province-ecuador-april-27-2016-other-polygons.thumb.jpg | 3.6 KB | 122026c65044... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./geodata-of-damage-density-in-the-city-of-portoviejo-manabi-province-ecuador-april-27-2016-other-polygons.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-damage-density-in-the-city-of-portoviejo-manabi-province-ecuador-april-27-2016](https://data.humdata.org/dataset/geodata-of-damage-density-in-the-city-of-portoviejo-manabi-province-ecuador-april-27-2016)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `PL_20160418_Atacames_Analysis`, `PL_20160418_Salinas_Analysis`, `PL_20160419_Bahia_SanVicente_Analysis_Limit`, `PL_20160419_Chone_Analysis`, `PL_20160419_Montecrisiti_AOI`, `PL_20160419_Portoviejo_Analysis`, `PL_20160420_Muisne_Analysis`, `PL_201604_19_La_Crucita_Analysis`, `WV_20160502_Jama_Analysis`.

## Attribution

UNITAR-UNOSAT

## License

[CC-BY-NC-SA-3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/)

## Contact

Portolan Mirrors <nissim@radiant.earth>

## Known Issues

This is a preliminary assessment and has not yet been validated in the field. It is important to consider the characteristics of the source imagery used in the analyses when interpreting results. For damage assessments it should be noted that only significant damage to the structural integrity of the buildings analyzed can be seen in imagery, while minor damage such as cracks or holes may not be visible at all. For flood extractions using radar data it is important to note that urban areas and highly vegetated areas may mask the flood signature and result in underestimation of flood waters. Users with specific questions or concerns should contact unosat@unitar.org to seek clarification.

---

*Generated by [Portolan](https://github.com/portolan-sdi/portolan-cli) from STAC metadata and .portolan/metadata.yaml*

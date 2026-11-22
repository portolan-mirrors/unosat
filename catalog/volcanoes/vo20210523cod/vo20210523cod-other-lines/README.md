# Other lines: Volcano, Democratic Republic of the Congo, 23 May 2021 (VO20210523COD)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/volcanoes/vo20210523cod/vo20210523cod-other-lines/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Other lines for Volcano, Democratic Republic of the Congo, 23 May 2021 (VO20210523COD): 21 features merged from 1 source layer. Lines layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Coulée de lave et structures affectées suite à l'éruption volcanique du Nyiragongo, Province du Nord-Kivu, RD Congo](https://data.humdata.org/dataset/coulee-de-lave-et-structures-affectees-suite-a-l-eruption-volcanique-du-nyiragongo-provinc)
- [Lava flow and affected structures caused by  the volcanic eruption of the 22 May 2021 in Kanyanza village, DR Congo](https://data.humdata.org/dataset/lava-flow-and-affected-structures-caused-by-the-volcanic-eruption-of-the-22-may-2021-in-ka)
- [Lava flow and affected structures caused by Nyiragongo volcanic eruption, Nord-Kivu Province, DR Congo](https://data.humdata.org/dataset/lava-flow-and-affected-structures-caused-by-nyiragongo-volcanic-eruption-nord-kivu-provinc)
- [Lava flow and affected structures caused by the volcanic eruption of the 22 May 2021 in north of Goma airport, DR Congo](https://data.humdata.org/dataset/lava-flow-and-affected-structures-caused-by-the-volcanic-eruption-of-the-22-may-2021-in-no)
- [Lava flow and geological information in NordKivu Province, DR Congo and Western Province, Rwanda as of 01 June 2021](https://data.humdata.org/dataset/lava-flow-and-geological-information-in-nordkivu-province-dr-congo-and-western-province-rw)
- [Lava flow and geological information related to the volcanic eruption in DR Congo and Rwanda as of 27 May 2021](https://data.humdata.org/dataset/lava-flow-and-geological-information-related-to-the-volcanic-eruption-in-dr-congo-and-rwan)
- [Lava flow extent and affected structures caused by the 22 May 2021 Nyiragongo volcanic eruption in Goma, DR Congo](https://data.humdata.org/dataset/lava-flow-extent-and-affected-structures-caused-by-the-22-may-2021-nyiragongo-volcanic-eru)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![geodata](https://img.shields.io/badge/geodata-blue) ![natural disasters](https://img.shields.io/badge/natural_disasters-blue) ![volcano](https://img.shields.io/badge/volcano-blue)

## Spatial Coverage

- **Bounding Box**: [29.24832517100009, -1.6015028889999599, 29.26608055400004, -1.553366743999959]

## Temporal Coverage

- **Start**: 2021-05-25T00:00:00Z
- **End**: 2021-06-03T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Shape_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Length_m | float |  |
| Length_km | float |  |
| Note | string | Free-text notes by the analyst. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./vo20210523cod-other-lines.parquet | 5.8 KB | 122005587272... |
| ./vo20210523cod-other-lines.pmtiles | 23.5 KB | 12204efc4682... |
| ./styles/default.json | 401 B | 12204cb54da3... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./vo20210523cod-other-lines.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/coulee-de-lave-et-structures-affectees-suite-a-l-eruption-volcanique-du-nyiragongo-provinc](https://data.humdata.org/dataset/coulee-de-lave-et-structures-affectees-suite-a-l-eruption-volcanique-du-nyiragongo-provinc)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `USGS_Fissures`.

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

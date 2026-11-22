# Other polygons: Earthquake, Colombia, 10 August 2026 (EQ20260810COL)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/earthquakes/2026/eq20260810col/eq20260810col-other-polygons/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Other polygons for Earthquake, Colombia, 10 August 2026 (EQ20260810COL): 10 features merged from 10 source layers. Polygons layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Building Damage Assessment Density Map in Zarzal City, Valle del Cauca Department, Colombia  as of 13 August 2026](https://data.humdata.org/dataset/building-damage-assessment-density-map-in-zarzal-city-valle-del-cauca-department-colombia-)
- [Building Damage Assessment in Viterbo Town, Caldas Department, Colombia  as of 12 August 2026](https://data.humdata.org/dataset/building-damage-assessment-in-viterbo-town-caldas-department-colombia-as-of-12-august-2026)
- [Evaluación de daños en edificaciones en la ciudad de Zarzal, Valle del Cauca, Colombia, al 13 de agosto de 2026](https://data.humdata.org/dataset/evaluacion-de-danos-en-edificaciones-en-la-ciudad-de-zarzal-valle-del-cauca-colombia-al-13)
- [M 7.4  in South of San José del Palmar, Colombia 10 August 2026 at 12:34 UTC](https://data.humdata.org/dataset/m-7-4-in-south-of-san-jose-del-palmar-colombia-10-august-2026-at-12-34-utc)
- [PRELIMINARY SATELLITE-DERIVED DAMAGE ASSESSMENT - San José Del Palmar municipality, Chocó department, Colombia](https://data.humdata.org/dataset/preliminary-satellite-derived-damage-assessment-san-jose-del-palmar-municipality-choco-dep)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![earthquake](https://img.shields.io/badge/earthquake-blue) ![earthquake-tsunami](https://img.shields.io/badge/earthquake--tsunami-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [-76.10029999999995, 4.368600000000072, -75.8436999999999, 5.091200000000072]

## Temporal Coverage

- **Start**: 2026-08-11T00:00:00Z
- **End**: 2026-08-21T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Name | string |  |
| FolderPath | string |  |
| SymbolID | int32 |  |
| AltMode | int16 |  |
| Base | double |  |
| Clamped | int16 |  |
| Extruded | int16 |  |
| Snippet | string |  |
| PopupInfo | string |  |
| Shape_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Shape_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./eq20260810col-other-polygons.parquet | 7.2 KB | 122035c1b15c... |
| ./eq20260810col-other-polygons.pmtiles | 31.8 KB | 1220ebe8876d... |
| ./styles/default.json | 664 B | 122048e7707f... |
| ./eq20260810col-other-polygons.thumb.jpg | 3.3 KB | 1220c26406df... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./eq20260810col-other-polygons.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/building-damage-assessment-density-map-in-zarzal-city-valle-del-cauca-department-colombia-](https://data.humdata.org/dataset/building-damage-assessment-density-map-in-zarzal-city-valle-del-cauca-department-colombia-)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Pleiades_20260812_AnalysedArea_Viterbo`, `Pleiades_20260813_AnalysedArea_Zarzal`.

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

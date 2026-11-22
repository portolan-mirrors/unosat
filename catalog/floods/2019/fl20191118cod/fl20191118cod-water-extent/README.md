# Water extent: Flood, Democratic Republic of the Congo, 18 November 2019 (FL20191118COD)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2019/fl20191118cod/fl20191118cod-water-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Water extent for Flood, Democratic Republic of the Congo, 18 November 2019 (FL20191118COD): 39 features merged from 4 source layers. Polygon layers with a water class column (such as `Water_Class`), or whose names mention flood, water, or inundation: satellite-detected water. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Satellite-detected flood waters over Mobayi-Mbongo, Nord-Ubangi Province, Democratic Republic of the Congo](https://data.humdata.org/dataset/flood-waters-over-mobayi-mbongo-nord-ubangi-province-democratic-republic-of-the-congo)
- [Satellite-detected flood waters, as of 12 November 2019, over Zongo, Democratic Republic of the Congo](https://data.humdata.org/dataset/flood-waters-as-of-12-november-2019-over-zongo-democratic-republic-of-the-congo)
- [Satellite-detected flood waters, as of 15 November 2019, Libenge, Libenge Territory, Democratic Republic of the Congo](https://data.humdata.org/dataset/flood-waters-as-of-15-november-2019-libenge-libenge-territory-democratic-republic-of-the-c)
- [Satellite-detected flooded structures, as of 12 November 2019, over Zongo, Democratic Republic of the Congo](https://data.humdata.org/dataset/flooded-structures-as-of-12-november-2019-over-zongo-democratic-republic-of-the-congo)
- [Satellite-detected flooded structures, as of 15 November 2019, over Libenge, Democratic Republic of the Congo](https://data.humdata.org/dataset/flooded-structures-as-of-15-november-2019-over-libenge-democratic-republic-of-the-congo)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [18.568124456000078, 3.5727813390000733, 21.699038623000035, 4.390663417000042]

## Temporal Coverage

- **Start**: 2019-11-18T00:00:00Z
- **End**: 2019-11-21T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Water_Class | int16 |  |
| Sensor_ID | int32 |  |
| Sensor_Date | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence_ID | int16 |  |
| Field_Validation | int16 |  |
| Water_StatusID | int32 |  |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| SenorID_old | int16 |  |
| StaffID | int32 |  |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20191118cod-water-extent.parquet | 436.3 KB | 12200e13d32c... |
| ./fl20191118cod-water-extent.pmtiles | 129.1 KB | 1220b8852807... |
| ./styles/default.json | 871 B | 122069264b35... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20191118cod-water-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/flood-waters-as-of-12-november-2019-over-zongo-democratic-republic-of-the-congo](https://data.humdata.org/dataset/flood-waters-as-of-12-november-2019-over-zongo-democratic-republic-of-the-congo)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `GE01_20191112_FloodWater_ZongoNW_COD`, `PL_20191115_FloodWater_Libenge_COD`, `ST1_20191118_WaterExtent_BasseKotto_CAF_AOI4`, `ST1_20191118_WaterExtent_BasseKotto_CAF_AOI5`.

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

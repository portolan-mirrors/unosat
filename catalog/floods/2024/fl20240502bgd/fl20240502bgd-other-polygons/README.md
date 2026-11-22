# Other polygons: Flood, Bangladesh, 2 May 2024 (FL20240502BGD)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2024/fl20240502bgd/fl20240502bgd-other-polygons/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Other polygons for Flood, Bangladesh, 2 May 2024 (FL20240502BGD): 7 features merged from 7 source layers. Polygons layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Flood impact analysis in Chhatak Upazila, Sunamganj District, Sylhet Division, Bangladesh as of 26 June 2024](https://data.humdata.org/dataset/flood-impact-analysis-in-chhatak-upazila-sunamganj-district-sylhet-division-bangladesh-as-)
- [Flood impact analysis in Sunamganj Sadar and Bishwambarpur Upazilas, Sunamganj District, Sylhet Division, Bangladesh as of 26 June 2024](https://data.humdata.org/dataset/flood-impact-analysis-in-sunamganj-sadar-and-bishwambarpur-upazilas-sunamganj-district-syl)
- [Satellite detected water extents between 16 & 23 July 2024 in Bangladesh](https://data.humdata.org/dataset/satellite-detected-water-extents-between-16-23-july-2024-in-bangladesh)
- [Satellite detected water extents between 4 & 11 July 2024 in Bangladesh](https://data.humdata.org/dataset/satellite-detected-water-extents-between-4-11-july-2024-in-bangladesh)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [91.33818831700006, 24.989815090000036, 91.70280289600004, 25.15006394100004]

## Temporal Coverage

- **Start**: 2024-07-01T00:00:00Z
- **End**: 2024-07-31T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int64 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `SensorID_label`, which is decoded per source file. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | int64 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| SHAPE_Leng | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20240502bgd-other-polygons.parquet | 6.2 KB | 12207d9060d4... |
| ./fl20240502bgd-other-polygons.pmtiles | 40.2 KB | 1220499269b4... |
| ./styles/default.json | 664 B | 12204d630ada... |
| ./fl20240502bgd-other-polygons.thumb.jpg | 6.1 KB | 1220784da42f... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20240502bgd-other-polygons.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/flood-impact-analysis-in-chhatak-upazila-sunamganj-district-sylhet-division-bangladesh-as-](https://data.humdata.org/dataset/flood-impact-analysis-in-chhatak-upazila-sunamganj-district-sylhet-division-bangladesh-as-)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `GLOBAL_20240626_AnglysisExtent_Sunamganj`, `PHR_20240626_AnglysisExtent_SunamganjSadar`.

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

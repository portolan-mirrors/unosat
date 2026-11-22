# Water extent: Flood, Bangladesh, 18 May 2018 (FL20180518BGD)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2018/fl20180518bgd/fl20180518bgd-water-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Water extent for Flood, Bangladesh, 18 May 2018 (FL20180518BGD): 934 features merged from 3 source layers. Polygon layers with a water class column (such as `Water_Class`), or whose names mention flood, water, or inundation: satellite-detected water. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Satellite Detected Water Extent in Teknaf Upazila, Cox's Bazar District, Chittagong Division, Bangladesh](https://data.humdata.org/dataset/satellite-detected-water-extent-in-teknaf-upazila-cox-s-bazar-district-chittagong-division-)
- [Satellite Detected Waters Evolution by Camp Extent in Cox's Bazar District, Chittagong Division, Bangladesh](https://data.humdata.org/dataset/satellite-detected-waters-evolution-by-camp-extent-in-cox-s-bazar-district-chittagong-division-)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [92.13048194500004, 20.91723348100004, 92.27261191000008, 21.22291853100006]

## Temporal Coverage

- **Start**: 2018-06-14T00:00:00Z
- **End**: 2018-06-20T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| Sensor_ID | string |  |
| Sensor_Dat | date32[day] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence | string |  |
| Field_Vali | string |  |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| StaffID | string |  |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| New_Camp_N | string |  |
| District | string |  |
| Upazila | string |  |
| Settlement | string |  |
| Union | string |  |
| Name_Alias | string |  |
| SSID | string |  |
| zone_code | int64 |  |
| mean_0523d | double |  |
| mean_0614d | double |  |
| std_0523db | double |  |
| std_0614db | double |  |
| std_diff | double |  |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| Water_Clas | string |  |
| Water_Stat | string |  |
| SenorID_ol | string |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20180518bgd-water-extent.parquet | 138.7 KB | 1220626a0853... |
| ./fl20180518bgd-water-extent.pmtiles | 160.7 KB | 1220f24adf5d... |
| ./styles/default.json | 879 B | 1220fece7d67... |
| ./fl20180518bgd-water-extent.thumb.jpg | 6.8 KB | 1220b8a4009f... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20180518bgd-water-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/satellite-detected-water-extent-in-teknaf-upazila-cox-s-bazar-district-chittagong-division-](https://data.humdata.org/dataset/satellite-detected-water-extent-in-teknaf-upazila-cox-s-bazar-district-chittagong-division-)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `RS20180614_Cox_Bazar_Flood_Water`, `ST20180522_Teknaf_Flood_Water`, `ST20180613_Teknaf_Flood_Water`.

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

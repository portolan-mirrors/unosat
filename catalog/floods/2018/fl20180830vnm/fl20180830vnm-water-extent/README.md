# Water extent: Flood, Viet Nam, 30 August 2018 (FL20180830VNM)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2018/fl20180830vnm/fl20180830vnm-water-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Water extent for Flood, Viet Nam, 30 August 2018 (FL20180830VNM): 1,394,185 features merged from 4 source layers. Polygon layers with a water class column (such as `Water_Class`), or whose names mention flood, water, or inundation: satellite-detected water. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Satellite Detected Surface Waters & Evolution in Long An Province, Vietnam](https://data.humdata.org/dataset/satellite-detected-surface-waters-evolution-in-long-an-province-vietnam-2840)
- [Satellite Detected Surface Waters Evolution in Southern Provinces of Kien Giang, Dong Thap & An Giang, Vietnam](https://data.humdata.org/dataset/satellite-detected-surface-waters-evolution-in-southern-provinces-of-kien-giang-dong-thap-an-giang-)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [104.38284749400003, 8.881159014000048, 107.27935256300003, 12.46471063000007]

## Temporal Coverage

- **Start**: 2018-08-31T00:00:00Z
- **End**: 2018-09-04T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| Water_Clas | string |  |
| Sensor_ID | string |  |
| Sensor_Dat | date32[day] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence | string |  |
| Field_Vali | string |  |
| Water_Stat | string |  |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| SenorID_ol | string |  |
| StaffID | string |  |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20180830vnm-water-extent.parquet | 113.1 MB | 122037107efc... |
| ./fl20180830vnm-water-extent.pmtiles | 124.9 MB | 12206152b4cc... |
| ./styles/default.json | 879 B | 122080ff4335... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20180830vnm-water-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/satellite-detected-surface-waters-evolution-in-long-an-province-vietnam-2840](https://data.humdata.org/dataset/satellite-detected-surface-waters-evolution-in-long-an-province-vietnam-2840)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `ST20180816_DongThapAnGiang_FloodWater`, `ST20180816_LangAn_Flood_Water`, `ST20180828_DongThapAnGiang_FloodWater`, `ST20180828_LangAn_Flood_Water`.

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

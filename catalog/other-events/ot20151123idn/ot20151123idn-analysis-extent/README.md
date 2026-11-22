# Analysis extent: Event, Indonesia, 23 November 2015 (OT20151123IDN)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/other-events/ot20151123idn/ot20151123idn-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Analysis extent for Event, Indonesia, 23 November 2015 (OT20151123IDN): 4,373 features merged from 6 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of Affected Mining Areas along Kahayan River, Central Kalimantan, Indonesia](https://data.humdata.org/dataset/geodata-of-affected-mining-areas-along-kahayan-river-central-kalimantan-indon-march-04-2016)
- [Geodata of Affected Mining Areas along Kapuas River, Central Kalimantan, Indonesia](https://data.humdata.org/dataset/geodata-of-affected-mining-areas-along-kapuas-river-central-kalimantan-indone-march-04-2016)
- [Geodata of Affected Mining Areas in Galangan & Katingan, Central Kalimantan, Indonesia](https://data.humdata.org/dataset/geodata-of-affected-mining-areas-in-galangan-katingan-central-kalimantan-ind-march-04-2016)
- [Geodata of Land Cover Classification along Kahayan River, Central Kalimantan, Indonesia](https://data.humdata.org/dataset/geodata-of-land-cover-classification-along-kahayan-river-central-kalimantan-i-march-04-2016)
- [Geodata of Land Cover Classification along Kapuas River, Central Kalimantan, Indonesia](https://data.humdata.org/dataset/geodata-of-land-cover-classification-along-kapuas-river-central-kalimantan-in-march-04-2016)
- [Geodata of Land Cover Classification of Galangan & Katingan, Central Kalimantan, Indonesia](https://data.humdata.org/dataset/geodata-of-land-cover-classification-of-galangan-katingan-central-kalimantan-march-04-2016)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![event](https://img.shields.io/badge/event-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [113.02885914100011, -2.1325537169999507, 114.56303821000006, -1.0396404839999605]

## Temporal Coverage

- **Start**: 2016-03-04T00:00:00Z
- **End**: 2016-03-04T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT 6; 42 = Sentinel-1; 43 = Komsat-2; 999 = Combination of Sensors. The decoded text is in `SensorID_label`. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 22 = WP; 33 = LB; 44 = JL; 55 = VG; 66 = CJ; 73 = RS; 77 = LD; 88 = HK; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 141 = KJP; 151 = MNY; 222 = CS; 1000 = Unknown. The decoded text is in `StaffID_label`. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Confidence_ID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `Confidence_ID_label`. |
| Field_Validation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `Field_Validation_label`. |
| Area_ha | float | Area in hectares, as UNOSAT computed it. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Confidence_ID_label | string | `Confidence_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Field_Validation_label | string | `Field_Validation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ot20151123idn-analysis-extent.parquet | 1.6 MB | 122031a9847f... |
| ./ot20151123idn-analysis-extent.pmtiles | 2.8 MB | 12206bbede9c... |
| ./styles/default.json | 671 B | 1220fae52aa4... |
| ./ot20151123idn-analysis-extent.thumb.jpg | 14.6 KB | 122044a6dcbd... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ot20151123idn-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-affected-mining-areas-along-kahayan-river-central-kalimantan-indon-march-04-2016](https://data.humdata.org/dataset/geodata-of-affected-mining-areas-along-kahayan-river-central-kalimantan-indon-march-04-2016)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Cloud_Mask_AOI1_20050807`, `Cloud_Mask_AOI1_20150803`, `Cloud_Mask_AOI2_20050807`, `Cloud_Mask_AOI2_20150803`, `Cloud_Mask_AOI3_20020526`, `Cloud_Mask_AOI3_20140924`.

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

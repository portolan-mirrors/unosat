# Analysis extent: Flood, Viet Nam, 9 November 2016 (FL20161109VNM)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2016/fl20161109vnm/fl20161109vnm-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Analysis extent for Flood, Viet Nam, 9 November 2016 (FL20161109VNM): 6 features merged from 6 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Satellite Detected Surface Water Extent Evolution of Dinh Binh Lake](https://data.humdata.org/dataset/satellite-detected-surface-water-extent-evolution-of-dinh-binh-lake)
- [Satellite Detected Surface Waters Extent and Evolution in Binh Dinh Province](https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-in-binh-dinh-province)
- [Satellite Detected Surface Waters Extent and Evolution in Ha Tinh Province](https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-in-ha-tinh-province)
- [Satellite Detected Surface Waters Extent and Evolution in Northern Quang Binh Province](https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-in-northern-quang-binh-province)
- [Satellite Detected Surface Waters Extent and Evolution in Phu Yen Province](https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-in-phu-yen-province)
- [Satellite Detected Surface Waters Extent and Evolution in Quang Nam Province](https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-in-quang-nam-province)
- [Satellite Detected Surface Waters Extent and Evolution in Quang Ngai Province](https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-in-quang-ngai-province)
- [Satellite Detected Surface Waters Extent and Evolution in Thua Thien Hue Province](https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-in-thua-thien-hue-province)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [105.10279846200007, 12.830606764000038, 110.15529087400006, 18.672580719000052]

## Temporal Coverage

- **Start**: 2016-11-22T00:00:00Z
- **End**: 2016-12-21T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT 6; 42 = Sentinel-1; 43 = Komsat-2; 999 = Combination of Sensors. The decoded text is in `SensorID_label`. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 16 = HA; 18 = AM; 22 = WP; 33 = LB; 44 = JL; 55 = VG; 66 = CJ; 73 = RS; 77 = LD; 88 = HK; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 141 = KJP; 151 = MNY; 161 = DC; 171 = SR; 222 = CS; 1000 = Unknown. The decoded text is in `StaffID_label`. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Area_ha | float | Area in hectares, as UNOSAT computed it. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20161109vnm-analysis-extent.parquet | 70.0 KB | 122010656f5f... |
| ./fl20161109vnm-analysis-extent.pmtiles | 758.6 KB | 12209a2eb028... |
| ./styles/default.json | 671 B | 1220cdd1c644... |
| ./fl20161109vnm-analysis-extent.thumb.jpg | 10.6 KB | 12201bc9ef9f... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20161109vnm-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/satellite-detected-surface-water-extent-evolution-of-dinh-binh-lake](https://data.humdata.org/dataset/satellite-detected-surface-water-extent-evolution-of-dinh-binh-lake)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Binhdinh_Phuyen_Provinces_Analysis_Extent`, `DinhBinh_Lake_Analysis_Extent`, `HaTinh_Province_Analysis_Extent`, `NorthernQuangBinh_Province_Analysis_Extent`, `QuangNgai_QuangNam_Provinces_Analysis_Extent`, `ThuaThienHue_Province_Analysis_Extent`.

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

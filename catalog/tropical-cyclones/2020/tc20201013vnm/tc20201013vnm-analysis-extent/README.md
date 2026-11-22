# Analysis extent: Tropical cyclone, Viet Nam, 13 October 2020 (TC20201013VNM)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/tropical-cyclones/2020/tc20201013vnm/tc20201013vnm-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Analysis extent for Tropical cyclone, Viet Nam, 13 October 2020 (TC20201013VNM): 15 features merged from 15 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Satellite detected waters in Ha Tinh and Nghe An Provinces of Viet Nam as of 18 October 2020](https://data.humdata.org/dataset/waters-in-ha-tinh-and-nghe-an-provinces-of-viet-nam-as-of-18-october-2020)
- [Satellite detected waters in Ha Tinh and Nghe An Provinces of Viet Nam as of 21 October 2020](https://data.humdata.org/dataset/waters-in-ha-tinh-and-nghe-an-provinces-of-viet-nam-as-of-21-october-2020)
- [Satellite detected waters in Minh Hoa and Tuyen Hoa district, Quang Binh province of Viet Nam as of 19 October 2020](https://data.humdata.org/dataset/waters-in-minh-hoa-and-tuyen-hoa-district-quang-binh-province-of-viet-nam-as-of-19-october)
- [Satellite detected waters in Quang Binh Province of Viet Nam as of 18 October 2020](https://data.humdata.org/dataset/satellite-detected-waters-in-quang-binh-province-of-viet-nam-as-of-18-october-2020)
- [Satellite detected waters in Quang Binh Province of Viet Nam as of 22 October 2020](https://data.humdata.org/dataset/satellite-detected-waters-in-quang-binh-province-of-viet-nam-as-of-22-october-2020)
- [Satellite detected waters in Quang Nam Province of Viet Nam as of 17 October 2020](https://data.humdata.org/dataset/satellite-detected-waters-in-quang-nam-province-of-viet-nam-as-of-17-october-2020)
- [Satellite detected waters in Quang Nam Province of Viet Nam as of 20 October 2020](https://data.humdata.org/dataset/satellite-detected-waters-in-quang-nam-province-of-viet-nam-as-of-20-october-2020)
- [Satellite detected waters in Quang Ngai Province of Viet Nam as of 17 October 2020](https://data.humdata.org/dataset/satellite-detected-waters-in-quang-ngai-province-of-viet-nam-as-of-17-october-2020)
- [Satellite detected waters in Quang Tri Province of Viet Nam as of 18 October 2020](https://data.humdata.org/dataset/satellite-detected-waters-in-quang-tri-province-of-viet-nam-as-of-18-october-2020)
- [Satellite detected waters in Quang Tri Province of Viet Nam as of 22 October 2020](https://data.humdata.org/dataset/satellite-detected-waters-in-quang-tri-province-of-viet-nam-as-of-22-october-2020)
- [Satellite detected waters in Quang Tri Province of Viet Nam as of 25 October 2020](https://data.humdata.org/dataset/satellite-detected-waters-in-quang-tri-province-of-viet-nam-as-of-25-october-2020)
- [Satellite detected waters in Thua Thien Hue Province of Viet Nam as of 22 October 2020](https://data.humdata.org/dataset/satellite-detected-waters-in-thua-thien-hue-province-of-viet-nam-as-of-22-october-2020)
- and 1 more; the event's [catalog page](../catalog.json) lists them all.

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![cyclones-hurricanes-typhoons](https://img.shields.io/badge/cyclones--hurricanes--typhoons-blue) ![geodata](https://img.shields.io/badge/geodata-blue) ![tropical cyclone](https://img.shields.io/badge/tropical_cyclone-blue)

## Spatial Coverage

- **Bounding Box**: [104.73649985000003, 14.226269926000043, 109.08463392400006, 18.97289749500004]

## Temporal Coverage

- **Start**: 2020-10-19T00:00:00Z
- **End**: 2020-10-26T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT-4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT-6; 42 = Sentinel-1; 43 = Kompsat-2; 44 = Sentinel-2; 45 = Sentinel-3; 46 = Kompsat-3; 47 = Deimos-2; 48 = TripleSat; 49 = PlanetLabs; 50 = RapidEye; 51 = WorldView-4; 52 = SPOT-7; 999 = Combination of Sensors. The decoded text is in `SensorID_label`. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 22 = WP; 33 = LB; 44 = JL; 45 = MD; 54 = HP; 55 = VG; 57 = PG; 66 = CJ; 70 = SG; 73 = RS; 77 = LD; 88 = HK; 91 = KA; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 141 = KJP; 151 = MNY; 161 = DC; 171 = SR; 181 = NL; 191 = DH; 212 = MH; 213 = JT; 214 = ES; 222 = CS; 1000 = Unknown. The decoded text is in `StaffID_label`. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Area_ha | float | Area in hectares, as UNOSAT computed it. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./tc20201013vnm-analysis-extent.parquet | 381.0 KB | 12202c5aa5be... |
| ./tc20201013vnm-analysis-extent.pmtiles | 1.2 MB | 12208c394684... |
| ./styles/default.json | 671 B | 1220b8c2d5c1... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./tc20201013vnm-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/satellite-detected-waters-in-quang-binh-province-of-viet-nam-as-of-18-october-2020](https://data.humdata.org/dataset/satellite-detected-waters-in-quang-binh-province-of-viet-nam-as-of-18-october-2020)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `K5_20201020_AnalysisExtent_QuangNam`, `Kompsat5_20201019_AnalysisExtent_MinhHoa_TuyenHoa`, `RCM1_20201017_AnalysisExtent_QuangNam`, `ST1_20201013_AnalysisExtent_CentralPart`, `ST1_20201015_AnalysisExtent_HaTinh`, `ST1_20201017_AnalysisExtent_QuangNgai`, `ST1_20201018_AnalysisExtent_HaTinh`, `ST1_20201018_AnalysisExtent_QuangTri`, `ST1_20201021_AnalysisExtent_HaTinh`, `ST1_20201022_AnalysisExtent_QuangBinh`, `ST1_20201022_AnalysisExtent_QuangTri`, `ST1_20201022_AnalysisExtent_ThuaThienHue`, `ST1_20201025_AnalysisExtent_QuangTri`, `ST1_20201025_AnalysisExtent_ThuaThienHue`, `TSX_20201018_AnalysisExtent_QuangBinh`.

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

# Analysis extent: Flood, Bangladesh, 13 July 2020 (FL20200713BGD)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2020/fl20200713bgd/fl20200713bgd-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Analysis extent for Flood, Bangladesh, 13 July 2020 (FL20200713BGD): 9 features merged from 9 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Population potentially exposed to floods between 12&21 July 2020  in Bangladesh](https://data.humdata.org/dataset/population-potentially-exposed-to-floods-between-12-21-july-2020-in-bangladesh)
- [Satellite detected water extent as of 18 July 2020 over Eastern part of Sylhet Division, Bangladesh](https://data.humdata.org/dataset/water-extent-as-of-18-july-2020-over-eastern-part-of-sylhet-division-bangladesh)
- [Satellite detected water extent as of 18 July 2020 over Mymensingh, Rajshahi and Rangpur Divisions, Bangladesh](https://data.humdata.org/dataset/water-extent-as-of-18-july-2020-over-mymensingh-rajshahi-and-rangpur-divisions-bangladesh)
- [Satellite detected water extent as of 19 July 2020 in NE Bangladesh](https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-19-july-2020-in-ne-bangladesh)
- [Satellite detected water extent as of 19 July 2020 of Bangladesh](https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-19-july-2020-of-bangladesh)
- [Satellite detected water extent as of 20 July 2020 over the Northeastern region of Bangladesh](https://data.humdata.org/dataset/water-extent-as-of-20-july-2020-over-the-northeastern-region-of-bangladesh)
- [Satellite detected water extent as of 21 July 2020 over Northwestern region of Bangladesh](https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-21-july-2020-over-northwestern-region-of-bangladesh)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [88.00862798600008, 20.590609348000044, 92.68030687500004, 26.634513010000035]

## Temporal Coverage

- **Start**: 2020-07-20T00:00:00Z
- **End**: 2020-07-24T23:59:59Z

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
| ./fl20200713bgd-analysis-extent.parquet | 2.1 MB | 12204f18bf71... |
| ./fl20200713bgd-analysis-extent.pmtiles | 3.3 MB | 122027c4fb89... |
| ./styles/default.json | 671 B | 12200ba0fdb4... |
| ./fl20200713bgd-analysis-extent.thumb.jpg | 18.7 KB | 1220bf695360... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20200713bgd-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/population-potentially-exposed-to-floods-between-12-21-july-2020-in-bangladesh](https://data.humdata.org/dataset/population-potentially-exposed-to-floods-between-12-21-july-2020-in-bangladesh)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `NOAA_20200723_20200727_AnalysisExtent_Bangladesh`, `ST1_20200719_AnalysisExtent_Bangladesh`, `ST1_20200720_AnalysisExtent_NE_Bangladesh`, `ST1_20200721_AnalysisExtent_CentralRegion`, `ST1_20200721_AnalysisExtent_Northwestern`, `ST1_20200808_AnalysisExtent_Central_Northern`, `TDX_20200719_AnalysisExtent_NE_Bangladesh`, `TSX_20200718_AnalysisExtent_E_Sylhet`, `TSX_20200718_AnalysisExtent_Mymensingh_Rajshahi_Rangpur`.

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

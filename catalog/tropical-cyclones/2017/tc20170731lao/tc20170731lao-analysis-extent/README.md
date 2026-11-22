# Analysis extent: Tropical cyclone, Lao People's Democratic Republic, 31 July 2017 (TC20170731LAO)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/tropical-cyclones/2017/tc20170731lao/tc20170731lao-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Analysis extent for Tropical cyclone, Lao People's Democratic Republic, 31 July 2017 (TC20170731LAO): 9 features merged from 9 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Satellite Detected Water Extent in Khamkeuth District, Borikhamxay Province, Lao PDR](https://data.humdata.org/dataset/satellite-detected-water-extent-in-khamkeuth-district-borikhamxay-province-lao-pdr)
- [Satellite Detected Water Extent in Khongxedone District, Salavan Province, Lao PDR](https://data.humdata.org/dataset/satellite-detected-water-extent-in-khongxedone-district-salavan-province-lao-pdr)
- [Satellite Detected Water Extent in the Phonhong & Viengkham Districts, Vientiane Province, Lao PDR](https://data.humdata.org/dataset/satellite-detected-water-extent-in-the-phonhong-viengkham-districts-vientiane-province-lao-pdr)
- [Satellite Detected Water Extent in the Sanamxay District, Attapeu Province, Lao PDR](https://data.humdata.org/dataset/satellite-detected-water-extent-in-the-sanamxay-district-attapeu-province-lao-pdr)
- [Story Map: Floods in Laos resulting from Tropical Cyclone Sonca 17](https://data.humdata.org/dataset/story-map-floods-in-laos-resulting-from-tropical-cyclone-sonca-17)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![cyclones-hurricanes-typhoons](https://img.shields.io/badge/cyclones--hurricanes--typhoons-blue) ![geodata](https://img.shields.io/badge/geodata-blue) ![tropical cyclone](https://img.shields.io/badge/tropical_cyclone-blue)

## Spatial Coverage

- **Bounding Box**: [102.04692757500004, 14.350045764000072, 106.75330644200005, 18.90636296200006]

## Temporal Coverage

- **Start**: 2017-08-03T00:00:00Z
- **End**: 2017-08-16T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT-4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT-6; 42 = Sentinel-1; 43 = Kompsat-2; 44 = Sentinel-2; 45 = Sentinel-3; 46 = Kompsat-3; 47 = Deimos-2; 48 = TripleSat; 49 = PlanetLabs; 50 = RapidEye; 51 = WorldView-4; 52 = SPOT-7; 999 = Combination of Sensors. The decoded text is in `SensorID_label`. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `StaffID_label`, which is decoded per source file. |
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
| ./tc20170731lao-analysis-extent.parquet | 177.9 KB | 12205770689c... |
| ./tc20170731lao-analysis-extent.pmtiles | 425.5 KB | 12202956d11d... |
| ./styles/default.json | 671 B | 1220c835a3ff... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./tc20170731lao-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/satellite-detected-water-extent-in-khamkeuth-district-borikhamxay-province-lao-pdr](https://data.humdata.org/dataset/satellite-detected-water-extent-in-khamkeuth-district-borikhamxay-province-lao-pdr)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `ST20170730_Laos_Champasack_Analysis_Extent`, `ST20170730_Laos_Khongxedone_Analysis_Extent`, `ST20170730_Laos_Pathoomphone_Analysis_Extent`, `ST20170730_Laos_Sanamxay_Analysis_Extent`, `ST20170730_Laos_Sukhuma_Analysis_Extent`, `ST20170801_Laos_Hinherb_Analysis_Extent`, `ST20170801_Laos_Phonhong_Analysis_Extent`, `ST20170801_Laos_Viengkham_Analysis_Extent`, `ST20170811_Laos_Khamkeuth_Analysis_Extent`.

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

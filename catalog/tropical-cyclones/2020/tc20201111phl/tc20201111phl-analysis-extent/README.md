# Analysis extent: Tropical cyclone, Philippines, 11 November 2020 (TC20201111PHL)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/tropical-cyclones/2020/tc20201111phl/tc20201111phl-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Analysis extent for Tropical cyclone, Philippines, 11 November 2020 (TC20201111PHL): 8 features merged from 8 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Potential affected buildings & impact caused by mudslides in Daraga Municipality, Albay Province, Philippines](https://data.humdata.org/dataset/potential-affected-buildings-impact-caused-by-mudslides-in-daraga-municipality-albay-provi)
- [Satellite detected waters in Albay and Camarines Sur Provinces, Bicol Region of Philippines as of 12 November 2020](https://data.humdata.org/dataset/waters-in-albay-and-camarines-sur-provinces-bicol-region-of-philippines-as-of-12-november-)
- [Satellite detected waters in Albay and Camarines Sur Provinces, Bicol Region of Philippines as of 13 November 2020](https://data.humdata.org/dataset/waters-in-albay-and-camarines-sur-provinces-bicol-region-of-philippines-as-of-13-november-)
- [Satellite detected waters in Albay and Sorsogon Provinces of Philippines as of 12 November 2020](https://data.humdata.org/dataset/waters-in-albay-and-sorsogon-provinces-of-philippines-as-of-12-november-2020)
- [Satellite detected waters in CAR and Cagayan Valley regions, Philippines as of 13 November 2020](https://data.humdata.org/dataset/waters-in-car-and-cagayan-valley-regions-philippines-as-of-13-november-2020)
- [Satellite detected waters in Camarines Norte Province, Bicol Region (Region V) of Philippines as of 12 November 2020](https://data.humdata.org/dataset/waters-in-camarines-norte-province-bicol-region-region-v-of-philippines-as-of-12-november-)
- [Satellite detected waters in Ilocos, Central Luzon and National Capital regions of Philippines as of 17 November 2020](https://data.humdata.org/dataset/waters-in-ilocos-central-luzon-and-national-capital-regions-of-philippines-as-of-17-novemb)
- [Satellite detected waters in Quezon Province, Bicol Region (Region V) of Philippines as of 12 November 2020](https://data.humdata.org/dataset/waters-in-quezon-province-bicol-region-region-v-of-philippines-as-of-12-november-2020)
- [Satellite detected waters in Sorsogon province, Bicol region of Philippines as of 13 November 2020](https://data.humdata.org/dataset/waters-in-sorsogon-province-bicol-region-of-philippines-as-of-13-november-2020)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![cyclones-hurricanes-typhoons](https://img.shields.io/badge/cyclones--hurricanes--typhoons-blue) ![geodata](https://img.shields.io/badge/geodata-blue) ![tropical cyclone](https://img.shields.io/badge/tropical_cyclone-blue)

## Spatial Coverage

- **Bounding Box**: [121.06834149200006, 12.850051887000063, 124.35074906400007, 18.58005260500005]

## Temporal Coverage

- **Start**: 2020-11-12T00:00:00Z
- **End**: 2020-11-18T23:59:59Z

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
| ./tc20201111phl-analysis-extent.parquet | 4.2 MB | 1220e293aeca... |
| ./tc20201111phl-analysis-extent.pmtiles | 731.6 KB | 12205ee997f5... |
| ./styles/default.json | 671 B | 1220de0e08b4... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./tc20201111phl-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/potential-affected-buildings-impact-caused-by-mudslides-in-daraga-municipality-albay-provi](https://data.humdata.org/dataset/potential-affected-buildings-impact-caused-by-mudslides-in-daraga-municipality-albay-provi)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `ST1_20201101_AnalysisExtent_Catanduanes`, `ST1_20201112_AnalysisExtent_Albay_CamarinesSur`, `ST1_20201112_AnalysisExtent_Albay_Sorsogon`, `ST1_20201112_AnalysisExtent_CamarinesNorte`, `ST1_20201112_AnalysisExtent_Quezon`, `ST1_20201113_AnalysisExtent_Albay_CamarinesSur`, `ST1_20201113_AnalysisExtent_Cagayan`, `ST1_20201113_AnalysisExtent_Sorsogon`.

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

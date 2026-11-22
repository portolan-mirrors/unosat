# Analysis extent: Flood, Kenya, 26 April 2024 (FL20240426KEN)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2024/fl20240426ken/fl20240426ken-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Analysis extent for Flood, Kenya, 26 April 2024 (FL20240426KEN): 123 features merged from 114 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Cumulative Satellite Detected Waters and Impact in Kenya between 24 to 28 April 2024](https://data.humdata.org/dataset/cumulative-satellite-detected-waters-and-impact-in-kenya-between-24-to-28-april-2024)
- [Flood Impact to Cropland in Nairobi and Kiambu County, Kenya as of 1 May 2024](https://data.humdata.org/dataset/flood-impact-to-cropland-in-nairobi-and-kiambu-county-kenya-as-of-1-may-2024)
- [Flood impact analysis  in Kiambu County, Kenya  as of 1 May 2024](https://data.humdata.org/dataset/flood-impact-analysis-in-kiambu-county-kenya-as-of-1-may-2024)
- [Flood impact analysis in Nairobi Kenya as of 1 May 2024](https://data.humdata.org/dataset/flood-impact-analysis-in-nairobi-kenya-as-of-1-may-2024)
- [Flood impact analysis in Nairobi and Kiambu County, Kenya as of 1 May 2024](https://data.humdata.org/dataset/flood-impact-analysis-in-nairobi-and-kiambu-county-kenya-as-of-1-may-2024)
- [Flood impact analysis in Nairobi and Machakos County, Kenya as of 1 May 2024](https://data.humdata.org/dataset/flood-impact-analysis-in-nairobi-and-machakos-county-kenya-as-of-1-may-2024)
- [Flood impact to  cropland in Nairobi and Machakos County, Kenya as of 1 May 2024](https://data.humdata.org/dataset/flood-impact-to-cropland-in-nairobi-and-machakos-county-kenya-as-of-1-may-2024)
- [Flood impact to cropland in Kiambu County, Kenya as of 1 May 2024](https://data.humdata.org/dataset/flood-impact-to-cropland-in-kiambu-county-kenya-as-of-1-may-2024)
- [Landslide/mudslide Impact in Mai Mahiu  and Kijabe Towns, Kenya as of 1 May 2024](https://data.humdata.org/dataset/landslide-mudslide-impact-in-mai-mahiu-and-kijabe-towns-kenya-as-of-1-may-2024)
- [Satellite detected water extent in Garissa City and Mororo Village, Kenya as of 29 April 2024](https://data.humdata.org/dataset/water-extent-in-garissa-city-and-mororo-village-kenya-as-of-29-april-2024)
- [Satellite detected water extent in Garissa City and Mororo Village, Kenya as of 5 May 2024](https://data.humdata.org/dataset/satellite-detected-water-extent-in-garissa-city-and-mororo-village-kenya-as-of-5-may-2024)
- [UNOSAT Live Web map- Flood in Kenya](https://data.humdata.org/dataset/unosat-live-web-map-flood-in-kenya)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [33.910288655000045, -4.676879882999913, 41.906021459000044, 5.414123535000044]

## Temporal Coverage

- **Start**: 2024-04-30T00:00:00Z
- **End**: 2024-05-10T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT-4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT-6; 42 = Sentinel-1; 43 = Kompsat-2; 44 = Sentinel-2; 45 = Sentinel-3; 46 = Kompsat-3; 47 = Deimos-2; 48 = TripleSat; 49 = PlanetLabs; 50 = RapidEye; 51 = WorldView-4; 52 = SPOT-7; 53 = Jilin-1; 54 = GaoFen-2; 55 = SkySat; 56 = ICEYE; 57 = Landsat-9; 58 = VIIRS-NOAA; 59 = RCM-1; 60 = RCM-2; 61 = RCM-3; 62 = TanDEM-X; 63 = BlackSky; …. The decoded text is in `SensorID_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 18 = TH; 22 = WP; 33 = LB; 44 = JL; 45 = MD; 54 = HP; 55 = VG; 57 = PG; 66 = CJ; 70 = SG; 73 = RS; 77 = LD; 88 = HK; 91 = KA; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 141 = KJP; 151 = MNY; 161 = DC; 171 = SR; 181 = NL; 191 = DH; 212 = MH; 213 = JT; 214 = ES; 215 = KB; 216 = JY; 218 = PA; 219 = SS; 220 = YM; 221 = IS; 222 = LD; 1000 = Unknown. The decoded text is in `StaffID_label`. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Shape_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Shape_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Area_ha | float | Area in hectares, as UNOSAT computed it. |
| Staff_ID | int32 |  |
| ConfidenceID_label | string | `ConfidenceID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| FieldValidation_label | string | `FieldValidation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| SiteID | int16 | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Stadium; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 42 = Military Facility; 45 = Suspected Mass Grave Site; 46 = Airport Facility; 47 = Church; 48 = Dam; 49 = Port. The decoded text is in `SiteID_label`. |
| Settlement_Name | string |  |
| Main_Damage_Site_Class | int16 | Coded value. The source geodatabase domain gives: 1 = Destroyed; 2 = Severe Damage; 3 = Moderate Damage; 4 = Possible Damage; 5 = Impact Crater (Damage to Road); 6 = No Visible Damage; 7 = Impact Crater (Damage to Field); 8 = Destroyed (Demolition Zone); 9 = Suspected Phosphorus shell Attack Zone; 10 = Road Damage from Tank Passage; 11 = Possible Damage from adjacent impact, debris; 12 = Lava Flow; 13 = Damage. The decoded text is in `Main_Damage_Site_Class_label`. |
| Grouped_Damage_Classes | int16 | Coded value. The source geodatabase domain gives: 1 = Damaged Buildings; 2 = Damaged Greenhouses; 3 = Impacts on Roads / Bridges; 4 = Impacts in Fields; 5 = Damaged Road segments; 6 = Damaged Port. The decoded text is in `Grouped_Damage_Classes_label`. |
| ImageID_Num | int32 |  |
| Grouped_Damage_Classes_label | string | `Grouped_Damage_Classes` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Main_Damage_Site_Class_label | string | `Main_Damage_Site_Class` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SiteID_label | string | `SiteID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20240426ken-analysis-extent.parquet | 9.2 MB | 122007671df8... |
| ./fl20240426ken-analysis-extent.pmtiles | 28.1 MB | 1220279dd1ee... |
| ./styles/default.json | 671 B | 1220fd5d2bcf... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20240426ken-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/cumulative-satellite-detected-waters-and-impact-in-kenya-between-24-to-28-april-2024](https://data.humdata.org/dataset/cumulative-satellite-detected-waters-and-impact-in-kenya-between-24-to-28-april-2024)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `PL_20240501_AnalysisExtent_CropLand_Nairobi_Kiambu`, `PL_20240501_AnalysisExtent_Nairobi_Kiambu`, `PL_20240501_CloudObstruction_MaiMahiu`, `PL_20240501_CloudObstruction_Nairobi_Kiambu`, `PL_20240505_AnalysisExtent_Garissa`, `S2_20240429_AnalysisExtent_AlongTanaRiver_GalanaRiver`, `S2_20240429_AnalysisExtent_Garissa`, `S2_20240429_CloudObstruction_AlongTanaRiver_GalanaRiver`, `VIIRS_20240424_20240428_AnalysisExtent_Kenya`, `VIIRS_20240424_20240428_CloudObstruction_Kenya`.

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

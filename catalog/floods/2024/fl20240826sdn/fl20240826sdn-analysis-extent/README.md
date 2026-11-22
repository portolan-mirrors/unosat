# Analysis extent: Flood, Sudan, 26 August 2024 (FL20240826SDN)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2024/fl20240826sdn/fl20240826sdn-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Analysis extent for Flood, Sudan, 26 August 2024 (FL20240826SDN): 91 features merged from 79 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Preliminary satellite-derived impact assessment on health facilities, Abu Hamad City, Abu Hamad Locality, River Nile State, 2 September 2024](https://data.humdata.org/dataset/preliminary-satellite-derived-impact-assessment-on-health-facilities-abu-hamad-city-abu-ha)
- [Preliminary satellite-derived impact assessment on health facilities, Arbaat Dam, Al Ganap Locality, Red Sea State, Sudan, 2 September 2024](https://data.humdata.org/dataset/preliminary-satellite-derived-impact-assessment-on-health-facilities-arbaat-dam-al-ganap-l)
- [Satellite detected water extent in Abu Hamad Locality, River Nile State, Sudan as of 19 August 2024](https://data.humdata.org/dataset/water-extent-in-abu-hamad-locality-river-nile-state-sudan-as-of-19-august-2024)
- [Satellite detected water extent in Ag Geneina and Kereneik, West Darfur State, Sudan as of 5 September 2024s of 5 September 2024](https://data.humdata.org/dataset/water-extent-in-ag-geneina-and-kereneik-west-darfur-state-sudan-as-of-5-september-2024s-of)
- [Satellite detected water extent in Al Fashir City, Al Fasher Department, Al Fasher State, Sudan as of 3 September 2024](https://data.humdata.org/dataset/water-extent-in-al-fashir-city-al-fasher-department-al-fasher-state-sudan-as-of-3-septembe)
- [Satellite detected water extent in Kassala and River Nile States, Sudan  as of 3 and 5 September 2024](https://data.humdata.org/dataset/water-extent-in-kassala-and-river-nile-states-sudan-as-of-3-and-5-september-2024)
- [Satellite detected water extent in Khartoum, White Nile, Aj Jazirah and Sennar States, Sudan  as of 8 September 2024](https://data.humdata.org/dataset/water-extent-in-khartoum-white-nile-aj-jazirah-and-sennar-states-sudan-as-of-8-september-2)
- [Satellite detected water extent in Tawkar Locality, Red Sea State, Sudan as of 26 August 2024](https://data.humdata.org/dataset/water-extent-in-tawkar-locality-red-sea-state-sudan-as-of-26-august-2024)
- [UNOSAT Live Webmap, Floods in Sudan - August 2024](https://data.humdata.org/dataset/unosat-live-webmap-floods-in-sudan-august-2024)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [22.282053030000043, 12.576382988000091, 38.087708037000084, 20.15722607200007]

## Temporal Coverage

- **Start**: 2024-08-28T00:00:00Z
- **End**: 2024-09-10T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT-4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT-6; 42 = Sentinel-1; 43 = Kompsat-2; 44 = Sentinel-2; 45 = Sentinel-3; 46 = Kompsat-3; 47 = Deimos-2; 48 = TripleSat; 49 = PlanetLabs; 50 = RapidEye; 51 = WorldView-4; 52 = SPOT-7; 53 = Jilin-1; 54 = GaoFen-2; 55 = SkySat; 56 = ICEYE; 57 = Landsat-9; 58 = VIIRS-NOAA; 59 = RCM-1; 60 = RCM-2; 61 = RCM-3; 62 = TanDEM-X; 63 = BlackSky; …. The decoded text is in `SensorID_label`. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 18 = TH; 22 = WP; 33 = LB; 44 = JL; 45 = MD; 54 = HP; 55 = VG; 57 = PG; 66 = CJ; 70 = SG; 73 = RS; 77 = LD; 88 = HK; 91 = KA; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 141 = KJP; 151 = MNY; 161 = DC; 171 = SR; 181 = NL; 191 = DH; 212 = MH; 213 = JT; 214 = ES; 215 = KB; 216 = JY; 218 = PA; 219 = SS; 220 = YM; 221 = IS; 222 = LD; 1000 = Unknown. The decoded text is in `StaffID_label`. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| FID_S2_20240826_CloudObstruction_Tokar | int32 |  |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Staff_ID | int32 |  |
| ConfidenceID_label | string | `ConfidenceID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| FieldValidation_label | string | `FieldValidation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Site_ID | int16 | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Stadium; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 42 = Military Facility; 45 = Suspected Mass Grave Site; 46 = Airport Facility; 47 = Church; 48 = Dam; 49 = Port. The decoded text is in `Site_ID_label`. |
| AgencyID | int32 |  |
| SiteName | string |  |
| Site_ID_label | string | `Site_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20240826sdn-analysis-extent.parquet | 49.9 MB | 1220650629e0... |
| ./fl20240826sdn-analysis-extent.pmtiles | 23.1 MB | 1220a9d93647... |
| ./styles/default.json | 671 B | 1220f5069daf... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20240826sdn-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/preliminary-satellite-derived-impact-assessment-on-health-facilities-abu-hamad-city-abu-ha](https://data.humdata.org/dataset/preliminary-satellite-derived-impact-assessment-on-health-facilities-abu-hamad-city-abu-ha)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `PHR_20240829_AnalysisExtent_HealthFacilityt_Assessment_Abuhamad`, `PHR_20240829_AnalysisExtent_HealthFacilityt_Assessment_Tokar`, `PHR_20240831_AnalysisExtent_HealthFacility_Assessment_AlGanab`, `S2_20240809_AnalysisExtent_AbuHamad`, `S2_20240809_CloudObstruction_AbuHamad`, `S2_20240819_AnalysisExtent_AbuHamad`, `S2_20240826_AnalysisExtent_Tokar`, `S2_20240826_CloudObstruction_Tokar`, `S2_20240903_20240905_AnalysisExtent_Kassala_RiverNile_RedSea`, `S2_20240903_20240905_CloudObstruction_Kassala_RiverNile_RedSea`, `S2_20240905_AnalysisExtent_AgGeneina`, `S2_20240905_CloudObstruction_AgGeneina`, `S2_20240908_AnalysisExtent_Khartoum_AjJazirah_WhiteNile_Sennar`, `S2_20240908_CloudObstruction_Khartoum_AjJazirah_WhiteNile_Sennar`, `WV3_20240903_AnalysisExtent_AlFashir`, `WV3_20240903_CloudObstruction_AlFashir`.

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

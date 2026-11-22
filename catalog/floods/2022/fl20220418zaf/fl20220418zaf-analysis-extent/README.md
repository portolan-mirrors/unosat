# Analysis extent: Flood, South Africa, 18 April 2022 (FL20220418ZAF)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2022/fl20220418zaf/fl20220418zaf-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Analysis extent for Flood, South Africa, 18 April 2022 (FL20220418ZAF): 16 features merged from 16 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Floods and landslides in KwaZulu-Natal (Republic of South Africa)](https://data.humdata.org/dataset/floods-and-landslides-in-kwazulu-natal-republic-of-south-africa)
- [Landslide analysis eThekwini, Metropolitan Municipality, KwaZulu-Natal Province, South Africa as of 28 April 2022](https://data.humdata.org/dataset/landslide-analysis-ethekwini-metropolitan-municipality-kwazulu-natal-province-south-africa)
- [Landslide analysis in Umzumbe & Ray Nkonyeni local municipality, Ugu District, South Africa as of 21 April 2022](https://data.humdata.org/dataset/landslide-analysis-in-umzumbe-ray-nkonyeni-local-municipality-ugu-district-south-africa-as)
- [Landslide and flash floods impact analysis West of Durban, eThekwini Metropolitan Municipality, KwaZulu-Natal Provincce,](https://data.humdata.org/dataset/landslide-and-flash-floods-impact-analysis-west-of-durban-ethekwini-metropolitan-municipal)
- [Landslide and flash floods impact analysis in Umdloti village, eThekwini Metropolitan Municipality, KwaZulu-Natal](https://data.humdata.org/dataset/landslide-and-flash-floods-impact-analysis-in-umdloti-village-ethekwini-metropolitan-munic)
- [Landslide impact analysis eThekwini, Metropolitan Municipality, KwaZulu-Natal Province, South Africa as of 21 April 2022](https://data.humdata.org/dataset/landslide-impact-analysis-ethekwini-metropolitan-municipality-kwazulu-natal-province-south)
- [Landslide impact analysis in eThekwini, Metropolitan Municipality, KwaZulu-NatalProvince, South Africa as of 20 April 20](https://data.humdata.org/dataset/landslide-impact-analysis-in-ethekwini-metropolitan-municipality-kwazulu-natalprovince-sou)
- [Landslide impact analysis in eThekwini, Metropolitan Municipality, South Africa as of 21 April 2022](https://data.humdata.org/dataset/landslide-impact-analysis-in-ethekwini-metropolitan-municipality-south-africa-as-of-21-apr)
- [PRELIMINARY SATELLITE-DERIVED FLOOD AND LANDSLIDE ASSESSMENT](https://data.humdata.org/dataset/preliminary-satellite-derived-flood-and-landslide-assessment)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [30.12762153700004, -30.772316222999905, 31.23074789700007, -29.21304422199995]

## Temporal Coverage

- **Start**: 2022-04-25T00:00:00Z
- **End**: 2022-05-11T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Site_ID | int16 | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Staduim; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 42 = Military Facility; 45 = Suspected Mass Grave Site; 46 = Airport Facility; 47 = Church. The decoded text is in `Site_ID_label`. |
| AgencyID | int32 |  |
| SiteName | string |  |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Site_ID_label | string | `Site_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT-4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT-6; 42 = Sentinel-1; 43 = Kompsat-2; 44 = Sentinel-2; 45 = Sentinel-3; 46 = Kompsat-3; 47 = Deimos-2; 48 = TripleSat; 49 = PlanetLabs; 50 = RapidEye; 51 = WorldView-4; 52 = SPOT-7; 53 = NewSat; 999 = Combination of Sensors. The decoded text is in `SensorID_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 18 = TH; 22 = WP; 33 = LB; 44 = JL; 45 = MD; 54 = HP; 55 = VG; 57 = PG; 66 = CJ; 70 = SG; 73 = RS; 77 = LD; 88 = HK; 91 = KA; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 141 = KJP; 151 = MNY; 161 = DC; 171 = SR; 181 = NL; 191 = DH; 212 = MH; 213 = JT; 214 = ES; 215 = KB; 216 = JY; 218 = PA; 219 = SS; 220 = IS; 222 = CS; 1000 = Unknown. The decoded text is in `StaffID_label`. |
| Staff_ID | int32 |  |
| ConfidenceID_label | string | `ConfidenceID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| FieldValidation_label | string | `FieldValidation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20220418zaf-analysis-extent.parquet | 284.0 MB | 1220d62e1ba4... |
| ./fl20220418zaf-analysis-extent.pmtiles | 4.7 MB | 122080eadae5... |
| ./styles/default.json | 671 B | 122000487b59... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20220418zaf-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/floods-and-landslides-in-kwazulu-natal-republic-of-south-africa](https://data.humdata.org/dataset/floods-and-landslides-in-kwazulu-natal-republic-of-south-africa)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `K3_20220421_AnalysisExtent_Maphumulo_Ndwedwe`, `K3_20220421_AnalysisExtent_MiddleDurban`, `K3_20220421_AnalysisExtent_PineTown`, `K3_20220421_AnalysisExtent_RayNkonyeni_Umzumbre`, `K3_20220421_AnalysisExtent_WestDurban`, `NewSat_20220413_AnalysisExtent_eThekwiniMetroMunicipality_SouthAfrica`, `S2_20220428_AnalysisExtent_PineTown`, `WV01_20220504_AnalysisExtent_Durban`, `WV03_20220414_AnalysisExtent_Durban`, `WV03_20220420_AnalysisExtent_Durban`, `WV03_20220420_AnalysisExtent_Umkomaas_Scottburgh`, `WV03_20220420_AnalysisExtent_Umlazi`, `WV03_20220427_AnalysisExtent_eThekwini_Umgungundlovu`, `WV03_20220427_CloudObstruction_eThekwini_Umgungundlovu`, `WV03_20220504_AnalysisExtent_KwaMakhutha_Umbogintwini`, `WV03_20220504_AnalysisExtent_SilverGreenReserve`.

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

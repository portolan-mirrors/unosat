# Other lines: Volcano, Tonga, 15 January 2022 (VO20220115TON)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/volcanoes/vo20220115ton/vo20220115ton-other-lines/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Other lines for Volcano, Tonga, 15 January 2022 (VO20220115TON): 6 features merged from 6 source layers. Lines layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Damage assessment in 'Ohonua town, 'Eua  Prope district, 'Eua division, Tonga as of 20 & 21 January 2022](https://data.humdata.org/dataset/damage-assessment-in-ohonua-town-eua-prope-district-eua-division-tonga-as-of-20-21-january)
- [Damage assessment in Atata Island, Kolovao district, Tongatapu division, Tonga as of 18 January 2022](https://data.humdata.org/dataset/damage-assessment-in-atata-island-kolovao-district-tongatapu-division-tonga-as-of-18-janua)
- [Damage assessment in Fonoifua Island, Mu'omu'a district, Ha'apai division, Tonga as of 20 January 2022](https://data.humdata.org/dataset/damage-assessment-in-fonoifua-island-mu-omu-a-district-ha-apai-division-tonga-as-of-20-jan)
- [Damage assessment in Mango Island, Mu'omu'a district, Ha'apai division, Tonga as of 18 January 2022 V2](https://data.humdata.org/dataset/damage-assessment-in-mango-island-mu-omu-a-district-ha-apai-division-tonga-as-of-18-januar)
- [Damage assessment in Nomuka Island, Mu'omu'a district, Ha'apai division,Tonga as of 18 January 2022](https://data.humdata.org/dataset/damage-assessment-in-nomuka-island-mu-omu-a-district-ha-apai-division-tonga-as-of-18-janua)
- [Damage assessment in Nomuka village, Mu'omu'a district, Ha'apai division, Nomuka Island, as of 17 January 2022](https://data.humdata.org/dataset/damage-assessment-in-nomuka-village-mu-omu-a-district-ha-apai-division-nomuka-island-as-of)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![geodata](https://img.shields.io/badge/geodata-blue) ![natural disasters](https://img.shields.io/badge/natural_disasters-blue) ![volcano](https://img.shields.io/badge/volcano-blue)

## Spatial Coverage

- **Bounding Box**: [-174.9591267, -21.3420464, -174.710801, -20.2501712]

## Temporal Coverage

- **Start**: 2022-01-17T00:00:00Z
- **End**: 2022-01-21T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SourceID | string |  |
| Picture | binary |  |
| Exs | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Definite; 2 = Doubtful. The decoded text is in `Exs_label`. |
| Notes | string | Free-text notes by the analyst. |
| WaterwayID | string |  |
| ONme | string |  |
| RteNme | string |  |
| Sec | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Good; 2 = Marginal; 3 = Poor. The decoded text is in `Sec_label`. |
| OpStatus | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Open; 2 = Restricted; 3 = Closed; 4 = Abandonned/Disused. The decoded text is in `OpStatus_label`. |
| DrySDepthM | double |  |
| WetSDepthM | double |  |
| AirDraugtM | double |  |
| WtwTpe | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Open Water - Sea; 2 = Open Water - Lake; 3 = Open Water - Pond; 4 = Resevoir; 5 = Navigation in restricted waterways; 6 = River; 7 = Seasonal Stream; 8 = Stream; 9 = Canal. The decoded text is in `WtwTpe_label`. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Staff_ID | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 18 = TH; 22 = WP; 33 = LB; 44 = JL; 45 = MD; 54 = HP; 55 = VG; 57 = PG; 66 = CJ; 70 = SG; 73 = RS; 77 = LD; 88 = HK; 91 = KA; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 141 = KJP; 151 = MNY; 161 = DC; 171 = SR; 181 = NL; 191 = DH; 212 = MH; 213 = JT; 214 = ES; 215 = KB; 216 = JY; 218 = PA; 219 = SS; 222 = CS; 1000 = Unknown. The decoded text is in `Staff_ID_label`. |
| Sensor_ID | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT-4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT-6; 42 = Sentinel-1; 43 = Kompsat-2; 44 = Sentinel-2; 45 = Sentinel-3; 46 = Kompsat-3; 47 = Deimos-2; 48 = TripleSat; 49 = PlanetLabs; 50 = RapidEye; 51 = WorldView-4; 52 = SPOT-7; 999 = Combination of Sensors. The decoded text is in `Sensor_ID_label`. |
| Sensor_Date | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Exs_label | string | `Exs` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| OpStatus_label | string | `OpStatus` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Sec_label | string | `Sec` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Sensor_ID_label | string | `Sensor_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Staff_ID_label | string | `Staff_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| WtwTpe_label | string | `WtwTpe` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./vo20220115ton-other-lines.parquet | 23.9 KB | 12200ae6caef... |
| ./vo20220115ton-other-lines.pmtiles | 24.8 KB | 12204a71ca84... |
| ./styles/default.json | 401 B | 1220b871f844... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./vo20220115ton-other-lines.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/damage-assessment-in-atata-island-kolovao-district-tongatapu-division-tonga-as-of-18-janua](https://data.humdata.org/dataset/damage-assessment-in-atata-island-kolovao-district-tongatapu-division-tonga-as-of-18-janua)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `PHR_20220118_Shoreline_NorthMangoIsland_Tonga`, `PHR_20220118_Shoreline_SW_NomukaIsland_Tonga`, `PHR_20220120_Shoreline_EuaIsland_Tonga`, `WV02_20211113_Shoreline_SW_NomukaIsland_Tonga`, `WV02_20211121_Shoreline_NorthMangoIsland_Tonga`, `WV03_20210914_Shoreline_EuaIsland_Tonga`.

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

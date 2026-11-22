# Water extent lines: Tropical cyclone, Vanuatu, 3 April 2020 (TC20200403VUT)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/tropical-cyclones/2020/tc20200403vut/tc20200403vut-water-extent-lines/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Water extent lines for Tropical cyclone, Vanuatu, 3 April 2020 (TC20200403VUT): 5 features merged from 2 source layers. Lines layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Buildings Damage Assessment & Related Density in South of Sanma Province, Vanuatu](https://data.humdata.org/dataset/buildings-damage-assessment-related-density-in-south-of-sanma-province-vanuatu)
- [Damage Assessment in Ambae Island, Penama Province, Vanuatu](https://data.humdata.org/dataset/damage-assessment-in-ambae-island-penama-province-vanuatu)
- [Damage Assessment in CanalFanafo, Luganville and South East Santo Municipalities, Sanma Province, Vanuatu](https://data.humdata.org/dataset/damage-assessment-in-canalfanafo-luganville-and-south-east-santo-municipalities-sanma-prov)
- [Damage Assessment in Luganville Municipality, Sanma Province, Vanuatu](https://data.humdata.org/dataset/damage-assessment-in-luganville-municipality-sanma-province-vanuatu)
- [Damage Assessment in Maewo Island, Penama Province, Vanuatu](https://data.humdata.org/dataset/damage-assessment-in-maewo-island-penama-province-vanuatu)
- [Damage Assessment in Malampa Province, Vanuatu](https://data.humdata.org/dataset/damage-assessment-in-malampa-province-vanuatu)
- [Damage Assessment in Malo Island, Sanma Province, Vanuatu](https://data.humdata.org/dataset/damage-assessment-in-malo-island-sanma-province-vanuatu)
- [Damage Assessment in Paama Island, Malampa Province, Vanuatu](https://data.humdata.org/dataset/damage-assessment-in-paama-island-malampa-province-vanuatu)
- [Damage Assessment in West Santo and South Santo Municipality, Sanma Province, Vanuatu](https://data.humdata.org/dataset/damage-assessment-in-west-santo-and-south-santo-municipality-sanma-province-vanuatu)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![cyclones-hurricanes-typhoons](https://img.shields.io/badge/cyclones--hurricanes--typhoons-blue) ![geodata](https://img.shields.io/badge/geodata-blue) ![tropical cyclone](https://img.shields.io/badge/tropical_cyclone-blue)

## Spatial Coverage

- **Bounding Box**: [167.75928038300003, -16.490896403999955, 168.18537093300006, -16.098263648999932]

## Temporal Coverage

- **Start**: 2020-04-09T00:00:00Z
- **End**: 2020-04-29T23:59:59Z

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
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Staff_ID | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 22 = WP; 33 = LB; 44 = JL; 55 = VG; 66 = CJ; 73 = RS; 77 = LD; 88 = HK; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 141 = KJP; 151 = MNY; 222 = CS; 1000 = Unknown. The decoded text is in `Staff_ID_label`. |
| Sensor_ID | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT 6; 42 = Sentinel-1; 43 = Komsat-2; 999 = Combination of Sensors. The decoded text is in `Sensor_ID_label`. |
| Sensor_Date | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
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
| ./tc20200403vut-water-extent-lines.parquet | 11.2 KB | 12209e5e4818... |
| ./tc20200403vut-water-extent-lines.pmtiles | 23.1 KB | 12200333ecb2... |
| ./styles/default.json | 429 B | 1220dea64e35... |
| ./tc20200403vut-water-extent-lines.thumb.jpg | 5.2 KB | 1220b9e31d00... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./tc20200403vut-water-extent-lines.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/buildings-damage-assessment-related-density-in-south-of-sanma-province-vanuatu](https://data.humdata.org/dataset/buildings-damage-assessment-related-density-in-south-of-sanma-province-vanuatu)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Waterways_AOI4_PortSandwich`, `Waterways_AOI8_Oral`.

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

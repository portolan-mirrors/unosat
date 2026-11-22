# Water extent: Flood, South Sudan, 10 January 2025 (FL20250110SSD)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2025/fl20250110ssd/fl20250110ssd-water-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Water extent for Flood, South Sudan, 10 January 2025 (FL20250110SSD): 26,933 features merged from 896 source layers. Polygon layers with a water class column (such as `Water_Class`), or whose names mention flood, water, or inundation: satellite-detected water. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Satellite detected water extents between 01 and 05 February 2025 over South Sudan](https://data.humdata.org/dataset/satellite-detected-water-extents-between-01-and-05-february-2025-over-south-sudan)
- [Satellite detected water extents between 01 and 05 March 2025 over South Sudan](https://data.humdata.org/dataset/satellite-detected-water-extents-between-01-and-05-march-2025-over-south-sudan)
- [Satellite detected water extents between 04 and 08 January 2025 over South Sudan](https://data.humdata.org/dataset/satellite-detected-water-extents-between-04-and-08-january-2025-over-south-sudan)
- [Satellite detected water extents between 13 and 17 August 2025 over South Sudan](https://data.humdata.org/dataset/satellite-detected-water-extents-between-13-and-17-august-2025-over-south-sudan)
- [Satellite detected water extents between 15 and 19 March 2025 over South Sudan](https://data.humdata.org/dataset/satellite-detected-water-extents-between-15-and-19-march-2025-over-south-sudan)
- [Satellite detected water extents between 18 and 22 January 2025 over South Sudan](https://data.humdata.org/dataset/satellite-detected-water-extents-between-18-and-22-january-2025-over-south-sudan)
- [Satellite detected water extents between 25 and 29 April 2025 over South Sudan](https://data.humdata.org/dataset/satellite-detected-water-extents-between-25-and-29-april-2025-over-south-sudan)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [24.178584176000072, 3.5048517790000915, 35.95158011400008, 12.238331947010021]

## Temporal Coverage

- **Start**: 2025-01-10T00:00:00Z
- **End**: 2025-08-20T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Water_Class | int16 | Coded value. The source geodatabase domain gives: 0 = Archive Water Extent / Pre-Flood Water; 1 = Flood Water; 2 = Satellite Detected Water / Possible Saturated Soil; 3 = Probable Flash Flood-Affected Land; 4 = Aquaculture; 5 = Possible Satuated, wet soil; 6 = Tsunami-Affected Land; 7 = Maximum Satellite Observed Water (Cumulative); 8 = Swamp / Marsh / Mangrove; 9 = Snow Cover. The decoded text is in `Water_Class_label`. |
| Sensor_ID | string | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT-4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT-6; 42 = Sentinel-1; 43 = Kompsat-2; 44 = Sentinel-2; 45 = Sentinel-3; 46 = Kompsat-3; 47 = Deimos-2; 48 = TripleSat; 49 = PlanetLabs; 50 = RapidEye; 51 = WorldView-4; 52 = SPOT-7; 53 = VIIRS-NOAA; 999 = Combination of Sensors. The decoded text is in `Sensor_ID_label`. |
| Sensor_Date | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence_ID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `Confidence_ID_label`. |
| Field_Validation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `Field_Validation_label`. |
| Water_StatusID | int32 | Coded value. The source geodatabase domain gives: 1 = New Water / Water Increase; 2 = No water change / Static Level; 3 = No water / Water levels decreased. The decoded text is in `Water_StatusID_label`. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| SenorID_old | int16 | Coded value. The source geodatabase domain gives: 1 = MODIS; 2 = ASAR WSM; 3 = ASAR IMP; 4 = Radarsat; 5 = DMC; 6 = SPOT5; 7 = ALOS Palsar WB1; 8 = ASAR APP. The decoded text is in `SenorID_old_label`. |
| StaffID | string | Coded value. The source geodatabase domain gives: 11 = EB; 18 = TH; 22 = WP; 33 = LB; 44 = JL; 45 = MD; 54 = HP; 55 = VG; 57 = PG; 66 = CJ; 70 = SG; 73 = RS; 77 = LD; 88 = HK; 91 = KA; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 141 = KJP; 151 = MNY; 161 = DC; 171 = SR; 181 = NL; 191 = DH; 212 = MH; 213 = JT; 214 = ES; 215 = KB; 216 = JY; 218 = PA; 219 = SS; 220 = IS; 221 = DS; 222 = CS; 1000 = Unknown. The decoded text is in `StaffID_label`. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Confidence_ID_label | string | `Confidence_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Field_Validation_label | string | `Field_Validation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SenorID_old_label | string | `SenorID_old` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Sensor_ID_label | string | `Sensor_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Water_Class_label | string | `Water_Class` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Water_StatusID_label | string | `Water_StatusID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| Area_km2 | double | Area in square kilometres, as UNOSAT computed it. |
| Pop | double |  |
| Adm0 | string |  |
| Adm1 | string |  |
| Adm2 | string |  |
| SHAPE_Leng | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Water_Clas | string |  |
| Sensor_Dat | date32[day] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence | string |  |
| Field_Vali | string |  |
| Water_Stat | string |  |
| SenorID_ol | string |  |
| d_Water_Cl | string |  |
| d_Sensor_I | string |  |
| d_Confiden | string |  |
| d_Field_Va | string |  |
| d_Water_St | string |  |
| d_SenorID_ | string |  |
| d_StaffID | string |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20250110ssd-water-extent.parquet | 28.2 MB | 122039ba0146... |
| ./fl20250110ssd-water-extent.pmtiles | 175.4 MB | 1220d0aebec0... |
| ./styles/default.json | 1.1 KB | 12203c4dd052... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20250110ssd-water-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/satellite-detected-water-extents-between-01-and-05-february-2025-over-south-sudan](https://data.humdata.org/dataset/satellite-detected-water-extents-between-01-and-05-february-2025-over-south-sudan)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `VIIRS_20190930_20191019_FloodExtent_SouthSudan`, `VIIRS_20200920_20201019_FloodExtent_SouthSudan`, `VIIRS_20210919_20211018_FloodExtent_SouthSudan`, `VIIRS_20210926_20210930_FloodExtent_SouthSudan`, `VIIRS_20211009_20211013_FloodExtent_SouthSudan`, `VIIRS_20211015_20211019_FloodExtent_SouthSudan`, `VIIRS_20211020_20211024_FloodExtent_SouthSudan`, `VIIRS_20211103_20211107_FloodExtent_SouthSudan`, `VIIRS_20211103_20211107_PermanentWater_SouthSudan`, `VIIRS_20211119_20211123_FloodExtent_SouthSudan`, `VIIRS_20211119_20211123_PermanentWater_SouthSudan`, `VIIRS_20220110_20220114_MaximumFloodWaterExtent_SouthSudan`, `VIIRS_20220115_20220119_MaximumFloodWaterExtent_SouthSudan`, `VIIRS_20220115_20220119_PermanentWater_SouthSudan`, `VIIRS_20220223_20220227_MaximumFloodWaterExtent_SouthSudan`, `VIIRS_20220223_20220227_PermanentWater_SouthSudan`, `VIIRS_20220305_20220309_MaximumFloodWaterExtent_SouthSudan`, `VIIRS_20220305_20220309_PermanentWater_SouthSudan`, `VIIRS_20220310_20220314_MaximumFloodWaterExtent_SouthSudan`, `VIIRS_20220310_20220314_PermanentWater_SouthSudan`, `VIIRS_20220401_20220405_MaximumFloodWaterExtent_SouthSudan`, `VIIRS_20220401_20220405_PermanentWater_SouthSudan`, `VIIRS_20220420_20220424_MaximumFloodWaterExtent_SouthSudan`, `VIIRS_20220420_20220424_PermanentWater_SouthSudan`, `VIIRS_20220514_20220518_MaximumFloodWaterExtent_SouthSudan`, `VIIRS_20220514_20220518_PermanentWater_SouthSudan`, `VIIRS_20220525_20220529_MaximumFloodWaterExtent_SouthSudan`, `VIIRS_20220525_20220529_PermanentWater_SouthSudan`, `VIIRS_20220608_20220612_MaximumFloodWater_SouthSudan`, `VIIRS_20220608_20220612_PermanentWater_SouthSudan`, `VIIRS_20220719_20220723_MaximumFloodWater_SouthSudan`, `VIIRS_20220719_20220723_PermanentWater_SouthSudan`, `VIIRS_20220803_20220807_MaximumFloodWater_SouthSudan`, `VIIRS_20220803_20220807_PermanentWater_SouthSudan`, `VIIRS_20220830_20220903_MaximumFloodWaterExtent_SouthSudan`, `VIIRS_20220830_20220903_PermanentWater_SouthSudan`, `VIIRS_20220910_20220914_MaximumFloodWaterExtent_SouthSudan`, `VIIRS_20220910_20220914_PermanentWater_SouthSudan`, `VIIRS_20221004_20221008_MaximumFloodWaterExtent_SouthSudan`, `VIIRS_20221004_20221008_PermanentWater_SouthSudan` and 93 more.

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

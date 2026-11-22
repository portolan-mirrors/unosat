# Water extent: Flood, Chad, 20 August 2024 (FL20240820TCD)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2024/fl20240820tcd/fl20240820tcd-water-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Water extent for Flood, Chad, 20 August 2024 (FL20240820TCD): 87 features merged from 75 source layers. Polygon layers with a water class column (such as `Water_Class`), or whose names mention flood, water, or inundation: satellite-detected water. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Satellite detected water extent in Bongor City as of 26 August 2024](https://data.humdata.org/dataset/satellite-detected-water-extent-in-bongor-city-as-of-26-august-2024)
- [Satellite detected water extent in Koukou Angarana City, Sila Region, Chad as of 3 September 2024](https://data.humdata.org/dataset/water-extent-in-koukou-angarana-city-sila-region-chad-as-of-3-september-2024)
- [Satellite detected water extent in N'Djamena City as of 08 October 2024](https://data.humdata.org/dataset/satellite-detected-water-extent-in-n-djamena-city-as-of-08-october-2024)
- [Satellite detected water extent in N'Djamena City as of 26 August 2024](https://data.humdata.org/dataset/satellite-detected-water-extent-in-n-djamena-city-as-of-26-august-2024)
- [Satellite detected water extents between 02 and 06 October 2024 over Chad](https://data.humdata.org/dataset/satellite-detected-water-extents-between-02-and-06-october-2024-over-chad)
- [Satellite detected water extents between 13 and 17 October 2024 over Chad](https://data.humdata.org/dataset/satellite-detected-water-extents-between-13-and-17-october-2024-over-chad)
- [Satellite detected water extents between 15 and 19 August 2024 over Chad](https://data.humdata.org/dataset/satellite-detected-water-extents-between-15-and-19-august-2024-over-chad)
- [Satellite detected water extents between 20 and 24 August 2024 over Chad](https://data.humdata.org/dataset/satellite-detected-water-extents-between-20-and-24-august-2024-over-chad)
- [Satellite detected water extents between 31 August and 04 September 2024 over Chad](https://data.humdata.org/dataset/satellite-detected-water-extents-between-31-august-and-04-september-2024-over-chad)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [13.51160425900008, 7.4669518550000475, 23.99312417300007, 22.60520385800004]

## Temporal Coverage

- **Start**: 2024-08-20T00:00:00Z
- **End**: 2024-10-18T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Water_Class | int16 | Coded value. The source geodatabase domain gives: 0 = Archive Water Extent / Pre-Flood Water; 1 = Flood Water; 2 = Satellite Detected Water / Possible Saturated Soil; 3 = Probable Flash Flood-Affected Land; 4 = Aquaculture; 5 = Possible Satuated, wet soil; 6 = Tsunami-Affected Land; 7 = Maximum Satellite Observed Water (Cumulative); 8 = Swamp / Marsh / Mangrove; 9 = Snow Cover. The decoded text is in `Water_Class_label`. |
| Sensor_ID | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT-4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT-6; 42 = Sentinel-1; 43 = Kompsat-2; 44 = Sentinel-2; 45 = Sentinel-3; 46 = Kompsat-3; 47 = Deimos-2; 48 = TripleSat; 49 = PlanetLabs; 50 = RapidEye; 51 = WorldView-4; 52 = SPOT-7; 53 = Jilin-1; 54 = GaoFen-2; 55 = SkySat; 56 = ICEYE; 57 = Landsat-9; 58 = VIIRS-NOAA; 59 = RCM-1; 60 = RCM-2; 61 = RCM-3; 62 = TanDEM-X; 63 = BlackSky; …. The decoded text is in `Sensor_ID_label`. |
| Sensor_Date | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence_ID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `Confidence_ID_label`. |
| Field_Validation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `Field_Validation_label`. |
| Water_StatusID | int32 | Coded value. The source geodatabase domain gives: 1 = New Water / Water Increase; 2 = No water change / Static Level; 3 = No water / Water levels decreased. The decoded text is in `Water_StatusID_label`. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| SenorID_old | int16 | Coded value. The source geodatabase domain gives: 1 = MODIS; 2 = ASAR WSM; 3 = ASAR IMP; 4 = Radarsat; 5 = DMC; 6 = SPOT5; 7 = ALOS Palsar WB1; 8 = ASAR APP. The decoded text is in `SenorID_old_label`. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| StaffID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
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
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20240820tcd-water-extent.parquet | 115.7 MB | 122089ceda45... |
| ./fl20240820tcd-water-extent.pmtiles | 31.2 MB | 1220bcd81f79... |
| ./styles/default.json | 1.1 KB | 122076bc4ab4... |
| ./fl20240820tcd-water-extent.thumb.jpg | 28.0 KB | 1220f8789d4b... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20240820tcd-water-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/satellite-detected-water-extent-in-bongor-city-as-of-26-august-2024](https://data.humdata.org/dataset/satellite-detected-water-extent-in-bongor-city-as-of-26-august-2024)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `PlanetScope_20240826_FloodExtent_Bongor`, `PlanetScope_20240826_FloodExtent_NDjamena`, `PlanetScope_20240826_WaterExtent_Bongor`, `PlanetScope_20240826_WaterExtent_NDjamena`, `Pleiades_20240903_FloodExtent_Koukou`, `VIIRS_20240815_20240819_MaximumFloodWaterExtent_Chad`, `VIIRS_20240815_20240819_PermanentWater_Chad`, `VIIRS_20240820_20240824_MaximumFloodWaterExtent_Chad`, `VIIRS_20240831_20240904_MaximumFloodWaterExtent_Chad`, `VIIRS_20240831_20240904_PermanentWater_Chad`, `VIIRS_20241002_20241006_MaximumFloodWaterExtent_Chad`, `VIIRS_20241002_20241006_PermanentWater_Chad`, `VIIRS_20241013_20241017_MaximumFloodWaterExtent_Chad`, `VIIRS_20241013_20241017_PermanentWater_Chad`, `WV02_20241008_WaterExtent_NDjamena`.

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

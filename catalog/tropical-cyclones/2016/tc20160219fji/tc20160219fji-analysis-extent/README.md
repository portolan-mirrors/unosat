# Analysis extent: Tropical cyclone, Fiji, 19 February 2016 (TC20160219FJI)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/tropical-cyclones/2016/tc20160219fji/tc20160219fji-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Analysis extent for Tropical cyclone, Fiji, 19 February 2016 (TC20160219FJI): 7 features merged from 7 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of Damage Assessment in Greater Lautoka Area, Ba Province, Western Division, Fiji](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-greater-lautoka-area-ba-province-western-divi-february-25-2016)
- [Geodata of Damage Assessment in Sasa Area, Ba Province, Western Division, Fiji](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-sasa-area-ba-province-western-division-fiji-march-03-2016)
- [Geodata of Damage Assessment in Vatukoula Area, Ba Province, Western Division, Fiji](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-vatukoula-area-ba-province-western-division-f-march-02-2016)
- [Geodata of Damage Assessment over north and west of Ba Town, Ba Province, Western Division, Fiji](https://data.humdata.org/dataset/geodata-of-damage-assessment-over-north-and-west-of-ba-town-ba-province-weste-march-03-2016)
- [Geodata of Population Exposure Analysis - Tropical Cyclone Winston - 19 February 2016](https://data.humdata.org/dataset/geodata-of-population-exposure-analysis-tropical-cyclone-winston-19-february-march-09-2016)
- [Geodata of Population Exposure Analysis - Tropical Cyclone Winston - 22 February 2016](https://data.humdata.org/dataset/geodata-of-population-exposure-analysis-tropical-cyclone-winston-22-february-march-09-2016)
- [Geodata of Satellite Detected Waters in Savu Area, Naitasiri Province, Central Division, Fiji](https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-in-savu-area-naitasiri-province-central-february-22-2016)
- [Geodata of UNOSAT Damage Assessment Activities in Viti Levu Island, Fiji](https://data.humdata.org/dataset/geodata-of-unosat-damage-assessment-activities-in-viti-levu-island-fiji-march-10-2016)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![cyclones-hurricanes-typhoons](https://img.shields.io/badge/cyclones--hurricanes--typhoons-blue) ![geodata](https://img.shields.io/badge/geodata-blue) ![tropical cyclone](https://img.shields.io/badge/tropical_cyclone-blue)

## Spatial Coverage

- **Bounding Box**: [177.39654764600004, -18.234660497999926, 178.8203683710001, -17.336882979999928]

## Temporal Coverage

- **Start**: 2016-02-22T00:00:00Z
- **End**: 2016-03-10T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Water_Class | int16 | Coded value. The source geodatabase domain gives: 0 = Preflood Water; 1 = Flood Water; 2 = Flood-Affected Land / Possible Flood water; 3 = Probable Flash Flood-Affected Land; 4 = Satellite Detected Waters; 6 = Possible Saturated, wet Soil/ possible Flood Water; 9 = Aquaculture (Wet Rice); 14 = Tsunami-Affected Land; 99 = Maximum Flood Water Extent (Cumulative). The decoded text is in `Water_Class_label`. |
| Sensor_ID | int32 | Coded value. The source geodatabase domain gives: 1 = Worldview-1; 2 = Worldview-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = Komsat-2; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleadies; 999 = Combination of Sensors. The decoded text is in `Sensor_ID_label`. |
| Sensor_Date | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence_ID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `Confidence_ID_label`. |
| Field_Validation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `Field_Validation_label`. |
| Water_StatusID | int32 | Coded value. The source geodatabase domain gives: 1 = New Water / Water Increase; 2 = No water change / Static Level; 3 = No water / Water levels decreased. The decoded text is in `Water_StatusID_label`. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| SenorID_old | int16 | Coded value. The source geodatabase domain gives: 1 = MODIS; 2 = ASAR WSM; 3 = ASAR IMP; 4 = Radarsat; 5 = DMC; 6 = SPOT5; 7 = ALOS Palsar WB1; 8 = ASAR APP. The decoded text is in `SenorID_old_label`. |
| StaffID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `StaffID_label`, which is decoded per source file. |
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
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT 6; 42 = Sentinel-1; 43 = Komsat-2; 999 = Combination of Sensors. The decoded text is in `SensorID_label`. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./tc20160219fji-analysis-extent.parquet | 8.3 KB | 12202796079a... |
| ./tc20160219fji-analysis-extent.pmtiles | 114.7 KB | 1220de2d6327... |
| ./styles/default.json | 671 B | 1220cacf5522... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./tc20160219fji-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-damage-assessment-in-greater-lautoka-area-ba-province-western-divi-february-25-2016](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-greater-lautoka-area-ba-province-western-divi-february-25-2016)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `PL_20160222_Lautoka_Analysis_Extent`, `PL_20160222_Nausori_Analysis_Extent`, `PL_20160226_Sassa_Damage_Analysis_Extent`, `PL_20160226_Vatukoula_Analysis_Extent`, `PL_20160226_West_Ba_Analysis_Extent`, `PL_20160228_Rakiraki_Analysis_Extent`, `RS2_20160221_Savu_AnalysisExtent`.

## Attribution

UNITAR-UNOSAT

## License

[CC-BY-NC-SA-3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/)

## Contact

Portolan Mirrors <nissim@radiant.earth>

## Known Issues

This is a preliminary assessment and has not yet been validated in the field. It is important to consider the characteristics of the source imagery used in the analyses when interpreting results. For damage assessments it should be noted that only significant damage to the structural integrity of the buildings analyzed can be seen in imagery, while minor damage such as cracks or holes may not be visible at all. For flood extractions using radar data it is important to note that urban areas and highly vegetated areas may mask the flood signature and result in underestimation of flood waters. Users with specific questions or concerns should contact unosat@unitar.org to seek clarification.

---

*Generated by [Portolan](https://github.com/portolan-sdi/portolan-cli) from STAC metadata and .portolan/metadata.yaml*

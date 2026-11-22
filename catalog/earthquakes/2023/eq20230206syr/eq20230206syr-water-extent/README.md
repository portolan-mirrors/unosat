# Water extent: Earthquake, Syrian Arab Republic, Türkiye, 6 February 2023 (EQ20230206SYR)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/earthquakes/2023/eq20230206syr/eq20230206syr-water-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Water extent for Earthquake, Syrian Arab Republic, Türkiye, 6 February 2023 (EQ20230206SYR): 34 features merged from 34 source layers. Polygon layers with a water class column (such as `Water_Class`), or whose names mention flood, water, or inundation: satellite-detected water. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [6 February 2023 M 7.8 Marash/Antep (Kehramanmarash) Earthquake, Preliminary Satellite-Based Comprehensive Damage Assessment Report](https://data.humdata.org/dataset/6-february-2023-m-7-8-marash-antep-kehramanmarash-earthquake-preliminary-satellite-based-c)
- [Damage Assessment  in Jableh City, Jableh District, Latakia Province, Syria as of 9 February 2023](https://data.humdata.org/dataset/damage-assessment-in-jableh-city-jableh-district-latakia-province-syria-as-of-9-february-2)
- [Damage Assessment Istamo (Latakia) as of 9 February 2023](https://data.humdata.org/dataset/damage-assessment-istamo-latakia-as-of-9-february-2023)
- [Damage Assessment in A'zaz City, Aleppo Governorate, Syria as of 9 February 2023](https://data.humdata.org/dataset/damage-assessment-in-a-zaz-city-aleppo-governorate-syria-as-of-9-february-2023)
- [Damage Assessment in Al Bab, Qabasin and Bza'a towns, Syria as of 11 February 2023](https://data.humdata.org/dataset/damage-assessment-in-al-bab-qabasin-and-bza-a-towns-syria-as-of-11-february-2023)
- [Damage Assessment in Al Bab, Syria as of 11 February 2023](https://data.humdata.org/dataset/damage-assessment-in-al-bab-syria-as-of-11-february-2023)
- [Damage Assessment in Idlib City, Syria as of 9 February 2023](https://data.humdata.org/dataset/damage-assessment-in-idlib-city-syria-as-of-9-february-2023)
- [Damage Assessment in Jindires and the surrounding area, Syria as of 10 February 2023](https://data.humdata.org/dataset/damage-assessment-in-jindires-and-the-surrounding-area-syria-as-of-10-february-2023)
- [Damage Assessment in Jindires, Afrin District, Aleppo Governorate, Syria as of 11 February 2023](https://data.humdata.org/dataset/damage-assessment-in-jindires-afrin-district-aleppo-governorate-syria-as-of-11-february-20)
- [Damage Assessment in Jisr al-Shughur City (Idleb) as of 9 February 2023](https://data.humdata.org/dataset/damage-assessment-in-jisr-al-shughur-city-idleb-as-of-9-february-2023)
- [Damage Assessment in Killi (Idlib District), Syria as of 16 February 2023](https://data.humdata.org/dataset/damage-assessment-in-killi-idlib-district-syria-as-of-16-february-2023)
- [Damage Assessment in Lilawa Village, Jarablus District, Aleppo Governorate, Syria as of 7 February 2023](https://data.humdata.org/dataset/damage-assessment-in-lilawa-village-jarablus-district-aleppo-governorate-syria-as-of-7-feb)
- and 5 more; the event's [catalog page](../catalog.json) lists them all.

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![earthquake](https://img.shields.io/badge/earthquake-blue) ![earthquake-tsunami](https://img.shields.io/badge/earthquake--tsunami-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [36.342603043000054, 36.012132429000076, 36.42847399100009, 36.25643295400005]

## Temporal Coverage

- **Start**: 2023-02-08T00:00:00Z
- **End**: 2023-03-16T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Water_Class | int16 | Coded value. The source geodatabase domain gives: 0 = Archive Water Extent / Pre-Flood Water; 1 = Flood Water; 2 = Satellite Detected Water / Possible Saturated Soil; 3 = Probable Flash Flood-Affected Land; 4 = Aquaculture; 5 = Possible Satuated, wet soil; 6 = Tsunami-Affected Land; 7 = Maximum Satellite Observed Water (Cumulative); 8 = Swamp / Marsh / Mangrove; 9 = Snow Cover. The decoded text is in `Water_Class_label`. |
| Sensor_ID | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT-4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT-6; 42 = Sentinel-1; 43 = Kompsat-2; 44 = Sentinel-2; 45 = Sentinel-3; 46 = Kompsat-3; 47 = Deimos-2; 48 = TripleSat; 49 = PlanetLabs; 50 = RapidEye; 51 = WorldView-4; 52 = SPOT-7; 999 = Combination of Sensors. The decoded text is in `Sensor_ID_label`. |
| Sensor_Date | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence_ID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `Confidence_ID_label`. |
| Field_Validation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `Field_Validation_label`. |
| Water_StatusID | int32 | Coded value. The source geodatabase domain gives: 1 = New Water / Water Increase; 2 = No water change / Static Level; 3 = No water / Water levels decreased. The decoded text is in `Water_StatusID_label`. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| SenorID_old | int16 | Coded value. The source geodatabase domain gives: 1 = MODIS; 2 = ASAR WSM; 3 = ASAR IMP; 4 = Radarsat; 5 = DMC; 6 = SPOT5; 7 = ALOS Palsar WB1; 8 = ASAR APP. The decoded text is in `SenorID_old_label`. |
| StaffID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `StaffID_label`, which is decoded per source file. |
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
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./eq20230206syr-water-extent.parquet | 112.2 KB | 122058312588... |
| ./eq20230206syr-water-extent.pmtiles | 123.5 KB | 12204dec1d01... |
| ./styles/default.json | 887 B | 1220d154f3f1... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./eq20230206syr-water-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/6-february-2023-m-7-8-marash-antep-kehramanmarash-earthquake-preliminary-satellite-based-c](https://data.humdata.org/dataset/6-february-2023-m-7-8-marash-antep-kehramanmarash-earthquake-preliminary-satellite-based-c)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `S2_20230209_FloodExtent_Jakarah_Syria`, `S2_20230214_FloodExtent_Jakarah_Syria`.

## Attribution

UNITAR-UNOSAT

## License

[other](https://opendefinition.org/licenses/cc-by-sa/)

## Contact

Portolan Mirrors <nissim@radiant.earth>

## Known Issues

HDX states the license as "Creative Commons Attribution Share-Alike (CC BY-SA)" with no version, so the collection's license is `other`, linked to the license definition HDX gives. This is a preliminary assessment and has not yet been validated in the field. It is important to consider the characteristics of the source imagery used in the analyses when interpreting results. For damage assessments it should be noted that only significant damage to the structural integrity of the buildings analyzed can be seen in imagery, while minor damage such as cracks or holes may not be visible at all. For flood extractions using radar data it is important to note that urban areas and highly vegetated areas may mask the flood signature and result in underestimation of flood waters. Users with specific questions or concerns should contact unosat@unitar.org to seek clarification. This is a preliminary assessment and has not yet been validated in the field. It is important to consider the characteristics of the source imagery used in the analyses when interpreting results. For damage assessments it should be noted that only significant damage to the structural integrity of the buildings analyzed can be seen in imagery, while minor damage such as cracks or holes may not be visible at all. For flood extractions using radar data it is important to note that urban areas and highly vegetated areas may mask the flood signature and result in underestimation of flood waters. Users with specific questions or concerns should contact unosat@unitar.org to seek clarification.
Glide: EQ-2023-000015-TUR

---

*Generated by [Portolan](https://github.com/portolan-sdi/portolan-cli) from STAC metadata and .portolan/metadata.yaml*

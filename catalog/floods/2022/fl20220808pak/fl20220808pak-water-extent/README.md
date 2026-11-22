# Water extent: Flood, Pakistan, 8 August 2022 (FL20220808PAK)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2022/fl20220808pak/fl20220808pak-water-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Water extent for Flood, Pakistan, 8 August 2022 (FL20220808PAK): 224 features merged from 161 source layers. Polygon layers with a water class column (such as `Water_Class`), or whose names mention flood, water, or inundation: satellite-detected water. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Preliminary Satellite Derived Flood Evolution Assessment, Islamic Republic of Pakistan-11 October 2022](https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-islamic-republic-of-pakistan-11-o)
- [Preliminary Satellite Derived Flood Evolution Assessment, Islamic Republic of Pakistan-19 October 2022](https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-islamic-republic-of-pakistan-19-o)
- [Preliminary Satellite Derived Flood Evolution Assessment, Islamic Republic of Pakistan-4 October 2022](https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-islamic-republic-of-pakistan-4-oc)
- [Preliminary satellite-derived flood evolution assessment - 16 September 2022](https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-16-september-2022)
- [Preliminary satellite-derived flood evolution assessment - 23 September 2022](https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-23-september-2022)
- [Satellite detected water extent in Khairpur Nathan Shah Town, Sindh Province, Pakistan as of 31 August 2022](https://data.humdata.org/dataset/water-extent-in-khairpur-nathan-shah-town-sindh-province-pakistan-as-of-31-august-2022)
- [Satellite detected water extent in Sindh Province, Pakistan as of 31 August 2022](https://data.humdata.org/dataset/satellite-detected-water-extent-in-sindh-province-pakistan-as-of-31-august-2022)
- [Satellite detected water extent in Sindh province, Pakistan, as of 06 August 2022](https://data.humdata.org/dataset/satellite-detected-water-extent-in-sindh-province-pakistan-as-of-06-august-2022)
- [Satellite detected water extent in Sindh province, Pakistan, as of 15 August 2022](https://data.humdata.org/dataset/satellite-detected-water-extent-in-sindh-province-pakistan-as-of-15-august-2022)
- [Satellite detected water extents between 01 and 07 September 2022 over Pakistan](https://data.humdata.org/dataset/satellite-detected-water-extents-between-01-and-07-september-2022-over-pakistan)
- [Satellite detected water extents between 01 and 29 August 2022 over Pakistan](https://data.humdata.org/dataset/satellite-detected-water-extents-between-01-and-29-august-2022-over-pakistan)
- [Satellite detected water extents between 03 and 23 August 2022 over Pakistan](https://data.humdata.org/dataset/satellite-detected-water-extents-between-03-and-23-august-2022-over-pakistan)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [61.271244024000055, 23.70784787900004, 77.62004405000005, 37.02859184700009]

## Temporal Coverage

- **Start**: 2022-08-10T00:00:00Z
- **End**: 2022-10-19T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Water_Class | int16 | Coded value. The source geodatabase domain gives: 0 = Archive Water Extent / Pre-Flood Water; 1 = Flood Water; 2 = Satellite Detected Water / Possible Saturated Soil; 3 = Probable Flash Flood-Affected Land; 4 = Aquaculture; 5 = Possible Satuated, wet soil; 6 = Tsunami-Affected Land; 7 = Maximum Satellite Observed Water (Cumulative); 8 = Swamp / Marsh / Mangrove; 9 = Snow Cover. The decoded text is in `Water_Class_label`. |
| Sensor_ID | string | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Sensor_ID_label`, which is decoded per source file. |
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
| StaffID | string | Coded value. The source geodatabase domain gives: 11 = EB; 18 = TH; 22 = WP; 33 = LB; 44 = JL; 45 = MD; 54 = HP; 55 = VG; 57 = PG; 66 = CJ; 70 = SG; 73 = RS; 77 = LD; 88 = HK; 91 = KA; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 141 = KJP; 151 = MNY; 161 = DC; 171 = SR; 181 = NL; 191 = DH; 212 = MH; 213 = JT; 214 = ES; 215 = KB; 216 = JY; 218 = PA; 219 = SS; 222 = CS; 1000 = Unknown. The decoded text is in `StaffID_label`. |
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
| Water_Clas | string |  |
| Sensor_Dat | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence | string |  |
| Field_Vali | string |  |
| Water_Stat | string |  |
| SenorID_ol | string |  |
| SHAPE_Leng | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Grid | int32 |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20220808pak-water-extent.parquet | 300.1 MB | 1220b08e7721... |
| ./fl20220808pak-water-extent.pmtiles | 413.0 MB | 1220628c04c8... |
| ./styles/default.json | 972 B | 1220a2ba3787... |
| ./fl20220808pak-water-extent.thumb.jpg | 12.8 KB | 122052d76642... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20220808pak-water-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-16-september-2022](https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-16-september-2022)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `LS8_20220829_FloodExtent_Punjab_Sindh`, `LS8_20220829_WaterExtent_Punjab_Sindh`, `S1_20220806_FloodExtent_Sindh`, `S1_20220806_WaterExtent_Sindh`, `S1_20220815_FloodExtent_SindhProvince`, `S1_20220815_WaterExtent_SindhProvince`, `S1_20220827_FloodExtent_Sindh_Balochistan`, `S2_20220831_FloodExtent_Sindh`, `S2_20220831_WaterExtent_Sindh`, `Terra_Modis_20100827_FloodExtent_PAK`, `Terra_Modis_20220827_20220828_FloodExtent_PAK`, `VIIRS_20220701_20220831_FloodExtent_PAK`, `VIIRS_20220712_20220721_FloodExtent_PAK`, `VIIRS_20220801_20220829_FloodExtent_PAK`, `VIIRS_20220801_20220831_FloodExtent_PAK`, `VIIRS_20220803_20220823_FloodExtent_PAK`, `VIIRS_20220825_20220831_FloodExtent_PAK`, `VIIRS_20220901_20220907_FloodExtent_PAK`, `VIIRS_20220908_20220914_FloodExtent_PAK`, `VIIRS_20220915_20220921_FloodExtent_PAK`, `VIIRS_20220926_20221002_FloodExtent_PAK`, `VIIRS_20221003_20221009_FloodExtent_PAK`, `VIIRS_20221011_20221017_FloodExtent_PAK`.

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

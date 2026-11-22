# Water extent: Flood, Sudan, 15 August 2019 (FL20190815SDN)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2019/fl20190815sdn/fl20190815sdn-water-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Water extent for Flood, Sudan, 15 August 2019 (FL20190815SDN): 5,814 features merged from 8 source layers. Polygon layers with a water class column (such as `Water_Class`), or whose names mention flood, water, or inundation: satellite-detected water. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Preliminary satellite derived flood assessment in White Nile State, Sudan](https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-in-white-nile-state-sudan)
- [Satellite detected water extents, as of 25 August 2019 over White Nile, Sennar and El Gazira states in Sudan](https://data.humdata.org/dataset/water-extents-as-of-25-august-2019-over-white-nile-sennar-and-el-gazira-states-in-sudan)
- [Satellite detected water extents, as of 27 Aug 2019 over White Nile State, Sudan](https://data.humdata.org/dataset/satellite-detected-water-extents-as-of-27-aug-2019-over-white-nile-state-sudan)
- [Satellite detected water extents, as of 28 Aug 2019 over White Nile State, Sudan](https://data.humdata.org/dataset/satellite-detected-water-extents-as-of-28-aug-2019-over-white-nile-state-sudan)
- [Satellite detected water extents, as of 28 August 2019 over Aljammalab region, White Nile State, Sudan](https://data.humdata.org/dataset/water-extents-as-of-28-august-2019-over-aljammalab-region-white-nile-state-sudan)
- [Satellite detected water extents, as of 28 August 2019 over North Al Tura, White Nile State, Sudan](https://data.humdata.org/dataset/water-extents-as-of-28-august-2019-over-north-al-tura-white-nile-state-sudan)
- [Satellite detected waters extents, as of 16 August 2019 over Khartoum, EI Gazira and White Nile State, Sudan](https://data.humdata.org/dataset/waters-extents-as-of-16-august-2019-over-khartoum-ei-gazira-and-white-nile-state-sudan)
- [Satellite detected waters extents, as of 16 August 2019 over White Nile State, Sudan](https://data.humdata.org/dataset/satellite-detected-waters-extents-as-of-16-august-2019-over-white-nile-state-sudan)
- [Satellite detected waters extents, as of 28 August 2019 over  Khartoum State, Sudan](https://data.humdata.org/dataset/satellite-detected-waters-extents-as-of-28-august-2019-over-khartoum-state-sudan)
- [Satellite detected waters extents, as of 28 August 2019 over Sennar State, Sudan](https://data.humdata.org/dataset/satellite-detected-waters-extents-as-of-28-august-2019-over-sennar-state-sudan)
- [Satellite detected waters in Red Sea District as of 15 August 2019](https://data.humdata.org/dataset/satellite-detected-waters-in-red-sea-district-as-of-15-august-2019)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [24.00337200000007, 3.0002640000000724, 38.125527598000076, 21.000000000000057]

## Temporal Coverage

- **Start**: 2019-08-19T00:00:00Z
- **End**: 2019-09-09T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Water_Class | int16 | Coded value. The source geodatabase domain gives: 0 = Archive Water Extent / Pre-Flood Water; 1 = Flood Water; 2 = Satellite Detected Water / Possible Saturated Soil; 3 = Probable Flash Flood-Affected Land; 4 = Aquaculture; 5 = Possible Satuated, wet soil; 6 = Tsunami-Affected Land; 7 = Maximum Satellite Observed Water (Cumulative); 8 = Swamp / Marsh / Mangrove; 9 = Snow Cover. The decoded text is in `Water_Class_label`. |
| Sensor_ID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Sensor_ID_label`, which is decoded per source file. |
| Sensor_Date | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| Confidence_ID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `Confidence_ID_label`. |
| Field_Validation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `Field_Validation_label`. |
| Water_StatusID | int32 | Coded value. The source geodatabase domain gives: 1 = New Water / Water Increase; 2 = No water change / Static Level; 3 = No water / Water levels decreased. The decoded text is in `Water_StatusID_label`. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| SenorID_old | int16 | Coded value. The source geodatabase domain gives: 1 = MODIS; 2 = ASAR WSM; 3 = ASAR IMP; 4 = Radarsat; 5 = DMC; 6 = SPOT5; 7 = ALOS Palsar WB1; 8 = ASAR APP. The decoded text is in `SenorID_old_label`. |
| StaffID | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 22 = WP; 33 = LB; 44 = JL; 45 = MD; 54 = HP; 55 = VG; 57 = PG; 66 = CJ; 70 = SG; 73 = RS; 77 = LD; 88 = HK; 91 = KA; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 141 = KJP; 151 = MNY; 161 = DC; 171 = SR; 181 = NL; 191 = DH; 212 = MH; 213 = JT; 214 = ES; 222 = CS; 1000 = Unknown. The decoded text is in `StaffID_label`. |
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
| ./fl20190815sdn-water-extent.parquet | 55.1 MB | 12202fe71da6... |
| ./fl20190815sdn-water-extent.pmtiles | 20.4 MB | 122013f87729... |
| ./styles/default.json | 887 B | 122064bf96dc... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20190815sdn-water-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-in-white-nile-state-sudan](https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-in-white-nile-state-sudan)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `PL20190828_FloodWater_Aljammalab_WhiteNileState`, `RS2_20190827_WaterEatent_WhiteNileState`, `SPOT6_20190828_WaterExtent_SennarState`, `SPOT6_20190828_WaterExtent_WhiteNileState`, `ST2_20190815_WaterExtent_RedSeaState`, `ST2_20190816_WaterExtent_KhartoumState`, `ST2_20190816_WaterExtent_WhiteNileState`, `VIIRS_20190822_25_WaterExtent_Sudan`.

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

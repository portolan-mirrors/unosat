# Analysis extent: Flood, Libya, 12 September 2023 (FL20230912LBY)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2023/fl20230912lby/fl20230912lby-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Analysis extent for Flood, Libya, 12 September 2023 (FL20230912LBY): 198 features merged from 77 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [10 September 2023 Mediterranean Sea Storm Daniel in Libya, Preliminary Satellite-Based Comprehensive Damage Assessment Report](https://data.humdata.org/dataset/10-september-2023-mediterranean-sea-storm-daniel-in-libya-preliminary-satellite-based-comp)
- [Flood impact assessment in Al Tamimi Town, Derna Governorate, East Province, Libya](https://data.humdata.org/dataset/flood-impact-assessment-in-al-tamimi-town-derna-governorate-east-province-libya)
- [Flood impact assessment in Dams over Benghazi and Almarj Governorates, East Province, Libya](https://data.humdata.org/dataset/flood-impact-assessment-in-dams-over-benghazi-and-almarj-governorates-east-province-libya)
- [Flood impact assessment in Derna City centre, East Province, Libya](https://data.humdata.org/dataset/flood-impact-assessment-in-derna-city-centre-east-province-libya)
- [Flood impact assessment in Derna City, East Province, Libya](https://data.humdata.org/dataset/flood-impact-assessment-in-derna-city-east-province-libya)
- [Flood impact assessment in Derna dams, East Province, Libya](https://data.humdata.org/dataset/flood-impact-assessment-in-derna-dams-east-province-libya)
- [Night-Time Light Loss Assessment in Derna & Al Bayda (Libya) using Night-time Light Imagery](https://data.humdata.org/dataset/night-time-light-loss-assessment-in-derna-al-bayda-libya-using-night-time-light-imagery)
- [Power Supply Assessment in Benghazi (Libya) using Night-time Light Imagery](https://data.humdata.org/dataset/power-supply-assessment-in-benghazi-libya-using-night-time-light-imagery)
- [Power Supply Assessment in Derna & Al Bayda (Libya) using Night-time Light Imagery](https://data.humdata.org/dataset/power-supply-assessment-in-derna-al-bayda-libya-using-night-time-light-imagery)
- [Preliminary satellite-derived reservoir assessment, Benghazi, Almarj & Derna governorates, East province, Libya - 19 September 2023](https://data.humdata.org/dataset/preliminary-satellite-derived-reservoir-assessment-benghazi-almarj-derna-governorates-east)
- [Storm Daniel in Libya, September 2023 - UNOSAT Live Web Map](https://data.humdata.org/dataset/storm-daniel-in-libya-september-2023-unosat-live-web-map)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue) ![libya-floods](https://img.shields.io/badge/libya--floods-blue)

## Spatial Coverage

- **Bounding Box**: [20.43066593000009, 32.304060597000046, 23.14161797400004, 32.803811187000065]

## Temporal Coverage

- **Start**: 2023-09-12T00:00:00Z
- **End**: 2023-10-11T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `SensorID_label`, which is decoded per source file. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 18 = TH; 22 = WP; 33 = LB; 44 = JL; 45 = MD; 54 = HP; 55 = VG; 57 = PG; 66 = CJ; 70 = SG; 73 = RS; 77 = LD; 88 = HK; 91 = KA; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 141 = KJP; 151 = MNY; 161 = DC; 171 = SR; 181 = NL; 191 = DH; 212 = MH; 213 = JT; 214 = ES; 215 = KB; 216 = JY; 218 = PA; 219 = SS; 220 = YM; 221 = IS; 222 = LD; 1000 = Unknown. The decoded text is in `StaffID_label`. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Shape_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Shape_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Area_ha | float | Area in hectares, as UNOSAT computed it. |
| Staff_ID | int32 |  |
| ConfidenceID_label | string | `ConfidenceID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| FieldValidation_label | string | `FieldValidation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20230912lby-analysis-extent.parquet | 286.5 KB | 122043c91349... |
| ./fl20230912lby-analysis-extent.pmtiles | 129.2 KB | 1220a1ce5c08... |
| ./styles/default.json | 671 B | 1220ff78818f... |
| ./fl20230912lby-analysis-extent.thumb.jpg | 3.6 KB | 1220eefc959d... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20230912lby-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/10-september-2023-mediterranean-sea-storm-daniel-in-libya-preliminary-satellite-based-comp](https://data.humdata.org/dataset/10-september-2023-mediterranean-sea-storm-daniel-in-libya-preliminary-satellite-based-comp)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `PHR_20230913_AnalysisExtent_Al_Tamimi`, `PT_20230914_AnalysisExtent_Bujarrar`, `PT_20230914_CloudObstruction_Bujarrar`, `PT_20230917_AnalysisExtent_AlMabni`, `PT_20230917_AnalysisExtent_Tocra`, `S2_20230912_AnalysisExtent_Derna`, `S2_20230912_CloudObstruction_Derna`.

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

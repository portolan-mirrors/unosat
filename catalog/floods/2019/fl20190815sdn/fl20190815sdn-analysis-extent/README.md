# Analysis extent: Flood, Sudan, 15 August 2019 (FL20190815SDN)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2019/fl20190815sdn/fl20190815sdn-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Analysis extent for Flood, Sudan, 15 August 2019 (FL20190815SDN): 7 features merged from 7 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

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

- **Bounding Box**: [32.06318052000006, 11.943922354000051, 38.14802759300005, 18.638749890000042]

## Temporal Coverage

- **Start**: 2019-08-19T00:00:00Z
- **End**: 2019-09-09T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `SensorID_label`, which is decoded per source file. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 22 = WP; 33 = LB; 44 = JL; 45 = MD; 54 = HP; 55 = VG; 57 = PG; 66 = CJ; 70 = SG; 73 = RS; 77 = LD; 88 = HK; 91 = KA; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 141 = KJP; 151 = MNY; 161 = DC; 171 = SR; 181 = NL; 191 = DH; 212 = MH; 213 = JT; 214 = ES; 222 = CS; 1000 = Unknown. The decoded text is in `StaffID_label`. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Area_ha | float | Area in hectares, as UNOSAT computed it. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20190815sdn-analysis-extent.parquet | 7.0 KB | 12204cfa5430... |
| ./fl20190815sdn-analysis-extent.pmtiles | 373.1 KB | 1220d8a49d14... |
| ./styles/default.json | 671 B | 1220eebbf604... |
| ./fl20190815sdn-analysis-extent.thumb.jpg | 7.1 KB | 1220deae3a96... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20190815sdn-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-in-white-nile-state-sudan](https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-in-white-nile-state-sudan)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `PL20190828_AnalysisExtent_Aljammalab_WhiteNileState`, `RS2_20190827_AnalysisExtent_WhiteNileState`, `SPOT6_20190828_AnalysisExtent_SennarState`, `SPOT6_20190828_Analysis_Extent_WhiteNileState`, `ST2_20190815_AnalysisExtent_RedSeaState`, `ST2_20190816_AnalysisExtent_KhartoumState`, `ST2_20190816_AnalysisExtent_WhiteNileState`.

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

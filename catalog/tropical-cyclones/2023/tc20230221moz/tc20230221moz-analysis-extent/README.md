# Analysis extent: Tropical cyclone, Mozambique, 21 February 2023 (TC20230221MOZ)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/tropical-cyclones/2023/tc20230221moz/tc20230221moz-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Analysis extent for Tropical cyclone, Mozambique, 21 February 2023 (TC20230221MOZ): 80 features merged from 80 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Flood Impact assessment of Vilankulo Town, Inhambane Province, Mozambique  as of 13 March 2023](https://data.humdata.org/dataset/flood-impact-assessment-of-vilankulo-town-inhambane-province-mozambique-as-of-13-march-202)
- [Satellite detected water  extents between 15 and 19 March 2023 over Inhambane, Sofala, Tete and Zambezia Provinces, Mozambique](https://data.humdata.org/dataset/water-extents-between-15-and-19-march-2023-over-inhambane-sofala-tete-and-zambezia-provinc)
- [Satellite detected water  extents over Sofala, Tete, and Zambezia Provinces, Mozambique as of 21 March 2023](https://data.humdata.org/dataset/water-extents-over-sofala-tete-and-zambezia-provinces-mozambique-as-of-21-march-2023)
- [Satellite detected water extent and evolution over Sofala and Zambezia Provinces, Mozambique between 13 and 17 March 2023](https://data.humdata.org/dataset/water-extent-and-evolution-over-sofala-and-zambezia-provinces-mozambique-between-13-and-17)
- [Satellite detected water extent over Matutuine District, Maputo Provinces, Mozambique as of 14 Mar. 2023](https://data.humdata.org/dataset/water-extent-over-matutuine-district-maputo-provinces-mozambique-as-of-14-mar-2023)
- [Satellite detected water extent over Sofala and Zambezia Provinces, Mozambique as of 13 Mar. 2023](https://data.humdata.org/dataset/water-extent-over-sofala-and-zambezia-provinces-mozambique-as-of-13-mar-2023)
- [Satellite detected water extent over Zambezia Provinces, Mozambique as of 24 March 2023](https://data.humdata.org/dataset/satellite-detected-water-extent-over-zambezia-provinces-mozambique-as-of-24-march-2023)
- [Satellite detected water extents between 21 and 25 March 2023 over Mozambique](https://data.humdata.org/dataset/satellite-detected-water-extents-between-21-and-25-march-2023-over-mozambique)
- [Satellite detected water extents between 27 and 31 March 2023 over Mozambique](https://data.humdata.org/dataset/satellite-detected-water-extents-between-27-and-31-march-2023-over-mozambique)
- [Satellite detected water extents over Sofala, Tete and Zambezia Provinces, Mozambique as of 26 March 2023](https://data.humdata.org/dataset/water-extents-over-sofala-tete-and-zambezia-provinces-mozambique-as-of-26-march-2023)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![cyclones-hurricanes-typhoons](https://img.shields.io/badge/cyclones--hurricanes--typhoons-blue) ![geodata](https://img.shields.io/badge/geodata-blue) ![tropical cyclone](https://img.shields.io/badge/tropical_cyclone-blue)

## Spatial Coverage

- **Bounding Box**: [30.23266800400006, -26.866434687999913, 40.83423620800005, -10.483548200999905]

## Temporal Coverage

- **Start**: 2023-03-13T00:00:00Z
- **End**: 2023-04-03T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The 3 source files of this collection use 3 different domains for it, so read `SensorID_label`, which is decoded per source file. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | int32 | Coded value. The 3 source files of this collection use 3 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Area_ha | float | Area in hectares, as UNOSAT computed it. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Staff_ID | int32 |  |
| ConfidenceID_label | string | `ConfidenceID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| FieldValidation_label | string | `FieldValidation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./tc20230221moz-analysis-extent.parquet | 8.1 MB | 1220c66837f7... |
| ./tc20230221moz-analysis-extent.pmtiles | 31.2 MB | 1220a2a3447c... |
| ./styles/default.json | 671 B | 1220a7b91eb7... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./tc20230221moz-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/flood-impact-assessment-of-vilankulo-town-inhambane-province-mozambique-as-of-13-march-202](https://data.humdata.org/dataset/flood-impact-assessment-of-vilankulo-town-inhambane-province-mozambique-as-of-13-march-202)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `RCM2_20230313_Zambezia_AnalysisExtent`, `ST1_20230228_Inhambane_AnalysisExtent`, `ST1_20230302_Matutuine_Maputo_AnalysisExtent`, `ST1_20230314_Matutuine_Maputo_AnalysisExtent`, `ST1_20230317_Zambezia_AnalysisExtent`, `ST1_20230324_Zambezia_AnalysisExtent`, `ST2_20230321_Central_Mozambique_AnalysisExtent`, `ST2_20230321_Central_Mozambique_CloudObstruction`, `ST2_20230326_Central_Mozambique_AnalysisExtent`, `ST2_20230326_Central_Mozambique_CloudObstruction`, `VIIRS_20230315_20230319_Mozambique_CloudObstruction`, `VIIRS_20230321_20230325_Mozambique_CloudObstruction`, `VIIRS_20230327_20230331_Mozambique_CloudObstruction`, `WV3_20230313_Vilankulo_AnalysisExtent`.

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

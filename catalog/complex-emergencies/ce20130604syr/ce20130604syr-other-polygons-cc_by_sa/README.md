# Other polygons: Complex emergency, Syrian Arab Republic, 4 June 2013 (CE20130604SYR)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20130604syr/ce20130604syr-other-polygons-cc_by_sa/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Other polygons for Complex emergency, Syrian Arab Republic, 4 June 2013 (CE20130604SYR): 1,662,252 features merged from 36 source layers. Polygons layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Damage Density in the City of Aleppo, Syria](https://data.humdata.org/dataset/damage-density-in-the-city-of-aleppo-syria)
- [Percentage damage in residential area of Aleppo City](https://data.humdata.org/dataset/percentage-damage-in-residential-area-of-aleppo-city)
- [Percentage of buildings damaged in the city of Aleppo](https://data.humdata.org/dataset/neighborhood-shelter-damage-percentages-in-aleppo-city)
- [Syria - 2014  Damage density  in Hama, Hama Governorate](https://data.humdata.org/dataset/damage-density-2014-of-hama-hama-governorate-syria)
- [Syria - 2016 Damage density in Hama, Hama Governorate](https://data.humdata.org/dataset/damage-density-2016-of-hama-hama-governorate-syria)
- [Syria - Damage assessement in Hama, Hama Governorate.](https://data.humdata.org/dataset/damage-assessement-of-hama-hama-governorate-syria)
- [Syria - Damage assessment of Deir Ez Zor, Deir Ez Zor Governorate](https://data.humdata.org/dataset/damage-assessment-of-deir-ez-zor-deir-ez-zor-governorate-syria)
- [Syria - Damage assessment of Idlib, Idlib Governorate](https://data.humdata.org/dataset/damage-assessment-of-idlib-idlib-governorate-syria)
- [Syria - Damage assessment of Jobar neighborhood and Irbin city, Damascus governorate.](https://data.humdata.org/dataset/damage-assessment-of-jobar-neighborhood-and-irbin-city-damascus-governorate-syria)
- [Syria - Damage density 2015 of Daraa, Daraa Governorate,](https://data.humdata.org/dataset/damage-density-2015-of-daraa-daraa-governorate-syria)
- [Syria - Damage density 2015 of Deir Ez Zor, Deir Ez Zor Governorate](https://data.humdata.org/dataset/damage-density-2015-of-deir-ez-zor-deir-ez-zor-governorate-syria)
- [Syria - Damage density 2015 of Idlib, Idlib Governorate](https://data.humdata.org/dataset/damage-density-2015-of-idlib-idlib-governorate-syria)
- and 4 more; the event's [catalog page](../catalog.json) lists them all.

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![damage assessment](https://img.shields.io/badge/damage_assessment-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [36.05691010000004, 32.589675500000055, 40.18096630000008, 36.295535820000055]

## Temporal Coverage

- **Start**: 2016-12-16T00:00:00Z
- **End**: 2017-01-17T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Settlement_Name | string |  |
| Neighborhood | string |  |
| Source | string |  |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| AOI | int16 |  |
| Name | string |  |
| Settlement | string |  |
| Type | string |  |
| OBJECTID_12 | int64 |  |
| Join_Count | int32 |  |
| TARGET_FID | int32 |  |
| Id | int32 |  |
| City | string |  |
| Name_Ar | string |  |
| ZoneMap | string |  |
| Shape_Leng | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Progress | int32 |  |
| OBJECTID_1 | int32 |  |
| Neighborho | string |  |
| Cnt_Neighb | int32 |  |
| FID_1 | int32 |  |
| OBJECTID_2 | int32 |  |
| Id_1 | int32 |  |
| City_1 | string |  |
| Name_1 | string |  |
| Name_Ar_1 | string |  |
| ZoneMap_1 | string |  |
| Shape_Le_1 | double |  |
| Shape_Ar_1 | double |  |
| Progress_1 | int32 |  |
| OBJECTID_3 | int32 |  |
| Neighbor_1 | string |  |
| Cnt_Neig_1 | int32 |  |
| Percent | float |  |
| GRIDCODE | int32 |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20130604syr-other-polygons-cc_by_sa.parquet | 35.9 MB | 12200cb2db25... |
| ./ce20130604syr-other-polygons-cc_by_sa.pmtiles | 16.4 MB | 12202f000778... |
| ./styles/default.json | 673 B | 122018288321... |
| ./ce20130604syr-other-polygons-cc_by_sa.thumb.jpg | 5.0 KB | 122079c50ff3... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20130604syr-other-polygons-cc_by_sa.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/damage-assessement-of-hama-hama-governorate-syria](https://data.humdata.org/dataset/damage-assessement-of-hama-hama-governorate-syria)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Aleppo_PercentageDamage_Neighborhood`, `Aleppo_ResidentialPercentageDamage`, `Damascus`, `Neighborhoods`, `No_Analysis_Areas_Aleppo`, `No_Analysis_Areas_Damascus`, `No_Analysis_Areas_Daraa`, `No_Analysis_Areas_Deir_ez_Zor`, `No_Analysis_Areas_Hama`, `No_Analysis_Areas_Homs`, `No_Analysis_Areas_Idlib`, `No_Analysis_Areas_Raqqa`.

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

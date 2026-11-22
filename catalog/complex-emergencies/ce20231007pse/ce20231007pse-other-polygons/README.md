# Other polygons: Complex emergency, State of Palestine, 7 October 2023 (CE20231007PSE)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20231007pse/ce20231007pse-other-polygons/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Other polygons for Complex emergency, State of Palestine, 7 October 2023 (CE20231007PSE): 162 features merged from 74 source layers. Polygons layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [UNOSAT - FAO Gaza Strip Cropland Damage Assessment - August 2024](https://data.humdata.org/dataset/unosat-fao-gaza-strip-cropland-damage-assessment-august-2024)
- [UNOSAT - FAO Gaza Strip Cropland Damage Assessment - December 2024](https://data.humdata.org/dataset/unosat-fao-gaza-strip-cropland-damage-assessment-december-2024)
- [UNOSAT - FAO Gaza Strip Cropland Damage Assessment - July 2024](https://data.humdata.org/dataset/unosat-fao-gaza-strip-cropland-damage-assessment-july-2024)
- [UNOSAT - FAO Gaza Strip Cropland Damage Assessment - July 2025](https://data.humdata.org/dataset/unosat-fao-gaza-strip-cropland-damage-assessment-july-2025)
- [UNOSAT - FAO Gaza Strip Cropland Damage Assessment - June 2024](https://data.humdata.org/dataset/unosat-fao-gaza-strip-cropland-damage-assessment-june-2024)
- [UNOSAT Gaza Strip Agricultural Damage Analysis 1km Stretch of Land from the Armistice Demarcation Line - April 2024](https://data.humdata.org/dataset/unosat-gaza-strip-agricultural-damage-analysis-1km-stretch-of-land-from-the-armistice-dema)
- [UNOSAT Gaza Strip Agricultural Damage Assessment - April 2024](https://data.humdata.org/dataset/unosat-gaza-strip-agricultural-damage-assessment-april-2024)
- [UNOSAT Gaza Strip Agricultural Damage Assessment - December 2023](https://data.humdata.org/dataset/unosat-gaza-strip-agricultural-damage-assessment-december-2023)
- [UNOSAT Gaza Strip Agricultural Damage Assessment - January 2024](https://data.humdata.org/dataset/unosat-gaza-strip-agricultural-damage-assessment-january-2024)
- [UNOSAT Gaza Strip Agricultural Damage Assessment - November 2023](https://data.humdata.org/dataset/unosat-gaza-strip-agricultural-damage-assessment-november-2023)
- [UNOSAT Gaza Strip Comprehensive Damage Assessment 1km Stretch of Land from the Armistice Demarcation Line - April 2024](https://data.humdata.org/dataset/unosat-gaza-strip-comprehensive-damage-assessment-1km-stretch-of-land-from-the-armistice-d)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![crisis-opt-israel-hostilities](https://img.shields.io/badge/crisis--opt--israel--hostilities-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [34.21971413400007, 31.219972015000053, 34.56802376500008, 31.59491934600004]

## Temporal Coverage

- **Start**: 2023-11-17T00:00:00Z
- **End**: 2025-07-30T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Class | string |  |
| Area_km2 | double | Area in square kilometres, as UNOSAT computed it. |
| Shape_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Shape_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| Id | int32 |  |
| gridcode | int32 |  |
| ClassMonth | string |  |
| Area_km2_TotalMonth | double |  |
| Value | int32 |  |
| BUFF_DIST | double |  |
| ORIG_FID | int32 |  |
| Name | string |  |
| Area | double |  |
| Classname | string |  |
| SUM_Area_km2 | double |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20231007pse-other-polygons.parquet | 1.8 GB | 122070042a10... |
| ./ce20231007pse-other-polygons.pmtiles | 20.0 MB | 12204b38a908... |
| ./styles/default.json | 664 B | 1220bd86f1a5... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20231007pse-other-polygons.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/unosat-fao-gaza-strip-cropland-damage-assessment-august-2024](https://data.humdata.org/dataset/unosat-fao-gaza-strip-cropland-damage-assessment-august-2024)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `CE20231007PSE_Gaza_1kmBufferZone`, `CE20231007PSE_UNOSAT_AgriculturalExtent_1kmBufferZone`, `Cropland_Damage_NDVI_Gaza_DA_2017_2023_20231027`, `Cropland_Damage_NDVI_Gaza_DA_2017_2023_20231126`, `Cropland_Damage_NDVI_Gaza_DA_2017_2023_20231226`, `Cropland_Damage_NDVI_Gaza_DA_2017_2024_20240429`, `Cropland_Damage_NDVI_Gaza_DA_2017_2024_20240529`, `Cropland_Damage_NDVI_Gaza_DA_2017_2024_20240628`, `Cropland_Damage_NDVI_Gaza_DA_2017_2024_20240728`, `Cropland_Damage_NDVI_Gaza_DA_2017_2024_20240827`, `Cropland_Damage_NDVI_Gaza_DA_2017_2024_20240926`, `Cropland_Damage_NDVI_Gaza_DA_2017_2024_20241026`, `Cropland_Damage_NDVI_Gaza_DA_2017_2024_20241230`, `Cropland_Damage_NDVI_Gaza_DA_2017_2025_20250429`, `Cropland_Damage_NDVI_Gaza_DA_2017_2025_20250728`, `Cropland_Damage_NDVI_Gaza_DA_2018_2024_20240130`, `Cropland_Damage_NDVI_Gaza_DA_2018_2024_20240224`, `Cropland_Damage_NDVI_Gaza_DA_2018_2024_20240330`, `Cropland_Damage_NDVI_Gaza_DA_2018_2025_20250223`, `Cropland_Damage_NDVI_Gaza_DA_2018_2025_20250330`, `Damage_NDVI_Gaza_DA_2017_2023_20231027`, `Damage_NDVI_Gaza_DA_2017_2023_20231111`, `Damage_NDVI_Gaza_DA_2017_2023_20231211`, `Damage_NDVI_Gaza_DA_2018_2024_20240130`, `Damage_NDVI_Gaza_DA_2018_2024_20240224`, `Damage_NDVI_Gaza_DA_2018_2024_20240424`.

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

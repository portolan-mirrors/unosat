# Other polygons: Complex emergency, Syrian Arab Republic, 4 June 2013 (CE20130604SYR)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20130604syr/ce20130604syr-other-polygons-cc_by_nc_sa_3_0/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Other polygons for Complex emergency, Syrian Arab Republic, 4 June 2013 (CE20130604SYR): 773,406 features merged from 10 source layers. Polygons layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of Damage Assessment for Ancient City of Palmyra, Syria](https://data.humdata.org/dataset/geodata-of-damage-assessment-for-ancient-city-of-palmyra-syria-april-06-2016)
- [Geodata of Damage Assessment of Aleppo, Aleppo Governorate, Syria](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-aleppo-aleppo-governorate-syria-july-21-2015)
- [Geodata of Damage Assessment of Ar Raqqa, Ar Raqqa Governorate, Syria](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-ar-raqqa-ar-raqqa-governorate-syria-july-21-2015)
- [Geodata of Damage Assessment of Daraa, Daraa Governorate, Syria](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-daraa-daraa-governorate-syria-july-21-2015)
- [Geodata of Damage Assessment of Deir Ez Zor, Deir Ez Zor Governorate, Syria](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-deir-ez-zor-deir-ez-zor-governorate-syria-july-21-2015)
- [Geodata of Damage Assessment of Idlib, Idlib Governorate, Syria](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-idlib-idlib-governorate-syria-july-21-2015)
- [Geodata of Damage Assessment of Tadmur and Al-Amiriyah, Homs Governorate, Syria](https://data.humdata.org/dataset/geodata-of-damage-assessment-of-tadmur-and-al-amiriyah-homs-governorate-syria-april-07-2016)
- [Geodata of Damage Density in the Cities of Homs, Aleppo, Hama, Deir Ez Zor, Ar Raqqa, and Daraa, Syria](https://data.humdata.org/dataset/geodata-of-damage-density-in-the-cities-of-homs-aleppo-hama-deir-ez-zor-ar-ra-july-21-2015)
- [Geodata of Neighborhood Damage Percentages, Aleppo, Syria](https://data.humdata.org/dataset/geodata-of-neighborhood-damage-percentages-aleppo-syria-february-18-2016)
- [Geodata of Percentages of Buildings Damaged, Aleppo, Syria](https://data.humdata.org/dataset/geodata-of-percentages-of-buildings-damaged-aleppo-syria-february-18-2016)
- [Geodata of Percentages of Buildings Damaged,Tadmur and Al-Miriyah, Homs Governorate, Syria](https://data.humdata.org/dataset/geodata-of-percentages-of-buildings-damagedtadmur-and-al-miriyah-homs-governo-april-20-2016)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [36.073136300000044, 32.59755320000005, 40.17925500000007, 36.296201341000085]

## Temporal Coverage

- **Start**: 2015-07-21T00:00:00Z
- **End**: 2016-04-20T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Name | string |  |
| Shape_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Shape_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| Id | int64 |  |
| gridcode | int64 |  |
| Shape_Leng | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| FID_1 | int32 |  |
| ZoneMap | string |  |
| Count_ | int64 |  |
| Count_1 | int64 |  |
| Percent_1 | double |  |
| F10 | double |  |
| Source | string |  |
| Settlement | string |  |
| Neighborho | string |  |
| Settlement_Name | string |  |
| Neighborhood | string |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20130604syr-other-polygons-cc_by_nc_sa_3_0.parquet | 25.9 MB | 1220f6f384f0... |
| ./ce20130604syr-other-polygons-cc_by_nc_sa_3_0.pmtiles | 17.2 MB | 12200bcb9dc3... |
| ./styles/default.json | 680 B | 122054253272... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20130604syr-other-polygons-cc_by_nc_sa_3_0.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-damage-assessment-for-ancient-city-of-palmyra-syria-april-06-2016](https://data.humdata.org/dataset/geodata-of-damage-assessment-for-ancient-city-of-palmyra-syria-april-06-2016)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `AOI_Palmyra`, `AOI_Tadmur`, `Aleppo_Continuous_PercentDamage`, `Aleppo_Neighborhood_PercentDamage`, `CityBorder`, `Neighborhoods`.

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

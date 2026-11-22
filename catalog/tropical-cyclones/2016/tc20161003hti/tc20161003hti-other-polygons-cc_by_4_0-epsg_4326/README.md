# Other polygons: Tropical cyclone, Cuba, Dominican Republic, Haiti and 1 more, 3 October 2016 (TC20161003HTI)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/tropical-cyclones/2016/tc20161003hti/tc20161003hti-other-polygons-cc_by_4_0-epsg_4326/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Other polygons for Tropical cyclone, Cuba, Dominican Republic, Haiti and 1 more, 3 October 2016 (TC20161003HTI): 600 features merged from 3 source layers. Polygons layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Cuba - Population Exposure Wind Speed from Hurricane Matthew (UNOSAT, 2016-10-06.)](https://data.humdata.org/dataset/unosat-cuba-popexposure-windspeed-matthew-20161006)
- [Haiti - Population Exposure Wind Speed from Hurricane Matthew (UNOSAT, 2016-10-06)](https://data.humdata.org/dataset/unosat-haiti-popexposure-windspeed-matthew-20161006)
- [Jamaica - Population Exposure  Wind Speed from Hurricanne Matthew (UNOSAT - 2016-10-06)](https://data.humdata.org/dataset/unosat-jamaica-popexposure-windspeed-matthew-20161006)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![cyclones-hurricanes-typhoons](https://img.shields.io/badge/cyclones--hurricanes--typhoons-blue) ![geodata](https://img.shields.io/badge/geodata-blue) ![tropical cyclone](https://img.shields.io/badge/tropical_cyclone-blue)

## Spatial Coverage

- **Bounding Box**: [-76.78335571289057, 17.38930511474615, -71.62215080999994, 21.2840251922608]

## Temporal Coverage

- **Start**: 2016-10-06T00:00:00Z
- **End**: 2016-10-06T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| ID_0 | int64 |  |
| ISO | string |  |
| NAME_0 | string |  |
| ID_1 | int64 |  |
| NAME_1 | string |  |
| ID_2 | int64 |  |
| NAME_2 | string |  |
| HASC_2 | string |  |
| CCN_2 | int64 |  |
| CCA_2 | string |  |
| TYPE_2 | string |  |
| ENGTYPE_2 | string |  |
| NL_NAME_2 | string |  |
| VARNAME_2 | string |  |
| WSZ_120kmh | double |  |
| WSZ_90kmh | double |  |
| WSZ_60kmh | double |  |
| Total | double |  |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| OBJECTID | int64 |  |
| id_Section | string |  |
| No_section | int64 |  |
| ID_Com | int64 |  |
| Id_dep | int64 |  |
| admin1pcod | string |  |
| admin2pcod | string |  |
| admin3pcod | string |  |
| admin1name | string |  |
| admin2name | string |  |
| admin3name | string |  |
| HASC_1 | string |  |
| CCN_1 | int64 |  |
| CCA_1 | string |  |
| TYPE_1 | string |  |
| ENGTYPE_1 | string |  |
| NL_NAME_1 | string |  |
| VARNAME_1 | string |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./tc20161003hti-other-polygons-cc_by_4_0-epsg_4326.parquet | 994.5 KB | 1220a0cfa654... |
| ./tc20161003hti-other-polygons-cc_by_4_0-epsg_4326.pmtiles | 3.1 MB | 1220c05e3015... |
| ./styles/default.json | 684 B | 12207526c70a... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./tc20161003hti-other-polygons-cc_by_4_0-epsg_4326.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/unosat-cuba-popexposure-windspeed-matthew-20161006](https://data.humdata.org/dataset/unosat-cuba-popexposure-windspeed-matthew-20161006)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `UNOSAT_Cuba_PopExposure_WindSpeed_Matthew_20161006_v1`, `UNOSAT_Haiti_PopExposure_WindSpeed_Matthew_20161006`, `UNOSAT_Jamaica_PopExposure_WindSpeed_Matthew_20161006_v1`.

## Attribution

UNITAR-UNOSAT

## License

[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

## Contact

Portolan Mirrors <nissim@radiant.earth>

## Known Issues

This is a preliminary assessment and has not yet been validated in the field. It is important to consider the characteristics and the limitations of the sources used to implement those results.

---

*Generated by [Portolan](https://github.com/portolan-sdi/portolan-cli) from STAC metadata and .portolan/metadata.yaml*

# Other polygons: Tropical Cyclone IRMA-17 : Population Exposure estimates
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/no-event-code/population-exposure-estimates-based-on-tropical-cyclone-irma-s-path/population-exposure-estimates-based-on-tropical-cyclone-irma-s-path-other-polygons-epsg_4326/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Other polygons for Tropical Cyclone IRMA-17 : Population Exposure estimates: 574 features merged from 17 source layers. Polygons layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Tropical Cyclone IRMA-17 : Population Exposure estimates](https://data.humdata.org/dataset/population-exposure-estimates-based-on-tropical-cyclone-irma-s-path)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![cyclones-hurricanes-typhoons](https://img.shields.io/badge/cyclones--hurricanes--typhoons-blue) ![dataset](https://img.shields.io/badge/dataset-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [-84.95236206054682, 15.20625114440918, -61.00013732910156, 27.271389007568473]

## Temporal Coverage

- **Start**: 2017-09-07T00:00:00Z
- **End**: 2017-09-07T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| ID_0 | int64 |  |
| ISO | string |  |
| NAME_ENGLI | string |  |
| NAME_ISO | string |  |
| NAME_FAO | string |  |
| NAME_LOCAL | string |  |
| NAME_OBSOL | string |  |
| NAME_VARIA | string |  |
| NAME_NONLA | string |  |
| NAME_FRENC | string |  |
| NAME_SPANI | string |  |
| NAME_RUSSI | string |  |
| NAME_ARABI | string |  |
| NAME_CHINE | string |  |
| WASPARTOF | string |  |
| CONTAINS | string |  |
| SOVEREIGN | string |  |
| ISO2 | string |  |
| WWW | string |  |
| FIPS | string |  |
| ISON | double |  |
| VALIDFR | string |  |
| VALIDTO | string |  |
| POP2000 | double |  |
| SQKM | double |  |
| POPSQKM | double |  |
| UNREGION1 | string |  |
| UNREGION2 | string |  |
| DEVELOPING | double |  |
| CIS | double |  |
| Transition | double |  |
| OECD | double |  |
| WBREGION | string |  |
| WBINCOME | string |  |
| WBDEBT | string |  |
| WBOTHER | string |  |
| CEEAC | double |  |
| CEMAC | double |  |
| CEPLG | double |  |
| COMESA | double |  |
| EAC | double |  |
| ECOWAS | double |  |
| IGAD | double |  |
| IOC | double |  |
| MRU | double |  |
| SACU | double |  |
| UEMOA | double |  |
| UMA | double |  |
| PALOP | double |  |
| PARTA | double |  |
| CACM | double |  |
| EurAsEC | double |  |
| Agadir | double |  |
| SAARC | double |  |
| ASEAN | double |  |
| NAFTA | double |  |
| GCC | double |  |
| CSN | double |  |
| CARICOM | double |  |
| EU | double |  |
| CAN | double |  |
| ACP | double |  |
| Landlocked | double |  |
| AOSIS | double |  |
| SIDS | double |  |
| Islands | double |  |
| LDC | double |  |
| Pop_60 | int64 |  |
| Pop_90 | int64 |  |
| Pop_120 | int64 |  |
| Total_pop | int64 |  |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| NAME_0 | string |  |
| ID_1 | int64 |  |
| NAME_1 | string |  |
| HASC_1 | string |  |
| CCN_1 | int64 |  |
| CCA_1 | string |  |
| TYPE_1 | string |  |
| ENGTYPE_1 | string |  |
| NL_NAME_1 | string |  |
| VARNAME_1 | string |  |
| ID_2 | int64 |  |
| NAME_2 | string |  |
| HASC_2 | string |  |
| CCN_2 | int64 |  |
| CCA_2 | string |  |
| TYPE_2 | string |  |
| ENGTYPE_2 | string |  |
| NL_NAME_2 | string |  |
| VARNAME_2 | string |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./population-exposure-estimates-based-on-tropical-cyclone-irma-s-path-other-polygons-epsg_4326.parquet | 3.5 MB | 12201fe15c0f... |
| ./population-exposure-estimates-based-on-tropical-cyclone-irma-s-path-other-polygons-epsg_4326.pmtiles | 9.6 MB | 12200ed299d3... |
| ./styles/default.json | 728 B | 12208265eb64... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./population-exposure-estimates-based-on-tropical-cyclone-irma-s-path-other-polygons-epsg_4326.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/population-exposure-estimates-based-on-tropical-cyclone-irma-s-path](https://data.humdata.org/dataset/population-exposure-estimates-based-on-tropical-cyclone-irma-s-path)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `AIA_adm0_pop`, `ATG_adm1_pop`, `BHS_adm1_pop`, `BLM_adm0_pop`, `CUB_adm2_pop`, `DMA_adm1_pop`, `DOM_adm2_pop`, `GLP_adm2_pop`, `HTI_adm2_pop`, `KNA_adm1_pop`, `MAF_adm0_pop`, `MSR_adm0_pop`, `PRI_adm1_pop`, `SXM_adm0_pop`, `TCA_adm1_pop`, `VGB_adm1_pop`, `VIR_adm2_pop`.

## Attribution

UNITAR-UNOSAT

## License

[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

## Contact

Portolan Mirrors <nissim@radiant.earth>

## Known Issues

This is a preliminary analysis and has not yet been validated in the field.

---

*Generated by [Portolan](https://github.com/portolan-sdi/portolan-cli) from STAC metadata and .portolan/metadata.yaml*

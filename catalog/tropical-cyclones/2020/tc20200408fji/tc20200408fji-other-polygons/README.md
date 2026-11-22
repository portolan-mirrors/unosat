# Other polygons: Tropical cyclone, Fiji, 8 April 2020 (TC20200408FJI)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/tropical-cyclones/2020/tc20200408fji/tc20200408fji-other-polygons/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Other polygons for Tropical cyclone, Fiji, 8 April 2020 (TC20200408FJI): 139 features merged from 5 source layers. Polygons layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Buildings Damage Assessment & Related Density  in Kadavu  Province, Eastern Division,  Republic of Fiji](https://data.humdata.org/dataset/buildings-damage-assessment-related-density-in-kadavu-province-eastern-division-republic-o)
- [Damage Assessment in Kadavu Province, Eastern Division,  Republic of Fiji](https://data.humdata.org/dataset/damage-assessment-in-kadavu-province-eastern-division-republic-of-fiji)
- [Damage Assessment in Ono-i-Lau, Lau Province, Eastern Division, Republic of Fiji](https://data.humdata.org/dataset/damage-assessment-in-ono-i-lau-lau-province-eastern-division-republic-of-fiji)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![cyclones-hurricanes-typhoons](https://img.shields.io/badge/cyclones--hurricanes--typhoons-blue) ![geodata](https://img.shields.io/badge/geodata-blue) ![tropical cyclone](https://img.shields.io/badge/tropical_cyclone-blue)

## Spatial Coverage

- **Bounding Box**: [-179.99999999999991, -21.04145368299993, 180.0, -12.479529531999958]

## Temporal Coverage

- **Start**: 2020-04-14T00:00:00Z
- **End**: 2020-04-17T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Site_ID | int16 | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Staduim; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 45 = Suspected Mass Grave Site. The decoded text is in `Site_ID_label`. |
| AgencyID | int16 | Coded value. The source geodatabase domain gives: 1 = UNOSAT; 2 = COPERNICUS; 3 = NGA. The decoded text is in `AgencyID_label`. |
| SiteName | string |  |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| AgencyID_label | string | `AgencyID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Site_ID_label | string | `Site_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| Shape_Leng | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| ADM0_EN | string |  |
| ADM0_PCODE | string |  |
| date | timestamp[us, tz=UTC] |  |
| validOn | timestamp[us, tz=UTC] |  |
| ADM1_EN | string |  |
| ADM1_PCODE | string |  |
| ADM2_EN | string |  |
| ADM2_PCODE | string |  |
| validTo | timestamp[us, tz=UTC] |  |
| ADM3_PCODE | string |  |
| ADM3_NAME | string |  |
| ADM2_NAME | string |  |
| ADM1_NAME | string |  |
| ADM0_NAME | string |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./tc20200408fji-other-polygons.parquet | 12.1 MB | 1220544c97dc... |
| ./tc20200408fji-other-polygons.pmtiles | 2.7 MB | 12203d0dbf28... |
| ./styles/default.json | 664 B | 122061e61861... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./tc20200408fji-other-polygons.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/buildings-damage-assessment-related-density-in-kadavu-province-eastern-division-republic-o](https://data.humdata.org/dataset/buildings-damage-assessment-related-density-in-kadavu-province-eastern-division-republic-o)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `AOI_UNOSAT`, `fji_admbnda_adm0`, `fji_admbnda_adm1`, `fji_admbnda_adm2`, `fji_admbnda_adm3`.

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

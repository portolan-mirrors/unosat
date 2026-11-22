# Other polygons: Earthquake, Mexico, 19 September 2017 (EQ20170919MEX)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/earthquakes/2017/eq20170919mex/eq20170919mex-other-polygons/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Other polygons for Earthquake, Mexico, 19 September 2017 (EQ20170919MEX): 33 features merged from 17 source layers. Polygons layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Damage Assessment in Central West Cuernavaca City, Municipality of Cuernavaca, State of Morelos](https://data.humdata.org/dataset/damage-assessment-in-central-west-cuernavaca-city-municipality-of-cuernavaca-state-of-morelos)
- [Damage Assessment in Jojutla town, Jojutla Municipality, State of Morelos, Mexico](https://data.humdata.org/dataset/damage-assessment-in-jojutla-town-jojutla-municipality-state-of-morelos-mexico-2698)
- [Damage Assessment in Mexico City, Mexico](https://data.humdata.org/dataset/damage-assessment-in-mexico-city-mexico-2711)
- [Damage Assessment in San Andrés Cholula and San Pedro Cholula, State of Puebla, Mexico](https://data.humdata.org/dataset/damage-assessment-in-san-andres-cholula-and-san-pedro-cholula-state-of-puebla-mexico-2717)
- [Damage Assessment in Tlaquiltenango Town, Municipality of Tlaquiltenango, State of Morelos, Mexico](https://data.humdata.org/dataset/damage-assessment-in-tlaquiltenango-town-municipality-of-tlaquiltenango-state-of-morelos-mexico-2705)
- [Damage Assessment in Tlayacapan town, Municipality of Tlayacapan, State of Morelos, Mexico](https://data.humdata.org/dataset/damage-assessment-in-tlayacapan-town-municipality-of-tlayacapan-state-of-morelos-mexico-2707)
- [Damage Assessment in Xochimilco and Tlahuac Municipalities, Federal State, Mexico](https://data.humdata.org/dataset/damage-assessment-in-xochimilco-and-tlahuac-municipalities-federal-state-mexico-2712)
- [Damage Assessment in the Historical Center of Puebla, State of Puebla](https://data.humdata.org/dataset/damage-assessment-in-the-historical-center-of-puebla-state-of-puebla-2700)
- [Damage Assessment in the south west of Cuauhtemoc Municipality, Federal District, Mexico](https://data.humdata.org/dataset/damage-assessment-in-the-south-west-of-cuauhtemoc-municipality-federal-district-mexico-2699)
- [Damage Assessment in the town of Atzala, Municipality of Atzala, State of Puebla, Mexico](https://data.humdata.org/dataset/damage-assessment-in-the-town-of-atzala-municipality-of-atzala-state-of-puebla-mexico)
- [Damage Assessment in the town of Coatetelco, Municipality of Miacatlan, State of Morelos, Mexico](https://data.humdata.org/dataset/damage-assessment-in-the-town-of-coatetelco-municipality-of-miacatlan-state-of-morelos-mexico)
- [Evaluación de daño en la colonia Capultitlan, Ciudad de México](https://data.humdata.org/dataset/evaluacion-de-dano-en-la-colonia-capultitlan-ciudad-de-mexico-2713)
- and 1 more; the event's [catalog page](../catalog.json) lists them all.

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![earthquake](https://img.shields.io/badge/earthquake-blue) ![earthquake-tsunami](https://img.shields.io/badge/earthquake--tsunami-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [-99.3427237119999, 18.53161775500007, -98.18304574299992, 19.545270000000073]

## Temporal Coverage

- **Start**: 2017-09-25T00:00:00Z
- **End**: 2017-11-06T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Site_ID | int16 | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Staduim; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 45 = Suspected Mass Grave Site. The decoded text is in `Site_ID_label`. |
| AgencyID | int32 | Coded value. The source geodatabase domain gives: 1 = UNOSAT; 2 = IGG-UNAM; 4 = UAEMex. The decoded text is in `AgencyID_label`. |
| SiteName | string |  |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Site_ID_label | string | `Site_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| AgencyID_label | string | `AgencyID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./eq20170919mex-other-polygons.parquet | 32.9 KB | 1220ee0c7ba9... |
| ./eq20170919mex-other-polygons.pmtiles | 86.7 KB | 12208246e453... |
| ./styles/default.json | 664 B | 1220bac77f4d... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./eq20170919mex-other-polygons.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/damage-assessment-in-central-west-cuernavaca-city-municipality-of-cuernavaca-state-of-morelos](https://data.humdata.org/dataset/damage-assessment-in-central-west-cuernavaca-city-municipality-of-cuernavaca-state-of-morelos)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `DG_SanAndresCholulaAndPedroCholula_Damage_Sites_AOI_UNAM`, `EQ20170919MEX_CentralMexicoCity_AOI_UAEMEX`, `PL20170921_Izucar_de_Matamoros_AOI`, `PL20170922_Atzala_AOI`, `PL20170922_LaGalarza_AOI`, `PL20170922_SanNicolasTolentinoAndAyutla_AOI`, `PL20170922_TepapayecaAndSantaCatarinaCoatepec_Damage_Sites_AOI`, `PL20171003_Jojutla_AOI`, `PL20171005_Tlaquiltenango_AOI`, `UAV_20171007_Tlayacapan_AOI`, `WV2_20170920_MexicoCity_Xochimilco_Tlahuac_AOI_UAEMEX`, `WV2_20170926_MexicoCity_Capultitlan_AOI_UAEMEX`, `WV2_20170926_MexicoCity_CuautepecMadero_AOI_UAEMEX`, `WV2_20170926_SouthWestCuauhtemoc_AOI`, `WV3_20170922_Coatetelco_AOI`, `WV3_20170922_Cuernavaca_AOI`, `WV3_20170923_PueblaCentroHistorico_AOI`.

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

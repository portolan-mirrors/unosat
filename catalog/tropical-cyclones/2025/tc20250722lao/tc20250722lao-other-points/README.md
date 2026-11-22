# Other points: Tropical cyclone, Lao People's Democratic Republic, 22 July 2025 (TC20250722LAO)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/tropical-cyclones/2025/tc20250722lao/tc20250722lao-other-points/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Other points for Tropical cyclone, Lao People's Democratic Republic, 22 July 2025 (TC20250722LAO): 4 features merged from 1 source layer. Points layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Mudflow impact in Kham District, Xiengkhouang Province, Lao PDR  as of 2 August 2025](https://data.humdata.org/dataset/mudflow-impact-in-kham-district-xiengkhouang-province-lao-pdr-as-of-2-august-2025)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![cyclones-hurricanes-typhoons](https://img.shields.io/badge/cyclones--hurricanes--typhoons-blue) ![geodata](https://img.shields.io/badge/geodata-blue) ![tropical cyclone](https://img.shields.io/badge/tropical_cyclone-blue)

## Spatial Coverage

- **Bounding Box**: [103.60736247300008, 19.581724700000052, 103.69422228400003, 19.604293073000065]

## Temporal Coverage

- **Start**: 2025-08-06T00:00:00Z
- **End**: 2025-08-06T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SourceID | string |  |
| Picture | binary |  |
| Exs | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Definite; 2 = Doubtful. The decoded text is in `Exs_label`. |
| Notes | string | Free-text notes by the analyst. |
| BridgeID | string |  |
| Nme | string |  |
| ReportNme | string |  |
| BridgeTpe | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Arch; 2 = Beam; 3 = Truss; 4 = Floating; 5 = Suspension; 6 = Culvert; 7 = Culvert - round; 8 = Culvert - box. The decoded text is in `BridgeTpe_label`. |
| TotLngthM | double |  |
| WidthM | double |  |
| MxTLdMT | double |  |
| OpStatus | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Open; 2 = Restricted; 3 = Closed; 4 = Abandonned/Disused. The decoded text is in `OpStatus_label`. |
| Dmg | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Appears intact; 2 = Appears damaged; 3 = Appears destroyed/collapsed. The decoded text is in `Dmg_label`. |
| RprsTpe | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Repairable locally; 2 = Requires external expertise; 3 = Not repairable. The decoded text is in `RprsTpe_label`. |
| IsUndrCstr | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Yes; 2 = No. The decoded text is in `IsUndrCstr_label`. |
| CstWrkETC | timestamp[us, tz=UTC] |  |
| BaseMtrl | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Wood; 2 = Concrete; 3 = Stone; 4 = Steel; 5 = PVC. The decoded text is in `BaseMtrl_label`. |
| SrfTpe | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Paved; 2 = Gravel; 3 = Dirt/Sand; 4 = Steel; 5 = Wood; 6 = Grass. The decoded text is in `SrfTpe_label`. |
| TptnFtCat | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Road; 2 = Rail; 3 = Both road and rail; 4 = Canal; 5 = Pipeline; 6 = Cabling. The decoded text is in `TptnFtCat_label`. |
| OvHdClrcM | double |  |
| HasBypass | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Yes; 2 = No. The decoded text is in `HasBypass_label`. |
| Sec | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Good; 2 = Marginal; 3 = Poor. The decoded text is in `Sec_label`. |
| CurntPrac | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Non-motorized; 2 = Motorbike; 3 = 4WD < 3.5MT; 4 = Light truck < 10MT; 5 = Heavy truck < 20MT; 6 = Truck + Trailer > 20MT. The decoded text is in `CurntPrac_label`. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| BaseMtrl_label | string | `BaseMtrl` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| BridgeTpe_label | string | `BridgeTpe` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| CurntPrac_label | string | `CurntPrac` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Dmg_label | string | `Dmg` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Exs_label | string | `Exs` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| HasBypass_label | string | `HasBypass` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| IsUndrCstr_label | string | `IsUndrCstr` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| OpStatus_label | string | `OpStatus` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| RprsTpe_label | string | `RprsTpe` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Sec_label | string | `Sec` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SrfTpe_label | string | `SrfTpe` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| TptnFtCat_label | string | `TptnFtCat` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./tc20250722lao-other-points.parquet | 7.8 KB | 12202db75637... |
| ./tc20250722lao-other-points.pmtiles | 23.7 KB | 122014f3bd0e... |
| ./styles/default.json | 695 B | 122013975723... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./tc20250722lao-other-points.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/mudflow-impact-in-kham-district-xiengkhouang-province-lao-pdr-as-of-2-august-2025](https://data.humdata.org/dataset/mudflow-impact-in-kham-district-xiengkhouang-province-lao-pdr-as-of-2-august-2025)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `PHR_20250802_DamagedBridges_KhamDistrict`.

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

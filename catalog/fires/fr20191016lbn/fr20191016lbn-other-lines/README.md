# Other lines: Fire, Lebanon, 16 October 2019 (FR20191016LBN)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/fires/fr20191016lbn/fr20191016lbn-other-lines/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Other lines for Fire, Lebanon, 16 October 2019 (FR20191016LBN): 63 features merged from 1 source layer. Lines layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Fire hotspots density in Lebanon and Syria as detected by VIIRS between October 15-16, 2019](https://data.humdata.org/dataset/fire-hotspots-density-in-lebanon-and-syria-as-detected-by-viirs-between-october-15-16-2019)
- [Wildfires east of Tyre, in South and El Nabatieh Governorates, Lebanon](https://data.humdata.org/dataset/wildfires-east-of-tyre-in-south-and-el-nabatieh-governorates-lebanon)
- [Wildfires in Akkar Governorate (Lebanon) Tartous and Homs Governorates (Syria).](https://data.humdata.org/dataset/wildfires-in-akkar-governorate-lebanon-tartous-and-homs-governorates-syria)
- [Wildfires in Al-Haffa and Al-Qardaha Districts, Lattakia Governorate, Syria](https://data.humdata.org/dataset/wildfires-in-al-haffa-and-al-qardaha-districts-lattakia-governorate-syria)
- [Wildfires south of Beirut, in Aley and Chouf districts, Lebanon](https://data.humdata.org/dataset/wildfires-south-of-beirut-in-aley-and-chouf-districts-lebanon)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![climate hazards](https://img.shields.io/badge/climate_hazards-blue) ![disaster risk reduction-drr](https://img.shields.io/badge/disaster_risk_reduction--drr-blue) ![fire](https://img.shields.io/badge/fire-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [29.77848841000008, 9.317164134000052, 29.80237060500008, 9.34412975600003]

## Temporal Coverage

- **Start**: 2019-10-17T00:00:00Z
- **End**: 2019-10-23T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SourceID | string |  |
| Picture | binary |  |
| Exs | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Definite; 2 = Doubtful. The decoded text is in `Exs_label`. |
| Notes | string | Free-text notes by the analyst. |
| RoadID | string |  |
| ONme | string |  |
| RteNme | string |  |
| FClass | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Highway; 2 = Primary; 3 = Secondary; 4 = Tertiary; 5 = Local/ Urban; 6 = Trail; 7 = Private. The decoded text is in `FClass_label`. |
| SrfTpe | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Paved; 2 = Gravel; 3 = Dirt/Sand; 4 = Steel; 5 = Wood; 6 = Grass. The decoded text is in `SrfTpe_label`. |
| SrfCond | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Rough (<40kph); 2 = Smooth (>40kph); 3 = Snow/Ice; 4 = Mud. The decoded text is in `SrfCond_label`. |
| SrfPrep | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Natural Compaction; 2 = Traffic Compaction; 3 = Engineered Compaction; 4 = Uncompacted. The decoded text is in `SrfPrep_label`. |
| IsSeasonal | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Yes; 2 = No. The decoded text is in `IsSeasonal_label`. |
| CurntPrac | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Non-motorized; 2 = Motorbike; 3 = 4WD < 3.5MT; 4 = Light truck < 10MT; 5 = Heavy truck < 20MT; 6 = Truck + Trailer > 20MT. The decoded text is in `CurntPrac_label`. |
| GdWthrPrac | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Non-motorized; 2 = Motorbike; 3 = 4WD < 3.5MT; 4 = Light truck < 10MT; 5 = Heavy truck < 20MT; 6 = Truck + Trailer > 20MT. The decoded text is in `GdWthrPrac_label`. |
| BdWthrPrac | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Non-motorized; 2 = Motorbike; 3 = 4WD < 3.5MT; 4 = Light truck < 10MT; 5 = Heavy truck < 20MT; 6 = Truck + Trailer > 20MT. The decoded text is in `BdWthrPrac_label`. |
| CurntSpeed | int32 |  |
| IsUndrCstr | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Yes; 2 = No. The decoded text is in `IsUndrCstr_label`. |
| CstWrkETC | timestamp[us, tz=UTC] |  |
| Sec | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Category A: low risk; 2 = Category B: low to medium risk; 3 = Category C: medium to high risk; 4 = Category D: high risk; 5 = Category E: critical risk. The decoded text is in `Sec_label`. |
| OpStatus | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Open; 2 = Restricted; 3 = Closed; 4 = Abandonned/Disused. The decoded text is in `OpStatus_label`. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| StaffID | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 22 = WP; 33 = LB; 44 = JL; 55 = VG; 66 = CJ; 77 = LD; 88 = HK; 99 = ER; 100 = KM; 111 = MFB; 777 = SB; 1000 = Unknown. The decoded text is in `StaffID_label`. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| BdWthrPrac_label | string | `BdWthrPrac` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| CurntPrac_label | string | `CurntPrac` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Exs_label | string | `Exs` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| FClass_label | string | `FClass` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| GdWthrPrac_label | string | `GdWthrPrac` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| IsSeasonal_label | string | `IsSeasonal` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| IsUndrCstr_label | string | `IsUndrCstr` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| OpStatus_label | string | `OpStatus` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Sec_label | string | `Sec` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SrfCond_label | string | `SrfCond` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SrfPrep_label | string | `SrfPrep` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SrfTpe_label | string | `SrfTpe` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fr20191016lbn-other-lines.parquet | 17.3 KB | 12206509e502... |
| ./fr20191016lbn-other-lines.pmtiles | 30.4 KB | 122060b3bc60... |
| ./styles/default.json | 401 B | 12206f6fdae9... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fr20191016lbn-other-lines.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/fire-hotspots-density-in-lebanon-and-syria-as-detected-by-viirs-between-october-15-16-2019](https://data.humdata.org/dataset/fire-hotspots-density-in-lebanon-and-syria-as-detected-by-viirs-between-october-15-16-2019)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Roads`.

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

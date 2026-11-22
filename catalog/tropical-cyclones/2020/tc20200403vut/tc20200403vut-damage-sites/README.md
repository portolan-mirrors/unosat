# Damage sites: Tropical cyclone, Vanuatu, 3 April 2020 (TC20200403VUT)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/tropical-cyclones/2020/tc20200403vut/tc20200403vut-damage-sites/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Damage sites for Tropical cyclone, Vanuatu, 3 April 2020 (TC20200403VUT): 14,381 features merged from 18 source layers. Point layers with a damage class column (such as `Main_Damage_Site_Class`): one point per assessed structure or site. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Buildings Damage Assessment & Related Density in South of Sanma Province, Vanuatu](https://data.humdata.org/dataset/buildings-damage-assessment-related-density-in-south-of-sanma-province-vanuatu)
- [Damage Assessment in Ambae Island, Penama Province, Vanuatu](https://data.humdata.org/dataset/damage-assessment-in-ambae-island-penama-province-vanuatu)
- [Damage Assessment in CanalFanafo, Luganville and South East Santo Municipalities, Sanma Province, Vanuatu](https://data.humdata.org/dataset/damage-assessment-in-canalfanafo-luganville-and-south-east-santo-municipalities-sanma-prov)
- [Damage Assessment in Luganville Municipality, Sanma Province, Vanuatu](https://data.humdata.org/dataset/damage-assessment-in-luganville-municipality-sanma-province-vanuatu)
- [Damage Assessment in Maewo Island, Penama Province, Vanuatu](https://data.humdata.org/dataset/damage-assessment-in-maewo-island-penama-province-vanuatu)
- [Damage Assessment in Malampa Province, Vanuatu](https://data.humdata.org/dataset/damage-assessment-in-malampa-province-vanuatu)
- [Damage Assessment in Malo Island, Sanma Province, Vanuatu](https://data.humdata.org/dataset/damage-assessment-in-malo-island-sanma-province-vanuatu)
- [Damage Assessment in Paama Island, Malampa Province, Vanuatu](https://data.humdata.org/dataset/damage-assessment-in-paama-island-malampa-province-vanuatu)
- [Damage Assessment in West Santo and South Santo Municipality, Sanma Province, Vanuatu](https://data.humdata.org/dataset/damage-assessment-in-west-santo-and-south-santo-municipality-sanma-province-vanuatu)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![cyclones-hurricanes-typhoons](https://img.shields.io/badge/cyclones--hurricanes--typhoons-blue) ![geodata](https://img.shields.io/badge/geodata-blue) ![tropical cyclone](https://img.shields.io/badge/tropical_cyclone-blue)

## Spatial Coverage

- **Bounding Box**: [166.7025433350001, -16.535481089999905, 168.27263837200007, -14.931900835999954]

## Temporal Coverage

- **Start**: 2020-04-09T00:00:00Z
- **End**: 2020-04-29T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SiteID | int16 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `SiteID_label`, which is decoded per source file. |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `SensorID_label`, which is decoded per source file. |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Settlement_Name | string |  |
| Notes | string | Free-text notes by the analyst. |
| Main_Damage_Site_Class | int16 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `Main_Damage_Site_Class_label`, which is decoded per source file. |
| Grouped_Damage_Classes | int16 | Coded value. The source geodatabase domain gives: 1 = Damaged Buildings; 2 = Damaged Greenhouses; 3 = Impacts on Roads / Bridges; 4 = Impacts in Fields; 5 = Damaged Road segments. The decoded text is in `Grouped_Damage_Classes_label`. |
| StaffID | int32 | Coded value. The 2 source files of this collection use 2 different domains for it, so read `StaffID_label`, which is decoded per source file. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Organization | string |  |
| ConfidenceID_label | string | `ConfidenceID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| FieldValidation_label | string | `FieldValidation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Grouped_Damage_Classes_label | string | `Grouped_Damage_Classes` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Main_Damage_Site_Class_label | string | `Main_Damage_Site_Class` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SiteID_label | string | `SiteID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| ImageID_Num | int32 |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./tc20200403vut-damage-sites.parquet | 586.4 KB | 1220a760e6c0... |
| ./tc20200403vut-damage-sites.pmtiles | 954.3 KB | 1220523dc4a1... |
| ./styles/default.json | 1.1 KB | 12204c296a15... |
| ./tc20200403vut-damage-sites.thumb.jpg | 13.4 KB | 12205dd1b9fe... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./tc20200403vut-damage-sites.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/buildings-damage-assessment-related-density-in-south-of-sanma-province-vanuatu](https://data.humdata.org/dataset/buildings-damage-assessment-related-density-in-south-of-sanma-province-vanuatu)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Damage_Points_AOI10_MaewoIsland`, `Damage_Points_AOI11_Oba`, `Damage_Points_AOI12_SouthSanto`, `Damage_Points_AOI13_Paama`, `Damage_Points_AOI4_PortSandwich`, `Damage_Points_AOI5_Sanma`, `Damage_Points_AOI6_Malampa`, `Damage_Points_AOI7_Panbanglap`, `Damage_Points_AOI8_Oral`, `Damage_Points_AOI9_Pentacost`, `Damage_Road_AOI11_Oba`, `Damage_Road_AOI12_SouthSanto`, `Damage_Road_AOI9_Pentacost`, `Damage_Road_NorthSanto`, `Damage_Road_SouthEastMalekula`, `Erosion_Points_AOI6_Malampa`, `Erosion_Points_AOI9_Pentacost`, `Landslide_Points_NorthSanto`.

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

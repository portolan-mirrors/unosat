# Other points: Tropical cyclone, Cuba, Dominican Republic, Haiti and 1 more, 3 October 2016 (TC20161003HTI)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/tropical-cyclones/2016/tc20161003hti/tc20161003hti-other-points/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Other points for Tropical cyclone, Cuba, Dominican Republic, Haiti and 1 more, 3 October 2016 (TC20161003HTI): 859 features merged from 7 source layers. Points layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Damage Assessment Overview of Jérémie area, Grande Anse Department](https://data.humdata.org/dataset/damage-assessment-overview-of-jeremie-area-grande-anse-department)
- [Damage Assessment Overview of Tiburon Commune, Sud Department](https://data.humdata.org/dataset/damage-assessment-overview-of-tiburon-commune-sud-department)
- [Damage Assessment of Tiburon town and surroundings](https://data.humdata.org/dataset/damage-assessment-of-tiburon-town-and-surroundings)
- [Haiti - Damage Assessment Overview of Dame Marie and Anse d'Hainault Areas, Grande Anse & Sud Departments](https://data.humdata.org/dataset/damage-assessment-overview-of-dame-marie-and-anse-d-hainault-areas-grande-anse-sud-departments)
- [Preliminary Satellite Based Damage Assessment Report - UPDATE 1: Grand Anse Département, Haiti](https://data.humdata.org/dataset/preliminary-satellite-based-damage-assessment-report-update-1-grand-anse-departement-haiti)
- [Preliminary Satellite Based Damage Assessment Report - UPDATE 3: Grand Anse and Sud Départements, Haiti](https://data.humdata.org/dataset/preliminary-satellite-based-damage-assessment-report-update-3-grand-anse-and-sud-departements-haiti)
- [Preliminary Satellite Based Damage Assessment Report: Grand Anse Département, Haiti](https://data.humdata.org/dataset/preliminary-satellite-based-damage-assessment-report-grand-anse-departement-haiti)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![cyclones-hurricanes-typhoons](https://img.shields.io/badge/cyclones--hurricanes--typhoons-blue) ![geodata](https://img.shields.io/badge/geodata-blue) ![tropical cyclone](https://img.shields.io/badge/tropical_cyclone-blue)

## Spatial Coverage

- **Bounding Box**: [-74.46958136399996, 18.285867777000078, -73.74918454299996, 18.671416514000043]

## Temporal Coverage

- **Start**: 2016-10-14T00:00:00Z
- **End**: 2016-11-24T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SourceID | string |  |
| Picture | binary |  |
| Exs | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Definite; 2 = Doubtful. The decoded text is in `Exs_label`. |
| Notes | string | Free-text notes by the analyst. |
| ObstacleID | string |  |
| Type | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Mines / UXO; 2 = Roadblock; 3 = Checkpoint-official; 4 = Checkpoint-unofficial; 5 = Debris; 6 = Wreckage; 7 = Avalanche / Snow; 8 = Flood; 9 = Landslide / Mudslide; 10 = Ford; 11 = Electric lines; 12 = Trees; 13 = Rapids / Cataracts; 14 = Dam; 15 = Sand bank; 16 = Submerged rock; 17 = Road damage; 18 = Railway damage; 19 = Bridge damage; 20 = Culvert damage; 21 = Traffic restriction; 22 = Overhead clearance; 23 = Ferry; 99 = Other (used for labelling). The decoded text is in `Type_label`. |
| Opstatus | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Open; 2 = Restricted; 3 = Closed; 4 = Abandonned/Disused. The decoded text is in `Opstatus_label`. |
| CurntPRAC | int32 | Coded value. The source geodatabase domain gives: 0 = Unspecified; 1 = Non-motorized; 2 = Motorbike; 3 = 4WD < 3.5MT; 4 = Light truck < 10MT; 5 = Heavy truck < 20MT; 6 = Truck + Trailer > 20MT. The decoded text is in `CurntPRAC_label`. |
| ReportNme | string |  |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| CurntPRAC_label | string | `CurntPRAC` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Exs_label | string | `Exs` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Opstatus_label | string | `Opstatus` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Type_label | string | `Type` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./tc20161003hti-other-points.parquet | 26.6 KB | 122006aeb352... |
| ./tc20161003hti-other-points.pmtiles | 82.7 KB | 12200649b4db... |
| ./styles/default.json | 695 B | 12208d30fe58... |
| ./tc20161003hti-other-points.thumb.jpg | 11.7 KB | 122023538e1c... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./tc20161003hti-other-points.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/damage-assessment-of-tiburon-town-and-surroundings](https://data.humdata.org/dataset/damage-assessment-of-tiburon-town-and-surroundings)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `PL20161007_UNOSAT_Obstacles_AOI1`, `PL20161012_UNOSAT_Obstacles_AOI2`, `PL20161109_UNOSAT_Obstacles_AOI3`, `WV20161017_UNOSAT_Obstacles_AOI4`.

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

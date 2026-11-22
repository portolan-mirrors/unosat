# Damage sites: Flood, Central African Republic, 28 October 2019 (FL20191028CAF)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2019/fl20191028caf/fl20191028caf-damage-sites/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Damage sites for Flood, Central African Republic, 28 October 2019 (FL20191028CAF): 395 features merged from 1 source layer. Point layers with a damage class column (such as `Main_Damage_Site_Class`): one point per assessed structure or site. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Satellite detected waters extents, as of 17 November 2019 over Basse-Kotto Prefecture of Central African Republic](https://data.humdata.org/dataset/waters-extents-as-of-17-november-2019-over-basse-kotto-prefecture-of-central-african-repub)
- [Satellite detected waters extents, as of 17 November 2019 over Ouaka Prefecture of Central African Republic](https://data.humdata.org/dataset/waters-extents-as-of-17-november-2019-over-ouaka-prefecture-of-central-african-republic)
- [Satellite detected waters extents, as of 17 November 2019 over Ouaka and Basse-Kotto, Central African Republic](https://data.humdata.org/dataset/waters-extents-as-of-17-november-2019-over-ouaka-and-basse-kotto-central-african-republic)
- [Satellite detected waters extents, as of 18 November 2019 over Basse-Kotto Prefecture-CAR and Nord-Ubangi Province-DRC](https://data.humdata.org/dataset/waters-extents-as-of-18-november-2019-over-basse-kotto-prefecture-car-and-nord-ubangi-prov)
- [Satellite detected waters extents, as of 5 November 2019 over Ouaka Prefecture of Central African Republic](https://data.humdata.org/dataset/waters-extents-as-of-5-november-2019-over-ouaka-prefecture-of-central-african-republic)
- [Satellite-detected water extents, as of 5 November 2019 over Basse-Kotto Prefecture of the Central African Republic](https://data.humdata.org/dataset/water-extents-as-of-5-november-2019-over-basse-kotto-prefecture-of-the-central-african-rep)
- [Satellite-detected water extents, as of 5 November 2019 over Basse-Kotto Prefectures of the Central African Republic](https://data.humdata.org/dataset/water-extents-as-of-5-november-2019-over-basse-kotto-prefectures-of-the-central-african-re)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [20.929966354000044, 4.31619515400007, 21.178289014000086, 4.446606366000083]

## Temporal Coverage

- **Start**: 2019-11-13T00:00:00Z
- **End**: 2019-11-22T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SiteID | int16 |  |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The source geodatabase domain gives: 1 = Worldview-1; 2 = Worldview-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = Komsat-2; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleadies; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 999 = Combination of Sensors. The decoded text is in `SensorID_label`. |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Settlement_Name | string |  |
| Notes | string | Free-text notes by the analyst. |
| Main_Damage_Site_Class | int16 | Coded value. The source geodatabase domain gives: 1 = Destroyed; 2 = Severe Damage; 3 = Moderate Damage; 4 = Possible Damage; 5 = Impact Crater (Damage to Road); 6 = No Visible Damage; 7 = Impact Crater (Damage to Field); 8 = Destroyed (Demolition Zone); 9 = Suspected Phosphorus shell Attack Zone; 10 = Road Damage from Tank Passage; 11 = Possible Damage from adjacent impact, debris. The decoded text is in `Main_Damage_Site_Class_label`. |
| Grouped_Damage_Classes | int16 | Coded value. The source geodatabase domain gives: 1 = Damaged Buildings; 2 = Damaged Greenhouses; 3 = Impacts on Roads / Bridges; 4 = Impacts in Fields; 5 = Damaged Road segments. The decoded text is in `Grouped_Damage_Classes_label`. |
| StaffID | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 22 = WP; 33 = LB; 44 = JL; 55 = MF; 66 = CA; 77 = LD; 88 = HK; 99 = ER; 100 = KM; 111 = MBF. The decoded text is in `StaffID_label`. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| ConfidenceID_label | string | `ConfidenceID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| FieldValidation_label | string | `FieldValidation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Grouped_Damage_Classes_label | string | `Grouped_Damage_Classes` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Main_Damage_Site_Class_label | string | `Main_Damage_Site_Class` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20191028caf-damage-sites.parquet | 21.4 KB | 12209efe94ba... |
| ./fl20191028caf-damage-sites.pmtiles | 59.9 KB | 12204164124b... |
| ./styles/default.json | 956 B | 122004970e8e... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20191028caf-damage-sites.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/water-extents-as-of-5-november-2019-over-basse-kotto-prefecture-of-the-central-african-rep](https://data.humdata.org/dataset/water-extents-as-of-5-november-2019-over-basse-kotto-prefecture-of-the-central-african-rep)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `WV02_20191102_DamageSites_Mobaye_CAF`.

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

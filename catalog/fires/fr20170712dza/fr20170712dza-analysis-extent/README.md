# Analysis extent: Fire, Algeria, 12 July 2017 (FR20170712DZA)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/fires/fr20170712dza/fr20170712dza-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Analysis extent for Fire, Algeria, 12 July 2017 (FR20170712DZA): 10,528 features merged from 3 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Densité des foyers d'incendies au nord de l'Algérie entre le 17 et le 19 juillet 2017](https://data.humdata.org/dataset/densite-des-foyers-d-incendies-au-nord-de-l-algerie-entre-le-17-et-le-19-juillet-2017)
- [Densité des foyers d'incendies dans le nord de l'Algérie entre le 01 et le 13 juillet 2017](https://data.humdata.org/dataset/densite-des-foyers-d-incendies-dans-le-nord-de-l-algerie-entre-le-01-et-le-13-juillet-2017)
- [Feux de Forêts au Nord de l'Algérie- Impact dans les wilayas de Tizi Ouzou, Boumerdès et Bouira](https://data.humdata.org/dataset/feux-de-forets-au-nord-de-l-algerie-impact-dans-les-wilayas-de-tizi-ouzou-boumerdes-et-bouira)
- [Feux de Forêts au nord de l'Algérie -  Impact dans les wilayas de Médéa et de Blida](https://data.humdata.org/dataset/feux-de-forets-au-nord-de-l-algerie-impact-dans-les-wilayas-de-medea-et-de-blida)
- [Feux de Forêts au nord de l'Algérie - Impact dans la wilaya de Médéa](https://data.humdata.org/dataset/feux-de-forets-au-nord-de-l-algerie-impact-dans-la-wilaya-de-medea)
- [Feux de Forêts au nord de l'Algérie - Impact dans les wilayas de Tizi Ouzou et de Béjaia](https://data.humdata.org/dataset/feux-de-forets-au-nord-de-l-algerie-impact-dans-les-wilayas-de-tizi-ouzou-et-de-bejaia)
- [Feux de Forêts dans les Wilayas Boumerdès et Tizi Ouzou, Algérie](https://data.humdata.org/dataset/feux-de-forets-dans-les-wilayas-boumerdes-et-tizi-ouzou-algerie)
- [Impact des Feux de Forêts dans les Wilayas de Médéa et d'Ain Defla](https://data.humdata.org/dataset/impact-des-feux-de-forets-dans-les-wilayas-de-medea-et-d-ain-defla)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![climate hazards](https://img.shields.io/badge/climate_hazards-blue) ![fire](https://img.shields.io/badge/fire-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [1.888653052000052, 35.543019077000054, 4.856668993000085, 36.97524490100005]

## Temporal Coverage

- **Start**: 2017-07-14T00:00:00Z
- **End**: 2017-07-25T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT-4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT-6; 42 = Sentinel-1; 43 = Kompsat-2; 44 = Sentinel-2; 45 = Sentinel-3; 46 = Kompsat-3; 47 = Deimos-2; 48 = TripleSat; 49 = PlanetLabs; 50 = RapidEye; 51 = WorldView-4; 52 = SPOT-7; 999 = Combination of Sensors. The decoded text is in `SensorID_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 16 = HA; 18 = AM; 22 = WP; 33 = LB; 44 = JL; 45 = MD; 54 = HP; 55 = VG; 57 = PG; 66 = CJ; 73 = RS; 77 = LD; 88 = HK; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 141 = KJP; 151 = MNY; 161 = DC; 171 = SR; 222 = CS; 1000 = Unknown. The decoded text is in `StaffID_label`. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Area_ha | float | Area in hectares, as UNOSAT computed it. |
| Staff_ID | int32 |  |
| Agency | int16 | Coded value. The source geodatabase domain gives: 1 = UNOSAT; 2 = ASAL. The decoded text is in `Agency_label`. |
| Shape_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Shape_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Agency_label | string | `Agency` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| ConfidenceID_label | string | `ConfidenceID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| FieldValidation_label | string | `FieldValidation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fr20170712dza-analysis-extent.parquet | 15.4 MB | 1220ffa11999... |
| ./fr20170712dza-analysis-extent.pmtiles | 6.4 MB | 12204f9bcdaf... |
| ./styles/default.json | 671 B | 12205645af41... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fr20170712dza-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/densite-des-foyers-d-incendies-au-nord-de-l-algerie-entre-le-17-et-le-19-juillet-2017](https://data.humdata.org/dataset/densite-des-foyers-d-incendies-au-nord-de-l-algerie-entre-le-17-et-le-19-juillet-2017)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `ST20170719_FR20170712DZA_TiziOuzou_Boumerdes_Bouira_CloudMask`, `ST_20170719_FR20170712DZA_zone_incendiee_Medea_cloud`, `ST_20170719_FR20170712DZA_zone_incendiee_TiziOuzou_Bejaia_cloud`.

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

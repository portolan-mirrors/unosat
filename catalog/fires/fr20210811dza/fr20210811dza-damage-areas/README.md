# Damage areas: Fire, Algeria, 11 August 2021 (FR20210811DZA)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/fires/fr20210811dza/fr20210811dza-damage-areas/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Damage areas for Fire, Algeria, 11 August 2021 (FR20210811DZA): 253 features merged from 4 source layers. Polygon layers with a damage class column: damaged areas, zones, or density cells. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Densité des foyers d'incendies dans les wilayas de Bejaia et Tizi Ouzou entre le 09 et le 16 août 2021](https://data.humdata.org/dataset/densite-des-foyers-d-incendies-dans-les-wilayas-de-bejaia-et-tizi-ouzou-entre-le-09-et-le-)
- [Densité des foyers d'incendies dans les wilayas de Bejaia et Tizi Ouzou entre le 10 et le 12 août 2021](https://data.humdata.org/dataset/densite-des-foyers-d-incendies-dans-les-wilayas-de-bejaia-et-tizi-ouzou-entre-le-10-et-le-)
- [Densité des foyers d'incendies dans les wilayas de Bejaia et Tizi Ouzou entre le 11 et le 13 août 2021](https://data.humdata.org/dataset/densite-des-foyers-d-incendies-dans-les-wilayas-de-bejaia-et-tizi-ouzou-entre-le-11-et-le-)
- [Zones incendiées le 12 août 2021 dans les wilayas de Blida, Bouira et Medea, Algérie](https://data.humdata.org/dataset/zones-incendiees-le-12-aout-2021-dans-les-wilayas-de-blida-bouira-et-medea-algerie)
- [Zones incendiées le 15 août 2021 dans la  commune d'El Amra, wilaya d'Ain-Defla, Algérie](https://data.humdata.org/dataset/zones-incendiees-le-15-aout-2021-dans-la-commune-d-el-amra-wilaya-d-ain-defla-algerie)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![disaster risk reduction-drr](https://img.shields.io/badge/disaster_risk_reduction--drr-blue) ![fire](https://img.shields.io/badge/fire-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [1.823011976000089, 36.171840528000075, 8.67720058000009, 37.071945768000035]

## Temporal Coverage

- **Start**: 2021-08-12T00:00:00Z
- **End**: 2021-08-17T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SiteID | int16 | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Staduim; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 42 = Military Facility; 45 = Suspected Mass Grave Site; 46 = Airport Facility; 47 = Church. The decoded text is in `SiteID_label`. |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT-4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT-6; 42 = Sentinel-1; 43 = Kompsat-2; 44 = Sentinel-2; 45 = Sentinel-3; 46 = Kompsat-3; 47 = Deimos-2; 48 = TripleSat; 49 = PlanetLabs; 50 = RapidEye; 51 = WorldView-4; 52 = SPOT-7; 53 = VIIRS; 999 = Combination of Sensors. The decoded text is in `SensorID_label`. |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| Settlement_Name | string |  |
| Notes | string | Free-text notes by the analyst. |
| Main_Damage_Site_Class | int16 | Coded value. The source geodatabase domain gives: 1 = Destroyed; 2 = Severe Damage; 3 = Moderate Damage; 4 = Possible Damage; 5 = Impact Crater (Damage to Road); 6 = No Visible Damage; 7 = Impact Crater (Damage to Field); 8 = Destroyed (Demolition Zone); 9 = Suspected Phosphorus shell Attack Zone; 10 = Road Damage from Tank Passage; 11 = Possible Damage from adjacent impact, debris; 12 = Lava Flow; 13 = Hotspot; 14 = Burned area. The decoded text is in `Main_Damage_Site_Class_label`. |
| Grouped_Damage_Classes | int16 | Coded value. The source geodatabase domain gives: 1 = Damaged Buildings; 2 = Damaged Greenhouses; 3 = Impacts on Roads / Bridges; 4 = Impacts in Fields; 5 = Damaged Road segments. The decoded text is in `Grouped_Damage_Classes_label`. |
| StaffID | int16 | Coded value. The source geodatabase domain gives: 11 = EB; 18 = TH; 22 = WP; 33 = LB; 44 = JL; 45 = MD; 54 = HP; 55 = VG; 57 = PG; 66 = CJ; 70 = SG; 73 = RS; 77 = LD; 88 = HK; 91 = KA; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 141 = KJP; 151 = MNY; 161 = DC; 171 = SR; 181 = NL; 191 = DH; 212 = MH; 213 = JT; 214 = ES; 215 = KB; 216 = JY; 218 = PA; 219 = SS; 222 = CS; 1000 = Unknown. The decoded text is in `StaffID_label`. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Area_m2 | float | Area in square metres, as UNOSAT computed it. |
| Area_ha | float | Area in hectares, as UNOSAT computed it. |
| ImageID_Num | int32 |  |
| Shape_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Shape_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
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
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fr20210811dza-damage-areas.parquet | 1.4 MB | 1220778072db... |
| ./fr20210811dza-damage-areas.pmtiles | 3.3 MB | 1220c7efc0d2... |
| ./styles/default.json | 951 B | 12207b2fbece... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fr20210811dza-damage-areas.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/densite-des-foyers-d-incendies-dans-les-wilayas-de-bejaia-et-tizi-ouzou-entre-le-09-et-le-](https://data.humdata.org/dataset/densite-des-foyers-d-incendies-dans-les-wilayas-de-bejaia-et-tizi-ouzou-entre-le-09-et-le-)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `S2_20210812_BurnedArea_Blida_Bouria_Medea`, `S2_20210815_BurnedArea_AinDefla`, `VIIRS_20210810_20210812_HotspotDensity_Bejaia_TiziOuzou`, `VIIRS_20210811_20210813_HotspotDensity_NorthAlgeria`.

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

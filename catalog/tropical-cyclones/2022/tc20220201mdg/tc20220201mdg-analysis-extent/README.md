# Analysis extent: Tropical cyclone, Madagascar, 1 February 2022 (TC20220201MDG)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/tropical-cyclones/2022/tc20220201mdg/tc20220201mdg-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Analysis extent for Tropical cyclone, Madagascar, 1 February 2022 (TC20220201MDG): 12 features merged from 12 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Satellite detected water extents in Betroka district, Anosy region, Madagascar as of 9 February 2022](https://data.humdata.org/dataset/water-extents-in-betroka-district-anosy-region-madagascar-as-of-9-february-2022)
- [Satellite detected water extents in Farafangana and Vangaindrano districts, Atsimo Atsinanana region, as of 15 Feb.2022](https://data.humdata.org/dataset/water-extents-in-farafangana-and-vangaindrano-districts-atsimo-atsinanana-region-as-of-15-)
- [Satellite detected water extents in Farafangana and Vangaindrano districts, Atsimo Atsinanana region, as of 8 Feb. 2022](https://data.humdata.org/dataset/water-extents-in-farafangana-and-vangaindrano-districts-atsimo-atsinanana-region-as-of-8-f)
- [Satellite detected water extents in Farafangana district, Atsimo Atsinanana region, Madagascar  as of 8 February 2022](https://data.humdata.org/dataset/water-extents-in-farafangana-district-atsimo-atsinanana-region-madagascar-as-of-8-february)
- [Satellite detected water extents in Farafangana district, Atsimo Atsinanana region, Madagascar as of 15 February 2022](https://data.humdata.org/dataset/water-extents-in-farafangana-district-atsimo-atsinanana-region-madagascar-as-of-15-februar)
- [Satellite detected water extents in Isandra, Lalangina, and Vohibato districts, Haute Matsiatra region, as of 12 Feb. 22](https://data.humdata.org/dataset/water-extents-in-isandra-lalangina-and-vohibato-districts-haute-matsiatra-region-as-of-12-)
- [Satellite detected water extents in Miandrivozo district, Menabe region, Madagascar as of 7 February 2022](https://data.humdata.org/dataset/water-extents-in-miandrivozo-district-menabe-region-madagascar-as-of-7-february-2022)
- [Satellite detected water extents in Midongy-Atsimo district, Atsimo Atsinanana region, Madagascar as of 8 February 2022](https://data.humdata.org/dataset/water-extents-in-midongy-atsimo-district-atsimo-atsinanana-region-madagascar-as-of-8-febru)
- [Satellite detected water extents in Vatovavy Fitovinany region, Madagascar  as of 8 February 2022](https://data.humdata.org/dataset/water-extents-in-vatovavy-fitovinany-region-madagascar-as-of-8-february-2022)
- [Satellite-detected water extents  in Amboasary-Atsimo and Taolagnaro districts, Anosy region as of 8 February 2022](https://data.humdata.org/dataset/water-extents-in-amboasary-atsimo-and-taolagnaro-districts-anosy-region-as-of-8-february-2)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![cyclones-hurricanes-typhoons](https://img.shields.io/badge/cyclones--hurricanes--typhoons-blue) ![geodata](https://img.shields.io/badge/geodata-blue) ![tropical cyclone](https://img.shields.io/badge/tropical_cyclone-blue)

## Spatial Coverage

- **Bounding Box**: [45.33512177100005, -25.200634100999935, 48.24292451000008, -19.244340595999915]

## Temporal Coverage

- **Start**: 2022-02-08T00:00:00Z
- **End**: 2022-02-17T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT-4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT-6; 42 = Sentinel-1; 43 = Kompsat-2; 44 = Sentinel-2; 45 = Sentinel-3; 46 = Kompsat-3; 47 = Deimos-2; 48 = TripleSat; 49 = PlanetLabs; 50 = RapidEye; 51 = WorldView-4; 52 = SPOT-7; 999 = Combination of Sensors. The decoded text is in `SensorID_label`. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 18 = TH; 22 = WP; 33 = LB; 44 = JL; 45 = MD; 54 = HP; 55 = VG; 57 = PG; 66 = CJ; 70 = SG; 73 = RS; 77 = LD; 88 = HK; 91 = KA; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 141 = KJP; 151 = MNY; 161 = DC; 171 = SR; 181 = NL; 191 = DH; 212 = MH; 213 = JT; 214 = ES; 215 = KB; 216 = JY; 218 = PA; 219 = SS; 222 = CS; 1000 = AI. The decoded text is in `StaffID_label`. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Area_ha | float | Area in hectares, as UNOSAT computed it. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| ConfidenceID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `ConfidenceID_label`. |
| FieldValidation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `FieldValidation_label`. |
| ConfidenceID_label | string | `ConfidenceID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| FieldValidation_label | string | `FieldValidation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./tc20220201mdg-analysis-extent.parquet | 943.8 KB | 1220cfa3cf53... |
| ./tc20220201mdg-analysis-extent.pmtiles | 900.8 KB | 122020f903f5... |
| ./styles/default.json | 671 B | 12208e949fe6... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./tc20220201mdg-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/water-extents-in-amboasary-atsimo-and-taolagnaro-districts-anosy-region-as-of-8-february-2](https://data.humdata.org/dataset/water-extents-in-amboasary-atsimo-and-taolagnaro-districts-anosy-region-as-of-8-february-2)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `K5_20220212_AnalysisExtent_HauteMatsiatra`, `RCM3_20220208_AnalysisExtent_Vangaindrano_Farafangana`, `S1_20220208_AnalysisExtent_AmboasaryAtsimo_Taolagnaro`, `S1_20220208_AnalysisExtent_Midongy_Atsimo`, `S1_20220208_AnalysisExtent_VatovavyFitovinany`, `S1_20220215_AnalysisExtent_Farafangana`, `S1_20220215_AnalysisExtent_Vangaindrano_Farafangana`, `S2_20220207_AnalysisExtent_Miandrivozo`, `S2_20220207_CloudObstruction_Miandrivozo`, `S2_20220209_AnalysisExtent_Betroka`, `S2_20220209_CloudObstruction_Betroka`, `TSX_20220208_AnalysisExtent_Farafangana`.

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

# Analysis extent: Earthquake, Syrian Arab Republic, Türkiye, 6 February 2023 (EQ20230206SYR)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/earthquakes/2023/eq20230206syr/eq20230206syr-analysis-extent/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Analysis extent for Earthquake, Syrian Arab Republic, Türkiye, 6 February 2023 (EQ20230206SYR): 377 features merged from 377 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [6 February 2023 M 7.8 Marash/Antep (Kehramanmarash) Earthquake, Preliminary Satellite-Based Comprehensive Damage Assessment Report](https://data.humdata.org/dataset/6-february-2023-m-7-8-marash-antep-kehramanmarash-earthquake-preliminary-satellite-based-c)
- [Damage Assessment  in Jableh City, Jableh District, Latakia Province, Syria as of 9 February 2023](https://data.humdata.org/dataset/damage-assessment-in-jableh-city-jableh-district-latakia-province-syria-as-of-9-february-2)
- [Damage Assessment Istamo (Latakia) as of 9 February 2023](https://data.humdata.org/dataset/damage-assessment-istamo-latakia-as-of-9-february-2023)
- [Damage Assessment in A'zaz City, Aleppo Governorate, Syria as of 9 February 2023](https://data.humdata.org/dataset/damage-assessment-in-a-zaz-city-aleppo-governorate-syria-as-of-9-february-2023)
- [Damage Assessment in Al Bab, Qabasin and Bza'a towns, Syria as of 11 February 2023](https://data.humdata.org/dataset/damage-assessment-in-al-bab-qabasin-and-bza-a-towns-syria-as-of-11-february-2023)
- [Damage Assessment in Al Bab, Syria as of 11 February 2023](https://data.humdata.org/dataset/damage-assessment-in-al-bab-syria-as-of-11-february-2023)
- [Damage Assessment in Idlib City, Syria as of 9 February 2023](https://data.humdata.org/dataset/damage-assessment-in-idlib-city-syria-as-of-9-february-2023)
- [Damage Assessment in Jindires and the surrounding area, Syria as of 10 February 2023](https://data.humdata.org/dataset/damage-assessment-in-jindires-and-the-surrounding-area-syria-as-of-10-february-2023)
- [Damage Assessment in Jindires, Afrin District, Aleppo Governorate, Syria as of 11 February 2023](https://data.humdata.org/dataset/damage-assessment-in-jindires-afrin-district-aleppo-governorate-syria-as-of-11-february-20)
- [Damage Assessment in Jisr al-Shughur City (Idleb) as of 9 February 2023](https://data.humdata.org/dataset/damage-assessment-in-jisr-al-shughur-city-idleb-as-of-9-february-2023)
- [Damage Assessment in Killi (Idlib District), Syria as of 16 February 2023](https://data.humdata.org/dataset/damage-assessment-in-killi-idlib-district-syria-as-of-16-february-2023)
- [Damage Assessment in Lilawa Village, Jarablus District, Aleppo Governorate, Syria as of 7 February 2023](https://data.humdata.org/dataset/damage-assessment-in-lilawa-village-jarablus-district-aleppo-governorate-syria-as-of-7-feb)
- and 5 more; the event's [catalog page](../catalog.json) lists them all.

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![earthquake](https://img.shields.io/badge/earthquake-blue) ![earthquake-tsunami](https://img.shields.io/badge/earthquake--tsunami-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [35.68472951600006, 35.31902979400007, 37.74933812900008, 36.70989018700004]

## Temporal Coverage

- **Start**: 2023-02-08T00:00:00Z
- **End**: 2023-03-16T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Shape_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Shape_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SiteName | string |  |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| Site_ID | int16 | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Staduim; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 42 = Military Facility; 45 = Suspected Mass Grave Site; 46 = Airport Facility; 47 = Church. The decoded text is in `Site_ID_label`. |
| AgencyID | int32 |  |
| Site_ID_label | string | `Site_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Sensor_ID | string |  |
| StaffID | string | Coded value. The source geodatabase domain gives: 11 = EB; 18 = TH; 22 = WP; 33 = LB; 44 = JL; 45 = MD; 54 = HP; 55 = VG; 57 = PG; 66 = CJ; 70 = SG; 73 = RS; 77 = LD; 88 = HK; 91 = KA; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 141 = KJP; 151 = MNY; 161 = DC; 171 = SR; 181 = NL; 191 = DH; 212 = MH; 213 = JT; 214 = ES; 215 = KB; 216 = JY; 218 = PA; 219 = SS; 220 = MM; 221 = CD; 222 = CS; 1000 = Unknown. The decoded text is in `StaffID_label`. |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT-4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT-6; 42 = Sentinel-1; 43 = Kompsat-2; 44 = Sentinel-2; 45 = Sentinel-3; 46 = Kompsat-3; 47 = Deimos-2; 48 = TripleSat; 49 = PlanetLabs; 50 = RapidEye; 51 = WorldView-4; 52 = SPOT-7; 999 = Combination of Sensors. The decoded text is in `SensorID_label`. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./eq20230206syr-analysis-extent.parquet | 12.9 KB | 122077c639b2... |
| ./eq20230206syr-analysis-extent.pmtiles | 136.5 KB | 1220a9eba87a... |
| ./styles/default.json | 671 B | 122072804dc0... |
| ./eq20230206syr-analysis-extent.thumb.jpg | 8.7 KB | 1220ef50d27e... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./eq20230206syr-analysis-extent.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/6-february-2023-m-7-8-marash-antep-kehramanmarash-earthquake-preliminary-satellite-based-c](https://data.humdata.org/dataset/6-february-2023-m-7-8-marash-antep-kehramanmarash-earthquake-preliminary-satellite-based-c)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `GF2_20230209_AnalysisExtent_Sarmada`, `PHR_20230207_AnalysisExtent_Salqin`, `PHR_20230209_AnalysisExtent_Azaz`, `PHR_20230209_AnalysisExtent_EinElsoda`, `PHR_20230209_AnalysisExtent_Idlib`, `PHR_20230209_AnalysisExtent_Jableh`, `PHR_20230209_AnalysisExtent_Jableh_North`, `PHR_20230209_AnalysisExtent_JisrChoughour`, `PHR_20230209_AnalysisExtent_Latakia`, `PHR_20230209_AnalysisExtent_Stomo`, `PHR_20230210_AnalysisExtent_Jindires`, `PHR_20230211_AnalysisExtent_AlAtaarib`, `PHR_20230211_AnalysisExtent_Albab`, `PHR_20230215_AnalysisExtent_AlAtaarib`, `PHR_20230216_AnalysisExtent_Sarmada`, `PHR_20230216_Analysisextent_Killi`, `S2_20230209_AnalysisExtent_Jakarah_Syria`, `WV2_20230217_AnalysisExtent_AdDana`, `WV2_20230217_AnalysisExtent_Rajo`, `WV3_20230207_AnalysisExtent_Lilawa_Jarablus_Aleppo`, `WV3_20230207_AnalysisExtent_Zayzafun_Azaz_Aleppo`, `WV3_20230211_AnalysisExtent_Yazibaxe`, `WV3_20230212_AnalysisExtent_Afrin`, `WV3_20230212_AnalysisExtent_SgoeNiyarah`, `WV3_20230324_AnalysisExtent_EinElkoroum`.

## Attribution

UNITAR-UNOSAT

## License

[other](https://opendefinition.org/licenses/cc-by-sa/)

## Contact

Portolan Mirrors <nissim@radiant.earth>

## Known Issues

HDX states the license as "Creative Commons Attribution Share-Alike (CC BY-SA)" with no version, so the collection's license is `other`, linked to the license definition HDX gives. This is a preliminary assessment and has not yet been validated in the field. It is important to consider the characteristics of the source imagery used in the analyses when interpreting results. For damage assessments it should be noted that only significant damage to the structural integrity of the buildings analyzed can be seen in imagery, while minor damage such as cracks or holes may not be visible at all. For flood extractions using radar data it is important to note that urban areas and highly vegetated areas may mask the flood signature and result in underestimation of flood waters. Users with specific questions or concerns should contact unosat@unitar.org to seek clarification. This is a preliminary assessment and has not yet been validated in the field. It is important to consider the characteristics of the source imagery used in the analyses when interpreting results. For damage assessments it should be noted that only significant damage to the structural integrity of the buildings analyzed can be seen in imagery, while minor damage such as cracks or holes may not be visible at all. For flood extractions using radar data it is important to note that urban areas and highly vegetated areas may mask the flood signature and result in underestimation of flood waters. Users with specific questions or concerns should contact unosat@unitar.org to seek clarification.
Glide: EQ-2023-000015-TUR

---

*Generated by [Portolan](https://github.com/portolan-sdi/portolan-cli) from STAC metadata and .portolan/metadata.yaml*

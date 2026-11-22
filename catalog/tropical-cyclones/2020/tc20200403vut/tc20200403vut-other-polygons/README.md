# Other polygons: Tropical cyclone, Vanuatu, 3 April 2020 (TC20200403VUT)
[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/tropical-cyclones/2020/tc20200403vut/tc20200403vut-other-polygons/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat) <!-- nav -->

Other polygons for Tropical cyclone, Vanuatu, 3 April 2020 (TC20200403VUT): 1,366 features merged from 9 source layers. Polygons layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

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

- **Bounding Box**: [166.54156380000006, -20.254446646999952, 170.23828392000007, -13.07170687599995]

## Temporal Coverage

- **Start**: 2020-04-09T00:00:00Z
- **End**: 2020-04-29T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Site_ID | int16 | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Staduim; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 45 = Suspected Mass Grave Site. The decoded text is in `Site_ID_label`. |
| AgencyID | int16 | Coded value. The source geodatabase domain gives: 1 = UNOSAT; 2 = COPERNICUS; 3 = NGA. The decoded text is in `AgencyID_label`. |
| SiteName | string |  |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| Area_ha | double | Area in hectares, as UNOSAT computed it. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| AgencyID_label | string | `AgencyID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Site_ID_label | string | `Site_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| Shape_Leng | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| ADM0_EN | string |  |
| ADM0_PCODE | string |  |
| date | timestamp[us, tz=UTC] |  |
| validOn | timestamp[us, tz=UTC] |  |
| ADM1_EN | string |  |
| ADM1_PCODE | string |  |
| ADM2_EN | string |  |
| ADM2_PCODE | string |  |
| validTo | timestamp[us, tz=UTC] |  |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The source geodatabase domain gives: 1 = WorldView-1; 2 = WorldView-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = WorldView-3; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 41 = SPOT 6; 42 = Sentinel-1; 43 = Komsat-2; 999 = Combination of Sensors. The decoded text is in `SensorID_label`. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 22 = WP; 33 = LB; 44 = JL; 55 = VG; 66 = CJ; 73 = RS; 77 = LD; 88 = HK; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 141 = KJP; 151 = MNY; 222 = CS; 1000 = Unknown. The decoded text is in `StaffID_label`. |
| Confidence_ID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `Confidence_ID_label`. |
| Land_Classification | int32 | Coded value. The source geodatabase domain gives: 1 = Forest (Generic); 2 = Grasslands / Shrublands (Generic); 3 = Croplands; 4 = Barren Land; 5 = Aquaculture; 6 = Wetlands / Marshlands; 7 = Riparian; 8 = Urban Area; 9 = Peat; 10 = Tundra; 11 = Mangrove; 12 = Palms / Oasis; 13 = Snow / Ice; 14 = Water; 15 = Not Mapped. The decoded text is in `Land_Classification_label`. |
| Field_Validation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `Field_Validation_label`. |
| Confidence_ID_label | string | `Confidence_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Field_Validation_label | string | `Field_Validation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Land_Classification_label | string | `Land_Classification` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./tc20200403vut-other-polygons.parquet | 2.7 MB | 122037b1d02f... |
| ./tc20200403vut-other-polygons.pmtiles | 2.0 MB | 12209ae2bf60... |
| ./styles/default.json | 664 B | 1220cfd90593... |
| ./tc20200403vut-other-polygons.thumb.jpg | 8.1 KB | 12208d19c74f... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./tc20200403vut-other-polygons.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/buildings-damage-assessment-related-density-in-south-of-sanma-province-vanuatu](https://data.humdata.org/dataset/buildings-damage-assessment-related-density-in-south-of-sanma-province-vanuatu)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `AOI_BLUECHAM_SAS`, `AOI_COPERNICUS`, `AOI_UNOSAT`, `Land_Cover_AOI4_PortSandwich`, `Land_Cover_AOI7_Panbanglap`, `Land_Cover_AOI8_Oral`, `vut_admbnda_adm0`, `vut_admbnda_adm1`, `vut_admbnda_adm2`.

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

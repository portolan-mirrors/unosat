# Other polygons: Complex emergency, State of Palestine, 15 July 2014 (CE20140715PSE)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20140715pse/ce20140715pse-other-polygons/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Other polygons for Complex emergency, State of Palestine, 15 July 2014 (CE20140715PSE): 5,410 features merged from 4 source layers. Polygons layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of 2009-2014 Density Comparison of Destroyed and Severely Damaged Structures in Gaza Strip, Occupied Palestinian Territory](https://data.humdata.org/dataset/geodata-of-2009-2014-density-comparison-of-destroyed-and-severely-damaged-str-september-19-2014)
- [Geodata of Damage Assessment In Central Gaza Strip - Occupied Palestinian Territory - 12 July 2014](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-central-gaza-strip-occupied-palestinian-terri-july-21-2014)
- [Geodata of Damage Assessment in Atatra, Gaza Strip - Occupied Palestinian Territory](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-atatra-gaza-strip-occupied-palestinian-territ-august-04-2014)
- [Geodata of Damage Assessment in Beit Hanun, Gaza Strip - Occupied Palestinian Territory](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-beit-hanun-gaza-strip-occupied-palestinian-te-july-28-2014)
- [Geodata of Damage Assessment in Beit Lahia, Gaza Strip - Occupied Palestinian Territory](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-beit-lahia-gaza-strip-occupied-palestinian-te-july-30-2014)
- [Geodata of Damage Assessment in Gaza City, Gaza Strip - Occupied Palestinian Territory](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-gaza-city-gaza-strip-occupied-palestinian-ter-july-31-2014)
- [Geodata of Damage Assessment in Gaza Strip, Occupied Palestinian Territory](https://data.humdata.org/dataset/geodata-of-health-facilities-damage-assessment-in-gaza-strip-occupied-palesti-september-26-2014)
- [Geodata of Damage Assessment in Jarara Area, Gaza Strip - Occupied Palestinian Territory](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-jarara-area-gaza-strip-occupied-palestinian-t-august-07-2014)
- [Geodata of Damage Assessment in Khuza'a and Al Qararra, Gaza Strip, Occupied Palestinian Territory](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-khuzaa-and-al-qararra-gaza-strip-occupied-pal-august-08-2014)
- [Geodata of Damage Assessment in Northeastern Gaza Strip - Occupied Palestinian Territory](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-northeastern-gaza-strip-occupied-palestinian-july-27-2014)
- [Geodata of Damage Assessment in Rafah, Gaza Strip - Occupied Palestinian Territory](https://data.humdata.org/dataset/geodata-of-damage-assessment-in-rafah-gaza-strip-occupied-palestinian-territo-august-07-2014)
- [Geodata of Damage to Agricultural Areas and Greenhouses, Gaza Strip - Occupied Palestinian Territory](https://data.humdata.org/dataset/geodata-of-damage-to-agricultural-areas-and-greenhouses-gaza-strip-occupied-p-september-23-2014)
- and 5 more; the event's [catalog page](../catalog.json) lists them all.

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![damage assessment](https://img.shields.io/badge/damage_assessment-blue) ![education](https://img.shields.io/badge/education-blue) ![education facilities-schools](https://img.shields.io/badge/education_facilities--schools-blue) ![geodata](https://img.shields.io/badge/geodata-blue) ![health](https://img.shields.io/badge/health-blue) ![health facilities](https://img.shields.io/badge/health_facilities-blue)

## Spatial Coverage

- **Bounding Box**: [34.26489478800005, 31.24088792300006, 34.56238889700006, 31.588293545000056]

## Temporal Coverage

- **Start**: 2014-07-21T00:00:00Z
- **End**: 2014-10-02T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The source geodatabase domain gives: 1 = Worldview-1; 2 = Worldview-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = Komsat-2; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 40 = Landsat-8; 999 = Combination of Sensors. The decoded text is in `SensorID_label`. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| StaffID | int32 | Coded value. The source geodatabase domain gives: 11 = EB; 22 = WP; 33 = LB; 44 = JL; 55 = VG; 66 = CJ; 77 = LD; 88 = HK; 99 = ER; 100 = KM; 111 = MBF; 121 = CN; 131 = SB; 222 = CS; 1000 = Unknown. The decoded text is in `StaffID_label`. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Confidence_ID | int16 | Coded value. The source geodatabase domain gives: 1 = Very High; 2 = Medium; 3 = Uncertain; 4 = To Be Evaluated. The decoded text is in `Confidence_ID_label`. |
| Land_Classification | int32 | Coded value. The source geodatabase domain gives: 1 = Forest (Generic); 2 = Grasslands / Shrublands (Generic); 3 = Croplands; 4 = Barren Land; 5 = Aquaculture; 6 = Wetlands / Marshlands; 7 = Riparian; 8 = Urban Area; 9 = Peat; 10 = Tundra; 11 = Mangrove; 12 = Palms / Oasis; 13 = Snow / Ice; 14 = Water; 15 = Not Mapped. The decoded text is in `Land_Classification_label`. |
| Field_Validation | int16 | Coded value. The source geodatabase domain gives: 0 = Not yet field validated; 1 = Validated (correct); 2 = Validated (not correct); 3 = Site Not Identified in Image. The decoded text is in `Field_Validation_label`. |
| Area_ha | float | Area in hectares, as UNOSAT computed it. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| Confidence_ID_label | string | `Confidence_ID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Field_Validation_label | string | `Field_Validation` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| Land_Classification_label | string | `Land_Classification` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| StaffID_label | string | `StaffID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20140715pse-other-polygons.parquet | 1.1 MB | 1220b8c1d217... |
| ./ce20140715pse-other-polygons.pmtiles | 1.7 MB | 1220da47af4d... |
| ./styles/default.json | 664 B | 1220b96a9016... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20140715pse-other-polygons.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-2009-2014-density-comparison-of-destroyed-and-severely-damaged-str-september-19-2014](https://data.humdata.org/dataset/geodata-of-2009-2014-density-comparison-of-destroyed-and-severely-damaged-str-september-19-2014)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `Vegetation_L8_20140707`, `Vegetation_L8_20140730`.

## Attribution

UNITAR-UNOSAT

## License

[CC-BY-NC-SA-3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/)

## Contact

Portolan Mirrors <nissim@radiant.earth>

## Known Issues

This is a preliminary assessment and has not yet been validated in the field. It is important to consider the characteristics of the source imagery used in the analyses when interpreting results. For damage assessments it should be noted that only significant damage to the structural integrity of the buildings analyzed can be seen in imagery, while minor damage such as cracks or holes may not be visible at all. For flood extractions using radar data it is important to note that urban areas and highly vegetated areas may mask the flood signature and result in underestimation of flood waters. Users with specific questions or concerns should contact unosat@unitar.org to seek clarification.

---

*Generated by [Portolan](https://github.com/portolan-sdi/portolan-cli) from STAC metadata and .portolan/metadata.yaml*

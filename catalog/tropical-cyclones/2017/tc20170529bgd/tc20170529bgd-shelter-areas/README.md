# Shelter areas: Tropical cyclone, Bangladesh, 29 May 2017 (TC20170529BGD)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/tropical-cyclones/2017/tc20170529bgd/tc20170529bgd-shelter-areas/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Shelter areas for Tropical cyclone, Bangladesh, 29 May 2017 (TC20170529BGD): 3 features merged from 3 source layers. Polygon layers with shelter or camp columns, or whose names mention camps, shelters, IDPs, or settlements. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Bangladesh - Satellite Detected Water Extent in Chittagong District, Chittagong  Division](https://data.humdata.org/dataset/satellite-detected-water-extent-in-chittagong-district-chittagong-division-bangladesh)
- [Bangladesh - Satellite Detected Water Extent in Cox's Bazar District, Chittagong Division](https://data.humdata.org/dataset/satellite-detected-water-extent-in-cox-s-bazar-district-chittagong-division-bangladesh)
- [Damage Assessment in Kutupalong Refugee Camp, Palong Khali Union, Bangladesh](https://data.humdata.org/dataset/damage-assessment-in-kutupalong-refugee-camp-palong-khali-union-bangladesh)
- [Damage Assessment in Leda Refugee Camp, Nhilla Union, Bangladesh](https://data.humdata.org/dataset/damage-assessment-in-leda-refugee-camp-nhilla-union-bangladesh)
- [Damage Assessment in Nayapara Refugee Camp, Teknaf Union, Bangladesh](https://data.humdata.org/dataset/damage-assessment-in-nayapara-refugee-camp-teknaf-union-bangladesh)
- [Satellite Detected Water Extent in Maheshkhali, Chakaria and Cox'S Bazar Sadar Upazilas](https://data.humdata.org/dataset/satellite-detected-water-extent-in-maheshkhali-chakaria-and-cox-s-bazar-sadar-upazilas)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![cyclones-hurricanes-typhoons](https://img.shields.io/badge/cyclones--hurricanes--typhoons-blue) ![geodata](https://img.shields.io/badge/geodata-blue) ![tropical cyclone](https://img.shields.io/badge/tropical_cyclone-blue)

## Spatial Coverage

- **Bounding Box**: [92.15781065900006, 20.952092615000083, 92.25388506700006, 21.21583399700006]

## Temporal Coverage

- **Start**: 2017-05-31T00:00:00Z
- **End**: 2017-06-07T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Site_ID | int16 | Coded value. The source geodatabase domain gives: 0 = UN Building; 1 = Mosque; 2 = Hospital; 3 = Refugee / IDP Camp Building; 4 = Market; 5 = School / University; 6 = Square; 7 = Government Building; 9 = Border Crossing Point; 12 = Cemetary; 13 = Ruins; 16 = Staduim; 19 = Sewage Treatment Facility; 21 = Greenhouse; 22 = Bridge; 23 = Road; 24 = Tower; 25 = Prison; 26 = Building (General / Default); 27 = Field; 28 = Industrial Facility; 30 = Refugee / IDP Camp Site; 35 = Transport Vehicle; 40 = Military Base; 41 = Checkpoint; 45 = Suspected Mass Grave Site. The decoded text is in `Site_ID_label`. |
| AgencyID | int32 | Coded value. The source geodatabase domain gives: 1 = UNOSAT. The decoded text is in `AgencyID_label`. |
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
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./tc20170529bgd-shelter-areas.parquet | 8.8 KB | 12201171c73f... |
| ./tc20170529bgd-shelter-areas.pmtiles | 31.4 KB | 1220a3c0ddfb... |
| ./styles/default.json | 658 B | 1220a2bf0f6e... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./tc20170529bgd-shelter-areas.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/damage-assessment-in-kutupalong-refugee-camp-palong-khali-union-bangladesh](https://data.humdata.org/dataset/damage-assessment-in-kutupalong-refugee-camp-palong-khali-union-bangladesh)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `PL_20170605_LedaRefugeeCamp_AOI`, `PL_20170605_NayaparaRefugeeCamp_AOI`, `PL_20170606_KutupalongRefugeeCamp_AOI`.

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

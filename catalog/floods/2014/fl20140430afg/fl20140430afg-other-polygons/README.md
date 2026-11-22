# Other polygons: Flood, Afghanistan, 30 April 2014 (FL20140430AFG)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/floods/2014/fl20140430afg/fl20140430afg-other-polygons/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Other polygons for Flood, Afghanistan, 30 April 2014 (FL20140430AFG): 4 features merged from 4 source layers. Polygons layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from.

From these HDX datasets:

- [Geodata of Estimated Rainfall Accumulation from 30 April to 06 May 2014, Afghanistan](https://data.humdata.org/dataset/geodata-of-estimated-rainfall-accumulation-from-30-april-to-06-may-2014-afgha-may-06-2014)
- [Geodata of Flood Waters Over Khwaja Du Koh, Jawzjan Province, Afghanistan](https://data.humdata.org/dataset/geodata-of-flood-waters-over-khwaja-du-koh-jawzjan-province-afghanistan-may-01-2014)
- [Geodata of Flood Waters Over Khwaja Du Koh, Jawzjan Province, Afghanistan](https://data.humdata.org/dataset/geodata-of-flood-waters-over-khwaja-du-koh-jawzjan-province-afghanistan-may-07-2014)
- [Geodata of Flood Waters Over Kulukh Tapah, Kunduz Province, Afghanistan](https://data.humdata.org/dataset/geodata-of-flood-waters-over-kulukh-tapah-kunduz-province-afghanistan-may-13-2014)
- [Geodata of Flood Waters and Inundation Near Khwaja Du Koh, Jawzjan Province, Afghanistan](https://data.humdata.org/dataset/geodata-of-flood-waters-and-inundation-near-khwaja-du-koh-jawzjan-province-af-may-01-2014)
- [Geodata of Inundation Near Sar-E Pol, Sar-E Pol Province, Afghanistan](https://data.humdata.org/dataset/geodata-of-inundation-near-sar-e-pol-sar-e-pol-province-afghanistan-may-02-2014)
- [Geodata of Inundation Near Sar-E Pol, Sar-E Pol Province, Afghanistan](https://data.humdata.org/dataset/geodata-of-inundation-near-sar-e-pol-sar-e-pol-province-afghanistan-may-07-2014)
- [Geodata of Landslide in Ab Barek, Badakshan Province, Afghanistan](https://data.humdata.org/dataset/geodata-of-landslide-in-ab-barek-badakshan-province-afghanistan-may-04-2014)
- [Geodata of Update: Landslide in Ab Barek, Badakshan Province, Afghanistan](https://data.humdata.org/dataset/geodata-of-landslide-in-ab-barek-badakshan-province-afghanistan-may-08-2014)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![flood](https://img.shields.io/badge/flood-blue) ![flooding](https://img.shields.io/badge/flooding-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [65.51621872700008, 36.14508060300005, 66.04959916300004, 36.91985248900005]

## Temporal Coverage

- **Start**: 2014-05-01T00:00:00Z
- **End**: 2014-05-13T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | int32 | Coded value. The source geodatabase domain gives: 1 = Worldview-1; 2 = Worldview-2; 3 = QuickBird-2; 4 = Ikonos; 5 = GeoEye-1; 6 = Formosat-2; 7 = SPOT-5; 8 = Komsat-2; 9 = MODIS-Aqua; 10 = MODIS-Terra; 11 = ASTER; 12 = EO-1 ALI; 13 = EO-1 Hyperion; 14 = MERIS; 15 = Landsat-7; 16 = Landsat-5; 17 = ASAR WSM; 18 = ASAR IMP; 19 = ASAR GM1; 20 = ASAR AP; 21 = Radarsat-1; 22 = Radarsat-2; 23 = TerraSAR-X; 24 = CosmoSkyMED; 25 = SPOT4; 26 = ALOS PALSAR; 27 = ASAR IMM; 30 = UAV (Swinglet-Cam); 33 = Alos AVNIR; 35 = Pleiades; 36 = DMC; 37 = RISAT-1; 38 = RISAT-2; 39 = RESOURCESAT-1; 999 = Combination of Sensors. The decoded text is in `SensorID_label`. |
| Notes | string | Free-text notes by the analyst. |
| Area_m2 | double | Area in square metres, as UNOSAT computed it. |
| GlobalID | string | ArcGIS global identifier of the feature. |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| Area_ha | float | Area in hectares, as UNOSAT computed it. |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SensorID_label | string | `SensorID` decoded with the coded-value domain of the source geodatabase. Null where the source had no domain or the code is not in it. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./fl20140430afg-other-polygons.parquet | 5.1 KB | 122044fbbba9... |
| ./fl20140430afg-other-polygons.pmtiles | 52.3 KB | 1220b9b317c4... |
| ./styles/default.json | 664 B | 12202e46a77c... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./fl20140430afg-other-polygons.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/geodata-of-estimated-rainfall-accumulation-from-30-april-to-06-may-2014-afgha-may-06-2014](https://data.humdata.org/dataset/geodata-of-estimated-rainfall-accumulation-from-30-april-to-06-may-2014-afgha-may-06-2014)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `KS_20140505_Extent`, `PL_20140501_Extent`, `WV02_20140429_Extent`, `WV02_20140507_Extent`.

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

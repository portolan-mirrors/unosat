# Other points: Complex emergency, Iraq, 13 June 2014 (CE20140613IRQ)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/complex-emergencies/ce20140613irq/ce20140613irq-other-points-epsg_32638/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Other points for Complex emergency, Iraq, 13 June 2014 (CE20140613IRQ): 532 features merged from 13 source layers. Points layers that match none of the named groups. The source layer names below say what each holds. The `source_layer` and `source_file` columns name the layer and file each row came from. The geometry is in EPSG:32638, the CRS of the source layers; the PMTiles copy is in Web Mercator.

From these HDX datasets:

- [Fires at the Al Qayyarah oil field, Nineveh Governorate, between 18 July 2016 and 24 January 2017](https://data.humdata.org/dataset/fires-at-the-al-qayyarah-oil-field-nineveh-governorate-between-18-july-2016-and-24-january-2017)
- [Fires at the Al Qayyarah oil field, Nineveh Governorate, between 18 July 2016 and 7 January 2017](https://data.humdata.org/dataset/fires-at-the-al-qayyarah-oil-field-nineveh-governorate-between-18-july-2016-and-7-january-2017)
- [Fires at the Al Qayyarah oil field, Nineveh Governorate, between 18 July and 14 December, 2016](https://data.humdata.org/dataset/fires-at-the-al-qayyarah-oil-field-nineveh-governorate-between-18-july-and-14-december-2016)
- [Iraq - Environmental damage in Al Qayyarah](https://data.humdata.org/dataset/environmental-damage-in-al-qayyarah-iraq)
- [Iraq - Fires at the Al Qayyarah oil field, Nineveh Governorate](https://data.humdata.org/dataset/fires-at-the-al-qayyarah-oil-field-nineveh-governorate-between-18-july-2016-and-13-march-2017)

Read [AGENTS.md](AGENTS.md) for the columns and query recipes.

![climate hazards](https://img.shields.io/badge/climate_hazards-blue) ![complex emergency](https://img.shields.io/badge/complex_emergency-blue) ![complex emergency-conflict-security](https://img.shields.io/badge/complex_emergency--conflict--security-blue) ![geodata](https://img.shields.io/badge/geodata-blue)

## Spatial Coverage

- **Bounding Box**: [42.13759856566344, 34.01755197125799, 45.038457079689834, 36.618248398722294]

## Temporal Coverage

- **Start**: 2016-07-18T00:00:00Z
- **End**: 2017-03-13T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| Name | string |  |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| SensorDate | timestamp[us, tz=UTC] | Acquisition date of the satellite image the feature was mapped from. |
| SensorID | string |  |
| Confidence | string |  |
| FieldValid | string |  |
| Settlement | string |  |
| Notes | string | Free-text notes by the analyst. |
| StaffID | string |  |
| EventCode | string | UNOSAT event code (or a Copernicus EMSR id), as recorded on the feature. It does not always equal the code of the event subcatalog. |
| ImageID_Nu | int32 |  |
| Status | string |  |
| pointid | int32 |  |
| precip_mm | double |  |
| OBJECTID_1 | int64 |  |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./ce20140613irq-other-points-epsg_32638.parquet | 22.6 KB | 12209341669d... |
| ./ce20140613irq-other-points-epsg_32638.pmtiles | 108.5 KB | 1220bfbfa00c... |
| ./styles/default.json | 706 B | 1220c934b260... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./ce20140613irq-other-points-epsg_32638.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/environmental-damage-in-al-qayyarah-iraq](https://data.humdata.org/dataset/environmental-damage-in-al-qayyarah-iraq)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `CE20140613IRQ_Al_Qayyarah_20161121_oil_fires`, `M77`, `M77_well`, `Oil_Fires`, `rain_over_smoke_20160718_20161025`, `rain_over_smoke_20160718_20161123`, `rain_over_smoke_20160718_20161214`, `rain_over_smoke_20160718_20170107`, `rain_over_smoke_20160718_20170123`, `rain_over_smoke_20160718_20170309`.

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

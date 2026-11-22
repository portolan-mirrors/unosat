# Analysis extent: Tropical cyclone, Vanuatu, 3 April 2020 (TC20200403VUT)
<!-- nav -->[Open in data browser](https://browser.portolan-sdi.org/#/external/data.source.coop/portolan-mirrors/unosat/tropical-cyclones/2020/tc20200403vut/tc20200403vut-analysis-extent-epsg_32758/collection.json) · [Source repository](https://github.com/portolan-mirrors/unosat) · [Report a problem](https://github.com/portolan-mirrors/unosat/issues) · [Hosting repository](https://source.coop/portolan-mirrors/unosat)

Analysis extent for Tropical cyclone, Vanuatu, 3 April 2020 (TC20200403VUT): 31 features merged from 2 source layers. Layers whose names mark the area UNOSAT analysed, or parts of it with no usable imagery (analysis extent, area of interest, cloud obstruction, no-data, image footprint). The `source_layer` and `source_file` columns name the layer and file each row came from. The geometry is in EPSG:32758, the CRS of the source layers; the PMTiles copy is in Web Mercator.

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

- **Bounding Box**: [167.67643466205953, -16.506340189682273, 168.2608044083484, -15.298773195686456]

## Temporal Coverage

- **Start**: 2020-04-09T00:00:00Z
- **End**: 2020-04-29T23:59:59Z

## Schema

| Column | Type | Description |
|--------|------|-------------|
| OBJECTID | int64 |  |
| SHAPE_Length | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| SHAPE_Area | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| geometry | binary | Feature geometry, as UNOSAT published it (not repaired). |
| source_layer | string | Name of the layer in the source file that this row came from. |
| source_file | string | Name of the file downloaded from HDX that this row came from. |
| SHAPE_Leng | double | Computed by ArcGIS in the units of the source layer's CRS (degrees for EPSG:4326), so it is not a metric measure. |
| bbox | struct<xmin: double, ymin: double, xmax: double, ymax: double> | Bounding box of the geometry (xmin, ymin, xmax, ymax), added for spatial filtering. |

## Files

| File | Size | Checksum |
|------|------|----------|
| ./tc20200403vut-analysis-extent-epsg_32758.parquet | 60.0 KB | 122067f058c0... |
| ./tc20200403vut-analysis-extent-epsg_32758.pmtiles | 65.2 KB | 122074bb0255... |
| ./styles/default.json | 682 B | 122086f6c901... |

## Quick Start

```python
import geopandas as gpd

gdf = gpd.read_parquet("./tc20200403vut-analysis-extent-epsg_32758.parquet")
print(gdf.head())
```

## STAC Metadata

- **root**: `../../../../catalog.json`
- **parent**: `../catalog.json`

## Source

[https://data.humdata.org/dataset/buildings-damage-assessment-related-density-in-south-of-sanma-province-vanuatu](https://data.humdata.org/dataset/buildings-damage-assessment-related-density-in-south-of-sanma-province-vanuatu)

## Processing Notes

Downloaded from HDX on 2026-11-22 and converted with GDAL ogr2ogr (to GeoPackage, multi-part geometry types, OGR_ORGANIZE_POLYGONS=CCW_INNER_JUST_AFTER_CW_OUTER) and geoparquet-io (GeoParquet 2.0, no geometry repair, bbox column added). Geometry is kept as published; no feature was repaired, dropped, or reprojected. Each layer's row count was checked against the source feature count. Layers merged with DuckDB `UNION ALL BY NAME`: a column a layer lacks is null for its rows. Coded geodatabase domains are decoded into `<field>_label` columns, per source file. Source layers: `CloudObstruction_AOI11_Oba`, `CloudObstruction_AOI13_Paama`.

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

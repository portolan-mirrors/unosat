#!/usr/bin/env python3
"""Write styles/default.json for the two combined collections.

The match values are the class labels measured in the combined files (a
DuckDB GROUP BY on damage_class and water_class). Labels are not normalized
upstream, so spelling variants share one colour.

    python3 tools/combined_styles.py
"""

import json
from pathlib import Path

C = Path(__file__).resolve().parent.parent / "catalog" / "combined"

DAMAGE = ["match", ["to-string", ["get", "damage_class"]],
          ["Destroyed", "Completely Destroyed"], "#7f0000",
          ["Severe Damage", "Severely damaged", "Highly Damaged"], "#d7301f",
          ["Moderate Damage", "Moderately damaged"], "#fc8d59",
          ["Damage", "Damaged"], "#ef6548",
          ["Possible damage", "Possible Damage", "Possibly damaged"], "#fdcc8a",
          ["No Visible Damage", "No visible damage"], "#969696",
          "Hotspot", "#7570b3",
          "#bdbdbd"]
WATER = ["match", ["to-string", ["get", "water_class"]],
         "Flood Water", "#08519c",
         "Satellite Detected Water", "#3182bd",
         "Possible Saturated, wet Soil/ possible Flood Water", "#6baed6",
         "Satellite Detected Water / Possible Saturated Soil", "#9ecae1",
         "Maximum Satellite Observed Water (Cumulative)", "#2171b5",
         "Preflood Water", "#c6dbef",
         "Flood-Affected Land / Possible Flood water", "#4292c6",
         "Archive Water Extent / Pre-Flood Water", "#deebf7",
         "#bdbdbd"]


def write(name, doc):
    d = C / name / "styles"
    d.mkdir(parents=True, exist_ok=True)
    (d / "default.json").write_text(json.dumps(doc, indent=2) + "\n")


def main():
    write("damage-sites", {
        "version": 8, "name": "Damage sites by damage class",
        "sources": {"data": {"type": "vector", "url": "pmtiles://../damage-sites.pmtiles"}},
        "layers": [{"source": "data", "source-layer": "damage-sites", "id": "damage-sites-points", "type": "circle",
                    "paint": {"circle-color": DAMAGE,
                              "circle-radius": ["interpolate", ["linear"], ["zoom"], 4, 1.5, 12, 3, 16, 6],
                              "circle-stroke-color": "#ffffff", "circle-stroke-width": 0.3}}]})
    write("water-extent", {
        "version": 8, "name": "Water extent by water class",
        "sources": {"data": {"type": "vector", "url": "pmtiles://../water-extent.pmtiles"}},
        "layers": [{"source": "data", "source-layer": "water-extent", "id": "water-extent-fill", "type": "fill",
                    "paint": {"fill-color": WATER, "fill-opacity": 0.7}},
                   {"source": "data", "source-layer": "water-extent", "id": "water-extent-outline", "type": "line",
                    "paint": {"line-color": "#333333", "line-width": 0.5, "line-opacity": 0.6}}]})
    print("combined styles written")


if __name__ == "__main__":
    main()

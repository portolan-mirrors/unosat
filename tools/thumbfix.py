"""Draw thumbnails for collections portolan could not render: a DuckDB
simplification of the geometry, plotted with matplotlib, then registered with
portolan's own writer."""
import json, subprocess, sys
from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from shapely import wkb
from portolan_cli.collection_thumbnail import register_collection_thumbnail
CAT = Path("/home/ubuntu/unosat/unosat/catalog")
for rel in sys.argv[1:]:
    c = CAT / rel; name = c.name
    pq = c / f"{name}.parquet"
    out = Path("/home/ubuntu/unosat/work/thumbfix") / f"{name}.wkb"
    # Simplify to about 1/500 of the bbox; drop slivers. Hex WKB rows.
    sql = f"""INSTALL spatial; LOAD spatial;
COPY (WITH b AS (SELECT max(bbox.xmax)-min(bbox.xmin) AS w FROM read_parquet('{pq}'))
SELECT hex(ST_AsWKB(ST_Simplify(geometry, (SELECT w FROM b)/500))) AS g
FROM read_parquet('{pq}') WHERE geometry IS NOT NULL) TO '{out}' (FORMAT csv, HEADER false);"""
    if pq.stat().st_size > 5e9:
        # Too many polygons to draw: one dot per row at its bbox centre.
        sql = f"""COPY (SELECT round((bbox.xmin+bbox.xmax)/2, 2) AS x, round((bbox.ymin+bbox.ymax)/2, 2) AS y
FROM read_parquet('{pq}') WHERE bbox.xmin IS NOT NULL GROUP BY ALL) TO '{out}' (FORMAT csv, HEADER false);"""
        subprocess.run(["duckdb", "-no-agent"], input=sql, text=True, check=True)
        xs, ys = zip(*[map(float, l.split(",")) for l in open(out) if l.strip()])
        fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
        fig.patch.set_facecolor("#f2efe9"); ax.set_facecolor("#f2efe9")
        ax.scatter(xs, ys, s=0.3, c="#3182bd", lw=0)
        ax.set_xlim(-180, 180); ax.set_ylim(-60, 75)
        ax.set_aspect("equal"); ax.axis("off"); fig.tight_layout(pad=0.2)
        img = c / f"{name}.thumb.jpg"
        fig.savefig(img, format="jpg", facecolor=fig.get_facecolor()); plt.close(fig); out.unlink()
        print(rel, register_collection_thumbnail(c, img), flush=True)
        continue
    subprocess.run(["duckdb", "-no-agent"], input=sql, text=True, check=True)
    fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
    fig.patch.set_facecolor("#f2efe9"); ax.set_facecolor("#f2efe9")
    color = "#3182bd" if "water" in name else "#d95f02"
    for line in open(out):
        line = line.strip()
        if not line: continue
        g = wkb.loads(bytes.fromhex(line))
        if g.is_empty: continue
        for p in getattr(g, "geoms", [g]):
            if p.geom_type == "Polygon":
                x, y = p.exterior.xy; ax.fill(x, y, color=color, lw=0)
            elif p.geom_type in ("LineString", "LinearRing"):
                x, y = p.xy; ax.plot(x, y, color=color, lw=0.5)
            elif p.geom_type == "Point":
                ax.plot(p.x, p.y, ".", color=color, ms=1)
    ax.set_aspect("equal"); ax.axis("off"); fig.tight_layout(pad=0.2)
    img = c / f"{name}.thumb.jpg"
    fig.savefig(img, format="jpg", facecolor=fig.get_facecolor()); plt.close(fig); out.unlink()
    print(rel, register_collection_thumbnail(c, img), flush=True)

"""Thumbnail for combined/water-extent (no PMTiles): feature centres over the
Esri World Light Gray basemap at zoom 2, in Web Mercator, framed 3:2."""
import math, sys
from PIL import Image, ImageDraw
T = "/home/ubuntu/unosat/work/thumbs/esri"
base = Image.new("RGB", (1024, 1024))
for y in range(4):
    for x in range(4):
        base.paste(Image.open(f"{T}/z2_{y}_{x}.png").convert("RGB"), (x * 256, y * 256))
d = ImageDraw.Draw(base, "RGBA")
def px(lon, lat):
    lat = max(min(lat, 85), -85)
    return ((lon + 180) / 360 * 1024, (1 - math.log(math.tan(math.radians(lat)) + 1 / math.cos(math.radians(lat))) / math.pi) / 2 * 1024)
for line in open(sys.argv[1]):
    x, y, n = line.split(","); X, Y = px(float(x), float(y))
    d.ellipse([X - 1.2, Y - 1.2, X + 1.2, Y + 1.2], fill=(8, 81, 156, 200))
# 3:2 crop between about 60S and 72N
top, bot = px(0, 72)[1], px(0, -58)[1]
h = bot - top; w = h * 1.5
img = base.crop((0, int(top), 1024, int(bot))) if w > 1024 else base.crop((int(512 - w / 2), int(top), int(512 + w / 2), int(bot)))
img = img.resize((1024, round(1024 / img.width * img.height)))
img.save(sys.argv[2], quality=85); print(img.size)

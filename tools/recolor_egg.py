"""Recolour the egg in a photo to a filament colour, keeping its shading.
Usage: recolor.py <photo> <colors.json> <out dir> [names...]"""
import sys, json, os, colorsys
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

src, colors_path, out_dir = sys.argv[1:4]
SATURATION = 0.85
VALUE = 0.88
wanted = set(sys.argv[4:])
img = Image.open(src).convert("RGB")
rgb = np.asarray(img).astype(np.float32) / 255
hsv = np.asarray(img.convert("HSV")).astype(np.float32)
hue = hsv[..., 0] * 360 / 255

# egg = blue hues; background/shadow are orange (24-40°)
mask = (hue > 185) & (hue < 265) & (hsv[..., 1] > 25)
mask = ndimage.binary_opening(mask, iterations=3)
labels, n = ndimage.label(mask)
largest = 1 + np.argmax(ndimage.sum(mask, labels, range(1, n + 1)))
mask = ndimage.binary_fill_holes(labels == largest)
mask = ndimage.binary_closing(mask, iterations=6)
soft = np.asarray(Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(2))).astype(np.float32)[..., None] / 255
Image.fromarray((mask * 255).astype(np.uint8)).save(os.path.join(out_dir, "_mask.png"))

lum = 0.299 * rgb[..., 0] + 0.587 * rgb[..., 1] + 0.114 * rgb[..., 2]
ref = np.median(lum[mask])
shade = (lum / ref)[..., None]
highlight = np.clip(shade - 1.05, 0, None)

for c in json.load(open(colors_path)):
    name = c["value"].split(" (")[0]
    if wanted and name not in wanted:
        continue
    target = np.array([int(c["hex"][i:i + 2], 16) for i in (1, 3, 5)], np.float32) / 255
    # Bambu's swatches are more vivid than the filament looks on camera (the real
    # Cyan egg photographs at 70% saturation / 56% brightness vs 100% / 84% for its
    # swatch). Full calibration dulled warm colours, so the owner picked a middle
    # setting: 85% saturation, 88% brightness.
    h, s, v = colorsys.rgb_to_hsv(*target)
    target = np.array(colorsys.hsv_to_rgb(h, s * SATURATION, v * VALUE), np.float32)
    col = np.clip(target * shade + highlight * 0.6, 0, 1)
    out = rgb * (1 - soft) + col * soft
    fn = os.path.join(out_dir, name.lower().replace(" ", "-") + ".jpg")
    Image.fromarray((out * 255).astype(np.uint8)).save(fn, "JPEG", quality=86, optimize=True, progressive=True)
    print("✓", name)

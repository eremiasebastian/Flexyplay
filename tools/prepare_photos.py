"""Brighten and add contrast per photo, based on its own measurements.
Usage: enhance.py <originals root> <out root>"""
import sys, os, math
from PIL import Image, ImageOps, ImageStat, ImageEnhance
src_root, out_root = sys.argv[1], sys.argv[2]
TARGET_MEAN, MIN_STD = 180.0, 45.0

def stats(im):
    st = ImageStat.Stat(im.convert("L")); return st.mean[0], st.stddev[0]

for group in sorted(os.listdir(src_root)):
    gdir = os.path.join(src_root, group)
    inner = [d for d in os.listdir(gdir) if os.path.isdir(os.path.join(gdir, d))][0]
    os.makedirs(os.path.join(out_root, group), exist_ok=True)
    for f in sorted(os.listdir(os.path.join(gdir, inner)), key=lambda x: int(x.split('.')[0])):
        im = ImageOps.exif_transpose(Image.open(os.path.join(gdir, inner, f))).convert("RGB")
        im.thumbnail((2048, 2048), Image.LANCZOS)
        m0, s0 = stats(im)
        # Work on brightness only (Y of YCbCr) so the filament colours stay true.
        y, cb, cr = im.convert("YCbCr").split()
        y = ImageOps.autocontrast(y, cutoff=0.3)
        s = ImageStat.Stat(y).stddev[0]
        if s < MIN_STD:
            y = ImageEnhance.Contrast(y).enhance(min(1.15, 1 + (MIN_STD - s) / 120))
        m = ImageStat.Stat(y).mean[0]
        if m < TARGET_MEAN - 3:
            g = max(0.8, math.log(TARGET_MEAN / 255) / math.log(m / 255))
            y = y.point([round(255 * (i / 255) ** g) for i in range(256)])
        im = Image.merge("YCbCr", (y, cb, cr)).convert("RGB")
        m1, s1 = stats(im)
        im.save(os.path.join(out_root, group, f), "JPEG", quality=86, optimize=True, progressive=True)
        print(f"{group:15} {f}: luminozitate {m0:5.1f} -> {m1:5.1f} | contrast {s0:4.1f} -> {s1:4.1f}")

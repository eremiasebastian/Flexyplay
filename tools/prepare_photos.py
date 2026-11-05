"""Resize product photos to 2048px, lift brightness/contrast on the luminance
channel, then boost colour (the owner picked the strong setting: 1.32 saturation,
target mean 170). Usage: prepare_photos.py <originals root> <out root> 1.32 170"""
import sys, os, math
from PIL import Image, ImageOps, ImageStat, ImageEnhance
src_root, out_root, SAT, TARGET_MEAN = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
MIN_STD = 48.0
for group in sorted(os.listdir(src_root)):
    gdir = os.path.join(src_root, group)
    inner = [d for d in os.listdir(gdir) if os.path.isdir(os.path.join(gdir, d))][0]
    os.makedirs(os.path.join(out_root, group), exist_ok=True)
    for f in sorted(os.listdir(os.path.join(gdir, inner)), key=lambda x: int(x.split('.')[0])):
        im = ImageOps.exif_transpose(Image.open(os.path.join(gdir, inner, f))).convert("RGB")
        im.thumbnail((2048, 2048), Image.LANCZOS)
        y, cb, cr = im.convert("YCbCr").split()
        y = ImageOps.autocontrast(y, cutoff=0.5)
        s = ImageStat.Stat(y).stddev[0]
        if s < MIN_STD:
            y = ImageEnhance.Contrast(y).enhance(min(1.2, 1 + (MIN_STD - s) / 100))
        m = ImageStat.Stat(y).mean[0]
        if m < TARGET_MEAN - 3:
            g = max(0.85, math.log(TARGET_MEAN / 255) / math.log(m / 255))
            y = y.point([round(255 * (i / 255) ** g) for i in range(256)])
        im = Image.merge("YCbCr", (y, cb, cr)).convert("RGB")
        im = ImageEnhance.Color(im).enhance(SAT)
        im.save(os.path.join(out_root, group, f), "JPEG", quality=86, optimize=True, progressive=True)

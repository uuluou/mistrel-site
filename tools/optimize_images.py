#!/usr/bin/env python3
"""Generate lightweight WebP variants (+ compressed hero video) into public/assets/opt/.
Originals are never modified. The server prefers opt/ variants automatically."""
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "public", "assets")
DST = os.path.join(SRC, "opt")
os.makedirs(DST, exist_ok=True)

MAX_W = 1000
count, saved = 0, 0
for fn in sorted(os.listdir(SRC)):
    p = os.path.join(SRC, fn)
    if not os.path.isfile(p):
        continue
    ext = os.path.splitext(fn)[1].lower()
    if ext not in (".png", ".jpg", ".jpeg"):
        continue
    base = os.path.splitext(fn)[0]
    out = os.path.join(DST, base + ".webp")
    if os.path.exists(out):
        continue
    im = Image.open(p)
    has_alpha = im.mode in ("RGBA", "LA") or "transparency" in im.info
    if not has_alpha:
        im = im.convert("RGB")
    if im.width > MAX_W:
        im = im.resize((MAX_W, int(im.height * MAX_W / im.width)), Image.LANCZOS)
    before = os.path.getsize(p)
    im.save(out, "WEBP", quality=75, method=6)
    after = os.path.getsize(out)
    saved += before - after
    count += 1
    print(f"{fn}: {before/1048576:.1f}MB -> {after/1024:.0f}KB")
print(f"\n{count} images, saved {saved/1048576:.1f}MB")

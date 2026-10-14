#!/usr/bin/env python3
"""Build responsive WebP derivatives (480/960/1600 wide) for every post image.

Reads `image:` from each post's front matter, writes NAME-480w.webp etc. beside the
original. Idempotent (skips up-to-date files), never touches the originals, and the
outputs are gitignored: CI regenerates them on every build. Needs `cwebp` (brew install
webp / apt-get install webp).
"""
import glob, os, re, struct, subprocess, sys

WIDTHS = (480, 960, 1600)

def dims(path):
    with open(path, "rb") as f:
        head = f.read(26)
        if head[:8] == b"\x89PNG\r\n\x1a\n":
            return struct.unpack(">II", head[16:24])
        f.seek(2)
        while True:
            marker = f.read(2)
            if len(marker) < 2 or marker[0] != 0xFF:
                return None
            if marker[1] in (0xC0, 0xC1, 0xC2):
                f.read(3)
                h, w = struct.unpack(">HH", f.read(4))
                return w, h
            size = struct.unpack(">H", f.read(2))[0]
            f.seek(size - 2, 1)

def images():
    seen = set()
    for post in sorted(glob.glob("_posts/*.md")):
        text = open(post, encoding="utf-8").read().split("---", 2)
        m = re.search(r"^image:\s*(\S+)\s*$", text[1], re.M) if len(text) > 2 else None
        if m and m.group(1).startswith("/assets/") and m.group(1) not in seen:
            seen.add(m.group(1))
            yield m.group(1).lstrip("/")

made = skipped = missing = 0
for src in images():
    if not os.path.exists(src):
        missing += 1
        continue
    d = dims(src)
    base = os.path.splitext(src)[0]
    for w in WIDTHS:
        out = f"{base}-{w}w.webp"
        if os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(src):
            skipped += 1
            continue
        args = ["cwebp", "-quiet", "-q", "82", "-m", "5"]
        if d and d[0] > w:
            args += ["-resize", str(w), "0"]
        subprocess.run(args + [src, "-o", out], check=True)
        made += 1
print(f"derive-images: {made} made, {skipped} up to date, {missing} missing sources")

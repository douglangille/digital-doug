#!/usr/bin/env python3
"""Post-build sanity checks for a built Jekyll site (_site/). Shared by digital-doug and darkling-whim.

Hard failures (exit 1, blocks the deploy): leftover Liquid, a missing asset a page asks for, a
malformed or non-absolute feed, a bad sitemap, or a colour pair in the compiled CSS under WCAG AA.
Warnings (printed, exit 0): internal links that don't resolve (old posts carry legacy links), a page
without exactly one <h1>/<title>/description, an <img> with no alt attribute.

Usage: python3 scripts/check-build.py [_site]
"""
import glob, os, re, sys, urllib.parse
import xml.etree.ElementTree as ET

SITE = sys.argv[1] if len(sys.argv) > 1 else "_site"
errors, warnings = [], []

def err(m): errors.append(m)
def warn(m): warnings.append(m)

pages = sorted(glob.glob(f"{SITE}/**/*.html", recursive=True))
STANDALONE = ("hub/", "404.html", "rss/", "search/")  # own markup or redirect stubs

def resolve(url, page):
    u = urllib.parse.unquote(url.split("#")[0].split("?")[0])
    if not u:
        return True
    if u.startswith("/"):
        p = SITE + u
    else:
        p = os.path.join(os.path.dirname(page), u)
    return os.path.exists(p) or os.path.exists(os.path.join(p, "index.html")) or os.path.exists(p + ".html")

for page in pages:
    rel = page[len(SITE) + 1:]
    h = open(page, encoding="utf-8").read()
    if rel.startswith("hub/"):
        continue  # standalone page with its own markup
    if re.search(r"\{\{|\{%", re.sub(r"<(script|pre|code)\b.*?</\1>", "", h, flags=re.S)):
        err(f"{rel}: leftover Liquid")
    for m in re.finditer(r'(?:src|srcset|href)="([^"]+)"', h):
        for part in (m.group(1).split(",") if m.group(0).startswith("srcset") else [m.group(1)]):
            u = part.strip().split(" ")[0]
            if not u or u.startswith(("http:", "https:", "mailto:", "tel:", "data:", "#", "//")):
                continue
            if u.startswith("/assets/"):
                if not resolve(u, page):
                    err(f"{rel}: missing asset {u}")
            elif not resolve(u, page):
                warn(f"{rel}: link does not resolve {u}")
    if any(s in rel for s in STANDALONE) and "hub" in rel:
        continue
    if rel.startswith(("rss", "search", "tag/")):
        continue
    if h.count("<h1") != 1 and rel != "404.html":
        warn(f"{rel}: {h.count('<h1')} <h1> elements")
    if len(re.findall(r"<title>", h)) != 1:
        warn(f"{rel}: <title> count {len(re.findall('<title>', h))}")
    if not re.search(r'<meta name="description" content="[^"]+"', h):
        warn(f"{rel}: no meta description")
    for img in re.findall(r"<img\b[^>]*>", h):
        if " alt=" not in img:
            warn(f"{rel}: <img> without alt: {img[:80]}")

# feeds
for feed in ("feed.xml", "substack.xml"):
    path = f"{SITE}/{feed}"
    if not os.path.exists(path):
        err(f"{feed} missing")
        continue
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as e:
        err(f"{feed}: not well-formed: {e}")
        continue
    items = root.findall(".//item")
    if not items:
        err(f"{feed}: no items")
    raw = open(path, encoding="utf-8").read()
    if re.search(r'(?:src|href)="/(?!/)', raw):
        err(f"{feed}: root-relative URL in content")
    if feed == "feed.xml" and not all((i.findtext("link") or "").startswith("https://") for i in items):
        err("feed.xml: non-absolute item link")

# sitemap
sm = f"{SITE}/sitemap.xml"
if os.path.exists(sm):
    locs = re.findall(r"<loc>([^<]+)</loc>", open(sm, encoding="utf-8").read())
    if any("/assets/" in l for l in locs):
        err("sitemap lists assets")
    if len(locs) < 5:
        err(f"sitemap only has {len(locs)} urls")
else:
    err("sitemap.xml missing")

# contrast of compiled tokens
def lum(h):
    h = h.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]

def ratio(a, b):
    x, y = sorted([lum(a), lum(b)], reverse=True)
    return (x + .05) / (y + .05)

css = open(f"{SITE}/assets/css/main.css", encoding="utf-8").read()
def tokens(block):
    return dict(re.findall(r"--([\w-]+):\s*(#[0-9a-fA-F]{6})", block))
light = tokens(re.search(r":root\{color-scheme:light;(.*?)\}", css, re.S).group(1))
dark = tokens(re.search(r"prefers-color-scheme:\s*dark\)\{:root\{color-scheme:dark;(.*?)\}", css, re.S).group(1))
PAIRS = [("text", "bg", 4.5), ("text", "surface", 4.5), ("muted", "bg", 4.5), ("muted", "overlay", 4.5),
         ("muted", "surface", 4.5), ("accent", "bg", 4.5), ("accent", "overlay", 4.5), ("accent-hover", "bg", 4.5),
         ("accent-ink", "accent-fill", 4.5), ("accent-ink", "accent-hover", 4.5), ("visited", "bg", 4.5), ("universe", "bg", 4.5), ("bg", "universe", 4.5),
         ("syn-kw", "overlay", 4.5), ("syn-str", "overlay", 4.5), ("syn-fn", "overlay", 4.5),
         ("syn-num", "overlay", 4.5), ("syn-cm", "overlay", 4.5), ("syn-name", "overlay", 4.5)]
for name, t in (("light", light), ("dark", dark)):
    for fg, bg, need in PAIRS:
        if fg in t and bg in t and ratio(t[fg], t[bg]) < need:
            err(f"contrast {name}: {fg} on {bg} = {ratio(t[fg], t[bg]):.2f} (< {need})")

print(f"checked {len(pages)} pages, 2 feeds, sitemap, {len(PAIRS) * 2} colour pairs")
for w in warnings[:25]:
    print("warn:", w)
if len(warnings) > 25:
    print(f"warn: ... and {len(warnings) - 25} more")
for e in errors[:60]:
    print("ERROR:", e)
print(f"{len(errors)} error(s), {len(warnings)} warning(s)")
sys.exit(1 if errors else 0)

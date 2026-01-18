#!/usr/bin/env python3
"""
substack_to_jekyll.py

Convert a Substack export (posts.csv + per-post HTML files) into Jekyll _posts Markdown,
downloading images locally and moving the first image into front matter as the feature image.

Key behavior:
- Images are saved to an ABSOLUTE filesystem directory (e.g. /Users/.../Workbench/assets/images)
- Image URLs written into Markdown/front matter are ROOT-relative (e.g. /assets/images/...)
- First image becomes feature image (front matter) and is removed from body.

Dependencies:
  pip install beautifulsoup4 requests python-dateutil markdownify

Usage example:
  python3 substack_to_jekyll.py \
    --posts-csv "/path/to/substack-export/posts.csv" \
    --html-dir  "/path/to/substack-export/posts" \
    --out-posts "/Users/W0001680/Workbench/_digital-doug/_posts" \
    --assets-disk-dir "/Users/W0001680/Workbench/assets/images" \
    --assets-url-prefix "/assets/images" \
    --assets-subdir "substack" \
    --category "digital-doug"
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional
from urllib.parse import urlparse, urljoin

import requests
from bs4 import BeautifulSoup
from dateutil import parser as dateparser
from markdownify import markdownify as md


# ----------------------------
# Helpers
# ----------------------------

def slugify(text: str) -> str:
    text = (text or "").strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text).strip("-")
    return text or "post"


def yaml_quote(s: str) -> str:
    s = (s or "").replace("\\", "\\\\").replace('"', '\\"')
    return f'"{s}"'


def first_present(row: dict, keys) -> Optional[str]:
    for k in keys:
        if k in row and row[k] is not None and str(row[k]).strip() != "":
            return str(row[k]).strip()
    return None


def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def guess_ext_from_content_type(ct: str) -> str:
    ct = (ct or "").split(";")[0].strip().lower()
    return {
        "image/jpeg": ".jpg",
        "image/jpg": ".jpg",
        "image/png": ".png",
        "image/gif": ".gif",
        "image/webp": ".webp",
        "image/svg+xml": ".svg",
        "image/avif": ".avif",
    }.get(ct, "")


def normalize_url(src: str, base_url: Optional[str]) -> Optional[str]:
    src = (src or "").strip()
    if not src:
        return None
    if src.startswith("data:"):
        return None
    if src.startswith("//"):
        return "https:" + src
    if src.startswith("http://") or src.startswith("https://"):
        return src
    if src.startswith("/") and base_url:
        return urljoin(base_url.rstrip("/") + "/", src.lstrip("/"))
    return None


def index_html_files(html_dir: Path) -> Dict[str, Path]:
    idx: Dict[str, Path] = {}
    for p in html_dir.rglob("*.html"):
        idx[p.stem] = p
    return idx


def find_html_for_post(
    html_index: Dict[str, Path],
    html_dir: Path,
    slug: str,
    post_id: Optional[str],
    filename_hint: Optional[str],
) -> Optional[Path]:
    if filename_hint:
        p = Path(filename_hint)
        if not p.is_absolute():
            p = html_dir / p
        if p.exists():
            return p

    if slug and slug in html_index:
        return html_index[slug]

    if post_id:
        if post_id in html_index:
            return html_index[post_id]
        for stem, p in html_index.items():
            if post_id in stem:
                return p

    if slug:
        for stem, p in html_index.items():
            if slug in stem:
                return p

    return None


def download_image(url: str, dest_dir: Path, prefer_name: Optional[str] = None) -> Optional[Path]:
    try:
        r = requests.get(url, timeout=30, stream=True)
        r.raise_for_status()

        parsed = urlparse(url)
        basename = os.path.basename(parsed.path) or ""
        basename = re.sub(r"[^\w.\-]+", "_", basename)

        if prefer_name:
            basename = re.sub(r"[^\w.\-]+", "_", prefer_name)

        ext = Path(basename).suffix.lower()
        if not ext:
            ext = guess_ext_from_content_type(r.headers.get("Content-Type", "")) or ".img"

        if not Path(basename).stem:
            h = hashlib.sha1(url.encode("utf-8")).hexdigest()[:12]
            basename = f"img-{h}{ext}"
        else:
            basename = f"{Path(basename).stem}{ext}"

        ensure_dir(dest_dir)
        out_path = dest_dir / basename

        if out_path.exists():
            h = hashlib.sha1(url.encode("utf-8")).hexdigest()[:8]
            out_path = dest_dir / f"{out_path.stem}-{h}{out_path.suffix}"

        with open(out_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        return out_path
    except Exception as e:
        print(f"[warn] image download failed: {url} ({e})", file=sys.stderr)
        return None


def join_url(prefix: str, *parts: str) -> str:
    # root-relative URL builder
    p = prefix.strip()
    if not p.startswith("/"):
        p = "/" + p
    p = p.rstrip("/")
    rest = "/".join([x.strip("/").replace("\\", "/") for x in parts if x and x.strip("/")])
    return f"{p}/{rest}" if rest else p


# ----------------------------
# Core conversion
# ----------------------------

@dataclass
class PostMeta:
    title: str
    subtitle: Optional[str]
    dt: Optional[datetime]
    slug: str
    post_id: Optional[str]
    canonical_url: Optional[str]


def build_front_matter(meta: PostMeta, category: str, feature_site_path: Optional[str]) -> str:
    fm = ["---"]
    fm.append(f"title: {yaml_quote(meta.title)}")

    if feature_site_path:
        fm.append(f"image: {feature_site_path}")
        fm.append("header:")
        fm.append(f"  teaser: {feature_site_path}")
        fm.append(f"  overlay_image: {feature_site_path}")

    fm.append("categories:")
    fm.append(f"  - {category}")

    if meta.subtitle:
        fm.append(f"excerpt: {yaml_quote(meta.subtitle)}")

    # Optional traceability (comment out if you don't want them)
    if meta.canonical_url:
        fm.append(f"substack_url: {yaml_quote(meta.canonical_url)}")
    if meta.post_id:
        fm.append(f"substack_post_id: {yaml_quote(meta.post_id)}")

    fm.append("---\n")
    return "\n".join(fm)


def html_to_markdown(html_fragment: str) -> str:
    md_text = md(
        html_fragment,
        heading_style="ATX",
        bullets="-",
        strip=["script", "style"],
    )
    md_text = md_text.replace("\r\n", "\n")
    md_text = re.sub(r"\n{3,}", "\n\n", md_text).strip() + "\n"
    return md_text


def convert_one(
    meta: PostMeta,
    html_path: Path,
    out_posts_dir: Path,
    assets_disk_dir: Path,
    assets_url_prefix: str,
    assets_subdir: str,
    category: str,
    base_url: Optional[str],
) -> Optional[Path]:
    html_raw = html_path.read_text(encoding="utf-8", errors="replace")
    soup = BeautifulSoup(html_raw, "html.parser")

    root = soup.body if soup.body else soup

    # Where images are saved on disk:
    #   <assets_disk_dir>/<assets_subdir>/<slug>/
    # URLs written into posts:
    #   <assets_url_prefix>/<assets_subdir>/<slug>/<filename>
    disk_leaf = Path(assets_subdir) / meta.slug if assets_subdir else Path(meta.slug)
    images_dir = assets_disk_dir / disk_leaf

    for img in root.find_all("img"):
        src = (img.get("src") or "").strip()

        # Leave already-root-relative /assets/... alone
        if src.startswith("/assets/"):
            continue

        url = normalize_url(src, base_url=base_url)
        if url:
            downloaded = download_image(url, images_dir)
            if downloaded:
                site_path = join_url(assets_url_prefix, *(disk_leaf.parts), downloaded.name)
                img["src"] = site_path

        for attr in ["srcset", "sizes", "decoding", "loading"]:
            if attr in img.attrs:
                del img.attrs[attr]

    feature_site_path = None
    first_img = root.find("img")
    if first_img:
        src = (first_img.get("src") or "").strip()
        if src.startswith("/assets/"):
            feature_site_path = src
            first_img.decompose()

    md_body = html_to_markdown(root.decode_contents())

    if meta.dt:
        date_prefix = meta.dt.strftime("%Y-%m-%d")
    else:
        date_prefix = datetime.now().strftime("%Y-%m-%d")

    out_name = f"{date_prefix}-{meta.slug}.md"
    out_path = out_posts_dir / out_name

    fm = build_front_matter(meta=meta, category=category, feature_site_path=feature_site_path)
    out_text = fm + md_body

    ensure_dir(out_posts_dir)
    out_path.write_text(out_text, encoding="utf-8")
    return out_path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--posts-csv", required=True, help="Path to Substack posts.csv")
    ap.add_argument("--html-dir", required=True, help="Directory containing per-post HTML files")

    ap.add_argument("--out-posts", default="_posts", help="Output Jekyll _posts directory")

    # NEW: separate disk path vs URL prefix
    ap.add_argument(
        "--assets-disk-dir",
        default="assets/images",
        help="Filesystem directory to write images into (can be absolute).",
    )
    ap.add_argument(
        "--assets-url-prefix",
        default="/assets/images",
        help="URL prefix to write into Markdown/front matter (root-relative).",
    )
    ap.add_argument(
        "--assets-subdir",
        default="substack",
        help='Optional subdir under assets (e.g. "substack"). Use "" to disable.',
    )

    ap.add_argument("--category", default="digital-doug", help="Single category to apply to all imported posts")
    ap.add_argument("--base-url", default=None, help="Optional base URL to resolve relative image URLs (e.g. https://your.substack.com)")
    ap.add_argument("--limit", type=int, default=0, help="Optional limit of posts to process (0 = no limit)")
    args = ap.parse_args()

    posts_csv = Path(args.posts_csv)
    html_dir = Path(args.html_dir)
    out_posts_dir = Path(args.out_posts)

    assets_disk_dir = Path(args.assets_disk_dir).expanduser()
    assets_url_prefix = args.assets_url_prefix.strip() or "/assets/images"
    assets_subdir = (args.assets_subdir or "").strip().strip("/")

    if not posts_csv.exists():
        print(f"[error] posts.csv not found: {posts_csv}", file=sys.stderr)
        return 2
    if not html_dir.exists():
        print(f"[error] html dir not found: {html_dir}", file=sys.stderr)
        return 2

    ensure_dir(assets_disk_dir)

    html_index = index_html_files(html_dir)

    processed = 0
    skipped = 0

    with open(posts_csv, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            title_raw = first_present(row, ["title", "Title"])
            if not title_raw:
                skipped += 1
                continue

            subtitle = first_present(row, ["subtitle", "Subtitle", "sub_title", "Sub Title", "description", "Description"])
            slug = first_present(row, ["slug", "Slug", "post_slug", "Post Slug"]) or slugify(title_raw)

            post_id = first_present(row, ["post_id", "Post ID", "id", "ID"])
            canonical_url = first_present(row, ["canonical_url", "Canonical URL", "url", "URL"])

            dt_str = first_present(row, ["post_date", "Post Date", "published_at", "Published At", "publication_date", "Publication Date", "date", "Date"])
            dt = None
            if dt_str:
                try:
                    dt = dateparser.parse(dt_str)
                except Exception:
                    dt = None

            filename_hint = first_present(row, ["filename", "Filename", "file", "File", "html_file", "HTML File"])

            meta = PostMeta(
                title=title_raw,
                subtitle=subtitle,
                dt=dt,
                slug=slug,
                post_id=post_id,
                canonical_url=canonical_url,
            )

            html_path = find_html_for_post(html_index, html_dir, slug=slug, post_id=post_id, filename_hint=filename_hint)
            if not html_path:
                print(f"[warn] no HTML found for slug={slug!r} post_id={post_id!r} title={title_raw!r}", file=sys.stderr)
                skipped += 1
                continue

            out_path = convert_one(
                meta=meta,
                html_path=html_path,
                out_posts_dir=out_posts_dir,
                assets_disk_dir=assets_disk_dir,
                assets_url_prefix=assets_url_prefix,
                assets_subdir=assets_subdir,
                category=args.category,
                base_url=args.base_url,
            )

            if out_path:
                processed += 1
                print(f"[ok] {out_path}")

            if args.limit and processed >= args.limit:
                break

    print(f"Done. processed={processed} skipped={skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

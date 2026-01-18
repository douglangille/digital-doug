# _digital-doug: Substack “break-glass” backup

This folder contains a **Substack export** and a repeatable conversion workflow that turns Substack HTML posts into Jekyll-ready Markdown posts (Minimal Mistakes-compatible), with local images and sane front matter.

The intent is to keep a full, portable archive that can be dropped into the main site if Substack ever becomes unusable.

## What’s in here

- `posts.csv` — Substack export metadata (titles, dates, ids, URLs, etc.).
- `posts/` — Substack per-post HTML files (the post bodies).
- `_posts/` — Output from the conversion script (Jekyll posts in Markdown).
- `substack_to_jekyll.py` — The converter script.

## Output conventions

The script produces Jekyll posts that:

- Use one category: `digital-doug` (no tags).
- Promote the first image in the post body to the post’s “feature image” and remove it from the body.
- Write feature image keys in Minimal Mistakes-style front matter (`image`, `header.teaser`, `header.overlay_image`).
- Download/relocate post images to a local assets folder and rewrite image URLs to site-root-relative paths like `/assets/images/...` (recommended for Jekyll sites).

## Prereqs

Create and activate a **local** virtual environment (not committed to git) and install dependencies:

```bash
cd /Users/W0001680/Workbench/_digital-doug
python3 -m venv .venv
source .venv/bin/activate

python -m pip install -U pip
python -m pip install beautifulsoup4 requests python-dateutil markdownify
```

### Note: urllib3 / LibreSSL warning

On some macOS Python builds that use LibreSSL, `urllib3 v2` may emit a warning and can be avoided by pinning urllib3 to the 1.26 line:

```bash
python -m pip install "urllib3==1.26.20"
```

## The command that worked

This is the exact successful invocation used for this backup:

```bash
source .venv/bin/activate

python substack_to_jekyll.py \
  --posts-csv "posts.csv" \
  --html-dir  "posts" \
  --out-posts "/Users/W0001680/Workbench/_digital-doug/_posts" \
  --assets-disk-dir "/Users/W0001680/Workbench/assets/images" \
  --assets-url-prefix "/assets/images" \
  --assets-subdir "" \
  --category "digital-doug"
```

### What those flags mean

- `--posts-csv` / `--html-dir`: point at the Substack export files.
- `--out-posts`: where to write the Jekyll-ready Markdown files.
- `--assets-disk-dir`: where images are written on disk (absolute path).
- `--assets-url-prefix`: what gets written into Markdown/front matter (root-relative URL prefix).
- `--assets-subdir ""`: no intermediate subfolder; images end up at:
  - Disk: `/Users/W0001680/Workbench/assets/images/<slug>/...`
  - URLs: `/assets/images/<slug>/...`

## Rerun workflow

1. Export your Substack archive.
2. Put `posts.csv` and the HTML `posts/` directory into this folder (or adjust flags accordingly).
3. Create/activate `.venv` locally and install deps.
4. Run the command above.
5. Review `_digital-doug/_posts/` for correctness.

## Notes / gotchas

- The first `<img>` in the HTML becomes the feature image; if Substack ever adds tracking/pixel images ahead of the real “hero”, the script may need a small heuristic tweak.
- `.venv/` is intentionally not part of this repo; it should be created locally as needed.

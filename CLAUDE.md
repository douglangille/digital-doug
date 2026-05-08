# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## About

Digital Doug is a Jekyll blog ([digital.douglangille.ca](https://digital.douglangille.ca)) using the [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) theme. Deployed automatically to GitHub Pages via GitHub Actions on push to `main`.

## Commands

```bash
bundle install          # Install dependencies (Ruby 3.1+ required)
bundle exec jekyll build   # Build the site to _site/
bundle exec jekyll serve   # Serve locally at http://localhost:4000
bundle exec jekyll serve --drafts  # Serve including _drafts/
```

## Architecture

**Content structure:**
- `_posts/` — Published articles, named `YYYY-MM-DD-title.md`
- `_drafts/` — Unpublished drafts (excluded from build by `_config.yml`)
- `_pages/` — Static pages (about, now, articles, 404, etc.)
- `assets/css/dark-mode.css` — Custom dark mode override for the Minimal Mistakes theme
- `_layouts/` — Custom layout overrides (`single.html`, `archive-taxonomy.html`)
- `_includes/` — Partial template overrides (`head/`, `related.html`, `navigation.yml`)
- `_data/navigation.yml` — Main nav links

**Configuration notes (`_config.yml`):**
- Categories are disabled; only tags are used for archives
- Tags auto-generate archive pages at `/:tag/` via `jekyll-archives` + `jekyll-paginate-v2`

## Post Front Matter

```yaml
---
title: "Post Title"
excerpt: "One-sentence teaser shown in listings."
tags: [tag1, tag2]
header:
  teaser: "/assets/images/post-slug/image.png"
  overlay_image: "/assets/images/post-slug/image.png"
---
```

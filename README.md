# Digital Doug

Website for digitaldoug.douglangille.ca

## About

This is a Jekyll site using the [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) theme, automatically built and deployed to GitHub Pages using GitHub Actions.

## Local Development

### Prerequisites

- Ruby 3.1 or higher
- Bundler

### Setup

1. Install dependencies:
   ```bash
   bundle install
   ```

2. Build the site:
   ```bash
   bundle exec jekyll build
   ```

3. Serve the site locally:
   ```bash
   bundle exec jekyll serve
   ```

4. Visit `http://localhost:4000` in your browser

## Deployment

The site is automatically deployed to GitHub Pages when changes are pushed to the `main` branch via the GitHub Actions workflow defined in `.github/workflows/jekyll.yml`.

## Adding Content

### Blog Posts

Create a new file in `_posts/` with the format `YYYY-MM-DD-title.md`:

```markdown
---
title: "Your Post Title"
date: YYYY-MM-DD
categories:
  - category
tags:
  - tag1
  - tag2
---

Your content here.
```

### Pages

Create a new file in `_pages/` with front matter:

```markdown
---
permalink: /page-name/
title: "Page Title"
---

Your content here.
```

## Configuration

Site configuration is managed in `_config.yml`. See the [Minimal Mistakes documentation](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) for all available options.

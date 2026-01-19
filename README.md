# Digital Doug

**Live Site**: [https://digital.douglangille.ca](https://digital.douglangille.ca)

## About

Digital Doug is Doug Langille's technology-focused blog exploring innovation, productivity, AI/LLMs, and higher education technology. This site was replatformed from Substack to Jekyll in January 2026 to gain more control over content, design, and integration with GitHub-based writing workflows.

**Tagline**: "Where Pixels Meet Purpose"

**Description**: Tech-related brain-droppings about innovation, productivity, and higher ed. You've been warned.

This Jekyll site uses the [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) theme and is deployed via GitHub Pages.

## Migration from Substack

This repository represents a platform migration from [douglangille.substack.com](https://douglangille.substack.com) to a self-hosted Jekyll site. The migration provides:

- Full content ownership and version control
- Integration with GitHub-based writing workflows
- Customizable design and features
- No platform lock-in
- RSS feed continuity

## Site Structure

- **Blog Posts** (`_posts/`): Tech articles, essays, and commentary
- **Pages** (`_pages/`): About, Now, and other static content
- **Assets** (`assets/`): Images, CSS, and media files

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
  - technology
tags:
  - AI
  - productivity
excerpt: "A compelling excerpt for the post."
---

Your content here.
```

### Pages

Create or edit files in `_pages/` with front matter:

```markdown
---
permalink: /page-name/
title: "Page Title"
---

Your content here.
```

## Configuration

Site configuration is managed in `_config.yml`. Key settings include:
- Site identity and metadata
- Author information and social links
- Theme customization
- Plugin configuration
- Pagination and archive settings

See the [Minimal Mistakes documentation](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) for all available options.

## Content Strategy

Digital Doug focuses on:
- AI and large language model developments
- Personal knowledge management
- Productivity workflows and tools
- Higher education technology
- IT management insights
- Digital transformation

## License

© 2019-2026 Doug Langille. Content rights reserved. Theme licensed under MIT.

# Digital Doug

**Live Site**: [https://digital.douglangille.ca](https://digital.douglangille.ca)

## About

Digital Doug is Doug Langille's technology-focused blog exploring AI integration, productivity systems, and higher education innovation. This site was replatformed from Substack to Jekyll in January 2026 for better content control and integration with GitHub-based workflows.

**Subtitle**: "Where pixels meet purpose"

**Description**: Tech-related brain-droppings about innovation, productivity, and higher ed. You've been warned.

This Jekyll site uses the [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) theme and is deployed via Netlify.

## Migration from Substack

This repository represents a platform migration from [douglangille.substack.com](https://douglangille.substack.com) completed in January 2026. The migration provides:

- Full content ownership and version control
- Integration with GitHub-based writing workflows
- Customizable design and features
- No platform lock-in
- RSS feed continuity

## Site Structure

- **Articles** (`_posts/`): Tech articles, essays, and commentary
- **About** (`_pages/about.md`): Site overview and author bio
- **Now** (`_pages/now.md`): Current projects and focus areas
- **Assets** (`assets/`): Images, CSS customizations, and media files

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

The site is automatically deployed to Netlify when changes are pushed to the `main` branch.

## Adding Content

### Blog Posts

Create a new file in `_posts/` with the format `YYYY-MM-DD-title.md`:

```markdown
---
title: "Your Post Title"
date: YYYY-MM-DD
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
- Tag-based archives (categories disabled)
- Pagination settings (12 posts per page)

See the [Minimal Mistakes documentation](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) for all available options.

## Content Focus

Digital Doug covers:
- AI and LLM integration in practice
- Personal knowledge management systems
- Productivity workflows (plaintext-first, markdown)
- Higher education technology implementation
- IT management and institutional change
- Digital craftsmanship philosophy

## License

© 2019-2026 Doug Langille. Content rights reserved. Theme licensed under MIT.

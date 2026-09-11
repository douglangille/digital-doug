---
permalink: /style-guide/
title: "Style Guide"
excerpt: "Internal reference: exercises every color token and mode-sensitive component on the site, for checking light/dark rendering."
author_profile: false
sitemap: false
search: false
share: false
comments: false
---

Internal reference page — not linked in nav. Exists to exercise every color token and hand-derived light/dark override in `main.scss` in one place, so both modes can be checked at a glance without hunting through posts. See `digital-doug/DESIGN.md` for the token table and the math behind each derived value.

## Typography

# Heading 1 — Libre Franklin 800
## Heading 2 — Libre Franklin 800
### Heading 3 — Libre Franklin 800

Body copy is Libre Baskerville, 1.125rem, 1.7 line-height. This paragraph exists to check that the serif body font, text color, and line spacing all read correctly against the background in both modes. It should feel warm and readable, not the flat gray of a system sans stack.

Here's a [default link](#), a [visited-style link](#) for comparison, and inline `code, styled as monospace`.

## Links (hover the ones below to check `--link-color-hover`)

- [Standard link](#) — uses `--link-color`
- **Bold link inside a sentence:** the quick brown fox jumps over the [lazy dog](#) here.

## Buttons

Exercises `.btn--primary` background, `--button-primary-hover-bg`, and `--button-primary-hover-text` — the button should stay legible (white text) in both modes, and the hover state should visibly darken/shift rather than disappear.

<a href="#" class="btn btn--primary">Primary button</a>
<a href="#" class="btn btn--success">Success button</a>
<a href="#" class="btn btn--warning">Warning button</a>
<a href="#" class="btn btn--danger">Danger button</a>
<a href="#" class="btn btn--info">Info button</a>
<a href="#" class="btn btn--inverse">Inverse button</a>

*(Success/warning/danger/info/inverse are fixed semantic colors, not mode-sensitive — included here only as a contrast check against the primary button, which is.)*

## Notices

`.notice--primary` is the one with hand-derived background/link/blockquote-border tokens (`--notice-primary-bg`, `--notice-primary-link`, `--notice-primary-blockquote-border`). The others are fixed semantic colors and shouldn't shift between modes — useful as a side-by-side sanity check.

{% capture notice-text %}
This is a **primary** notice. It should have a distinct background derived from `--primary-color`, a themed link color for [links like this one](#), and — if it contains a blockquote — a colored left border.

> A blockquote inside the notice, to check `--notice-primary-blockquote-border`.

Some `inline code` inside the notice, to check `--notice-primary-code-bg`.
{% endcapture %}
<div class="notice--primary">{{ notice-text | markdownify }}</div>

{% capture notice-info %}This is an **info** notice — fixed color, should look identical in light and dark.{% endcapture %}
<div class="notice--info">{{ notice-info | markdownify }}</div>

{% capture notice-warning %}This is a **warning** notice — fixed color, should look identical in light and dark.{% endcapture %}
<div class="notice--warning">{{ notice-warning | markdownify }}</div>

{% capture notice-success %}This is a **success** notice — fixed color, should look identical in light and dark.{% endcapture %}
<div class="notice--success">{{ notice-success | markdownify }}</div>

{% capture notice-danger %}This is a **danger** notice — fixed color, should look identical in light and dark.{% endcapture %}
<div class="notice--danger">{{ notice-danger | markdownify }}</div>

## Table (checks `--border-color-strong`)

| Column A | Column B | Column C |
|---|---|---|
| Row one | Some value | Another value |
| Row two | Some value | Another value |
| Row three | Some value | Another value |

## Form focus states (checks `--focus-shadow-text` / `--focus-shadow-primary`)

Click into each field below — the focus ring should be visible and appropriately subtle in both modes, not invisible against the background and not harsh.

<form>
  <div class="field">
    <label for="sg-text">Text input</label><br>
    <input type="text" id="sg-text" placeholder="Click to test focus ring">
  </div>
  <br>
  <div class="field">
    <label for="sg-textarea">Textarea</label><br>
    <textarea id="sg-textarea" placeholder="Click to test focus ring"></textarea>
  </div>
  <br>
  <div class="field">
    <label for="sg-select">Select</label><br>
    <select id="sg-select">
      <option>Option one</option>
      <option>Option two</option>
    </select>
  </div>
</form>

## Search toggle (checks `--search-toggle-hover`)

The magnifying glass icon in the site nav — hover it and confirm the icon color shifts rather than disappearing against the masthead background.

## Masthead / navigation

Check the site title, subtitle, nav links, and their hover states at the top of this page against `--masthead-link-color` / `--masthead-link-color-hover` / `--navicon-link-color-hover`.

## Code block

```python
def check_dark_mode(background_color, text_color):
    """Code blocks use --code-background-color and --code-background-color-dark."""
    contrast = calculate_contrast(background_color, text_color)
    return contrast >= 4.5  # WCAG AA minimum
```

## Muted text (checks `--muted-text-color`)

This sentence and the search-results excerpt styling both use the muted text token — it should read as a clearly de-emphasized gray relative to body text, in both modes, never low enough contrast to be hard to read.

---

**Checklist**: toggle your OS light/dark setting (or use browser devtools' rendered emulation) and confirm every section above holds up in both modes — particularly the primary button hover, the primary notice, table borders, and form focus rings, since those are the hand-derived tokens rather than direct variable substitutions. See `digital-doug/DESIGN.md` for the exact values each should resolve to.

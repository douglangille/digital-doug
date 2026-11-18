---
layout: default
permalink: /masthead/
title: "Masthead"
sitemap: false
robots: noindex
---
<style>
  /* One-off 1344x256 Substack masthead, text only. Screenshot the .mast element (the site header class is .masthead, so do not reuse it). Not linked from anywhere. */
  .skip, .masthead, .footer { display: none; }
  html, body { margin: 0; background: var(--bg); }
  main { padding: 0; }
  .mast { position: relative; width: 1344px; height: 256px; overflow: hidden; background: var(--bg); color: var(--text); display: flex; align-items: center; justify-content: center; }
  .mast__mark { margin: 0; text-align: center; font-family: var(--font-mark); font-weight: 400; font-size: 90px; line-height: 1; letter-spacing: 0; white-space: nowrap; color: var(--accent); }
</style>
<div class="mast" id="mast">
  <h1 class="mast__mark">{{ site.title }}</h1>
</div>

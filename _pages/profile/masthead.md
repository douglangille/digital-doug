---
layout: default
permalink: /masthead/
title: "Masthead"
sitemap: false
robots: noindex
---
<style>
  /* One-off 1344x256 Substack masthead, text only. Screenshot the .masthead element. Not linked from anywhere. */
  .skip, .masthead, .footer { display: none; }
  html, body { margin: 0; background: var(--bg); }
  main { padding: 0; }
  .masthead { position: relative; width: 1344px; height: 256px; overflow: hidden; background: var(--bg); color: var(--text); display: flex; align-items: center; justify-content: center; }
  .masthead__mark { margin: 0; text-align: center; font-family: var(--font-mark); font-weight: 400; font-size: 90px; line-height: 1; letter-spacing: 0; white-space: nowrap; color: var(--accent); }
</style>
<div class="masthead" id="masthead">
  <h1 class="masthead__mark">{{ site.title }}</h1>
</div>

---
layout: default
permalink: /square/
title: "Square"
sitemap: false
robots: noindex
---
<style>
  /* One-off 512x512 monogram. Screenshot the .square element. Not linked from anywhere. */
  .skip, .masthead, .footer { display: none; }
  html, body { margin: 0; background: var(--bg); }
  main { padding: 0; }
  .square { position: relative; width: 512px; height: 512px; overflow: hidden; background: var(--bg); color: var(--text); display: flex; align-items: center; justify-content: center; }
  .square__mark { margin: 0; text-align: center; font-family: var(--font-mark); font-weight: 400; font-size: 240px; line-height: 1; letter-spacing: 0; white-space: nowrap; color: var(--accent); }
</style>
<div class="square" id="square">
  <h1 class="square__mark">DD</h1>
</div>

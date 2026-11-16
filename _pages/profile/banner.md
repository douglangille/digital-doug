---
layout: default
permalink: /banner/
title: "Banner"
sitemap: false
robots: noindex
---
<style>
  /* One-off 1500x500 banner. Screenshot the .banner element. Not linked from anywhere. */
  .skip, .masthead, .footer { display: none; }
  html, body { margin: 0; background: var(--bg); }
  main { padding: 0; }
  .banner { position: relative; width: 1500px; height: 500px; overflow: hidden; background: var(--bg); color: var(--text); }
  .banner svg { position: absolute; inset: 0; width: 100%; height: 100%; }
  .banner__mark { position: absolute; left: 110px; top: 50%; transform: translateY(-50%); margin: 0; font-family: var(--font-mark); font-weight: 400; font-size: 96px; line-height: 1; letter-spacing: 0; white-space: nowrap; color: var(--accent); }
</style>
<div class="banner" id="banner">
  <svg viewBox="0 0 1500 500" aria-hidden="true" fill="none">
    <defs>
      <pattern id="grid" width="50" height="50" patternUnits="userSpaceOnUse">
        <path d="M50 0H0V50" stroke="var(--line)" stroke-width="1"/>
      </pattern>
    </defs>
    <rect width="1500" height="500" fill="url(#grid)" opacity=".55"/>
    <!-- frame -->
    <rect x="40" y="40" width="1420" height="420" stroke="var(--line)" stroke-width="2"/>
    <path d="M40 90V40H90 M1410 40H1460V90 M1460 410V460H1410 M90 460H40V410" stroke="var(--accent)" stroke-width="4"/>
    <!-- rule under the wordmark -->
    <path d="M116 392H1384" stroke="var(--accent)" stroke-width="3"/>
    <path d="M116 392H436" stroke="var(--accent)" stroke-width="3"/>
    <!-- cursor block -->
    <rect x="1330" y="150" width="60" height="200" fill="var(--accent)"/>
  </svg>
  <h1 class="banner__mark">{{ site.title }}</h1>
</div>

---
layout: default
title: Articles
permalink: /articles/
---
<div class="wrap">
  <header class="page-head">
    <h1>Articles</h1>
    <p>{{ site.posts.size }} posts, newest first.</p>
    <ul class="chips" aria-label="Browse by tag">
      {% assign alltags = site.tags | sort %}
      {% for tag in alltags %}<li><a class="chip" href="{{ tag[0] | slugify | prepend: '/tag/' | append: '/' | relative_url }}">{{ tag[0] }} <small>{{ tag[1].size }}</small></a></li>{% endfor %}
    </ul>
  </header>
  {% assign by_year = site.posts | group_by_exp: "p", "p.date | date: '%Y'" %}
  {% for y in by_year %}
  <h2 class="year">{{ y.name }}</h2>
  <ul class="rows">{% for post in y.items %}<li>{% include card.html post=post row=true %}</li>{% endfor %}</ul>
  {% endfor %}
</div>

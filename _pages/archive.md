---
layout: archive
title: Browse
permalink: /archive/
entries_layout: grid
search: false
classes: wide
author_profile: true
pagination:
    enabled: true
---


{% assign alltags = site.tags | sort %}
<ul class="taxonomy__index">
  {% for tag in alltags %}
    <li>
      <a href="{{ site.baseurl }}/{{ tag[0] | slugify }}/">
        <strong>{{ tag[0] }}</strong> <span class="taxonomy__count">{{ tag[1].size }}</span>
      </a>
    </li>
  {% endfor %}
</ul>

    <div class="entries-{{ page.entries_layout }}">
    {% for post in paginator.posts %}
      {% include archive-single.html type=page.entries_layout %}
    {% endfor %}
    </div>

    {% include paginator.html %}






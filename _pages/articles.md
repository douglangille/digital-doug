---
layout: default
title: Articles
permalink: /articles/
---
<div class="wrap">
  <header class="page-head">
    <h1>Articles</h1>
    <p id="count" role="status">{{ site.posts.size }} posts, newest first.</p>
    <input class="search-box" id="search" type="search" placeholder="Search titles, excerpts and tags" autocomplete="off" aria-label="Search articles">
    <div class="filters" role="group" aria-label="Filter by tag">
      <div class="filter"><ul class="chips"><li><a class="chip" data-all aria-current="true" href="{{ page.url | relative_url }}">all <small>{{ site.posts.size }}</small></a></li></ul></div>
      {% for g in site.tag_groups %}
      <div class="filter" data-group="{{ g.label }}">
        <ul class="chips">
          {% for t in g.tags %}{% assign n = site.tags[t].size %}{% if n > 0 %}<li><a class="chip" href="{{ t | slugify | prepend: '/tag/' | append: '/' | relative_url }}" data-tag="{{ t }}">{{ t }} <small>{{ n }}</small></a></li>{% endif %}{% endfor %}
        </ul>
      </div>
      {% endfor %}
    </div>
  </header>
  {% assign by_year = site.posts | group_by_exp: "p", "p.date | date: '%Y'" %}
  <div id="list">
  {% for y in by_year %}
  <section class="year-group">
    <h2 class="year">{{ y.name }}</h2>
    <ul class="rows">
      {% for post in y.items %}
      <li data-tags="{{ post.tags | join: ' ' | downcase }}" data-hay="{{ post.title | strip_html | downcase | escape }} {{ post.excerpt | strip_html | strip | normalize_whitespace | downcase | escape }}">{% include card.html post=post row=true %}</li>
      {% endfor %}
    </ul>
  </section>
  {% endfor %}
  </div>
  <p id="none" hidden>Nothing matches. Try fewer words, or clear a filter.</p>
</div>
<script>
(function () {
  var q = document.getElementById("search"), count = document.getElementById("count"), none = document.getElementById("none");
  var items = [].slice.call(document.querySelectorAll("#list li[data-tags]")), groups = [].slice.call(document.querySelectorAll(".year-group"));
  var chips = [].slice.call(document.querySelectorAll(".chip[data-tag], .chip[data-all]")), total = items.length;
  var current = null; // one tag at a time, like a tag browser
  function apply() {
    var terms = q.value.toLowerCase().split(/\s+/).filter(Boolean), shown = 0;
    items.forEach(function (li) {
      var ok = terms.every(function (t) { return (li.dataset.hay + " " + li.dataset.tags).indexOf(t) > -1; }) &&
        (!current || li.dataset.tags.split(" ").indexOf(current) > -1);
      li.hidden = !ok; if (ok) shown++;
    });
    groups.forEach(function (g) { g.hidden = !g.querySelector("li:not([hidden])"); });
    none.hidden = shown > 0;
    count.textContent = (terms.length || current) ? shown + " of " + total + " posts" : total + " posts, newest first.";
  }
  function select(tag) {
    current = (tag === current) ? null : tag;
    chips.forEach(function (c) { if (c.dataset.tag === current || (!current && c.hasAttribute("data-all"))) c.setAttribute("aria-current", "true"); else c.removeAttribute("aria-current"); });
    apply();
  }
  chips.forEach(function (c) {
    c.addEventListener("click", function (e) { e.preventDefault(); select(c.hasAttribute("data-all") ? null : c.dataset.tag); });
  });
  q.addEventListener("input", apply);
  var m = location.search.match(/[?&]q=([^&]*)/); if (m) { q.value = decodeURIComponent(m[1].replace(/\+/g, " ")); apply(); }
  if (location.hash === "#search") q.focus();
})();
</script>

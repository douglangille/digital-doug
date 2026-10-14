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
    <div class="filters">
      {% for g in site.tag_groups %}
      <div class="filter" data-group="{{ g.label }}">
        <span class="filter__label">{{ g.label }}</span>
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
  var chips = [].slice.call(document.querySelectorAll(".chip[data-tag]")), total = items.length;
  var active = {}; // group -> [tags]
  function groupOf(chip) { return chip.closest(".filter").dataset.group; }
  function apply() {
    var terms = q.value.toLowerCase().split(/\s+/).filter(Boolean), shown = 0;
    items.forEach(function (li) {
      var tags = li.dataset.tags.split(" ");
      var ok = terms.every(function (t) { return (li.dataset.hay + " " + li.dataset.tags).indexOf(t) > -1; }) &&
        Object.keys(active).every(function (g) { return !active[g].length || active[g].some(function (t) { return tags.indexOf(t) > -1; }); });
      li.hidden = !ok; if (ok) shown++;
    });
    groups.forEach(function (g) { g.hidden = !g.querySelector("li:not([hidden])"); });
    none.hidden = shown > 0;
    var filtered = terms.length || Object.keys(active).some(function (g) { return active[g].length; });
    count.textContent = filtered ? shown + " of " + total + " posts" : total + " posts, newest first.";
  }
  chips.forEach(function (c) {
    c.addEventListener("click", function (e) {
      e.preventDefault();
      var g = groupOf(c), t = c.dataset.tag; active[g] = active[g] || [];
      var i = active[g].indexOf(t); if (i > -1) active[g].splice(i, 1); else active[g].push(t);
      c.setAttribute("aria-current", i > -1 ? "false" : "true"); if (i > -1) c.removeAttribute("aria-current");
      apply();
    });
  });
  q.addEventListener("input", apply);
  var m = location.search.match(/[?&]q=([^&]*)/); if (m) { q.value = decodeURIComponent(m[1].replace(/\+/g, " ")); apply(); }
  if (location.hash === "#search") q.focus();
})();
</script>

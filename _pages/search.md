---
layout: default
title: Search
permalink: /search/
sitemap: false
---
<div class="wrap">
  <header class="page-head">
    <h1>Search</h1>
    <input class="search-box" id="q" type="search" placeholder="Search titles, excerpts and tags" autocomplete="off" autofocus aria-label="Search articles">
    <p id="count" role="status"></p>
  </header>
  <ul class="rows" id="results"></ul>
</div>
<script>
(function () {
  var q = document.getElementById("q"), out = document.getElementById("results"), count = document.getElementById("count"), data = [];
  function esc(s) { return s.replace(/[&<>"]/g, function (c) { return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]; }); }
  function render(list) {
    count.textContent = q.value ? list.length + " result" + (list.length === 1 ? "" : "s") : "";
    out.innerHTML = list.slice(0, 60).map(function (p) {
      return '<li><article class="card row"><a class="card__img" href="' + p.url + '" tabindex="-1" aria-hidden="true">' + (p.image ? '<img src="' + p.image + '" alt="" loading="lazy">' : "") + '</a><h3 class="card__title"><a href="' + p.url + '">' + esc(p.title) + '</a></h3><p class="meta">' + esc(p.date) + '</p><p class="card__ex">' + esc(p.excerpt) + '</p></article></li>';
    }).join("");
  }
  function run() {
    var terms = q.value.toLowerCase().split(/\s+/).filter(Boolean);
    if (!terms.length) return render([]);
    render(data.filter(function (p) { return terms.every(function (t) { return p.hay.indexOf(t) > -1; }); }));
  }
  fetch("{{ '/search.json' | relative_url }}").then(function (r) { return r.json(); }).then(function (d) {
    data = d.map(function (p) { p.hay = (p.title + " " + p.excerpt + " " + p.tags).toLowerCase(); return p; });
    var m = location.search.match(/[?&]q=([^&]*)/); if (m) q.value = decodeURIComponent(m[1].replace(/\+/g, " "));
    run();
  });
  q.addEventListener("input", run);
})();
</script>

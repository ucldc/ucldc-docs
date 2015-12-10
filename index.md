---
layout: default
title: Get Answers.
---

<header class="homepage__banner">
  <h1 class="homepage__header">Get Answers.</h1>
</header>

<div class="container-fluid">
  <h2 class="homepage__header">
    Select a user guide:
  </h2>
  <div class="row">
    {% for collection in site.collections %}
    {% assign collection-data-tuple = site.data.sidebars | where:"collection",collection[1].label %}
    {% assign collection-data = collection-data-tuple[0] %}

    <a href="{{ site.url }}{{ site.baseurl }}{{ collection-data.index }}" class="homepage__guide-link">
      <div class="col-md-4" style="margin: 15px 0;">
        <img src="{{ collection[1].icon-url }}" class="homepage__icon {{ collection[1].label }}"/>
        <h3 class="homepage__header">{{ collection-data.display-title }}</h3>
        {{ collection-data.description }}<br>
      </div>
    </a>
    {% endfor %}
  </div>
</div>

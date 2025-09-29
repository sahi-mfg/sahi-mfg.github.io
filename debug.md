---
layout: default
title: Debug Categories
permalink: /debug/
---

# Debug des catégories

## Toutes les catégories disponibles:
{% for category in site.categories %}
- **{{ category[0] }}** ({{ category[1].size }} articles)
  {% for post in category[1] %}
  - {{ post.title }}
  {% endfor %}
{% endfor %}

## Posts avec leurs catégories:
{% for post in site.posts %}
- **{{ post.title }}**
  - Catégories: {{ post.categories | join: ', ' }}
  - Date: {{ post.date }}
{% endfor %}

## site.categories en raw:
{{ site.categories }}
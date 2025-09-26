---
layout: page
title: Categories
permalink: /categories/

##  Categories

{% for category in categories %}
  {% if category %}
- [{{ category | upcase }}](#{{ category | slugify }}) ({{ site.posts | where: 'category', category | size }} posts)
  {% endif %}
{% endfor %}

<style>
.post-list li {
  margin-bottom: 2em;
  padding-bottom: 1em;
  border-bottom: 1px solid #eee;
}

.post-list li:last-child {
  border-bottom: none;
}

h2 {
  color: #2a7ae4;
  margin-top: 2em;
  padding-bottom: 0.5em;
  border-bottom: 2px solid #2a7ae4;
}
</style>

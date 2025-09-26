---
layout: page
title: Categories
permalink: /categories/
---

# Browse by Category

Explorez les posts organisés par différent domaines:

{% assign categories = site.posts | map: 'category' | uniq | sort %}

{% for category in categories %}
  {% if category %}
    <h2 id="{{ category | slugify }}">{{ category | upcase }}</h2>

    {% assign category_posts = site.posts | where: 'category', category %}
    <ul class="post-list">
      {% for post in category_posts %}
        <li>
          <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>
          <h3>
            <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
          </h3>
          {% if post.excerpt %}
            <p>{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
          {% endif %}
        </li>
      {% endfor %}
    </ul>
  {% endif %}
{% endfor %}

---

## Quick Links to Categories

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

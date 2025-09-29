---
layout: default
title: "Catégories d'Articles"
permalink: /categories/
---

# EXPLORER PAR DOMAINE

*Découvrez mes articles organisés par thèmes et domaines d'expertise.*

---

{% assign all_categories = site.posts | map: 'categories' | join: ',' | split: ',' | uniq | sort %}

{% for category in all_categories %}
  {% if category != "" %}
## 📂 {{ category | upcase }}

{% assign posts_in_category = site.posts | where: 'categories', category %}
{% for post in posts_in_category %}
### [{{ post.title }}]({{ post.url | relative_url }})
**{{ post.date | date: "%d %B %Y" }}** • *{{ post.author | default: "Sahi MFG" }}*

{{ post.excerpt | strip_html | truncatewords: 25 }}

[Lire l'article 🚀]({{ post.url | relative_url }})

---
{% endfor %}
  {% endif %}
{% endfor %}

[← Retour à l'accueil 🚀](/)

---

*Vous ne trouvez pas ce que vous cherchez ? [Contactez-moi 🚀](mailto:mohamedfrancissahi@gmail.com) pour suggérer de nouveaux sujets !*
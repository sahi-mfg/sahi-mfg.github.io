---
layout: default
title: "Bienvenue dans Mon Journal d'Apprentissage"
---

# Hello, je suis Sahi ! 👋

Bienvenue sur mon blog personnel où je partage ce que j'apprends à travers divers domaines de la connaissance. En tant qu'apprenant curieux de Côte d'Ivoire, j'explore et j'écris sur :

## 📚 Ce que vous trouverez ici

- **Mathématiques** - Des concepts fondamentaux aux sujets avancés
- **Programmation** - Tutoriels de code, bonnes pratiques et aperçus de projets
- **Science des Données** - Analyse, apprentissage automatique (Machine Learning) et visualisation de données
- **Physique** - Comprendre le monde naturel à travers les principes scientifiques
- **Philosophie** - Réflexions profondes sur l'existence, l'éthique et la nature humaine
- **Sociologie** - Exploration de la société, de la culture et du comportement humain
- **Politique Locale** - Perspectives sur la gouvernance et les enjeux sociaux en Côte d'Ivoire
- Et bien d'autres sujets

## 🌟 Ma Mission

L'apprentissage ne s'arrête jamais, et je crois que le savoir grandit lorsqu'il est partagé. À travers ce blog, mon but est de :

- Documenter mon parcours d'apprentissage à travers plusieurs disciplines
- Partager des idées qui pourraient aider d'autres apprenants
- Faire le pont entre différents domaines de la connaissance pour trouver des connexions
- Contribuer au discours intellectuel, particulièrement d'un point de vue africain

## 📖 Articles Récents

{% for post in site.posts limit: 5 %}
### [{{ post.title }}]({{ post.url | relative_url }})

**{{ post.date | date: "%d %B %Y" }}** 
{% if post.categories %}
{% for category in post.categories %}
*{{ category | upcase }}*
{% endfor %}
{% endif %}

{{ post.excerpt | strip_html | truncatewords: 30 }}

[Lire la suite →]({{ post.url | relative_url }})

---
{% endfor %}

## 🔗 Navigation

- [Parcourir par catégorie](/categories)
- [S'abonner via RSS](/feed.xml)

---

*Suivez mon parcours tandis que j'explore les liens fascinants entre la science, la technologie, la philosophie et la société. Chaque publication est un pas en avant dans la compréhension de notre monde complexe.*

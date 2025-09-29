# Journal d'Apprentissage de Sahi

Un blog personnel utilisant **Quarto** et **Python** pour partager mes pensées, expériences et connaissances sur divers sujets qui me passionnent.

🌐 **Site en ligne**: [https://sahi-mfg.github.io](https://sahi-mfg.github.io)

## 🚀 Technologies utilisées

- **[Quarto](https://quarto.org/)** - Framework de publication scientifique
- **Python** - Langage principal pour les analyses et visualisations
- **uv** - Gestionnaire de paquets Python moderne et rapide
- **GitHub Pages** - Hébergement du site web
- **Jupyter** - Notebooks pour le développement interactif

## 📁 Structure du projet

```
├── _quarto.yml          # Configuration Quarto
├── index.qmd            # Page d'accueil
├── about.qmd            # Page "À propos"
├── posts.qmd            # Listing de tous les articles
├── posts/               # Articles du blog
│   ├── 2025-09-26-seconde.qmd
│   └── 2025-09-29-test-categorisation.qmd
├── categories/          # Pages de catégories
│   ├── physique.qmd
│   ├── mathematiques.qmd
│   ├── programmation.qmd
│   ├── data-science.qmd
│   └── philosophie.qmd
├── custom.scss          # Styles personnalisés
├── styles.css           # CSS supplémentaires
├── build.py            # Script de construction et déploiement
├── pyproject.toml      # Configuration Python/uv
└── _site/              # Site généré (ignoré par Git)
```

## 🛠️ Installation et développement

### Prérequis

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) installé

### Installation

```bash
# Cloner le repository
git clone https://github.com/sahi-mfg/sahi-mfg.github.io.git
cd sahi-mfg.github.io

# Installer les dépendances avec uv
uv sync
```

### Développement

```bash
# Prévisualiser le site (mode développement)
uv run quarto preview

# Ou utiliser le script Python
python build.py preview
```

Le site sera accessible à l'adresse : http://localhost:4000

### Construction

```bash
# Construire le site
uv run quarto render

# Ou utiliser le script Python
python build.py build
```

### Déploiement

```bash
# Déployer sur GitHub Pages
python build.py deploy
```

## 📝 Créer un nouvel article

1. Créer un nouveau fichier `.qmd` dans le dossier `posts/`
2. Utiliser le format de nommage : `YYYY-MM-DD-titre.qmd`
3. Ajouter le front matter YAML :

```yaml
---
title: "Titre de l'article"
description: "Description courte"
author: "Sahi Mohamed Francis Gonsangbeu"
date: "YYYY-MM-DD"
categories: [categorie1, categorie2]
---
```

4. Écrire le contenu en Markdown avec du code Python intégré si nécessaire
5. Prévisualiser avec `quarto preview`

## 🎨 Personnalisation

- **Styles** : Modifier `custom.scss` et `styles.css`
- **Configuration** : Éditer `_quarto.yml`
- **Thème** : Basé sur le thème "cosmo" de Bootstrap

## 🔧 Commandes utiles

```bash
# Installer une nouvelle dépendance Python
uv add nom-du-paquet

# Mettre à jour les dépendances
uv sync --upgrade

# Nettoyer le cache Quarto
uv run quarto render --cache-refresh

# Vérifier la syntaxe des fichiers Quarto
uv run quarto check
```

## 🌐 Site en ligne

Le site est automatiquement déployé sur GitHub Pages : https://sahi-mfg.github.io

## 📚 Catégories d'articles

- **🔬 Science des données** - Analyses, machine learning et visualisations
- **💻 Programmation** - Tutoriels pratiques et bonnes pratiques  
- **🧮 Mathématiques** - Concepts expliqués simplement
- **⚗️ Physique** - Comprendre le monde qui nous entoure
- **🤔 Philosophie** - Réflexions sur l'existence et la société

## 📞 Contact

- **Email** : mohamedfrancissahi@gmail.com
- **GitHub** : [@sahi-mfg](https://github.com/sahi-mfg)


## Structure

- `_config.yml` - configuration du site
- `_layouts/` - Les templates
- `_posts/` - Les posts
- `assets/css/` - Style custom
- `index.md` - Page d'accueil
- `about.md` - Page à propos
- `categories.md` - Les posts organisés par catégories

---

## Contact

Pour toute question ou suggestion, vous pouvez me contacter à l'adresse suivante : [mohamedfrancissahi@gmail.com](mailto:mohamedfrancissahi@gmail.com)

Merci de votre visite et bonne lecture !

Built with ❤️ using Jekyll and hosted on GitHub Pages.
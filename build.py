#!/usr/bin/env python3
"""
Script de construction et de déploiement pour le site Quarto
"""

import subprocess
import sys
from pathlib import Path

def run_command(cmd, description):
    """Exécute une commande avec gestion d'erreur"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} terminé avec succès")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de {description}")
        print(f"Code de sortie: {e.returncode}")
        print(f"Erreur: {e.stderr}")
        return None

def build_site():
    """Construit le site Quarto"""
    print("🚀 Construction du site Quarto...")
    
    # Vérifier que nous sommes dans le bon répertoire
    if not Path("_quarto.yml").exists():
        print("❌ Fichier _quarto.yml non trouvé. Êtes-vous dans le bon répertoire ?")
        return False
    
    # Nettoyer le cache si nécessaire
    run_command("uv run quarto render --cache-refresh", "Nettoyage du cache")
    
    # Construire le site
    result = run_command("uv run quarto render", "Construction du site")
    if result is None:
        return False
    
    print("✅ Site construit avec succès dans le dossier _site/")
    return True

def preview_site():
    """Lance la prévisualisation du site"""
    print("👀 Lancement de la prévisualisation...")
    run_command("uv run quarto preview", "Prévisualisation du site")

def deploy_to_github():
    """Déploie le site sur GitHub Pages"""
    print("🚀 Déploiement sur GitHub Pages...")
    
    # Vérifier l'état Git
    result = run_command("git status --porcelain", "Vérification de l'état Git")
    if result and result.strip():
        print("⚠️  Il y a des fichiers non commités. Voulez-vous continuer ? (y/N)")
        if input().lower() != 'y':
            print("Déploiement annulé")
            return False
    
    # Ajouter tous les fichiers
    run_command("git add .", "Ajout des fichiers au staging")
    
    # Commit
    commit_msg = input("Message de commit (ou Entrée pour un message par défaut): ").strip()
    if not commit_msg:
        commit_msg = "Mise à jour du site"
    
    run_command(f'git commit -m "{commit_msg}"', "Commit des changements")
    
    # Push
    result = run_command("git push origin main", "Push vers GitHub")
    if result is not None:
        print("✅ Site déployé avec succès !")
        print("🌐 Votre site sera disponible à: https://sahi-mfg.github.io")
        return True
    
    return False

def main():
    """Fonction principale"""
    if len(sys.argv) < 2:
        print("Usage: python build.py [build|preview|deploy]")
        print("  build   - Construit le site")
        print("  preview - Lance la prévisualisation")
        print("  deploy  - Déploie sur GitHub Pages")
        return
    
    command = sys.argv[1].lower()
    
    if command == "build":
        build_site()
    elif command == "preview":
        preview_site()
    elif command == "deploy":
        if build_site():
            deploy_to_github()
    else:
        print(f"Commande inconnue: {command}")
        print("Commandes disponibles: build, preview, deploy")

if __name__ == "__main__":
    main()
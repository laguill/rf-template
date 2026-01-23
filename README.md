# 🚀 Guide d’Installation et Utilisation

**Tests Automatisés avec Robot Framework**

![Python](https://img.shields.io/badge/python-3.14-blue)
![Robot Framework](https://img.shields.io/badge/robot--framework-latest-orange)

Ce projet permet de créer et d'exécuter des tests automatisés avec **Robot Framework**, un outil puissant pour écrire des scripts de test en langage simple. <br>
Il utilise **uv** pour l’exécution rapide des scripts Python et **rust-just** pour gérer les commandes terminal de manière pratique et reproductible.

Voici comment l’installer et l’utiliser.

## 📌 Prérequis (À installer avant tout)

Avant de commencer, assurez-vous d’avoir les outils suivants sur votre ordinateur :

### 1. Outil pour installer des logiciels (Windows uniquement) en ligne de commande (Normalement déjà présent sur Win11).

Installez Winget, un gestionnaire de paquets Windows :

[winget install](https://apps.microsoft.com/detail/9nblggh4nns1?hl=fr-FR&gl=FR)

### 2. Gestionnaire de bibliothèques Python (uv)

<kbd>uv</kbd> simplifie l’installation des dépendances Python. Installez-le avec :

Exécuter la commande suivante dans PowerShell :

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 3. Éditeur de code (Optionnel mais recommandé)

Installez VS Code pour éditer les fichiers :

```powershell
winget install -e --id Microsoft.VisualStudioCode
```

## Executer les tests (pour les devs voir plus bas)

### 1. Cloner le dépôt

**Important** : Clonez le dépôt dans le dossier `~/source/repos/` pour une organisation cohérente :

```powershell
# Créez le dossier parent si nécessaire
mkdir -p ~/source/repos/

# Clonez le dépôt
cd ~/source/repos/rf-template
git clone https://github.com/laguill/rf-template.git
cd rf-template
```

### 2. Pour exécuter les tests uniquement

1. Ouvrez un terminal **(PowerShell ou CMD)** dans le dossier du projet.
2. Installez les dépendances minimales :

   ```powershell
      uv run just set-up install
   ```

   _Cela installe Python et les outils nécessaires pour lancer les tests._

3. Executer les tests

   ```powershell
      uv run just test
   ```

   _Tous les tests Robot Framework seront exécutés._
   _Le résumé des résultats s'affiche dans le navigateur._

!!! tip "Mettre à Jour le Projet"

      Pour actualiser les dépendances :

      ```powershell
      uv run just update
      ```

## ✨ INstaller les dépendances pour le Développement

### 1. Cloner le dépôt

**Important** : Clonez le dépôt dans le dossier `~/source/repos/` pour une organisation cohérente :

Si vous êtes automaticien et que vous avez suivis les instructions précédentes vous pouvez tout supprimer 😉.

```powershell
# Créez le dossier parent si nécessaire
mkdir -p ~/source/repos/TestsAutos
cd ~/source/repos/TestsAutos

# Cloner en mode bare dans .git (recommandé pour les worktrees)
cd ~/source/repos/rf-template
git clone --bare https://github.com/laguill/rf-template.git .git

# Configurer le fetch pour récupérer toutes les branches
git config remote.origin.fetch '+refs/heads/*:refs/remotes/origin/*'

# Récupérer toutes les branches distantes
git fetch

# Configurer le tracking des branches locales
git for-each-ref --format='%(refname:short)' refs/heads | ForEach-Object { git branch --set-upstream-to=origin/$_ $_ }
```
Lister les branches distantes
```powershell
git branch -vv
```

### 2. Pour le développement de nouveaux tests


> [tip]
> Pour une meilleure organisation, nous recommandons d'utiliser les **worktrees Git** plutôt que les branches traditionnelles. Consultez notre guide : [Utilisation des Worktrees](../conventions/worktree_usage.md)

### 3. Utiliser les tasks dans vscode

> [tip]
> Des actions sont configurées dans vscode pour faciliter l'usage des commandes powershell. Pour les utiliser, ouvrez la palette de commandes (Ctrl+Shift+P), tapez "Run Task" et sélectionnez une des tâches disponibles comme "test", "install-dev" ou "update-dev".

!!! tip "Mettre à Jour le Projet"

      Pour actualiser les dépendances :

      ```powershell
      uv run just update-dev
      ```

## 📚 Ressources utiles

- [Robot Framework](https://robotframework.org/)

- [Just (Rust)](https://just.systems)

- [uv](https://docs.astral.sh/uv/)

- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/#summary)

[cc]: https://www.conventionalcommits.org/en/v1.0.0/#summary

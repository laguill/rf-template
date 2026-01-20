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

## 🛠 Installation de l’environnement de développement

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

### 2. Pour exécuter les tests uniquement (sans coder)

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

4. Mettre à Jour le Projet

   Pour actualiser les dépendances :

   ```powershell
   uv run just update
   ```

## ✨ Développement

### 1. Cloner le dépôt

**Important** : Clonez le dépôt dans le dossier `~/source/repos/` pour une organisation cohérente :

Si vous êtes automaticien et que vous avez suivis les instructions précédentes vous pouvez tout supprimer.

```powershell
# Créez le dossier parent si nécessaire
mkdir -p ~/source/repos/rf-template

# Clonez le dépôt
cd ~/source/repos/rf-template
git clone --bare https://github.com/laguill/rf-template.git .git
```

1. Installez toutes les dépendances (incluant les outils de développement) :

   ```powershell
      uv run just set-up install-dev
   ```

   _Cette commande installe les dépendances python et des outils comme robocop pour vérifier la qualité du code._

> [tip]
> Pour une meilleure organisation, nous recommandons d'utiliser les **worktrees Git** plutôt que les branches traditionnelles. Consultez notre guide : [Utilisation des Worktrees](docs/conventions/worktree_usage.md)

2. Utiliser les tasks dans vscode

> [tip]
> Des actions sont configurées dans vscode pour faciliter l'usage des commandes powershell. Pour les utiliser, ouvrez la palette de commandes (Ctrl+Shift+P), tapez "Run Task" et sélectionnez une des tâches disponibles comme "test", "install-dev" ou "update-dev".

3. Mettre à Jour le Projet

   Pour actualiser les dépendances :

   ```powershell
   uv run just update-dev
   ```

## 📝 Développer de Nouveaux Tests

1. Ouvrez le projet dans VS Code :

   - Lancez VS Code > Fichier > Ouvrir un dossier > Sélectionnez le dossier du projet.

2. Créez/modifiez des tests :
   - Ajoutez vos fichiers de test dans le dossier /tests (format .robot).
3. Vérifiez vos changements :

   ```powershell
   uv run just test
   ```

4. Exemple : Un fichier mon\*test.robot pourrait ressembler à :

   ```RobotFramework
   *** Settings ***
   Library   Browser

   *** Test Cases ***
   Example Test
      New Page    https://playwright.dev
      Get Text    h1    contains    Playwright
   ```

## 🤝 Contribuer

Pour contribuer, voir le guide complet : [CONTRIBUTING.md](CONTRIBUTING.md)

- PR fusionnées après validation par un mainteneur et passage de tous les tests.

- Respectez les conventions de commit et la structure des tests.

## 📚 Ressources utiles

- [Robot Framework](https://robotframework.org/)

- [Just (Rust)](https://just.systems)

- [uv](https://docs.astral.sh/uv/)

- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/#summary)

[cc]: https://www.conventionalcommits.org/en/v1.0.0/#summary

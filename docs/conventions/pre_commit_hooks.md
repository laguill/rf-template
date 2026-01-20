# Utilisation des hooks de pre-commit

Les hooks de pre-commit sont des scripts qui s'exécutent automatiquement avant chaque commit pour vérifier la qualité du code et de la documentation. Ils permettent de détecter et corriger des problèmes potentiels avant qu'ils ne soient commités.

## Installation et configuration

### Prérequis

- Avoir [uv](https://github.com/astral-sh/uv) installé sur votre machine

### Installation des hooks

Pour installer les hooks de pre-commit, exécutez la commande suivante à la racine du projet :

```powershell
uv run prek install
```

Cette commande installe les hooks dans le répertoire `.git/hooks/` de votre dépôt.

## Utilisation de uv

`uv` est un outil moderne pour gérer les environnements Python et les dépendances. Il est utilisé dans ce projet pour exécuter les commandes de développement.

### Commandes courantes

- **Installer les dépendances** :
  ```powershell
  uv sync
  ```

- **Exécuter une commande dans l'environnement isolé** :
  ```powershell
  uv run <commande>
  ```

- **Exécuter tous les hooks manuellement** :
  ```powershell
  uv run prek
  ```

## Hooks disponibles

Voici la liste des hooks configurés dans ce projet :

### 1. Robocop (Robot Framework linter)
- **Description** : Vérifie la qualité du code Robot Framework
- **Fonctionnalité** : Analyse les fichiers `.robot` pour détecter les problèmes de style et de syntaxe

### 2. Robocop Format (Robot Framework formatter)
- **Description** : Formate automatiquement le code Robot Framework
- **Fonctionnalité** : Applique un style de code cohérent à tous les fichiers Robot Framework

### 3. Ruff Check
- **Description** : Linter Python rapide
- **Fonctionnalité** : Vérifie la qualité du code Python et corrige automatiquement certains problèmes

### 4. Ruff Format
- **Description** : Formateur Python
- **Fonctionnalité** : Formate le code Python selon les conventions PEP 8

### 5. Ty Check
- **Description** : Vérification de type Python
- **Fonctionnalité** : Vérifie la cohérence des types dans le code Python

### 6. Build Documentation
- **Description** : Construction de la documentation
- **Fonctionnalité** : Vérifie que la documentation peut être construite sans erreurs
- **Commande** : `uv run mkdocs build --strict --verbose`
- **Options** :
  - `--strict` : Fait échouer le commit si des avertissements sont présents
  - `--verbose` : Affiche des détails sur la construction

### 7. Prevent commits to main
- **Description** : Empêche les commits directs sur la branche main
- **Fonctionnalité** : Protège la branche main en exigeant des pull requests

### 8. Check YAML
- **Description** : Vérification de la syntaxe YAML
- **Fonctionnalité** : Vérifie que les fichiers YAML sont bien formés

### 9. End of File Fixer
- **Description** : Ajoute des sauts de ligne à la fin des fichiers
- **Fonctionnalité** : Assure que tous les fichiers se terminent par un saut de ligne

### 10. Check Added Large Files
- **Description** : Vérifie les fichiers volumineux ajoutés
- **Fonctionnalité** : Empêche l'ajout de fichiers trop volumineux au dépôt

### 11. Check Merge Conflict
- **Description** : Vérifie les conflits de fusion
- **Fonctionnalité** : Détecte les marqueurs de conflit de fusion dans les fichiers

### 12. CSpell
- **Description** : Vérification de l'orthographe
- **Fonctionnalité** : Vérifie l'orthographe dans les fichiers de code et de documentation

### 13. Conventional Commits
- **Description** : Vérification des messages de commit
- **Fonctionnalité** : Assure que les messages de commit suivent la convention [Conventional Commits](conventional_commits.md)

### 14. Commitizen
- **Description** : Assistant pour les messages de commit
- **Fonctionnalité** : Aide à créer des messages de commit conformes aux conventions

### 15. Biome Check
- **Description** : Vérification du code JavaScript/TypeScript
- **Fonctionnalité** : Vérifie la qualité du code JavaScript et TypeScript

## Exécution manuelle des hooks

Pour exécuter tous les hooks manuellement sur tous les fichiers :

```powershell
uv run prek
```

Pour exécuter un hook spécifique :

```powershell
uv run prek run <hook-id> --all-files
```

Par exemple, pour exécuter uniquement le hook de construction de la documentation :

```powershell
uv run prek run build-docs --all-files
```

## Désactivation temporaire des hooks

Si vous devez désactiver temporairement les hooks pour un commit spécifique, utilisez l'option `--no-verify` :

```powershell
git commit --no-verify -m "Votre message de commit"
```

⚠️ **Attention** : Utilisez cette option avec parcimonie, uniquement lorsque cela est absolument nécessaire.

## Bonnes pratiques

1. **Exécutez les hooks régulièrement** : Exécutez `uv run prek` avant de push vos modifications pour éviter les surprises.

2. **Corrigez les problèmes immédiatement** : Plus vous attendez pour corriger les problèmes détectés par les hooks, plus il sera difficile de les résoudre.

3. **Utilisez les outils de formatage** : Les hooks comme `robocop-format` et `ruff-format` peuvent corriger automatiquement certains problèmes. Utilisez-les régulièrement.

4. **Respectez les conventions** : Suivez les conventions de nommage et de style définies dans les autres documents de la section [Conventions](conventional_commits.md).

5. **Documentation** : Si vous modifiez la documentation, assurez-vous qu'elle peut être construite sans erreurs avant de commiter.

## Dépannage

### Les hooks prennent trop de temps

Si les hooks prennent trop de temps à s'exécuter, vous pouvez :

1. Exécuter les hooks manuellement pour identifier les problèmes :
   ```powershell
   uv run prek
   ```

2. Désactiver temporairement certains hooks dans le fichier `.pre-commit-config.yaml`

3. Utiliser `--no-verify` pour un commit spécifique (à utiliser avec parcimonie)

### Les hooks échouent sans raison apparente

1. Vérifiez que toutes les dépendances sont installées :
   ```powershell
   uv sync
   ```

2. Supprimez et réinstallez les hooks :
   ```powershell
   uv run pre-commit uninstall
   uv run pre-commit install
   ```

3. Vérifiez les logs d'erreur pour identifier le problème spécifique

### Problèmes avec uv

Si vous rencontrez des problèmes avec uv, assurez-vous d'avoir la dernière version :

```powershell
uv self update
```

Et réinstallez les dépendances :

```powershell
uv sync
```

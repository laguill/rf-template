# 🌳 Utilisation des Worktrees pour le Développement

**Guide pour les petites équipes**

Les worktrees Git sont une alternative aux branches traditionnelles. Ils permettent de travailler sur plusieurs fonctionnalités ou corrections simultanément, sans avoir à basculer entre des branches.

## 📚 Pourquoi utiliser les worktrees ?

- **Simplicité** : Pas besoin de changer de branche constamment
- **Isolation** : Chaque worktree a son propre répertoire de travail
- **Parallélisme** : Travaillez sur plusieurs tâches en même temps
- **Clarté** : Structure de dossier explicite pour chaque fonctionnalité

## 🛠 Configuration initiale

### 1. Cloner le dépôt dans le bon emplacement

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

```powershell
## Lister les branches distantes
git branch -vv
```
### 2. Structure de dossier recommandée

```powershell
TestsAutos/
├── .git/              # Dépôt bare (hub central)
├── master/            # Worktree branche de production
├── develop/           # Worktree branche d'intégration (BASE pour les développements) contient toutes les features en pre-prod
├── features/          # Dossier pour les nouvelles fonctionnalités
│   ├── feature-auth/
│   ├── feature-api/
│   └── feature-dashboard/
├── docs/              # Dossier pour la documentation
│   ├── fix-readme/
│   ├── add-api-doc/
│   └── translate-fr/
├── fixes/             # Dossier pour les corrections de bugs
│   ├── fix-bug-123/
│   └── fix-login-error/
├── hotfixes/          # Dossier pour les corrections urgentes production
│   └── hotfix-security/
└── releases/          # Dossier pour les branches de release (optionnel)
    └── release-1.2.0/
```

## Workflows avec Worktree

Comprendre `develop` vs `master`
deux branches permanentes

- `master` : branche de production

   Code stable, testé, déployé
   Merge uniquement depuis `develop` ou `hotfix`
   Chaque commit = une version en production


- `develop` : branche d'**intégration**

   Base pour créer toutes les branches de développement
   Intègre toutes les features avant la release
   Plus avancée que `master`

Flux : `feature` → `master` → `déploiement`

!!! warning  "Important"

    Une fois la branche créée, il faut réinstaller les dépendances de dev **DANS chaque nouvelle branche** avec la commande suivante:
    ```powershell
    uv run just install-dev
    ```

### Initialiser les branches principales

```powershell
# Créer le worktree master (production)
git worktree add ./master master

# Créer le worktree develop (intégration)
git worktree add ./develop develop

# develop devient votre base de travail quotidien
```

### Travailler sur la branche principale

```powershell
# Git Flow : travailler sur develop
cd develop
git pull
# ... modifications directes si nécessaire ...
git add .
git commit -m "chore: mise à jour de configuration"
git push

# GitHub Flow : travailler sur master
cd master
git pull
# ... modifications directes si nécessaire ...
git add .
git commit -m "chore: mise à jour de configuration"
git push
```
!!! warning "Attention"

    Évitez les commits directs sur les branches principales. Préférez toujours passer par des branches de feature/fix et des Pull Requests.


!!! info "Convention de nommage"

      | Type                     | Préfixe       | Exemple                          |
      |--------------------------|---------------|----------------------------------|
      | Nouvelle fonctionnalité  | feature/      | `feature/user-authentication`    |
      | Correction de bug        | fix/          | `fix/login-error`                |
      | Documentation            | docs/         | `docs/update-readme`             |
      | Hotfix urgent            | hotfix/       | `hotfix/security-patch`          |

## Développer une nouvelle feature

### WorkFlow (depuis `develop`)

```powershell
# Créer un worktree pour une nouvelle feature À PARTIR DE DEVELOP
git worktree add ./features/ma-feature -b feature/ma-feature develop

# Naviguer dans le worktree
cd features/ma-feature

# Développer la feature
# ... modifications ...
git add .
git commit -m "feat: implémentation de ma feature"
git push -u origin feature/ma-feature

# Créer une Pull Request vers DEVELOP sur Azure devops
```
### WorkFlow (depuis `master`)

```powershell
# Créer un worktree pour une nouvelle feature À PARTIR DE MASTER
git worktree add ./features/ma-feature -b feature/ma-feature master

# Naviguer dans le worktree
cd features/ma-feature

# Développer la feature
# ... modifications ...
git add .
git commit -m "feat: implémentation de ma feature"
git push -u origin feature/ma-feature

# Créer une Pull Request vers MASTER sur Azure devops
```
### Convention de nommage des branches :

- `feature/nom-descriptif` pour les nouvelles fonctionnalités
- `feature/issue-123-description` si lié à une issue

!!! example

    `feature/login`, `feature/sortie_poche`

### Cycle de vie :

- Créer un worktree depuis `develop` (ou `master`)
- Développer et commiter
- Pousser et créer une PR
- Review et tests
- Merge dans `develop` (ou `master`)
- Supprimer la branche et le worktree

## Corriger la documentation

### WorkFlow (depuis `develop`)

```powershell
# Créer un worktree pour la documentation À PARTIR DE DEVELOP
git worktree add ./docs/fix-readme -b docs/fix-readme develop

# Naviguer dans le worktree
cd docs/fix-readme

# Corriger la documentation
# ... modifications ...
git add .
git commit -m "docs: correction des instructions d'installation"
git push -u origin docs/fix-readme

# Créer une Pull Request vers DEVELOP sur GitHub
```

### WorkFlow (depuis `master`)

```powershell
# Créer un worktree pour la documentation À PARTIR DE MASTER
git worktree add ./docs/fix-readme -b docs/fix-readme master

# Naviguer dans le worktree
cd docs/fix-readme

# Corriger la documentation
# ... modifications ...
git add .
git commit -m "docs: correction des instructions d'installation"
git push -u origin docs/fix-readme

# Créer une Pull Request vers MASTER sur GitHub
```

**Convention de nommage des branches :**

- `docs/nom-descriptif` pour la documentation

!!! example "Exemple"

    `docs/fix-typo`, `docs/update-installation`, `docs/add-api-reference`, `docs/translate-fr`

**✅ Pourquoi créer une branche pour la documentation ?**

- Permet la revue par les pairs (Pull Request)
- Traçabilité des changements
- Tests de génération de doc (CI/CD)
- Évite les erreurs sur la branche principale
- Même workflow que pour le code

## Corriger un bug

### WorkFlow (depuis `develop`)

```powershell
# Créer un worktree pour corriger un bug À PARTIR DE DEVELOP
git worktree add ./fixes/fix-bug-123 -b fix/bug-123 develop

# Naviguer dans le worktree
cd fixes/fix-bug-123

# Corriger le bug
# ... modifications ...
git add .
git commit -m "fix: correction du bug #123"
git push -u origin fix/bug-123

# Créer une Pull Request vers DEVELOP sur GitHub
```

### WorkFlow (depuis `master`)

```powershell
# Créer un worktree pour corriger un bug à partir de master
git worktree add ./fixes/fix-bug-123 -b fix/bug-123 master

# Naviguer dans le worktree
cd fixes/fix-bug-123

# Corriger le bug
# ... modifications ...
git add .
git commit -m "fix: correction du bug #123"
git push -u origin fix/bug-123

# Créer une Pull Request sur GitHub
```

**Convention de nommage des branches :**

!!! example "Exemple"
    - `fix/bug-123` ou `fix/description-du-bug`
    - `bugfix/nom-descriptif` (alternative)


## Hotfix urgent en production

**Contexte :** Un bug critique est découvert en production et doit être corrigé immédiatement, sans attendre les features en développement.

### WorkFlow (TOUJOURS depuis `master`)

```powershell
# Créer un worktree pour un hotfix À PARTIR DE MASTER (jamais develop)
git worktree add ./hotfixes/hotfix-critical -b hotfix/critical-security master

# Naviguer dans le worktree
cd hotfixes/hotfix-critical

# Corriger le problème critique
# ... modifications ...
git add .
git commit -m "hotfix: correction critique de sécurité"
git push -u origin hotfix/critical-security

# Créer une Pull Request vers MASTER
# Après merge dans master, merger AUSSI dans develop pour synchroniser
cd ../develop
git pull origin develop
git merge master
git push
```

### WorkFlow (depuis `master`)

```powershell
# Créer un worktree pour un hotfix À PARTIR DE MASTER
git worktree add ./hotfixes/hotfix-critical -b hotfix/critical-security master

# Naviguer dans le worktree
cd fixes/fix-bug-123

# Corriger le bug
# ... modifications ...
git add .
git commit -m "fix: correction du bug #123"
git push -u origin fix/bug-123

# Créer une Pull Request sur GitHub
```

**Convention de nommage des branches :**

- `hotfix/nom-descriptif` pour les corrections urgentes

!!! example

    `hotfix/critical-security`, `hotfix/payment-failure`

!!! danger

    - Hotfix part TOUJOURS de `master` (production)
    - Merge dans `master` d'abord (correction en production)
    - Puis merge dans `develop` (synchronisation)

## Règles d'or pour les branches

1. **Toujours créer une branche** pour feature, fix, docs (jamais de commit direct sur `master` ou `develop`)
2. **Une branche = une tâche** (pas de multi-tâches dans une branche)
3. **Partir de la bonne base** :

   - WorkFlow : features/fixes/docs → depuis `develop`
   - WorkFlow : hotfixes → depuis `master`

4. **Pull Request obligatoire** pour merger dans `master` ou `develop`
5. **Nettoyer après merge** : supprimer branche et worktree
6. **Synchroniser régulièrement** : `git pull` sur `master` ou `develop`

## Travailler sur plusieurs tâches en parallèle

Avantage principal des worktrees : travailler sur plusieurs branches simultanément sans changer de contexte.

```powershell
# Terminal 1 : Travailler sur une feature
cd features/user-auth
# ... développement ...

# Terminal 2 : Corriger un bug urgent en parallèle
cd fixes/fix-critical-bug
# ... correction ...

# Terminal 3 : Mettre à jour la documentation
cd fixes/fix-doc
# ... documentation ...
```

## 🔧 Commandes utiles

```powershell
# Voir tous les worktrees
git worktree list
```

```powershell
# Nettoyer les worktrees invalides
git worktree prune
```

```powershell
# Supprimez un worktree local (après fusion)
cd ~/source/repos/rf-template
git worktree remove ../rf-template-feature-nom-de-la-fonctionnalité

# Supprimez la branche distante après fusion
git push origin --delete feature-nom-de-la-fonctionnalité
```

## ⚠️ Attention

- Les worktrees partagent le même dépôt `.git` - ne supprimez pas le dossier `.git`
- Chaque worktree a son propre répertoire de travail mais partage l'historique Git
- Les modifications dans un worktree n'affectent pas les autres worktrees
- Vous ne pouvez pas checker la même branche dans plusieurs worktrees simultanément

## 📚 Ressources supplémentaires

- [Documentation officielle Git Worktree](https://git-scm.com/docs/git-worktree)
- [Guide pratique des worktrees](https://www.atlassian.com/git/tutorials/git-worktree)
- [Comparaison worktrees vs branches](https://www.git-tower.com/learn/git/faq/git-worktree/)

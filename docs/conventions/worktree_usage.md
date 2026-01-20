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
mkdir -p ~/source/repos/rf-template

# Clonez le dépôt
cd ~/source/repos/rf-template
git clone --bare https://github.com/laguill/rf-template.git .git
```

### 2. Configurer votre environnement

```powershell
# Installez les dépendances de développement
uv run just set-up install-dev
```

## 🌱 Créer un nouveau worktree

### Pour une nouvelle fonctionnalité :

```powershell
# Depuis la racine du dépôt
git worktree add feature-nom-de-la-fonctionnalité
```

### Pour une correction de bug :

```powershell
git worktree add bugfix-nom-du-bug
```

# 🔄 Basculer entre les worktrees

```powershell
# Listez tous vos worktrees
cd ~/source/repos/rf-template
git worktree list

# Allez dans un worktree spécifique
cd ~/source/repos/rf-template/feature-nom-de-la-fonctionnalité
```

## 💾 Sauvegarder vos changements

```powershell
# Dans votre worktree
cd ~/source/repos/rf-template/feature-nom-de-la-fonctionnalité

# Ajoutez vos modifications
git add .

# Commitez avec un message clair
git commit -m "feat: ajouter nouvelle fonctionnalité X"

# Poussez vers la branche distante (créée automatiquement)
git push --set-upstream origin feature-nom-de-la-fonctionnalité
```

## 🧹 Nettoyer les worktrees

```powershell
# Supprimez un worktree local (après fusion)
cd ~/source/repos/rf-template
git worktree remove ../rf-template-feature-nom-de-la-fonctionnalité

# Supprimez la branche distante après fusion
git push origin --delete feature-nom-de-la-fonctionnalité
```

## 🎯 Bonnes pratiques

### Nommage et organisation

1. **Nommage clair** : Utilisez des noms descriptifs pour vos worktrees
   - Exemples : `courrier`, `documentation`, `login`
   - Évitez d'utiliser le même nom que la branche

2. **Un worktree = une tâche** : Évitez de mélanger plusieurs fonctionnalités

### Gestion des branches

4. **Synchronisation régulière** : Faites des pulls fréquents depuis _master

### Nettoyage et maintenance

6. **Nettoyage** : Supprimez les worktrees inutilisés

## 🔧 Commandes utiles

```powershell
# Voir tous les worktrees
git worktree list
```

```powershell
# Voir l'état de tous les worktrees
git worktree list --porcelain
```

## 📝 Exemple de workflow complet

1. **Création** :
   ```powershell
   cd ~/source/repos/rf-template
   git worktree add feature-login
   ```

2. **Développement** :
   ```powershell
   cd ~/source/repos/feature-login
   # Modifiez les fichiers, testez, etc.
   ```

3. **Commit** :
   ```powershell
   git add .
   git commit -m "feat: implémenter système de login"
   ```

4. **Push** :
   ```powershell
   git push --set-upstream origin feature-login
   ```

5. **Fusion** :
   - Créez une PR depuis feature-login vers main
   - Après fusion, supprimez le worktree et la branche

## ⚠️ Attention

- Les worktrees partagent le même dépôt `.git` - ne supprimez pas le dossier `.git`
- Chaque worktree a son propre répertoire de travail mais partage l'historique Git
- Les modifications dans un worktree n'affectent pas les autres worktrees
- Vous ne pouvez pas checker la même branche dans plusieurs worktrees simultanément

## 📚 Ressources supplémentaires

- [Documentation officielle Git Worktree](https://git-scm.com/docs/git-worktree)
- [Guide pratique des worktrees](https://www.atlassian.com/git/tutorials/git-worktree)
- [Comparaison worktrees vs branches](https://www.git-tower.com/learn/git/faq/git-worktree/)

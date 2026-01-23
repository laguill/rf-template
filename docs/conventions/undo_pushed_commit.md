# 🔙 Annuler un commit déjà poussé sur le dépôt

**Guide pour les équipes utilisant les worktrees**

Il arrive parfois qu'un commit soit poussé par erreur ou contienne des modifications qui doivent être annulées. Voici comment procéder en toute sécurité.

## ⚠️ Important

- **Ne jamais utiliser `git reset --hard` sur la branche main/master** si d'autres personnes ont déjà récupéré les changements
- **Privilégier les worktrees** pour isoler les modifications
- **Communiquer avec l'équipe** avant d'annuler des commits poussés

## 🛠 Méthodes pour annuler un commit poussé

### 1. Annuler le dernier commit (sans perdre les modifications)

Si vous avez poussé un commit par erreur mais que vous voulez garder les modifications :

```powershell
# Annule le dernier commit mais garde les modifications dans l'index
git reset --soft HEAD~1

# Si vous voulez aussi annuler les modifications dans l'index
git reset HEAD~1

# Puis poussez la nouvelle histoire
git push --force
```

⚠️ **Attention** : Le `--force` peut causer des problèmes pour les autres membres de l'équipe.

### 2. Annuler un commit spécifique avec un nouveau commit (méthode recommandée)

Cette méthode est plus sûre car elle ne réécrit pas l'historique :

```powershell
# Créez un nouveau commit qui annule les changements du commit précédent
git revert <commit-hash>

# Exemple : git revert abc1234

# Puis poussez le nouveau commit
git push
```

### 3. Annuler plusieurs commits avec worktree (méthode avancée)

Si vous devez annuler plusieurs commits et que vous travaillez en équipe :

```powershell
# 1. Créez un worktree dédié pour cette opération
cd ~/source/repos/rf-template
git worktree add ../rf-template-fix-history

# 2. Allez dans le worktree
cd ~/source/repos/rf-template-fix-history

# 3. Annulez les commits avec reset (attention, cela réécrit l'historique)
git reset --hard <commit-hash>

# 4. Forcez le push (uniquement si vous êtes sûr que personne d'autre n'a travaillé sur ces commits)
git push --force

# 5. Informe l'équipe pour qu'ils fassent un pull

# 6. Supprimez le worktree quand vous avez terminé
git worktree remove ../rf-template-fix-history
```

### 4. Annuler un commit et garder l'historique (méthode la plus sûre)

```powershell
# 1. Créez un worktree pour isoler les modifications
cd ~/source/repos/rf-template
git worktree add ../rf-template-cleanup

# 2. Allez dans le worktree
cd ~/source/repos/rf-template-cleanup

# 3. Annulez le commit avec revert (créé un nouveau commit qui annule les changements)
git revert <commit-hash>

# 4. Poussez le nouveau commit
git push

# 5. Supprimez le worktree
git worktree remove ../rf-template-cleanup
```

## 📋 Workflow complet avec worktree

### Scénario : Annuler un commit poussé par erreur

1. **Créer un worktree dédié** :
   ```powershell
   cd ~/source/repos/rf-template
   git worktree add ../rf-template-undo-commit
   ```

2. **Aller dans le worktree** :
   ```powershell
   cd ~/source/repos/rf-template-undo-commit
   ```

3. **Vérifier l'historique** :
   ```powershell
   git log --oneline
   ```

4. **Choisir la méthode d'annulation** :
   - **Pour annuler et garder les modifications** : `git reset --soft HEAD~1`
   - **Pour annuler complètement** : `git reset HEAD~1`
   - **Pour créer un commit d'annulation** : `git revert <commit-hash>`

5. **Pousser les changements** :
   ```powershell
   git push --force  # Si vous avez utilisé reset
   git push          # Si vous avez utilisé revert
   ```

6. **Informer l'équipe** :
   - Envoyez un message dans le canal de communication de l'équipe
   - Demandez à tout le monde de faire un `git pull`

7. **Nettoyer** :
   ```powershell
   git worktree remove ../rf-template-undo-commit
   ```

## ⚠️ Bonnes pratiques

1. **Communiquez toujours** avant d'annuler des commits poussés
2. **Préférez `git revert`** à `git reset --force` pour éviter de réécrire l'historique
3. **Utilisez des worktrees** pour isoler les opérations dangereuses
4. **Faites des sauvegardes** avant d'annuler des commits importants
5. **Testez localement** avant de pousser des annulations

## 📚 Exemple concret

### Situation : Un commit avec une faute de frappe a été poussé

```powershell
# 1. Créer un worktree
cd ~/source/repos/rf-template
git worktree add ../rf-template-fix-typo

# 2. Aller dans le worktree
cd ~/source/repos/rf-template-fix-typo

# 3. Utiliser revert pour créer un commit d'annulation
git revert abc1234 -m 1  # -m 1 pour choisir le message du commit parent

# 4. Pusher le commit d'annulation
git push

# 5. Informer l'équipe

# 6. Supprimer le worktree
git worktree remove ../rf-template-fix-typo
```

## 🔧 Commandes utiles

```powershell
# Voir l'historique des commits
git log --oneline

# Voir les différences entre commits
git diff <commit1> <commit2>

# Annuler le dernier commit (sans perdre les modifications)
git reset --soft HEAD~1

# Annuler le dernier commit (et perdre les modifications)
git reset HEAD~1

# Annuler un commit spécifique avec un nouveau commit
git revert <commit-hash>

# Forcer le push (à utiliser avec prudence)
git push --force

# Lister les worktrees
git worktree list

# Supprimer un worktree
git worktree remove <chemin>
```

## 📝 Ressources supplémentaires

- [Documentation officielle Git Revert](https://git-scm.com/docs/git-revert)
- [Documentation officielle Git Reset](https://git-scm.com/docs/git-reset)
- [Guide sur les opérations dangereuses avec Git](https://git-scm.com/book/en/v2/Git-Branching-Rewriting-History)
- [Meilleures pratiques pour les équipes](https://www.atlassian.com/git/tutorials/undoing-changes)

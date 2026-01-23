# Contribution

Bienvenue dans l’équipe Test ! Voici quelques lignes directrices pour vous aider a démarrer.

## Processus de Pull Request

1. Assurez-vous que toutes les dépendances ou fichiers génères sont supprimes ou ignores avant de créer un commit.
2. Les commits doivent suivre les [conventions de commit](https://www.conventionalcommits.org/en/v1.0.0/#summary) ([types de commit pris en charge](commitlintrc.yml)).
3. Mettez a jour la documentation avec les details des modifications apportées a la fonctionnalité, y compris pour toute nouvelle fonctionnalité ou segment important.
4. Les Pull Requests sont fusionnées une fois que tous les tests passent et qu’un mainteneur du projet a approuvé la PR.

## Development local

> [tip]
> Pour une meilleure organisation, nous recommandons d'utiliser les **worktrees Git** plutôt que les branches traditionnelles. Consultez notre guide : [Utilisation des Worktrees](../conventions/worktree_usage.md)

Les libraries python sont définies dans [pyproject.toml].

Pour initialiser l'environnement de dev. Placez vous dans le dossier avec un shell powershell.
Puis executer le commande suivante

```pwsh
uv run just set-up install-dev
```

### Execution des tests automatiques

Executer la commande suivante

```pwsh
uv just run test
```

### Commit des fichiers depuis VSCode

Cliquer sur le bouton, puis suivre les instructions à l'écran.
![Commit depuis Vscode](docs/_static/vscode_commit.png)

### Ressources utiles

[cc]: https://www.conventionalcommits.org/en/v1.0.0/#summary
[cc-types]: .commitlintrc.yml
[pyproject.toml]: pyproject.toml

# Global configuration
# =========================================

# Cross platform shebang:
shebang := if os() == 'windows' {
  'powershell.exe'
} else {
  '/usr/bin/env pwsh'
}

# Use PowerShell everywhere
set windows-shell := ["powershell.exe", "-NoLogo", "-NoProfile", "-Command"]

@_:
    just --list

# =========================================
# Utils
# =========================================

# Display comments with colors
[group("utils")]
banner MESSAGE:
    #!{{shebang}}
    Write-Host '===============================' -ForegroundColor DarkBlue;
    Write-Host '{{MESSAGE}}' -ForegroundColor DarkBlue;
    Write-Host '===============================' -ForegroundColor DarkBlue;



# =========================================
# Lifecycle (common to all users)
# =========================================

# Premiere installation des outils
[group("lifecycle")]
set-up:
    @just banner "Installation des outils systeme"

    @just banner "Installation de uv"
    -irm https://astral.sh/uv/install.ps1 | iex

    @just banner "Installation de Node.js"
    -winget install -e --id OpenJS.NodeJS.LTS --scope user --silent --source winget

    @just banner "Installation de OpenJDK"
    -winget install openjdk --scope user --silent --source winget

    @just banner "Installation de Allure Commandline"
    -npm install -g allure-commandline

    @just banner "Installation de biomejs"
    -npm i -D -E @biomejs/biome


# Install les library pour un utilisateur
[group("lifecycle")]
install:
    @just banner "Installation des dependances runtime"
    uv sync --no-dev
    uv run rfbrowser install chromium
    uv run rfbrowser install firefox


# Mise a jour des library
[group("lifecycle")]
update:
    @just banner "Mis a jour de uv ..."
    uv self update
    @just banner "Mise a jour des dependances python"
    uv sync --upgrade --no-dev
    @just banner "Clean node"
    uv run rfbrowser clean-node
    @just banner "Mise a jour de chromium"
    uv run rfbrowser install chromium
    @just banner "Mise a jour de firefox"
    uv run rfbrowser install firefox
    @just banner "Mise a jour de npm"

    @just banner "Mise a jour de allure"
    npm update -g allure-commandline


# Suppression des fichiers temporaires
[group("lifecycle")]
clean:
    @just banner "Suppression du dossier .venv ..."
    powershell -NoProfile -Command " \
        if (Test-Path './.venv') { \
            Remove-Item -Recurse -Force './.venv'; \
            Write-Host 'Dossier supprime.' -ForegroundColor Green; \
        } else { \
            Write-Host 'Dossier non trouve.' -ForegroundColor Yellow; \
        }"


# Recreate project virtualenv from nothing
[group("lifecycle")]
fresh: set-up clean install


# =========================================
# Dev (réservé aux développeurs)
# =========================================

# Install les library de dev
[group("dev")]
install-dev:
    @just banner "Installation des dependances DEV"
    uv sync --all-groups -U
    @just banner "Clean node"
    uv run rfbrowser clean-node
    @just banner "Mise a jour de chromium"
    uv run rfbrowser install chromium
    @just banner "Mise a jour de firefox"
    uv run rfbrowser install firefox
    @just banner "Mise a jour de npm"

    @just banner "Mise a jour de allure"
    npm update -g allure-commandline

    @just banner "Installation des hooks de pre-commit"
    uv run prek install

# Mise a jour des library de dev
[group("dev")]
update-dev:
    @just banner "Mis a jour de uv ..."
    uv self update
    @just banner "Mise a jour des dependances DEV"
    uv sync --upgrade
    uv run rfbrowser clean-node
    uv run rfbrowser install chromium firefox
    npm update -g allure-commandline

# Lancer chrome en mode debug
[group("dev")]
start-chrome-debug:
    @just banner "Lancement de chrome en mode debug pour dev un test sur page web existante voir /debug/debug.robot"
    Start-Process chrome.exe -ArgumentList "--remote-debugging-port=9222", "--user-data-dir=$env:TEMP\chrome-robot-debug", "--no-first-run", "--no-default-browser-check", "--start-maximized", "--ignoreHTTPSErrors"

# =========================================
# QA
# =========================================

# Run tests
[group("qa")]
test:
    @just banner "Lancement des tests"
    -uv run robot \
    --listener allure_robotframework \
    ./tests

    @just banner "Generation du rapport des tests"
    -allure generate output/allure \
    --lang fr \
    --single-file \
    --clean

    @just banner "Ouverture du rapport"
    -allure open


# Run linters
[group("qa")]
lint:
    @just banner "Analyse et formatage Robot Framework"
    uv run robocop check
    uv run robocop format


# =========================================
# Playwright
# =========================================

# Commande pour lancer playwright codegen avec Chromium et ignorer les erreurs HTTPS
[group("playwright")]
codegen url:
    -uv run playwright codegen \
    --browser=chromium \
    --ignore-https-errors \
    --lang "fr-FR" \
    {{url}}

# =========================================
# Documentation (réservé aux developpeurs)
# =========================================

# Commande pour ouvrir la documentation en local
[group("documentation")]
doc-serve:
    -uv run mkdocs serve

# Commande pour construire la documentation
[group("documentation")]
doc-build:
    -uv run mkdocs build

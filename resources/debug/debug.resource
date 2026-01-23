*** Settings ***
Documentation
...                 Test case use Chrome Debug (CDP)

Library             Browser    auto_closing_level=KEEP

*** Variables ***
${CHROME_DEBUG_URL} =       http://localhost:9222

*** Keywords ***
Se Connecter Au Chrome Debug
    [Documentation]    Connexion au Chrome lancé en mode debug
    [Arguments]    ${url}=${CHROME_DEBUG_URL}

    TRY
        Connect To Browser    ${url}    use_cdp=${True}
        Log    ✓ Connecté à Chrome Debug sur ${url}
    EXCEPT    AS    ${error}
        Log    ❌ Chrome Debug non disponible. Lancez d'abord:    WARN
        Log    just chrome-local    WARN
        Log    ou: uv run start_chrome_debug.py local    WARN
        Fatal Error    ${error}
    END

Aller Vers
    [Documentation]    Navigation vers une page (utilise New Page avec Chrome Debug)
    [Arguments]    ${url}

    New Page    ${url}
    Log    ✓ Page ouverte: ${url}

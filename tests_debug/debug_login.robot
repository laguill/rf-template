*** Settings ***
Documentation       Test de debug pour la page de login
...                 Prérequis: Chrome Debug lancé avec 'just chrome-local'

Resource            ../resources/debug/debug.resource

Test Setup          Se Connecter Au Chrome Debug

*** Variables ***
${BASE_URL} =       https://exemple.com

*** Test Cases ***
Debug - Workflow complet
    [Documentation]    Test d'un workflow complet avec pauses
    [Tags]    debug    workflow

    # Navigation initiale
    Aller Vers    ${BASE_URL}

    # Étape 1 - Login
    Fill Text    id=txtLogin    txt=root
    Click    id=btnConnexion

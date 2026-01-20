*** Settings ***
Library             Browser    auto_closing_level=KEEP

Suite Teardown      No Operation

*** Variables ***
${BROWSER} =        chromium
${HEADLESS} =       False
${URL} =            https://exemple.com

*** Test Cases ***
Connexion Au Compte
    Fill Text    id=txtLogin    txt=root
    Click    id=btnConnexion

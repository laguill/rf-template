*** Settings ***
Library             Browser    auto_closing_level=KEEP

Suite Setup         Open Site
Suite Teardown      No Operation

*** Variables ***
${BROWSER} =        chromium
${HEADLESS} =       False
${URL} =            https://exemple.com

*** Test Cases ***
Connexion Au Compte
    Fill Text    id=txtLogin    txt=root
    Click    id=btnConnexion

*** Keywords ***
Connect To Existing Browser
    Connect To Browser    ws://127.0.0.1:2026/chromium/1
    New Context
    New Page    https://example.com

Open Site
    [Documentation]
    ...    1. Open Chrome en mode headless
    ...    2. Open new tab/window.
    ...    3. Change browser window size to 1800x720 taille minimal supportée par site
    ...    4. navigate to ${URL}
    Log To Console    Accès au site : ${URL}
    New Browser    browser=${BROWSER}    headless=${HEADLESS}
    New Context    ignoreHTTPSErrors=True    viewport={'width':1800, 'height':720}
    New Page    ${URL}

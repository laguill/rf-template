*** Settings ***
Library     Browser    auto_closing_level=KEEP

*** Test Cases ***
Mon Test Iteratif
    Connect To Browser    http://localhost:9222    use_cdp=${True}
    # Pas besoin de New Page ou Go To, vous utilisez la page déjà ouverte !

    # Vos tests ici
    Fill Text    id=txtLogin    txt=root
    Click    id=btnConnexion

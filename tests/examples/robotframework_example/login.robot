*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${LOGIN_URL}    http://localhost:8000/login
${USERNAME}     testuser
${PASSWORD}     password123
${DASHBOARD_SELECTOR}    css:div.dashboard-header

*** Test Cases ***
Successful Klubster Login
    [Documentation]    Test login and dashboard for Klubster
    Open Browser    ${LOGIN_URL}    Chrome
    Maximize Browser Window
    Wait Until Page Contains Element    name=username    10s
    Input Text    name=username    ${USERNAME}
    Input Text    name=password    ${PASSWORD}
    Click Button    id=login-btn
    Wait Until Page Contains Element    ${DASHBOARD_SELECTOR}    10s
    Element Should Be Visible    ${DASHBOARD_SELECTOR}
    Title Should Contain    Dashboard
    [Teardown]    Close Browser

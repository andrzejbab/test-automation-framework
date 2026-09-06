*** Settings ***
Library    SeleniumLibrary
Resource   pages.resource

*** Variables ***
${LOGIN_URL}    http://localhost:8000/login
${USERNAME}     testuser
${PASSWORD}     password123

*** Test Cases ***
Successful Klubster Login With POM
    [Documentation]    Test login and dashboard for Klubster using Page Object Model
    Open Browser    ${LOGIN_URL}    Chrome
    Maximize Browser Window
    Login Page Should Be Open
    Login With Credentials    ${USERNAME}    ${PASSWORD}
    Dashboard Should Be Visible
    [Teardown]    Close Browser

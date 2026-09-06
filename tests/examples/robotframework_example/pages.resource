*** Keywords ***
Login Page Should Be Open
    Wait Until Page Contains Element    name=username    10s
    Element Should Be Visible    name=username

Login With Credentials
    [Arguments]    ${username}    ${password}
    Input Text    name=username    ${username}
    Input Text    name=password    ${password}
    Click Button    id=login-btn

Dashboard Should Be Visible
    Wait Until Page Contains Element    css:div.dashboard-header    10s
    Element Should Be Visible    css:div.dashboard-header
    Title Should Contain    Dashboard

# test-automation-framework
Comprehensive QA automation suite for a containerized SaaS platform. Features black-box testing including UI automation (Selenium), property-based API testing (Schemathesis/Swagger), and test orchestration Pytest

# SaaS Automation Testing Framework

This repository demonstrates a complete, black-box quality assurance pipeline for a containerized SaaS application. The framework executes automated API validation and End-to-End (E2E) UI testing against isolated Docker environments.

## Tech Stack & Tooling

| Technology | Category | Purpose |
| :--- | :--- | :--- |
| **Selenium** | UI Automation | Cross-browser End-to-End testing of user workflows. |
| **Schemathesis** | API Testing | Property-based testing relying on the OpenAPI/Swagger specification. |
| **Pytest** | Test Runner | Execution and orchestration of Python-based test scripts. |
| **JUnit** | Test Runner / Reporting | Java-based test execution and standardized XML report generation. |
| **Docker** | Orchestration | Provisioning the isolated frontend and backend SaaS packages. |

## Test Scope

*   **Property-Based API Testing:** Automated generation of test cases using **Schemathesis** against the backend's **Swagger** documentation to ensure robust endpoint contracts.
*   **UI End-to-End Testing:** Simulated user interactions and critical path validations on the frontend using **Selenium WebDriver**.
*   **Continuous Integration:** Headless execution within GitHub Actions, pulling private Docker packages securely to run the test matrix.

## Getting Started


### Runner ###
From root workpace:
    python3 -m venv tests/venv
    source tests/venv/bin/activate
    pip install --upgrade pip
    pip install -r tests/requirements.txt

Verify:
    which python
    python -m pytest --version

Select the interpreter in VS Code
    -> Open Command Palette with Ctrl+Shift+P:
    -> Python: Select Interpreter
    -> path to python

## Feature: Files open in new tab VS Code ##
Press Ctrl+Shift+P
Select Preferences: Open User Settings (JSON)
Add:
"workbench.editor.enablePreview": false,
"workbench.editor.enablePreviewFromQuickOpen": false


### Start test target ####
docker compose pull
docker compose up

### UI test requirement ##
Test on unbuntu -> browser must be installed(chrome or firefox)
sudo apt-get update
sudo apt-get install -y chromium chromium-driver

wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get update
sudo apt-get install -y ./google-chrome-stable_current_amd64.deb
google-chrome --version

### Tests run (for UI test only in mode headless=true) ###
-> all tests:
    pytests tests/
-> api tests
    pytest tests/api
-> ui tests
    pytest tests/ui


## Test run with visible browser window in Codespace via VNC -> developer debug + Testing VS Code in mode headless=false##
1. Install a virtual display, lightweight window manager, VNC server, and browser-based VNC client:
    sudo apt-get install -y xvfb x11vnc fluxbox novnc

2. Start the virtual desktop(in terminal):
    Xvfb :99 -screen 0 1920x1080x24 &
    export DISPLAY=:99
    fluxbox >/tmp/fluxbox.log 2>&1 &
    x11vnc -display :99 -forever -shared -rfbport 5900 -nopw >/tmp/x11vnc.log 2>&1 &
    /usr/share/novnc/utils/novnc_proxy --vnc localhost:5900 --listen 6080 >/tmp/novnc.log 2>&1 &

3. Navigate to:
    http://localhost:6080/vnc.html
    Click Connect

4. Run tests options for UI Tests:
    1. Terminal:
        export DISPLAY=:99
        export CHROME_BINARY=/usr/bin/google-chrome
        export UI_HEADLESS=false
        pytest tests/ui -m ui --ui-headless false
        pytest tests/ui -k "test_login_logout" --ui-headless false

    2. Run tests with "Testing" Panel (UI over VNC from Github codespace):
        Add VNC variables to venv file example:
        UI_HEADLESS=false
        DISPLAY=:99
        CHROME_BINARY=/usr/bin/google-chrome
        PYTHONPATH=/workspaces/Klubster 

    3. Run tests with "Run and Debug" (UI over VNC from Github codespace)
        Open Run and Debug, select Run Pytest.
        Current configuration runs all tests:
            "args": [
                "tests",
                "-s"
            ]

5. Results:
    /test/allure_results
    install allure:
    npm install -g allure-commandline

    local:
    allure serve tests/allure-results

    codespace:
    allure generate tests/allure-results -o allure-report --clean
    python3 -m http.server 8001 --directory allure-report


# Test env variables
-> Create env in root directory with following envs:

TEST_API_ADMIN_USERNAME="example admin"
TEST_API_ADMIN_PASSWORD=1234567
TEST_API_BASE_URL=http://127.0.0.1:8000/
MAILPIT_HOST = http://127.0.0.1:8025/
UI_BROWSER=firefox
UI_HEADLESS=true
TEST_UI_BASE_URL=http://127.0.0.1:3000/

# For browser use if headless = false for debug needed
UI_HEADLESS=false
DISPLAY=:99
CHROME_BINARY=/usr/bin/google-chrome
PYTHONPATH=/workspaces/Klubster


## License
MIT

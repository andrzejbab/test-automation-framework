# test-automation-framework
Comprehensive QA automation suite for a containerized SaaS platform. Features black-box testing including UI automation (Selenium), property-based API testing (Schemathesis/Swagger), and test orchestration Pytest

# SaaS Automation Testing Framework

This repository demonstrates a complete, black-box quality assurance pipeline for a containerized SaaS application. The framework executes automated API validation and End-to-End (E2E) UI testing against isolated Docker environments. It is designed to run locally or seamlessly within GitHub Codespaces, featuring advanced visual debugging over VNC.

## Tech Stack & Tooling

| Technology | Category | Purpose |
| :--- | :--- | :--- |
| **Selenium** | UI Automation | Cross-browser End-to-End testing of user workflows. |
| **Schemathesis** | API Testing | Property-based testing relying on the OpenAPI/Swagger specification. |
| **Pytest** | Test Runner | Execution and orchestration of Python-based test scripts. |
| **Docker** | Orchestration | Provisioning the isolated frontend and backend SaaS packages. |

## Test Scope

*   **Property-Based API Testing:** Automated generation of test cases using **Schemathesis** against the backend's **Swagger** documentation to ensure robust endpoint contracts.
*   **UI End-to-End Testing:** Simulated user interactions and critical path validations on the frontend using **Selenium WebDriver**.
*   **Continuous Integration:** Headless execution within GitHub Actions, pulling private Docker packages securely to run the test matrix.

## Getting Started

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
* Docker & Docker Compose (to run the target application)
* Python 3.x
* Node.js & npm (for generating Allure reports)

---

## 🚀 Getting Started

### 1. Configure Environment Variables
Create a .env file in the root directory and add the following configurations:

#Frontend
REACT_APP_API_HOST=https://fluffy-potato-v67j9r6g9w4x3x7j6-8000.app.github.dev
REACT_APP_FRONTEND_HOST=https://fluffy-potato-v67j9r6g9w4x3x7j6-3000.app.github.dev

#Backend
SECRET_KEY=@9r-o=5(%2#b=y3fht1ndf1tc*!1(bfwyc8h-nb8s)ob+v741+
BACKEND_HOST=https://fluffy-potato-v67j9r6g9w4x3x7j6-8000.app.github.dev
FRONTEND_HOST=https://fluffy-potato-v67j9r6g9w4x3x7j6-3000.app.github.dev
ALLOWED_HOSTS=fluffy-potato-v67j9r6g9w4x3x7j6-8000.app.github.dev,localhost,127.0.0.1

#Set admin for django db
DJANGO_ADMIN_USER=admin
DJANGO_ADMIN_EMAIL=admin@local.local
DJANGO_ADMIN_PASSWORD=1234567

#Tests
TEST_API_BASE_URL=http://127.0.0.1:8000/
TEST_API_ADMIN_USERNAME="example admin"
TEST_API_ADMIN_PASSWORD=1234567
MAILPIT_HOST=http://127.0.0.1:8025/
TEST_UI_BASE_URL=http://127.0.0.1:3000/
UI_BROWSER=chrome
UI_HEADLESS=true


### 2. Start the Target Application
Pull and spin up the required services for the test environment:

docker compose -f docker-compose-pull.yml pull
docker compose -f docker-compose-pull.yml up -d


### 3. Setup Python Virtual Environment
Initialize your environment and install dependencies:

python3 -m venv tests/venv
source tests/venv/bin/activate
pip install --upgrade pip
pip install -r tests/requirements.txt

Verify installation: python -m pytest --version


### 4. Install Browsers (Ubuntu/Linux)
UI tests require a browser to be installed. Run the following to install Chromium and Google Chrome:

sudo apt-get update
sudo apt-get install -y chromium chromium-driver

wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get install -y ./google-chrome-stable_current_amd64.deb
google-chrome --version

---

## 🏃‍♂️ Running Tests

By default, UI tests run in headless mode. Make sure your virtual environment is activated.

* Run all tests:
  pytest tests/

* Run API tests only:
  pytest tests/api

* Run UI tests only:
  pytest tests/ui

---

## 📊 Test Reporting (Allure)

Test results are saved in tests/allure-results. To view them, install the Allure command-line tool:

npm install -g allure-commandline


Viewing locally:
allure serve tests/allure-results


Viewing in Codespaces / Remote servers:
allure generate tests/allure-results -o allure-report --clean
python3 -m http.server 8001 --directory allure-report

(Then, open the forwarded port 8001 in your browser.)

---

## 🛠️ Advanced: Visual Debugging via VNC (Codespaces)

When developing in GitHub Codespaces, you can run UI tests with a visible browser window (headless=false) by routing the display through a virtual VNC server.

### 1. Install Dependencies
sudo apt-get install -y xvfb x11vnc fluxbox novnc


### 2. Start the Virtual Desktop
Run these commands in your terminal to initialize the display:

Xvfb :99 -screen 0 1920x1080x24 &
export DISPLAY=:99
fluxbox >/tmp/fluxbox.log 2>&1 &
x11vnc -display :99 -forever -shared -rfbport 5900 -nopw >/tmp/x11vnc.log 2>&1 &
/usr/share/novnc/utils/novnc_proxy --vnc localhost:5900 --listen 6080 >/tmp/novnc.log 2>&1 &


### 3. Connect to VNC
* Open your browser and navigate to: http://localhost:6080/vnc.html
* Click Connect.


### 4. Run UI Tests Visually
To execute tests and watch them run in your VNC window, export the display variables and override the headless flag:

export DISPLAY=:99
export CHROME_BINARY=/usr/bin/google-chrome
pytest tests/ui -m ui --ui-headless false

(Alternatively, you can append UI_HEADLESS=false and DISPLAY=:99 to your .env file for use with the VS Code "Testing" panel).

---

## 💻 VS Code Configuration Tips

1. Select the correct interpreter:
* Press Ctrl+Shift+P -> Type Python: Select Interpreter
* Choose the path to ./tests/venv/bin/python

2. Prevent files from opening in preview tabs:
* Press Ctrl+Shift+P -> Type Preferences: Open User Settings (JSON)
* Add these lines to your settings:
  "workbench.editor.enablePreview": false,
  "workbench.editor.enablePreviewFromQuickOpen": false

---

## 📄 License
This project is licensed under the MIT License.

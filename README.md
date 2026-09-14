# Test Automation Framework

All automated test cases in this project are executed through a GitHub-based CI pipeline, enabling repeatable, version-controlled test runs in the cloud without requiring local orchestration for every execution.

A comprehensive QA automation suite for a containerized SaaS platform. This project combines black-box UI automation with API contract validation and test orchestration to provide end-to-end quality coverage for modern web applications.

## Run in GitHub without installing locally

You can start and run this project directly in GitHub without installing dependencies on your machine:

### Option 1: Use GitHub Codespaces

1. Open the repository in GitHub.
2. Click the `Code` button.
3. Select `Codespaces` and create a new codespace.
4. Once the environment is ready, the repository is already mounted in a preconfigured dev environment.
5. Start the app and run the tests from the terminal inside the codespace.

### Option 2: Use GitHub Actions

1. Push your branch to GitHub.
2. Open the repository's `Actions` tab.
3. Select the workflow for test execution.
4. Run the workflow manually or let it trigger automatically on pushes and pull requests.
5. Review the test logs and artifacts directly in the GitHub UI.

This approach is ideal for CI validation, remote collaboration, and environments where local setup is not required.

## Overview

This repository demonstrates a complete automation pipeline for a SaaS product deployed in isolated Docker environments. It validates:

- API behavior using OpenAPI/Swagger-driven property-based testing
- End-to-end user flows using Selenium UI automation
- Test execution and reporting with Pytest and Allure
- Local and remote execution in GitHub Codespaces or Dockerized environments

## Tech Stack

| Technology | Category | Purpose |
| :--- | :--- | :--- |
| Pytest | Test runner | Orchestrates test execution and integration with fixtures |
| Selenium | UI automation | Automates browser interactions for E2E validation |
| Schemathesis | API testing | Generates property-based API tests from OpenAPI specs |
| Docker | Environment orchestration | Runs the app and dependencies in isolated containers |
| Allure | Reporting | Produces rich HTML reports for test outcomes |

## Test Scope

- Property-based API testing using Schemathesis against the backend Swagger/OpenAPI schema
- End-to-end UI validation for user journeys and critical flows
- CI-friendly execution with headless browser support and report generation
- Visual debugging support using VNC for local and remote development workflows

## Prerequisites

Before starting, ensure the following tools are installed:

- Docker and Docker Compose
- Python 3.x
- Node.js and npm
- Git

## Environment Setup

Create a `.env` file in the project root with the following values:

```env
# Frontend
REACT_APP_API_HOST=http://127.0.0.1:8000/
REACT_APP_FRONTEND_HOST=http://127.0.0.1:3000/

# Backend
SECRET_KEY=your_secret_key
BACKEND_HOST=http://127.0.0.1:8000/
FRONTEND_HOST=http://127.0.0.1:3000/
ALLOWED_HOSTS=localhost,127.0.0.1
DJANGO_ADMIN_USER=your_admin
DJANGO_ADMIN_EMAIL=your_admin@local.local
DJANGO_ADMIN_PASSWORD=your_password

# Tests
TEST_API_BASE_URL=http://127.0.0.1:8000/
TEST_API_ADMIN_USERNAME=your_admin
TEST_API_ADMIN_PASSWORD=your_password
MAILPIT_HOST=http://127.0.0.1:8025/
TEST_UI_BASE_URL=http://127.0.0.1:3000/
UI_BROWSER=chrome
UI_HEADLESS=true
```

## Getting Started

### 1) Start the target application

Pull the Docker images and start the app stack:

```bash
export GITHUB_TOKEN="token_here"
echo "$GITHUB_TOKEN" | docker login ghcr.io -u github_username --password-stdin
docker compose -f docker-compose-pull.yml pull
docker compose -f docker-compose-pull.yml up -d
```

### 2) Set up a Python virtual environment

```bash
python3 -m venv tests/venv
source tests/venv/bin/activate
pip install --upgrade pip
pip install -r tests/requirements.txt
```

Verify that Pytest is installed correctly:

```bash
python -m pytest --version
```

### 3) Install browser dependencies

For Linux-based UI testing, install Chromium and Google Chrome:

```bash
sudo apt-get update
sudo apt-get install -y chromium chromium-driver
wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get install -y ./google-chrome-stable_current_amd64.deb
google-chrome --version
```

## Running Tests

Make sure your virtual environment is active before running the suite.

### Run all tests

```bash
pytest -m "api or ui"
```

### Run API tests only

```bash
pytest -m "api"
```

### Run UI tests only

```bash
pytest -m "ui"
```

## Test Reporting with Allure

Test results are stored in `tests/allure-results`.

Install Allure CLI:

```bash
npm install -g allure-commandline
```

View the report locally:

```bash
allure serve tests/allure-results
```

Generate a static report on a remote or Codespace environment:

```bash
allure generate tests/allure-results -o allure-report --clean
python3 -m http.server 8001 --directory allure-report
```

Then open the forwarded port `8001` in your browser.

## Visual Debugging with VNC

When working in GitHub Codespaces or remote environments, you can run UI tests with a visible browser window by exposing a virtual desktop.

For development / debugging with Codespace install extensions:  "Python Debugger", "Python", "Pylance" on your codespace

### 1) Install VNC dependencies

```bash
sudo apt-get install -y xvfb x11vnc fluxbox novnc
```

### 2) Start the virtual desktop

```bash
Xvfb :99 -screen 0 1920x1080x24 &
export DISPLAY=:99
fluxbox >/tmp/fluxbox.log 2>&1 &
x11vnc -display :99 -forever -shared -rfbport 5900 -nopw >/tmp/x11vnc.log 2>&1 &
/usr/share/novnc/utils/novnc_proxy --vnc localhost:5900 --listen 6080 >/tmp/novnc.log 2>&1 &
```

### 3) Connect to the browser session

Open:

```text
http://localhost:6080/vnc.html
```

Then click Connect.

### 4) Run UI tests visually

```bash
export DISPLAY=:99
export CHROME_BINARY=/usr/bin/google-chrome
pytest tests/ui -m ui --ui-headless false
```

You can also set `UI_HEADLESS=false` and `DISPLAY=:99` in your `.env` file for use with the VS Code testing panel.

## VS Code Configuration Tips

1. Select the correct Python interpreter:
   - Press `Ctrl+Shift+P`
   - Run `Python: Select Interpreter`
   - Choose `./tests/venv/bin/python`

2. Disable preview tab behavior for files:
   - Press `Ctrl+Shift+P`
   - Open `Preferences: Open User Settings (JSON)`
   - Add:

```json
{
  "workbench.editor.enablePreview": false,
  "workbench.editor.enablePreviewFromQuickOpen": false
}
```


## License

This project is licensed under the MIT License.

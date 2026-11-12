# Test Automation Framework

A comprehensive QA automation suite for a containerized SaaS platform. This project combines black-box UI automation with API contract validation and test orchestration to provide end-to-end quality coverage for modern web applications.

All automated test cases in this project are executed through a GitHub-based CI pipeline, enabling repeatable, version-controlled test runs in the cloud without requiring local orchestration for every execution.

## Overview

This repository demonstrates a complete automation pipeline for a SaaS product deployed in isolated Docker environments. It validates:

- Contract and REST API validation using OpenAPI/Swagger-driven testing
- End-to-end user flows using Selenium UI automation
- Application performance under load using JMeter load testing
- Test execution and reporting with Pytest and Allure
- Local and remote execution in GitHub Codespaces or Dockerized environments

## Tech Stack

| Technology | Category | Purpose |
| :--- | :--- | :--- |
| Pytest | Test runner | Orchestrates test execution and integration with fixtures |
| Selenium | UI automation | Automates browser interactions for E2E validation |
| Schemathesis | API testing | Generates property-based API tests from OpenAPI specs |
| SQLAlchemy | Database toolkit | Manages database engines and sessions and executes SQL queries |
| Docker | Environment orchestration | Runs the app and dependencies in isolated containers |
| Taurus | Orchestration | Coordinates and executes JMeter test plans with configurable load profiles and reusable test configuration |
| JMeter | Load testing | Generates realistic user traffic and measures application performance under load |
| Allure | Reporting | Produces rich HTML reports for test outcomes |


## Test Scope

- Property-based API testing using Schemathesis against the backend Swagger/OpenAPI schema
- End-to-end UI validation for user journeys and critical flows
- Load testing with JMeter to measure application performance and identify bottlenecks
- CI-friendly execution with headless browser support and report generation
- Visual debugging support using VNC for local and remote development workflows



## Environment Setup for GitHub Actions CI

The CI pipeline reads configuration from GitHub Actions secrets and variables.Values are injected into the test environment and Docker Compose configuration before the application stack and test suites are started.

Required GitHub Actions configuration:
- `GHCR_PAT` — GitHub Container Registry token used to pull the required Docker images(test target).

Recommended GitHub secrets:
- `SECRET_KEY`
- `DJANGO_ADMIN_USER`
- `DJANGO_ADMIN_EMAIL`
- `DJANGO_ADMIN_PASSWORD`
- `POSTGRES_DB`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_HOST`
- `POSTGRES_PORT`

Recommended GitHub variables:
- `BACKEND_HOST`
- `FRONTEND_HOST`
- `ALLOWED_HOSTS`
- `REACT_APP_FRONTEND_HOST`
- `TEST_API_BASE_URL`
- `TEST_UI_BASE_URL`
- `MAILPIT_HOST`
- `UI_BROWSER`
- `UI_HEADLESS`
- `MOBILE`
- `VUSERS`
- `RAMPUP`
- `HOLDFOR`

If a secret or variable is not defined, the workflow falls back to local development defaults such as `http://localhost:8000` and `http://localhost:3000`.

 CI default configuration:

```bash
# Postgres
POSTGRES_DB=db_test
POSTGRES_USER=db_test
POSTGRES_PASSWORD=strong-database-password
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

# GitHub Secrets
GHCR_PAT=your_github_token
SECRET_KEY=test_secret_1234567
DJANGO_ADMIN_USER=test_admin
DJANGO_ADMIN_EMAIL=your_admin@local.local
DJANGO_ADMIN_PASSWORD=test_admin_pass_1234567

# GitHub Variables
BACKEND_HOST=http://localhost:8000
FRONTEND_HOST=http://localhost:3000
ALLOWED_HOSTS=localhost,127.0.0.1
REACT_APP_FRONTEND_HOST=http://localhost:3000

# Test environment
TEST_API_ADMIN_USERNAME=test_admin
TEST_API_ADMIN_PASSWORD=test_admin_pass_1234567
TEST_API_BASE_URL=http://localhost:8000/
TEST_UI_BASE_URL=http://localhost:3000/
MAILPIT_HOST=http://localhost:8025
UI_BROWSER=chrome
UI_HEADLESS=true
MOBILE=false
VUSERS=2
RAMPUP=3s
HOLDFOR=20s
```

The workflow creates a `.env` file automatically at runtime from these values, which is then used by Docker Compose and the test suite.

To start the CI workflow, push a commit to a branch or open a pull request in the repository. GitHub Actions will automatically trigger the pipeline and execute the contract, API, UI, and load tests in sequence.

## Environment Setup

This setup was tested locally on Ubuntu and GitHub Codespaces.

Before starting, ensure the following tools are installed:

- Docker Engine with the Docker Compose plugin
- Git

Python, the browser, Java, JMeter, and Allure CLI are installed in the test-runner image; they do not need to be installed on the host.
The runner targets `linux/amd64`; Docker uses emulation on ARM computers, which may run more slowly.

Create a `.env` file in the project root with the values required to start the application. The test runner uses Compose service names for the API, UI, database, and Mailpit, so the localhost URLs in this example are for host-based access and are overridden inside the test container.

When working in a browser-accessible environment such as GitHub Codespaces, the application is typically exposed through a proxy HTTPS endpoint rather than `localhost`. In those cases, use the generated Codespace URL instead of the local host address.

Example URLs:
- Local: `http://127.0.0.1:8000`
- Codespace: `https://<hash>-8000.app.github.dev`

```env
# Postgres
POSTGRES_DB=db_test
POSTGRES_USER=db_test
POSTGRES_PASSWORD=strong-database-password
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

# Target application
REACT_APP_API_HOST=http://127.0.0.1:8000
REACT_APP_FRONTEND_HOST=http://127.0.0.1:3000
BACKEND_HOST=http://127.0.0.1:8000
FRONTEND_HOST=http://127.0.0.1:3000
ALLOWED_HOSTS=localhost,127.0.0.1, ,https://<hash>-8000.app.github.dev,https://<hash>-3000.app.github.dev
SECRET_KEY=your_secret_key
DJANGO_ADMIN_USER=test_admin
DJANGO_ADMIN_EMAIL=your_admin@local.local
DJANGO_ADMIN_PASSWORD=test_admin_pass_1234567

# Functional tests
TEST_API_BASE_URL=http://127.0.0.1:8000
TEST_API_ADMIN_USERNAME=test_admin
TEST_API_ADMIN_PASSWORD=test_admin_pass_1234567
# Optional credentials for mock authentication with --use-mock-client
TEST_API_USERNAME=test_admin
TEST_API_PASSWORD=test_admin_pass_1234567
MAILPIT_HOST=http://127.0.0.1:8025
TEST_UI_BASE_URL=http://127.0.0.1:3000
UI_BROWSER=chrome
# The Docker test runner uses headless Chrome
UI_HEADLESS=true
MOBILE=false

# JMeter
VUSERS=2
RAMPUP=3s
HOLDFOR=20s
```

### Optional CLI overrides

The values above are the default environment settings used by the suite, but they can be overridden at runtime with pytest CLI options. CLI flags take precedence over the matching environment variables.

| Environment variable | Pytest CLI option |
| :--- | :--- |
| `TEST_API_BASE_URL` | `--api-base-url` |
| `TEST_API_ADMIN_USERNAME` | `--api-admin-username` |
| `TEST_API_ADMIN_PASSWORD` | `--api-admin-password` |
| `UI_BROWSER` | `--ui-browser` |
| `UI_HEADLESS` | `--ui-headless` |
| `TEST_UI_BASE_URL` | `--ui-base-url` |
| `MAILPIT_HOST` | `--api-mailpit-host` |
| `MOBILE` | `--mobile` |
| `VUSERS` | `--vusers` |
| `RAMPUP` | `--rampup` |
| `HOLDFOR` | `--holdfor` |
| `POSTGRES_DB` | `--postgres_db` |
| `POSTGRES_USER` | `--postgres_user` |
| `POSTGRES_PASSWORD` | `--postgres_password` |

Use `--use-mock-client` to force the shared API client to use the mock client. For mock token authentication, set `TEST_API_USERNAME` and `TEST_API_PASSWORD` to the expected credentials.

Example:

```bash
pytest -m "api or ui" \
  --api-base-url=http://127.0.0.1:8000 \
  --api-admin-username=admin \
  --api-admin-password=secret \
  --ui-browser=chrome \
  --ui-headless=true \
  --ui-base-url=http://127.0.0.1:3000
```

This is useful when you want to run the same suite against a different environment without changing the project `.env` file.

## Getting Started

### 1) Start the target application
The application designated for testing is a web-based Software as a Service (SaaS) solution for small sports club management ahead of its upcoming release.

If the application images are private, log in to GitHub Container Registry:

```bash
echo "$GITHUB_TOKEN" | docker login ghcr.io -u GITHUB_USERNAME --password-stdin
```

Pull and start the app, database, and Mailpit:

```bash
docker compose pull
docker compose up -d
```

### 2) Build the test runner

The first build installs the Python test requirements, Chrome, Java, JMeter, and Allure CLI:

```bash
docker compose build test-runner
```

### 3) Open a test-runner shell and run tests

The repository is mounted into the container at `/workspace`, so edits and generated reports remain on your computer. On Linux or macOS, pass your user ID to avoid root-owned output files:

```bash
LOCAL_UID="$(id -u)" LOCAL_GID="$(id -g)" \
  docker compose --profile test run --rm test-runner bash
```

The runner waits for the application, frontend, and Mailpit to respond before opening the shell. From inside it:

```bash
pytest -m "contract or api or ui"
```

The container sets the service URLs and database connection settings, so no host-specific URL overrides are needed. Headless Chrome is configured by default.

Run `exit` to leave the shell. Stop the app stack when finished with `docker compose down`; add `-v` only if you also want to delete the Postgres data volume.

### Use VS Code Test and Debug buttons

The repository includes a Dev Container configuration that connects VS Code to the test-runner container and starts the app dependencies.

On Linux, set `LOCAL_UID` and `LOCAL_GID` in the project `.env` file to the values printed by `id -u` and `id -g`. This lets the container write test reports and generated files as your host user. For example, if those commands print `1001` and `1001`, add:

```env
LOCAL_UID=1001
LOCAL_GID=1001
```

Then install the VS Code **Dev Containers** extension, open the repository folder, and run **Dev Containers: Reopen in Container** from the Command Palette. On first use, VS Code builds the test-runner image and starts the backend, frontend, Postgres, and Mailpit services. When setup completes:

- Open the Testing panel to discover and run pytest tests in the container.
- Use a test's **Debug Test** action to debug it in the container.
- Or open a test file and press `F5` to use the **Debug current pytest file** launch configuration.

The selected Python interpreter and installed test dependencies are inside the container; you do not need a local Python environment. The runner uses headless Chrome.

## Running Functional Testing

Run these commands inside the test-runner shell.

### Run all functional tests

```bash
pytest -m "contract or api or ui"
```

This runs the contract, API, and UI test groups. It does not include the Pydantic model-generation helper or the separate JMeter performance tests below.

### Run API Contract tests only

```bash
pytest -m "contract"
```

### Run API tests only

```bash
pytest -m "api"
```

### Run UI tests only

```bash
pytest -m "ui"
```

### Run the Pydantic model-generation helper

```bash
pytest tests/api/intern/test_create_pydantic_models.py
```

### Test Reporting with Allure

Pytest writes Allure results to `allure-results/` at the repository root. Generate a static report:

```bash
allure generate allure-results -o allure-report --clean
```

To view it without installing tools on the host, exit the shell and serve the generated report from the runner:

```bash
LOCAL_UID="$(id -u)" LOCAL_GID="$(id -g)" \
  docker compose --profile test run --rm --service-ports test-runner \
  python3 -m http.server 8001 --directory allure-report
```

Open `http://localhost:8001` in your browser.
## Running Non-Functional Testing

The load test configuration requires the following parameters to be defined:

- `concurrency`: number of concurrent virtual users (VUSERS in env file)
- `ramp-up`: duration required to reach the target concurrency level (RAMPUP in env file)
- `hold-for`: duration for which the target load is sustained (HOLDFOR in env file)
- TEST_API_BASE_URL in env file

```bash
#Start performance test
python -m bzt \
  -o settings.artifacts-dir="tests/jmeter-report" \
  -o modules.jmeter.path="$JMETER_HOME/bin/jmeter" \
  tests/performance/taurus_test_suite.yml
```



## Test Reporting JMeter

```bash
"$JMETER_HOME/bin/jmeter" -g "tests/jmeter-report/kpi.jtl" -o tests/jmeter-report/html
```

To view the report, exit the runner shell and start a server with its port published:

```bash
LOCAL_UID="$(id -u)" LOCAL_GID="$(id -g)" \
  docker compose --profile test run --rm --service-ports test-runner \
  python3 -m http.server 8001 --directory tests/jmeter-report
```

Open `http://localhost:8001/html/index.html`.

## DB Postgres

```
# see available docker container
docker ps

# connect to postgres in docker
docker exec -it <docker name> sh -c 'psql -U "$POSTGRES_USER" -d "$POSTGRES_DB"'

# connect to postgres on localhost
psql -h localhost -p 5432 -U "$POSTGRES_USER" -d "$POSTGRES_DB"

```


## Visual Debugging with VNC

This optional workflow runs UI tests with a visible browser. The Docker test runner uses headless Chrome by default; its image also includes Xvfb and VNC tools for visible runs.

When working in GitHub Codespaces or remote environments, you can run UI tests with a visible browser window by exposing a virtual desktop.

For development / debugging with Codespace install extensions:  "Python Debugger", "Python", "Pylance" on your codespace

### 1) Rebuild the test runner if needed

```bash
docker compose build test-runner
```

### 2) Run the visible UI tests

```bash
./scripts/run_ui_tests_no_headless.sh
```

The script starts a virtual desktop on display `:99` if one is not already running. In VS Code, open the forwarded port at:

```text
http://localhost:6080/vnc.html
```

Click **Connect** to view the browser. The VNC server uses the Xvfb display, so the startup script ignores any inherited `WAYLAND_DISPLAY` setting. Outside the Dev Container, publish or forward port `6080` to access noVNC.

### Open JMeter GUI with VNC
```bash
export DISPLAY=:99
export JMETER_HOME=/workspaces/test-automation-framework/apache-jmeter-5.6.3
export PATH="$JMETER_HOME/bin:$PATH"
jmeter
```
or use: __./scripts/start_jmeter_in_vnc.sh__

## VS Code Configuration Tips

1. When reopened in the Dev Container, VS Code uses `/usr/local/bin/python` from the test-runner image. If needed, use `Python: Select Interpreter` and choose that interpreter.

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

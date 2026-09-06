# Klubster Professional Testing Playbook (Step by Step)

This guide describes a practical, production-style strategy for testing Klubster backend and UI.

Goals:
- Backend contract testing based on generated OpenAPI schema
- API functional and integration tests with pytest
- UI end-to-end testing with Selenium (pytest)
- BDD scenarios with pytest-bdd (Cucumber style)
- Keyword-driven acceptance tests with Robot Framework
- Quality gates for CI/CD

---

## 1. Testing Architecture (What to test, with what)

Use a testing pyramid with contract-first backend validation.

1) Fast checks
- Linting, formatting, static checks
- Smoke API tests

2) API contract and behavior
- OpenAPI contract checks (Schemathesis + generated schema)
- Functional API tests with pytest
- Authentication, permissions, error cases

3) UI and user journeys
- Selenium + pytest Page Object tests
- BDD high-level scenarios (pytest-bdd)
- Robot Framework acceptance flows

4) Non-functional
- Performance/load (existing performance folder, JMeter if needed)

Recommended quality gate policy:
- Pull request: fast API tests + selected contract smoke + selected UI smoke
- Main branch/nightly: full API + broader contract fuzzing + full UI and BDD/Robot suites

---

## 2. Project baseline in Klubster

Existing helpful structure already in project:
- tests/openapi
- tests/api
- tests/ui
- tests/cucumber_example
- tests/robotframework_example
- pytest.ini with markers and CLI options

Use this guide to standardize and scale what already exists.

---

## 3. Environment Setup (One-time)

### 3.1 Backend test environment

1. Create and activate backend venv
2. Install backend dependencies
3. Install test-specific dependencies

Suggested packages:
- pytest
- pytest-django
- pytest-cov
- pytest-xdist
- schemathesis
- httpx
- requests-mock
- openapi-python-client
- selenium
- pytest-bdd
- robotframework
- robotframework-seleniumlibrary

### 3.2 Browser automation dependencies

- Install Chrome/Edge browser
- Install matching WebDriver (or use Selenium Manager)
- Ensure headless mode can run in CI

### 3.3 Test data and secrets

Use environment variables for test credentials and URLs:
- TEST_API_BASE_URL
- TEST_API_USERNAME
- TEST_API_PASSWORD
- TEST_UI_BASE_URL
- UI_BROWSER
- UI_HEADLESS

Never hardcode real credentials in tests.

---

## 4. Backend Contract Testing with OpenAPI (Mandatory for endpoints)

This is the core requirement: backend endpoints must be verified against generated Swagger/OpenAPI schema.

### 4.1 Generate schema from running backend

Use drf-spectacular endpoint already configured:
- Schema endpoint: /api/schema/
- Swagger UI: /api/docs/

Recommended process:
1. Start backend locally
2. Export schema from /api/schema/
3. Save canonical test copy to tests/openapi/schema.yaml
4. Regenerate schema copy when API changes (in PRs touching API)

### 4.2 Add contract checks with Schemathesis

Use two contract layers:

1) Focused endpoint contract tests (stable and quick)
- Examples and coverage phases
- Selected critical paths

2) Broader fuzzing (nightly or main branch)
- Fuzzing enabled
- Exclude unstable endpoints if needed

Suggested commands:
- Quick contract pass:
  schemathesis run tests/openapi/schema.yaml --url=http://localhost:8000 --phases=examples,coverage

- Endpoint-focused check:
  schemathesis run tests/openapi/schema.yaml --url=http://localhost:8000 --include-path=/api/user_management/profile/ --phases=examples,coverage

- Full contract fuzzing (nightly):
  schemathesis run tests/openapi/schema.yaml --url=http://localhost:8000

### 4.3 Keep contract tests reliable

Rules:
- Always authenticate where endpoint requires auth
- Avoid random production data assumptions
- Seed deterministic data in fixtures
- Mark destructive tests and isolate them

---

## 5. API Tests with pytest (Functional + Permission Coverage)

### 5.1 What every endpoint should have

For each endpoint group, test at least:
- Success path (2xx)
- Validation failures (400)
- Unauthorized (401)
- Forbidden (403)
- Not found (404) when applicable
- Contract consistency with schema fields

### 5.2 Organize tests by app/domain

Recommended pattern:
- tests/api/test_user_management_*.py
- tests/api/test_sports_objects_*.py
- tests/api/test_training_*.py

Use markers from pytest.ini:
- api, integration, smoke, slow, mock

### 5.3 API run examples

- Run all API tests:
  pytest tests/api -m api

- Run smoke API tests:
  pytest tests/api -m "api and smoke"

- Run one module:
  pytest tests/api/test_user_management.py

---

## 6. OpenAPI Client Validation (Consumer perspective)

Keep generated client tests for high-value auth and critical flows.

### 6.1 Regenerate OpenAPI client

1. Ensure tests/openapi/schema.yaml is current
2. Regenerate client in tests/openapi/openapi_client

### 6.2 Test client-generated calls

- Keep tests similar to test_token_openapi_client.py
- Validate parsed models and status codes
- This catches backward-incompatible schema changes early

---

## 7. UI End-to-End with Selenium + pytest

### 7.1 Standardize with Page Object Model

Use this structure:
- tests/ui/pages
- tests/ui/test_cases
- shared fixtures in tests/ui/conftest.py

Best practices:
- Explicit waits (never sleep)
- Stable selectors (data-testid preferred)
- One assertion theme per test
- Keep tests independent

### 7.2 Minimal UI smoke suite

Always include:
- Login success
- Login failure
- One critical business flow per module

### 7.3 UI run examples

- Run UI smoke:
  pytest tests/ui -m "ui and smoke"

- Run headless in CI:
  pytest tests/ui -m ui --ui-headless

---

## 8. BDD with pytest-bdd (Cucumber style)

Use BDD for cross-team readable business scenarios.

### 8.1 When to use

Use for behavior narratives, not all low-level tests.

Examples:
- Parent pays training month online
- Coach sees assigned calendar
- Child-linked profile cannot create object reservation

### 8.2 Structure

- Feature files in tests/cucumber_example
- Step definitions in corresponding Python modules
- Reuse page objects / API fixtures instead of duplicating logic

### 8.3 BDD run examples

- Run BDD scenarios:
  pytest tests/cucumber_example -m ui

---

## 9. Robot Framework acceptance tests

Use Robot for stakeholder-friendly acceptance checks and readable keyword-driven flows.

### 9.1 Scope

- Keep Robot suite small and focused on acceptance smoke/regression
- Reuse common keywords in resource files

### 9.2 Run examples

- Run Robot suite:
  robot tests/robotframework_example

- With output directory:
  robot -d reports/robot tests/robotframework_example

---

## 10. CI/CD pipeline blueprint

Implement staged gates:

Stage A: Fast PR gate
1. Python checks (if configured)
2. pytest API smoke
3. Schemathesis examples+coverage for critical endpoints
4. Selenium smoke (headless)

Stage B: Main branch gate
1. Full pytest api
2. Broader Schemathesis run
3. Full UI suite
4. BDD suite
5. Robot suite

Stage C: Nightly/weekly
1. Full fuzzing contract tests
2. Performance tests
3. Extended regression set

Artifacts to publish:
- pytest JUnit XML
- coverage XML/HTML
- Robot reports
- Selenium screenshots on failures
- Schemathesis logs

---

## 11. Coverage and quality thresholds

Recommended minimums for backend:
- Line coverage target: 75%+ at start
- Critical modules target: 85%+

Mandatory checks for API changes:
- Updated schema in tests/openapi/schema.yaml
- At least one API functional test for changed endpoint
- Contract test run evidence

---

## 12. Practical step-by-step rollout plan for Klubster

Week 1:
1. Freeze schema export process and document update rules
2. Add missing contract smoke tests for top-risk endpoints
3. Create shared auth/token fixtures used by openapi + api tests

Week 2:
1. Fill endpoint matrix for 2xx/4xx coverage per app
2. Harden Selenium smoke path with stable selectors
3. Add 3-5 critical BDD features

Week 3:
1. Add Robot acceptance smoke suite
2. Add CI stages A and B
3. Start coverage tracking and failure triage workflow

Week 4:
1. Introduce nightly fuzzing and performance checks
2. Review flaky tests and quarantine policy
3. Baseline test duration and optimize with pytest-xdist

---

## 13. Definition of Done for a backend endpoint change

A backend endpoint change is done only if:
1. Endpoint is documented in Swagger/OpenAPI
2. tests/openapi/schema.yaml is updated
3. Contract test passes (examples+coverage at minimum)
4. pytest API tests for success + failure paths pass
5. Relevant E2E path (if user-facing) is covered or updated

---

## 14. Suggested command set for daily use

- API tests:
  pytest tests/api -m api

- Contract quick pass:
  schemathesis run tests/openapi/schema.yaml --url=http://localhost:8000 --phases=examples,coverage

- UI smoke:
  pytest tests/ui -m "ui and smoke" --ui-headless

- BDD:
  pytest tests/cucumber_example

- Robot:
  robot -d reports/robot tests/robotframework_example

- Full local verification:
  pytest tests -m "not slow"

---

## 15. Common anti-patterns to avoid

- Only manual Swagger clicking without automated contract checks
- Testing only happy path
- UI tests with brittle CSS/XPath selectors
- Huge end-to-end suites with no smoke subset
- No separation between smoke, regression, and slow tests
- Hardcoded credentials in repository

---

This playbook is designed to be iterative: start with contract-first API quality, then grow UI and acceptance depth while keeping CI fast and reliable.

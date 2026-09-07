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

To run this test suite locally, you will need Docker and Docker Compose installed.

1. Authenticate with the GitHub Container Registry (GHCR) using a Personal Access Token.
2. Spin up the application environment:
   `docker compose up -d`
3. Execute the API tests:
   `pytest tests/api/ --tb=short`
4. Execute the UI tests:
   `pytest tests/ui/ --junitxml=reports/ui_report.xml`
5. Tear down the environment:
   `docker compose down`
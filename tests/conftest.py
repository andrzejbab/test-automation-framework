import pytest
from utility.utility import load_env_files
# Fixtures are loaded at top-level via tests/conftest.py

# Pytest hook to add CLI options
def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--api-base-url",
        action="store",
        default=None,
        help="Base URL for API tests (overrides TEST_API_BASE_URL)",
    )
    parser.addoption(
        "--use-mock-client",
        action="store_true",
        default=False,
        help="Force mock client")
    
    parser.addoption(
        "--api-admin-username",
        action="store",
        default=None,
        help="Admin username for API tests (overrides TEST_API_ADMIN_USERNAME)",
    )
    parser.addoption(
        "--api-admin-password",
        action="store",
        default=None,
        help="Admin password for API tests (overrides TEST_API_ADMIN_PASSWORD)",
    )

    parser.addoption(
        "--ui-browser",
        action="store",
        default=None,
        help="Browser for UI tests (chrome|firefox), overrides UI_BROWSER env",
    )

    parser.addoption(
        "--ui-headless",
        action="store",
        default=None,
        help="Run UI tests headless (true|false), overrides UI_HEADLESS env",
    )

    parser.addoption(
        "--ui-base-url",
        action="store",
        default=None,
        help="Base URL for UI tests (overrides TEST_UI_BASE_URL)",
    )

    parser.addoption(
        "--api-mailpit-host",
        action="store",
        default=None,
        help="Base URL for UI tests (overrides MAILPIT_HOST)",
    )



# Load env files before fixtures run.
load_env_files()

# Register shared fixtures for the entire test suite.
pytest_plugins = ["fixtures.user_fixtures", "fixtures.user_fixtures_ui"]


import os
import pytest
from typing import Dict
from sqlalchemy.engine import URL
from api.api_clients.api_client_auth_user import ApiClientAuthUser
from api.api_clients.api_client_auth_admin import ApiClientAuthAdmin 
from api.api_clients.api_client_base import ApiClient, MockApiClient
from utility.utility import get_option_env, fetch_and_validate_tokens
from utility.factories import make_user_data_abonament_testing
from utility.emails import get_activation_token_from_email_body, clear_emails_mailpit
from utility.db_manager import DatabaseManager


@pytest.fixture(scope="session")
def api_client(request, api_base_url):  # api_base_url from your existing fixture
    """Return a real or mocked ApiClient depending on CLI flags or markers."""
    use_mock = request.config.getoption("--use-mock-client") or request.node.get_closest_marker("mock")
    if use_mock:
        mocker = request.getfixturevalue("requests_mock")  # only attach mock adapter when requested
        yield MockApiClient(api_base_url, mocker)
    else:
        yield ApiClient(api_base_url)
    # Teardown, cleanup


@pytest.fixture(scope="session")
def auth_api_client_admin(api_base_url, valid_credentials_admin):
    """Return a standalone client configured with admin tokens."""
    client = ApiClientAuthAdmin(base_url=api_base_url)
    client.set_api_tokens(fetch_and_validate_tokens(client=client, credentials=valid_credentials_admin))
    yield client
    # Teardown, cleanup

@pytest.fixture(scope="function")
def auth_api_client(api_base_url, new_user_account):
    """Return standalone client configured with user tokens"""
    client = ApiClientAuthUser(base_url=api_base_url)
    user_credentials = {
        "username": new_user_account.get("email"),
        "password": new_user_account.get("password")
    }
    client.set_api_tokens(fetch_and_validate_tokens(client=client, credentials=user_credentials))
    yield client
    # Teardown, cleanup

@pytest.fixture(scope="function")
def no_auth_api_client(api_base_url, new_user_account):
    """Return standalone client configured with user tokens"""
    client = ApiClientAuthUser(base_url=api_base_url)
    yield client
    # Teardown, cleanup


@pytest.fixture(scope="session")
def clean_mailpit(pytestconfig: pytest.Config):
    """Clears all messages from Mailpit before every test."""
    mailpit_host = get_option_env(pytestconfig, "--api-mailpit-host", "MAILPIT_HOST")
    clear_emails_mailpit(mailpit_host)
    yield
    clear_emails_mailpit(mailpit_host)

@pytest.fixture(scope="function")
def registered_user(api_client):
    """Register a new user (unactivated) - for contract tests and activation flows"""
    user_data = make_user_data_abonament_testing()
    response = api_client.api_register_user(**user_data)
    assert response.status_code == 201, f"Failed to register user: {response.text}"
    return user_data


@pytest.fixture(scope="function")
def activated_user(api_client, registered_user):
    """Activate a registered user - transitions from unactivated to activated state"""
    user_email = registered_user.get("email")
    # Get activation token from Email (Mailpit)
    activation_token = get_activation_token_from_email_body(user_email)
    response = api_client.api_activate_user(activation_token)
    assert response.status_code == 302, f"Failed to activate user: {response.text}"
    return registered_user

@pytest.fixture(scope="function")
def activated_user_reset_password(api_client, activated_user):
    user_email = activated_user.get("email")
    response = api_client.api_password_reset(user_email)
    assert response.status_code == 200, f"Failed to reset password: {response.text}"
    return activated_user

@pytest.fixture(scope="function")
def new_user_account(activated_user, auth_api_client_admin):
    """Provides fully activated test user with automatic cleanup"""
    yield activated_user
    # Cleanup - remove user
    response = auth_api_client_admin.api_delete_user(activated_user.get("email"))
    assert response.status_code == 200, f"Failed to delete user: {response.text}"


@pytest.fixture(scope="session")
def db_manager(pytestconfig: pytest.Config):
    postgres_db = get_option_env(pytestconfig, "--postgres_db", "POSTGRES_DB")
    postgres_user = get_option_env(pytestconfig, "--postgres_user", "POSTGRES_USER")
    postgres_password = get_option_env(pytestconfig, "--postgres_password", "POSTGRES_PASSWORD")
    db_url = URL.create(
        "postgresql+psycopg",
        username=postgres_user,
        password=postgres_password,
        host=os.getenv("POSTGRES_HOST", "localhost"),
        port=int(os.getenv("POSTGRES_PORT", "5432")),
        database=postgres_db,
    )
    db_manager_obj = DatabaseManager(db_url=db_url)
    yield db_manager_obj
    # cleanup
    db_manager_obj.close()

@pytest.fixture(scope="function")
def db_session(db_manager):
    session_factory = db_manager.get_session_factory()
    session = session_factory()
    yield session
    # Clean up
    session.close()


@pytest.fixture(scope="session")
def api_base_url(pytestconfig: pytest.Config) -> str:
    """Resolve API base URL from CLI options or TEST_API_BASE_URL env variable."""
    return get_option_env(pytestconfig, "--api-base-url", "TEST_API_BASE_URL")


@pytest.fixture(scope="session")
def valid_credentials_admin(pytestconfig: pytest.Config) -> Dict[str, str]:
    """Load admin credentials from CLI options or environment variables."""
    return {
        "username": get_option_env(pytestconfig, "--api-admin-username", "TEST_API_ADMIN_USERNAME"),
        "password": get_option_env(pytestconfig, "--api-admin-password", "TEST_API_ADMIN_PASSWORD"),
    }









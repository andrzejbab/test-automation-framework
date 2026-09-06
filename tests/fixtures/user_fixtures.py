import pytest
from typing import Dict
from tests.api.api_clients.api_client_auth_user import ApiClientAuthUser
from tests.api.api_clients.api_client_auth_admin import ApiClientAuthAdmin 
from tests.api.api_clients.api_client_base import ApiClient, MockApiClient
from tests.utility.utility import get_option_env, fetch_and_validate_tokens
from tests.utility.factories import make_user_data_abonament_basic
from tests.utility.emails import get_activation_token_from_email_body, clear_emails_mailpit
import os
from django.contrib.auth import get_user_model

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
def new_user_account(api_client, auth_api_client_admin, clean_mailpit):
    """Create test user account """
    user_data = make_user_data_abonament_basic()
    response = api_client.api_register_user(**user_data)  
    # Ensure the registration was successful (201 Created)
    assert response.status_code == 201, f"Failed to create user: {response.text}"

    user_email = user_data.get("email")
    # Get activation token from Email (mailpit)
    activation_token = get_activation_token_from_email_body(user_email)
    response = api_client.api_activate_user(activation_token)
    assert response.status_code == 302, f"Failed to activate user: {response.text}"
    yield user_data
    # cleanup - remove user
    response = auth_api_client_admin.api_delete_user(user_email)
    assert response.status_code == 200, f"Failed to delete user: {response.text}"


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


#@pytest.fixture(scope="session", autouse=True)
@pytest.fixture(scope="session")
def ensure_admin_user(django_db_setup, django_db_blocker):
    """Ensure an admin user exists in the Django DB with env-provided credentials."""
    username = os.getenv("TEST_API_ADMIN_USERNAME")
    password = os.getenv("TEST_API_ADMIN_PASSWORD")
    if not username or not password:
        pytest.skip("admin credentials missing")
    with django_db_blocker.unblock():
        User = get_user_model()
        user, created = User.objects.get_or_create(username=username, defaults={"is_staff": True, "is_superuser": True})
        if created:
            user.set_password(password)
        else:
            user.set_password(password)  # keep in sync with env in case password changed
        user.is_staff = True
        user.is_superuser = True
        user.save()
    return {"username": username, "password": password}





import pytest
from utility.utility import get_option_env
from ui.pom.pages.user_management.login_page import LoginPage
from utility.utility import (get_browser, get_headless, build_chrome_driver,
                                     build_firefox_driver, normalize_bool)
from utility.factories import make_display_size


@pytest.fixture(scope="session")
def ui_base_url(pytestconfig: pytest.Config) -> str:
    """Resolve UI base URL from CLI options or TEST_UI_BASE_URL env variable."""
    return get_option_env(pytestconfig, "--ui-base-url", "TEST_UI_BASE_URL")


@pytest.fixture(scope="function")
def mobile_screen_size():
     pass

@pytest.fixture(scope="function")
def driver(pytestconfig: pytest.Config):
    browser = get_browser(pytestconfig)
    headless = get_headless(pytestconfig)
    is_mobile = normalize_bool(get_option_env(pytestconfig, "--mobile", "MOBILE"))

    if browser == "chrome":
        driver_instance = build_chrome_driver(headless, *make_display_size(is_mobile))
    elif browser == "firefox":
        driver_instance = build_firefox_driver(headless, *make_display_size(is_mobile))
    else:
        raise ValueError(
            "Unsupported browser for UI tests. Use chrome or firefox via --ui-browser or UI_BROWSER"
        )
    
    yield driver_instance
    # Clean up, tear down
    driver_instance.quit()




@pytest.fixture()
def log_in_user(new_user_account, driver): 
        club_management_page = LoginPage(driver).login_page.open().login_as_valid_user(new_user_account.get("email"), 
                                                   new_user_account.get("password"))
        assert club_management_page.check_user_registered()
        yield
        # cleanup
        assert club_management_page.logout_click().is_loaded()

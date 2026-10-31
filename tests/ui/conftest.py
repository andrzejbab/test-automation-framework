import pytest
import allure
from allure_commons.types import AttachmentType

from utility.utility import get_option_env
from ui.pom.pages.user_management.login_page import LoginPage
from utility.utility import (get_browser, get_headless, build_chrome_driver,
                                     build_firefox_driver, normalize_bool)
from utility.factories import make_display_size



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    # Check if the test failed during the execution ("call") phase
    if report.when == "call" and report.failed:
        
        # Access the 'driver' fixture from the test's arguments
        # Note: This assumes WebDriver fixture is named 'driver'
        if "driver" in item.funcargs:
            driver = item.funcargs["driver"]
            
            try:
                # 1. Attach the Visual Screenshot
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"Screenshot on Failure: {item.name}",
                    attachment_type=AttachmentType.PNG
                )
                
                # 2. Attach the HTML DOM Source
                allure.attach(
                    driver.page_source,
                    name="HTML DOM state at failure",
                    attachment_type=AttachmentType.HTML
                )
            except Exception as e:
                print(f"Failed to capture evidence for Allure: {e}")


@pytest.fixture(scope="session")
def ui_base_url(pytestconfig: pytest.Config) -> str:
    """Resolve UI base URL from CLI options or TEST_UI_BASE_URL env variable."""
    return get_option_env(pytestconfig, "--ui-base-url", "TEST_UI_BASE_URL")


@pytest.fixture(scope="function")
def mobile_screen_size():
     pass

@pytest.fixture(scope="function")
def driver(pytestconfig: pytest.Config):
    """Initail driver settings"""
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
    """Create new user and login to default news page"""
    news_page = LoginPage(driver).open().login_as_valid_user(new_user_account.get("email"), 
                                                   new_user_account.get("password"))
    assert news_page.top_bar.user_settings_dropdown.check_user_registered()
    yield news_page
    # cleanup
    assert news_page.top_bar.user_settings_dropdown.logout_click().is_loaded()
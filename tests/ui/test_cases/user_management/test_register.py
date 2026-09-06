import pytest
from tests.ui.pom.pages.user_management.landing_page import LandingPage
from tests.ui.pom.pages.user_management.register_page import RegisterPage
import allure


@pytest.mark.ui
@allure.epic("Authentication & Onboarding")
@allure.feature("User Registration")
class TestRegisterUser:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Setup fixture to initialize the starting page object."""
        self.landing_page = LandingPage(driver)

    @allure.story("User can register, activate account via email, login, and logout")
    @pytest.mark.parametrize("user", [{
        "email": "testuser@test.local",
        "password": "2345432",
        "password_confirm": "2345432",
        "terms": True,
        "privacy": True
    }])
    def test_register_and_login_user(self, user, auth_api_client_admin, clean_mailpit):
        """
        E2E Test Specification:
        1. Navigate to landing page and select standard plan.
        2. Submit registration form with valid credentials.
        3. Verify registration success message.
        4. Activate user via Mailpit activation link.
        5. Log in with newly registered credentials.
        6. Verify dashboard access and log out.
        7. Clean up user via REST API.
        """
        email = user.get("email")
        register_page = (
            self.landing_page.open()
            .click_select_standard_plan()
            .fill_registration_form(
                email=email,
                password=user.get("password"),
                confirm_password=user.get("password_confirm"),
                terms=user.get("terms"),
                privacy=user.get("privacy")
            )
            .click_register_submit()
        )
        assert register_page.get_register_successful_message() == RegisterPage.REGISTER_MSG
        
        login_page = register_page.activate_user(email)
        
        news_page = login_page.login_as_valid_user(email, user.get("password"))
        assert news_page.top_bar.user_settings_dropdown.check_user_registered()
        assert news_page.top_bar.user_settings_dropdown.logout_click().is_loaded()
        
        auth_api_client_admin.api_delete_user(username=email)
import pytest
from ui.pom.pages.user_management.login_page import LoginPage
from ui.pom.pages.user_management.password_reset_page import PasswordResetPage
from ui.pom.pages.user_management.landing_page import LandingPage
from ui.pom.pages.news_page import NewsPage
import allure



@pytest.mark.ui
@allure.epic("Authentication & Onboarding")
@allure.feature('User Login')
@allure.story("User can login, logout")
class TestUserManagementLoginUser:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Setup fixture to initialize the starting page object."""
        self.login_page = LoginPage(driver)
        self.landing_page = LandingPage(driver)
        
    
    @allure.story("User can login, logout")
    def test_login_logout(self, new_user_account):
        """
        E2E Test Specification:
        1. Login as valid user
        2. Logout
        """
        news_page: NewsPage = self.login_page.open().login_as_valid_user(new_user_account.get("email"), 
                                                   new_user_account.get("password"))
        assert news_page.top_bar.user_settings_dropdown.check_user_registered()
        assert news_page.top_bar.user_settings_dropdown.logout_click().is_loaded()


    @allure.story("User enter wrong credentials. Message with error should be shown.")
    def test_invalid_login(self):
        """
        E2E Test Specification:
        1. Login with invalid credentials
        2. Check error message
        """
        login_page = self.login_page.open().login_as_invalid_user("invalid_user", "wrong_password")
        assert login_page.get_error_message() == LoginPage.INVALID_CREDENTIALS_MSG


    @allure.story("User can reset password over link on login page."
                  " Link to password reset page should come over email.")
    def test_reset_password(self, new_user_account):
        """
        E2E Test Specification:
        1. Request reset password over link on login page 
        2. Reset password over link from email
        3. Login with new password
        4. Logout
        """
        new_password = "123"
        password_reset_page = self.login_page.open().click_forgot_password()
        submit_msg = (password_reset_page.enter_email(new_user_account.get("email"))
                      .submit_request()
                      .get_submit_message())
        assert PasswordResetPage.SUBMIT_MSG == submit_msg
        password_change_page = (password_reset_page.click_password_reset_link_from_email(new_user_account.get("email"))
                                .set_new_password(new_password, new_password)
                                .submit())
        login_page = password_change_page.wait_for_login_redirect()
        assert login_page.is_loaded()
        news_page: NewsPage = self.login_page.open().login_as_valid_user(new_user_account.get("email"), new_password)
        assert news_page.top_bar.user_settings_dropdown.check_user_registered()
        assert news_page.top_bar.user_settings_dropdown.logout_click().is_loaded()


    @allure.story("Login over landing page")
    def test_login_from_landing_page(self, new_user_account):
        """
        E2E Test Specification:
        1. Click Login button in landing page
        2. Login
        3. Logout
        """
        login_page = self.landing_page.open().click_login_in()
        news_page: NewsPage = login_page.login_as_valid_user(new_user_account.get("email"), 
                                                   new_user_account.get("password"))
        assert news_page.top_bar.user_settings_dropdown.check_user_registered()
        assert news_page.top_bar.user_settings_dropdown.logout_click().is_loaded()












import allure
from selenium.webdriver.common.by import By
from ui.pom.base.base_page import BasePage    
from ui.constants import LOGIN_URL_FRAGMENT, CLUB_MANAGEMENT_URL_FRAGMENT
from selenium.common.exceptions import TimeoutException

from utility.utility import get_url_ui


class LoginPage(BasePage):
    INVALID_CREDENTIALS_MSG = "Nieprawidłowy login lub hasło."

    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-btn")
        self.error_message = (By.ID, "login-error-message")
        self.forgot_password_button = (By.ID, "forgot-password-btn")

    @allure.step("Open Login Page")
    def open(self):
        self.driver.get(get_url_ui(LOGIN_URL_FRAGMENT))
        self.wait_until_loaded()
        return self

    def wait_until_loaded(self):
        self.wait_until_element_to_be_clickable(self.login_button)
        return self
    
    def is_loaded(self):
        try: 
            self.wait_until_loaded()
            return True
        except TimeoutException:
            return False
    
    # Allure automatically replaces {username} with the value passed into the method
    @allure.step("Login as valid user: {username}")
    def login_as_valid_user(self, username: str, password: str):
        """Fills form, clicks login, waits for transition, and returns next page."""
        self._enter_username(username=username)
        self._enter_password(password=password)
        self._click_login()
        self.handle_cookie_popup()
        self.wait_until_url_contain(text=CLUB_MANAGEMENT_URL_FRAGMENT)
        
        # Fixing circular import problem
        from ui.pom.pages.news_page import NewsPage
        return NewsPage(self.driver)
    
    @allure.step("Attempt login with invalid credentials for user: {username}")
    def login_as_invalid_user(self, username: str, password: str):
        """Fills form, clicks login, and returns self (since we expect to stay here)."""
        self._enter_username(username=username)
        self._enter_password(password=password)
        self._click_login()
        return self
    
    @allure.step("Click 'Register' button")
    def register_click(self):
        self.driver.find_element(By.ID, "register-btn").click()

    @allure.step("Get login error message text")
    def get_error_message(self):
        try:
            return self.wait_until_visibility_of_element_located(self.error_message).text
        except TimeoutException:
            return False
    
    @allure.step("Click 'Forgot Password' button")
    def click_forgot_password(self):
        self.wait_until_element_to_be_clickable(self.forgot_password_button).click()
        from ui.pom.pages.user_management.password_reset_page import PasswordResetPage
        return PasswordResetPage(self.driver)
    
    @allure.step("Enter username: {username}")
    def _enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    # Security Best Practice: Never inject {password} into the Allure step description
    @allure.step("Enter password")
    def _enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    @allure.step("Click Login button")
    def _click_login(self):
        self.driver.find_element(*self.login_button).click()
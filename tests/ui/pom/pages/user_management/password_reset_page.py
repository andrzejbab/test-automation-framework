
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure
from tests.ui.pom.base.base_page import BasePage
from tests.utility.emails import get_url_from_email_body


class PasswordResetPage(BasePage):
    SUBMIT_MSG = "Jeśli podany email istnieje, wysłaliśmy instrukcje resetowania hasła."

    def __init__(self, driver):
        super().__init__(driver)
        self.email_field = (By.ID, "password-reset-email")
        self.submit_button = (By.ID, "password-reset-submit-btn")
        self.back_to_login_link = (By.ID, "password-reset-back-btn")
        self.submit_message = (By.ID, "password-reset-success-message") 

    @allure.step("Enter password reset email: {email}")
    def enter_email(self, email):
        email_field = self.wait_until_visibility_of_element_located(self.email_field)
        email_field.clear()
        email_field.send_keys(email)
        return self

    @allure.step("Submit password reset request")
    def submit_request(self):
        self.wait_until_element_to_be_clickable(self.submit_button).click()    
        return self

    @allure.step("Click back to login link")
    def click_back_to_login(self):
        self.wait_until_element_to_be_clickable(self.back_to_login_link).click()
        from tests.ui.pom.pages.user_management.login_page import LoginPage
        return LoginPage(self.driver)

    @allure.step("Get password reset submit message")
    def get_submit_message(self):
        return self.wait_until_visibility_of_element_located(self.submit_message).text

    @allure.step("Open password reset URL from email for recipient: {recipient}")
    def click_password_reset_link_from_email(self, recipient):
        reset_url = get_url_from_email_body(recipient=recipient)
        self.driver.get(reset_url)
        from tests.ui.pom.pages.user_management.change_password_page import ChangePasswordPage
        return ChangePasswordPage(self.driver)


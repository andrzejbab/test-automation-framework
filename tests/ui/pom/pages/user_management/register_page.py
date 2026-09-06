from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure
from tests.ui.pom.base.base_page import BasePage
from tests.utility.emails import get_url_from_email_body


class RegisterPage(BasePage):
    REGISTER_MSG = "Wysłaliśmy email aktywacyjny. Aktywuj konto klikając w link w wiadomości (sprawdź także folder SPAM)."

    def __init__(self, driver):
        super().__init__(driver)
        # Locators
        self.username_input = (By.ID, "register-username")
        self.email_input = (By.ID, "register-email")
        self.password_input = (By.ID, "register-password")
        self.confirm_password_input = (By.ID, "register-confirm-password")
        self.register_submit_button = (By.ID, "register-submit-btn")
        self.success_message_locator = (By.ID, "register-success-message")
        self.error_message_locator = (By.ID, "register-error-message")
        self.terms_checkbox = (By.XPATH, "//label[contains(., 'Regulamin')]//input[@type='checkbox']")
        self.privacy_policy_checkbox = (By.XPATH, "//label[contains(., 'Politykę')]//input[@type='checkbox']")

    @allure.step("Fill registration form for email: {email}")
    def fill_registration_form(self, email, password, confirm_password, terms, privacy):
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        self.set_terms_checkbox(terms)
        self.set_privacy_policy_checkbox(privacy)
        return self
        
    @allure.step("Enter username: {username}")
    def enter_username(self, username):
        username_input = self.wait.until(EC.visibility_of_element_located(self.username_input))
        username_input.clear()  
        username_input.send_keys(username)
        return self
    
    @allure.step("Enter email: {email}")
    def enter_email(self, email):
        email_input = self.wait.until(EC.visibility_of_element_located(self.email_input))
        email_input.clear()  
        email_input.send_keys(email)   
        return self 
    
    @allure.step("Enter password")
    def enter_password(self, password):
        password_input = self.wait.until(EC.visibility_of_element_located(self.password_input))
        password_input.clear()  
        password_input.send_keys(password)
        return self 

    @allure.step("Enter confirm password")
    def enter_confirm_password(self, confirm_password):
        confirm_password_input = self.wait.until(EC.visibility_of_element_located(self.confirm_password_input))
        confirm_password_input.clear()  
        confirm_password_input.send_keys(confirm_password)
        return self 

    @allure.step("Click register submit button")
    def click_register_submit(self):
        register_submit_button = self.wait.until(EC.element_to_be_clickable(self.register_submit_button))
        register_submit_button.click() 
        return self

    @allure.step("Set privacy policy checkbox to: {state}")
    def set_privacy_policy_checkbox(self, state: bool=True):
        privacy_checkbox_elem = self.wait.until(EC.element_to_be_clickable(self.privacy_policy_checkbox))
        self._set_checkbox_element(privacy_checkbox_elem, state)
        return self
    
    @allure.step("Set terms checkbox to: {state}")
    def set_terms_checkbox(self, state: bool=True):
        terms_checkbox_elem = self.wait.until(EC.element_to_be_clickable(self.terms_checkbox))
        self._set_checkbox_element(terms_checkbox_elem, state)
        return self
    
    # Intentionally leaving Allure step off this internal method to keep report clean
    def _set_checkbox_element(self, element, state):
        is_selected = element.is_selected()
        if state and not is_selected:
            element.click()
        elif not state and is_selected:
            element.click()

    @allure.step("Get register successful message")
    def get_register_successful_message(self):   
        success_message = self.wait.until(EC.visibility_of_element_located(self.success_message_locator))
        return success_message.text
    
    @allure.step("Get register error message")
    def get_register_error_message(self):   
        error_message = self.wait.until(EC.visibility_of_element_located(self.error_message_locator))
        return error_message.text
    
    @allure.step("Activate user by extracting URL from email for recipient: {recipient}")
    def activate_user(self, recipient):
        activation_url = get_url_from_email_body(recipient=recipient)
        self.driver.get(activation_url)
        from tests.ui.pom.pages.user_management.login_page import LoginPage
        return LoginPage(self.driver)


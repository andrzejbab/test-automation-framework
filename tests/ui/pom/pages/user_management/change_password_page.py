import allure
from ui.pom.base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from ui.pom.pages.user_management.login_page import LoginPage


class ChangePasswordPage(BasePage):
    SUCCESS_MSG = "Hasło zostało zmienione. Możesz się teraz zalogować."

    def __init__(self, driver):
        super().__init__(driver)
        self.new_password_input = (By.XPATH, '//input[@placeholder="Nowe hasło"]')
        self.confirm_password_input = (By.XPATH, '//input[@placeholder="Powtórz hasło"]')
        self.submit_button = (By.XPATH, '//button[@type="submit" and contains(text(), "Zmień hasło")]')
        self.message = (By.XPATH,'//p[text()="Hasło zostało zmienione."]')
        self.login_button = (By.ID, "login-btn")

    @allure.step("Set new password")
    def set_new_password(self, password, password_confirm):
        self.enter_new_password(password)
        self.enter_confirm_password(password_confirm)
        return self

    @allure.step("Enter new password")
    def enter_new_password(self, password):
        self.wait_until_visibility_of_element_located(self.new_password_input).send_keys(password)

    @allure.step("Enter confirmation password")
    def enter_confirm_password(self, password):
        self.wait_until_visibility_of_element_located(self.confirm_password_input).send_keys(password)

    @allure.step("Submit change password form")
    def submit(self):
        self.wait.until(EC.element_to_be_clickable(self.submit_button)).click()
        return self

    @allure.step("Get change password success message")
    def get_message(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self.message)).text
    
    @allure.step("Wait for redirect to login page")
    def wait_for_login_redirect(self):
        self.wait_until_element_to_be_clickable(self.login_button)
        from ui.pom.pages.user_management.login_page import LoginPage
        return LoginPage(self.driver)
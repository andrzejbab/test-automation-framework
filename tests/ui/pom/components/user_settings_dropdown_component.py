from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from ui.pom.base.base_page import BasePage
from ui.pom.pages.user_management.login_page import LoginPage
from ui.pom.pages.user_management.change_password_page import ChangePasswordPage

class UserSettingsDropdownComponent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.toggle = (By.ID, "dropdown-user")
        self.dropdown_toggle = (By.ID, "dropdown-user-toggle")
        self.dropdown_user_name = (By.ID, "dropdown-user-name")
        self.dropdown_change_password = (By.ID, "dropdown-change-password")
        self.logout_button = (By.ID, "dropdown-logout")

    def _is_dropdown_open(self):
        toggle = self.wait.until(EC.element_to_be_clickable(self.toggle))
        return toggle.get_attribute("aria-expanded") == "true"

    def _open_dropdown(self):
        if not self._is_dropdown_open():
            self.wait.until(EC.element_to_be_clickable(self.dropdown_toggle)).click()

    def _get_username(self):
        return self.wait.until(EC.visibility_of_element_located(self.dropdown_user_name)).text
    
    def change_password_click(self):
        self._open_dropdown()
        self.wait.until(EC.element_to_be_clickable(self.dropdown_change_password)).click()
        return ChangePasswordPage(self.driver)      
    
    def logout_click(self):
        self._open_dropdown()
        self.wait.until(EC.element_to_be_clickable(self.logout_button)).click()
        return LoginPage(self.driver)

    def check_user_registered(self):
        self._open_dropdown()
        actual_username = self._get_username()
        return  "Guest" not in actual_username
from ui.pom.base.base_page import BasePage
from selenium.webdriver.common.by import By
import allure
from utility.utility import get_url_ui
import time


class LandingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Locators
        self.login_btn = (By.XPATH, "//button[text()='Zaloguj']")
        self.test_plan_btn = (By.XPATH, "//div[contains(@class, 'card')][.//h5[text()='testowy']]//button[text()='Wybierz plan']")
        self.standard_plan_btn = (By.XPATH, "//div[contains(@class, 'card')][.//h5[text()='standardowy']]//button[text()='Wybierz plan']")
        self.start_for_free_btn = (By.XPATH, "//a[text()='Zacznij za darmo']")
        self.price_link = (By.XPATH, "//span[text()='Cennik']")

    @allure.step("Open landing page")
    def open(self):
        self.driver.get(get_url_ui(""))
        self.wait_until_loaded()
        return self

    @allure.step("Wait until landing page is loaded")
    def wait_until_loaded(self):
        self.wait_until_element_to_be_clickable(self.start_for_free_btn)
        return self

    @allure.step("Click login button")
    def click_login_in(self):
        self.wait_until_element_to_be_clickable(self.login_btn).click()
        from ui.pom.pages.user_management.login_page import LoginPage
        return LoginPage(self.driver)
    
    @allure.step("Select 'testowy' (Test) plan")
    def click_select_test_plan(self):
        self.wait_until_element_to_be_clickable(self.test_plan_btn).click()
        from ui.pom.pages.user_management.register_page import RegisterPage
        return RegisterPage(self.driver)
    
    @allure.step("Select 'standardowy' (Standard) plan")
    def click_select_standard_plan(self):
        time.sleep(2)
        self.wait_until_visibility_of_element_located(self.standard_plan_btn)
        self.wait_until_element_to_be_clickable(self.standard_plan_btn).click()
        from ui.pom.pages.user_management.register_page import RegisterPage
        return RegisterPage(self.driver)

    @allure.step("Click 'Cennik' link")
    def click_price_link(self):
        self.wait_until_element_to_be_clickable(self.price_link).click()
        
        return self
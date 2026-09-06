from selenium.webdriver.support.ui import WebDriverWait
from tests.ui.constants import WAITTIMEOUT_SECONDS
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, WAITTIMEOUT_SECONDS)
        self.cookie_accept_btn = (By.XPATH, "//button[contains(text(), 'Akceptuję')]")

    def wait_until_url_contain(self, text):
        return self.wait.until(EC.url_contains(text))

    def wait_until_element_to_be_clickable(self, element):
        return self.wait.until(EC.element_to_be_clickable(element))
    
    def wait_until_visibility_of_element_located(self, element):
        return self.wait.until(EC.visibility_of_element_located(element))

    def handle_cookie_popup(self):
        self.wait_until_element_to_be_clickable(self.cookie_accept_btn).click()

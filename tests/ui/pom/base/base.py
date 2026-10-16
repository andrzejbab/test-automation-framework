from selenium.webdriver.support.ui import WebDriverWait
from ui.constants import WAITTIMEOUT_SECONDS
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Base:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, WAITTIMEOUT_SECONDS)

    def wait_until_url_contain(self, text):
        return self.wait.until(EC.url_contains(text))

    def wait_until_element_to_be_clickable(self, element):
        return self.wait.until(EC.element_to_be_clickable(element))
    
    def wait_until_visibility_of_element_located(self, element):
        return self.wait.until(EC.visibility_of_element_located(element))


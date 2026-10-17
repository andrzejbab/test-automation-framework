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

    # It must be present in the DOM.
    # It must be enabled (not disabled).
    # It must be visible on the screen (rendered with height 
    # and width greater than zero).
    def wait_until_element_to_be_clickable(self, element):
        return self.wait.until(EC.element_to_be_clickable(element))

    # Checks if the element is rendered and visible 
    # on the screen (Will fail for hidden inputs).
    def wait_until_visibility_of_element_located(self, element):
        return self.wait.until(EC.visibility_of_element_located(element))

    # Checks if the element exists anywhere in the HTML DOM tree, 
    # regardless of whether it is visible to the user or hidden by CSS.
    def wait_until_presence_of_element_located(self, element):
        return self.wait.until(EC.presence_of_element_located(element))


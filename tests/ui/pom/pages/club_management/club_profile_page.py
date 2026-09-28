from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

from tests.ui.pom.club_management.club_sidebar import ClubSidebar

class ClubProfilePage:
    def __init__(self, driver):
        self.sidebar = ClubSidebar(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.logo = (By.ID, "club-logo-input")
        self.current_logo = (By.ID, "club-current-logo")
        self.logo_preview = (By.ID, "club-logo-preview")
        self.name = (By.ID, "club-name-input")
        self.phone = (By.ID, "club-phone-input")
        self.email = (By.ID, "club-email-input")    
        self.location = (By.ID, "club-location-input")
        self.save_button = (By.ID, "club-profile-submit-btn")

    def upload_logo(self, file_path):
        self.sidebar.go_to_profile()
        logo_input = self.wait.until(EC.visibility_of_element_located(self.logo))
        logo_input.send_keys(file_path)
    
    def update_name(self, name):
        self.sidebar.go_to_profile()
        name_input = self.wait.until(EC.visibility_of_element_located(self.name))
        name_input.clear()
        name_input.send_keys(name)  

    def update_phone(self, phone):
        self.sidebar.go_to_profile()
        phone_input = self.wait.until(EC.visibility_of_element_located(self.phone))
        phone_input.clear()
        phone_input.send_keys(phone)

    def update_email(self, email):
        self.sidebar.go_to_profile()
        email_input = self.wait.until(EC.visibility_of_element_located(self.email))
        email_input.clear()
        email_input.send_keys(email)

    def update_location(self, location):
        self.sidebar.go_to_profile()
        location_input = self.wait.until(EC.visibility_of_element_located(self.location))
        location_input.clear()
        location_input.send_keys(location)

    def save_profile(self):
        self.sidebar.go_to_profile()
        save_button = self.wait.until(EC.element_to_be_clickable(self.save_button))
        save_button.click()

    def reload(self):
        self.driver.refresh()

    def get_current_logo_src(self):
        self.sidebar.go_to_profile()
        logo_img = self.wait.until(EC.visibility_of_element_located(self.current_logo))
        return logo_img.get_attribute("src")
    
    def get_logo_preview_src(self):
        self.sidebar.go_to_profile()
        logo_img = self.wait.until(EC.visibility_of_element_located(self.logo_preview))
        return logo_img.get_attribute("src")

    def get_name(self):
        self.sidebar.go_to_profile()
        name_input = self.wait.until(EC.visibility_of_element_located(self.name))
        value = name_input.get_attribute("value")
        return value
    
    def get_phone(self):
        self.sidebar.go_to_profile()
        phone_input = self.wait.until(EC.visibility_of_element_located(self.phone))
        value = phone_input.get_attribute("value")
        return value
    
    def get_email(self):
        self.sidebar.go_to_profile()
        email_input = self.wait.until(EC.visibility_of_element_located(self.email))
        value = email_input.get_attribute("value")
        return value
    
    def get_location(self):
        self.sidebar.go_to_profile()
        location_input = self.wait.until(EC.visibility_of_element_located(self.location))
        value = location_input.get_attribute("value")
        return value    
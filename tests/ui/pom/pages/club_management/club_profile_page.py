from selenium.webdriver.common.by import By
import allure
from ui.pom.base.base_page import BasePage


class ClubProfilePage(BasePage):

    SAVE_MESSAGE = "Profil klubu został zaktualizowany."
    def __init__(self, driver):
        super().__init__(driver)

        # Alerts
        self.alert_save = (By.XPATH, "//div[contains(@role, 'alert')]")

        # Basic club data
        self.name = (By.ID, "club-name-input")
        self.phone = (By.ID, "club-phone-input")
        self.email = (By.ID, "club-email-input")
        self.website = (By.ID, "club-website-input")
        self.location = (By.ID, "club-location-input")

        # Opening hours
            
        # Save profile data
        self.save_button = (By.ID, "club-profile-submit-btn") 

    @allure.step("Get allert message")
    def get_alert_message(self):
        return self.wait_until_visibility_of_element_located(self.alert_save).text

    @allure.step("Update club basic data")
    def update_club_basic_data(self, club_name, phone, email, website, location):
        self.wait_until_element_to_be_clickable(self.name).send_keys(club_name)
        self.wait_until_element_to_be_clickable(self.phone).send_keys(phone)
        self.wait_until_element_to_be_clickable(self.email).send_keys(email)
        self.wait_until_element_to_be_clickable(self.website).send_keys(website)
        self.wait_until_element_to_be_clickable(self.location).send_keys(location)
        return self

    @allure.step("Save club profil")
    def save_profile(self):
        self.wait_until_element_to_be_clickable(self.save_button).click()
        return self

        
    



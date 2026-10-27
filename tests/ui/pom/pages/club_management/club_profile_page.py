import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from ui.pom.base.base_page import BasePage
from utility.utility import get_abs_path_to_tests
from pathlib import Path


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
        self.opening_simultaneously = (By.XPATH, "//input[contains(@aria-label, 'Godzina otwarcia')]")
        self.closing_simultaneously = (By.XPATH, "//input[contains(@aria-label, 'Godzina zamknięcia')]")
        self.apply_simultaneously = (By.XPATH, "//button[contains(text(), 'Zastosuj')]")

        # Pictures
        self.logo_pic = (By.ID, "club-logo-input")
        self.club_pics = (By.ID, "club-photos-input")
            
        # Save profile data
        self.save_button = (By.ID, "club-profile-submit-btn") 


    def _set_time(self, opening_elem, opening_hr, closing_elem, closing_hr):
        # JavaScript snippet that sets the value and fires both input and change events
        # This script uses the native prototype setter to force React/Vue components to recognize the value
        set_time_script = """
                const element = arguments[0];
                const value = arguments[1];
                
                // Get the native setter from HTMLInputElement prototype
                const nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
                
                // Apply the value using the native setter
                nativeInputValueSetter.call(element, value);
                
                // Dispatch events so the framework's state updates
                element.dispatchEvent(new Event('input', { bubbles: true }));
                element.dispatchEvent(new Event('change', { bubbles: true }));
            """

        # Execute for opening hour
        self.driver.execute_script(set_time_script, opening_elem, opening_hr)
        
        # Execute for closing hour
        self.driver.execute_script(set_time_script, closing_elem, closing_hr)

    @allure.step("Get allert message")
    def get_alert_message(self):
        return self.wait_until_visibility_of_element_located(self.alert_save).text


    @allure.step("Set club basic data {club_name}, {phone}, {email}, {website}, {location}")
    def update_club_basic_data(self, club_name, phone, email, website, location):
        self.wait_until_element_to_be_clickable(self.name).send_keys(club_name)
        self.wait_until_element_to_be_clickable(self.phone).send_keys(phone)
        self.wait_until_element_to_be_clickable(self.email).send_keys(email)
        self.wait_until_element_to_be_clickable(self.website).send_keys(website)
        self.wait_until_element_to_be_clickable(self.location).send_keys(location)   
        return self

    @allure.step("Get club name")
    def get_club_name(self):
        return self.wait_until_element_to_be_clickable(self.name).get_attribute("value")

    @allure.step("Get club phone")
    def get_club_phone(self):
        return self.wait_until_element_to_be_clickable(self.phone).get_attribute("value")

    @allure.step("Get club email")
    def get_club_email(self):
        return self.wait_until_element_to_be_clickable(self.email).get_attribute("value")

    @allure.step("Get club website")
    def get_club_website(self):
        return self.wait_until_element_to_be_clickable(self.website).get_attribute("value")

    @allure.step("Get club location")
    def get_club_location(self):
        return self.wait_until_element_to_be_clickable(self.location).get_attribute("value")


    @allure.step("Set opening / closign hours: ({day}): {opening_hr} \n {closing_hr}")
    def update_opening_closing_hours(self, day, opening_hr, closing_hr):
        opening_locator = (By.XPATH, f"//div[div[normalize-space()='{day}']]/input[1]")
        closing_locator = (By.XPATH, f"//div[div[normalize-space()='{day}']]/input[2]")
        opening_elem = self.wait_until_presence_of_element_located(opening_locator)
        closing_elem = self.wait_until_presence_of_element_located(closing_locator)
        self._set_time(opening_elem, opening_hr, closing_elem, closing_hr)
        return self

    @allure.step("Get opening hour single day")
    def get_opening_hour(self, day: str):
        opening_locator = (By.XPATH, f"//div[div[normalize-space()='{day}']]/input[1]")
        return self.wait_until_presence_of_element_located(opening_locator).get_attribute("value")[:5]

    @allure.step("Get closing hour single day")
    def get_closing_hour(self, day: str):
        closing_locator = (By.XPATH, f"//div[div[normalize-space()='{day}']]/input[2]")
        return self.wait_until_presence_of_element_located(closing_locator).get_attribute("value")[:5]


    @allure.step("Set opening / closing hours simultaneously (mo-fr): {opening_hr} \n {closing_hr}")
    def update_opening_closing_hours_mo_fr(self, opening_hr, closing_hr):
        opening_elem = self.wait_until_presence_of_element_located(self.opening_simultaneously)
        closing_elem = self.wait_until_presence_of_element_located(self.closing_simultaneously)
        self._set_time(opening_elem, opening_hr, closing_elem, closing_hr)
        # Click the apply button
        self.wait_until_element_to_be_clickable(self.apply_simultaneously).click()
        return self
    
    @allure.step("Get opening hour simultaneously")
    def get_opening_hour_simultaneously(self):
        return self.wait_until_presence_of_element_located(self.opening_simultaneously).get_attribute("value")

    @allure.step("Get closing hour simultaneously")
    def get_closing_hour_simultaneously(self):
        return self.wait_until_presence_of_element_located(self.closing_simultaneously).get_attribute("value")

    @allure.step("Upload club logo picture: {picture_name}")
    def update_logo_picture(self, picture_name):
        picture_path = str(Path(get_abs_path_to_tests(),"resource",picture_name))
        self.wait_until_presence_of_element_located(self.logo_pic).send_keys(picture_path)
        return self

    @allure.step("Upload clubpicture: {picture_name_list}")
    def upload_club_picture(self, picture_name_list: list):
        pics_to_upload = []    
        for picture in picture_name_list:
            pics_to_upload.append(str(Path(get_abs_path_to_tests(),"resource",picture)))
        
        self.wait_until_presence_of_element_located(self.club_pics).send_keys("\n".join(pics_to_upload))
        return self

    @allure.step("Save club profil")
    def save_profile(self):
        save = self.wait_until_presence_of_element_located(self.save_button)
        ActionChains(self.driver).move_to_element(save).click().perform()
        return self

        
    

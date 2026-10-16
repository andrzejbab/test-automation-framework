from selenium.webdriver.common.by import By
from ui.pom.components.user_settings_dropdown_component import UserSettingsDropdownComponent
from ui.pom.base.base_component import BaseComponent


class TopBarComponent(BaseComponent):
    def __init__(self, driver):
        super().__init__(driver)
        # Selectors
        self.caledar_icon_locator = (By.XPATH, "//button[@aria-label='Kalendarz klubowy']")
        # Components
        self.user_settings_dropdown: UserSettingsDropdownComponent = UserSettingsDropdownComponent(driver)

    def click_on_calendar(self):
        self.wait_until_element_to_be_clickable(self.caledar_icon_locator).click()
        # return calendar page
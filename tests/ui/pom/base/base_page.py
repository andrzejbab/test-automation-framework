from selenium.webdriver.common.by import By
from ui.pom.components.top_bar_component import TopBarComponent
from ui.pom.components.side_menu_component import ClubSideMenuComponent
from ui.pom.base.base import Base

class BasePage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        # Components
        self.top_bar = TopBarComponent(driver)
        self.side_menu = ClubSideMenuComponent(driver)
        
        # Locators
        self.cookie_accept_btn = (By.XPATH, "//button[contains(text(), 'Akceptuję')]")


    def handle_cookie_popup(self):
        self.wait_until_element_to_be_clickable(self.cookie_accept_btn).click()

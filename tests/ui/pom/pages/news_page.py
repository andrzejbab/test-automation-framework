from ui.pom.base.base_page import BasePage
from ui.pom.components.top_bar_component import UserSettingsDropdownComponent
from ui.pom.components.side_menu_component import ClubSideMenuComponent
from ui.pom.components.top_bar_component import TopBarComponent

class NewsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Components
        self.top_bar = TopBarComponent(driver)
        self.side_menu = ClubSideMenuComponent(driver)
        # Locators

    

    
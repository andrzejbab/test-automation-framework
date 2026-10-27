from ui.pom.base.base_page import BasePage
from selenium.webdriver.common.by import By
from ui.pom.components.add_user_modal_component import AddUserModalComponent


class MemberManagementPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Components
        self.add_modal_user_component = AddUserModalComponent(self.driver)

        # Locators
        self.add_club_member = (By.ID, "add-member-button")

    def add_member(self):
        self.wait_until_element_to_be_clickable(self.add_club_member).click()
        return self.add_modal_user_component


    

        

    
        
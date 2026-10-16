
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from ui.pom.base.base_component import BaseComponent



class ClubSideMenuComponent(BaseComponent):

    # collapse status for club management
    CLUB_MANAGEMENT_COLLAPSE_STATUS = False

    def __init__(self, driver):
        super().__init__(driver)
        # Components
        # Locators
        self.news = (By.ID, "sidebar-aktualnosci-btn")

        self.club_profile_collapse = (By.ID, "sidebar-club-toggle") 
        self.club_profile = (By.ID, "sidebar-profile-btn")

        #self.members = (By.ID, "sidebar-members-btn")


    def _open_club_management(self):
        if ClubSideMenuComponent.CLUB_MANAGEMENT_COLLAPSE_STATUS:
            return
        self.wait_until_element_to_be_clickable(self.club_profile_collapse).click()
        ClubSideMenuComponent.CLUB_MANAGEMENT_COLLAPSE_STATUS = True


    def go_to_create_club_profile(self):
        self._open_club_management()
        self.wait_until_element_to_be_clickable(self.club_profile).click()
        from ui.pom.pages.club_management.club_profile_page import ClubProfilePage
        return ClubProfilePage(self.driver)
    

    def go_to_news(self):
        self.wait_until_element_to_be_clickable(self.news).click()
        from ui.pom.pages.news_page import NewsPage
        return NewsPage(self.driver)

    
    def go_to_members(self):
        self._open_club_management()
        members_button = self.wait.until(EC.element_to_be_clickable(self.members))
        members_button.click()

  
        


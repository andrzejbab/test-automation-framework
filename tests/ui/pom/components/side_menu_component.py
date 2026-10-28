from selenium.webdriver.common.by import By
from ui.pom.base.base_component import BaseComponent
from selenium.common.exceptions import TimeoutException




class ClubSideMenuComponent(BaseComponent):

    def __init__(self, driver):
        super().__init__(driver)
        # Locators
        self.news = (By.ID, "sidebar-aktualnosci-btn")
        # Club management
        self.club_profile_toggle = (By.ID, "sidebar-club-toggle") 
        # Create club profile
        self.club_profile_btn = (By.ID, "sidebar-profile-btn")
        # Create members
        self.members_btn = (By.ID, "sidebar-members-btn")


    def _open_sidebar_menu_element(self, toggle_locator, btn_locator):
        try:
            # check if menu position already opened 
            elem_btn = self.change_driver_wait_time(1).wait_until_element_to_be_clickable(btn_locator)
            self.set_defualt_driver_wait_time()
            elem_btn.click()
        except TimeoutException:
            # open menu position
            self.set_defualt_driver_wait_time()
            self.wait_until_visibility_of_element_located(toggle_locator).click()
            self.wait_until_element_to_be_clickable(btn_locator).click()
        

    def go_to_news(self):
        self.wait_until_element_to_be_clickable(self.news, move_to_element=True).click()
        from ui.pom.pages.news_page import NewsPage
        return NewsPage(self.driver)

    def go_to_create_club_profile(self):
        self._open_sidebar_menu_element(self.club_profile_toggle, self.club_profile_btn)
        from ui.pom.pages.club_management.club_profile_page import ClubProfilePage
        return ClubProfilePage(self.driver)
      
    def go_to_manage_members(self):
        self._open_sidebar_menu_element(self.club_profile_toggle, self.members_btn)
        from ui.pom.pages.club_management.member_management_page import MemberManagementPage
        return MemberManagementPage(self.driver)

  
        


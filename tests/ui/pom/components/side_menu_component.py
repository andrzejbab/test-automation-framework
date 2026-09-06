
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ClubSideMenuComponent:
    CLUB_COLLAPSE_STATUS = False
    MESSAGE_COLLAPSE_STATUS = False

    def __init__(self, driver):
        self.driver = driver
        self.club = (By.ID, "sidebar-club-toggle")   
        self.profile = (By.ID, "sidebar-profile-btn")
        self.members = (By.ID, "sidebar-members-btn")
        self.wait = WebDriverWait(self.driver, 2)

    def _open_club(self):
        if ClubSideMenuComponent.CLUB_COLLAPSE_STATUS:
            return
        self.wait.until(EC.element_to_be_clickable(self.club))
        self.wait.until(EC.element_to_be_clickable(self.club)).click()
        ClubSideMenuComponent.CLUB_COLLAPSE_STATUS = True
    
    def go_to_profile(self):
        self._open_club()
        profile_button = self.wait.until(EC.element_to_be_clickable(self.profile))
        profile_button.click()

    def go_to_members(self):
        self._open_club()
        members_button = self.wait.until(EC.element_to_be_clickable(self.members))
        members_button.click()

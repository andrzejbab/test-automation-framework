
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.ui.pom.club_management.club_sidebar import ClubSidebar

class MemberManagementPage:
    def __init__(self, driver):
        self.driver = driver
        self.club_sidebar = ClubSidebar(driver)
        self.add_member_button = (By.ID, 'add-member-button')
        self.table_rows = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/table/tbody/tr')  # Select all rows in the table body
        self.wait = WebDriverWait(self.driver, 10)

    def click_add_member(self):
        self.club_sidebar.go_to_members()
        self.wait.until(EC.element_to_be_clickable(self.add_member_button)).click()

    def get_member(self):
        self.club_sidebar.go_to_members()
        rows = self.wait.until(EC.presence_of_all_elements_located(self.table_rows))
        members = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            member = {
                'first_name': cells[0].text,
                'last_name': cells[1].text,
                'email': cells[2].text,
                'roles': cells[3].text.split(', '),  # Assuming roles are comma-separated              
            }
            members.append(member)
        return members

        

    
        
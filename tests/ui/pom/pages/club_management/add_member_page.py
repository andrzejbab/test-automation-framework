from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddMemberPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.first_name_input = (By.ID, 'first-name')
        self.last_name_input = (By.ID, 'last-name')
        self.email_input = (By.ID, 'email')
        self.telephone_input = (By.ID, 'phone')
        self.role_player = (By.ID, 'role-Zawodnik')
        self.role_coach = (By.ID, 'role-Trener')
        self.role_parent = (By.ID, 'role-Rodzic')
        self.role_manager = (By.ID, 'role-Prezes')
        self.permission_klub_management = (By.ID, 'permission-1')
        self.permission_members_management = (By.ID, 'permission-2')
        self.permission_profile_edit = (By.ID, 'permission-3')
        self.save_button = (By.ID, 'save-member-button')

    def enter_first_name(self, first_name):
        first_name_field = self.wait.until(EC.visibility_of_element_located(self.first_name_input))
        first_name_field.clear()
        first_name_field.send_keys(first_name)
    
    def enter_last_name(self, last_name):
        last_name_field = self.wait.until(EC.visibility_of_element_located(self.last_name_input))
        last_name_field.clear()
        last_name_field.send_keys(last_name)

    def enter_email(self, email):
        email_field = self.wait.until(EC.visibility_of_element_located(self.email_input))
        email_field.clear()
        email_field.send_keys(email)

    def enter_telephone(self, telephone):
        telephone_field = self.wait.until(EC.visibility_of_element_located(self.telephone_input))
        telephone_field.clear()
        telephone_field.send_keys(telephone)    

    def select_role(self, role):
        role_locator = {
            'Zawodnik': self.role_player,
            'Trener': self.role_coach,
            'Rodzic': self.role_parent,
            'Prezes': self.role_manager
        }.get(role)

        if role_locator:
            role_element = self.wait.until(EC.element_to_be_clickable(role_locator))
            role_element.click()
        else:
            raise ValueError(f"Invalid role: {role}")
        
    def set_permission(self, permission, value=True):
        permission_locator = {
            'Klub Management': self.permission_klub_management,
            'Members Management': self.permission_members_management,
            'Profile Edit': self.permission_profile_edit
        }.get(permission)

        if permission_locator:
            permission_element = self.wait.until(EC.element_to_be_clickable(permission_locator))
            is_selected = permission_element.is_selected()
            if value != is_selected:
                permission_element.click()
        else:
            raise ValueError(f"Invalid permission: {permission}")
        
    def click_save(self):
        save_button_element = self.wait.until(EC.element_to_be_clickable(self.save_button))
        save_button_element.click()
        

import allure
from selenium.webdriver.common.by import By
from ui.pom.base.base_component import BaseComponent


class AddUserModalComponent(BaseComponent):

    def __init__(self, driver):
        super().__init__(driver)

        # Locators
        self.modal_locator = (By.XPATH, "//div[contains(@class, 'modal-body')]")
        self.modal = None

        self.first_name= (By.ID, 'first-name')
        self.last_name = (By.ID, 'last-name')
        self.email = (By.ID, 'email')
        self.phone = (By.ID, 'phone')
        self.no_email_available = (By.ID, 'member-no-email')

        # member roles
        self.role_player = (By.ID, 'role-zawodnik')
        self.role_coach = (By.ID, 'role-trener')
        self.role_parent = (By.ID, 'role-rodzic')
        self.role_manager = (By.ID, 'role-prezes')
        self.role_administrator = (By.ID, 'role-administrator')
        self.role_skarbinik = (By.ID, 'role-skarbnik')
        self.role_recepcja = (By.ID, 'role-recepcja')
        self.role_rekreacja = (By.ID, 'role-rekreacja')
        self.role_gosc = (By.ID, 'role-gosc')

        self.save_button = (By.ID, 'save-member-button')

    def wait_for_modal(self):
        if self.modal is None:
            self.modal = self.wait_until_visibility_of_element_located(self.modal_locator)
        return self.modal

    def _clear_and_send_keys(self, element, keys):
        element.clear()
        element.send_keys(keys)
        return element

    def _checkbox_selection(self, element, select=True): 
        if not element.is_selected() and select:
            element.click()
            return element
        if element.is_selected() and not select:
            element.click()
            return element
        return element
        

    @allure.step("Enter name: {name}")
    def enter_name(self, name: str):
        self._clear_and_send_keys(self.wait_for_modal().find_element(*self.first_name), name)
        return self

    @allure.step("Enter last name: {last_name}")
    def enter_last_name(self, last_name: str):
        self._clear_and_send_keys(self.wait_for_modal().find_element(*self.last_name), last_name)
        return self

    @allure.step("Enter email: {email}")
    def enter_email(self, email: str):
        self._clear_and_send_keys(self.wait_for_modal().find_element(*self.email), email)
        return self

    @allure.step("Set no email available: {}")
    def set_no_email_available(self, no_email: bool):
        self._checkbox_selection(self.wait_for_modal().find_element(*self.no_email_available), no_email)
        return self

    @allure.step("Enter phone: {phone}")
    def enter_phone(self, phone: str):
        self._clear_and_send_keys(self.wait_for_modal().find_element(*self.phone), phone)
        return self

    @allure.step("Set player: {}")
    def set_player(self, select: bool):
        self._checkbox_selection(self.wait_for_modal().find_element(*self.role_player), select)
        return self

    @allure.step("Set coach: {}")
    def set_coach(self, select: bool):
        self._checkbox_selection(self.wait_for_modal().find_element(*self.role_coach), select)
        return self

    @allure.step("Save member")
    def save_member(self):
        self.wait_until_element_to_be_clickable(self.save_button, move_to_element=True)
        
    #@allure.step("Set member role: {role}")
    #def set_member_role(self, role: str):
    #    self._checkbox_selection(self.wait_for_modal().find_element(*self.role_player))
    #    return self



  
        


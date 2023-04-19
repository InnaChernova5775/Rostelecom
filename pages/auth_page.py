from selenium.webdriver.common.by import By
from pages.base import BasePage


class AuthPageLocators:
    LOCATOR_TAB_EMAIL = (By.ID,'t-btn-tab-mail')
    LOCATOR_AUTH_EMAIL = (By.ID,'username')
    LOCATOR_AUTH_PASS = (By.ID, 'password')
    LOCATOR_AUTH_BTN_ENTER = (By.ID,'kc-login')
    LOCATOR_LINK_GO_TO_REGISTRATION = (By.ID, 'kc-register')
    LOCATOR_HEADING_AUTH_PAGE = (By.XPATH,'//*[@id="page-right"]/div/div/h1')


class AuthPageHelper(BasePage):
    def click_tab_email(self):
        return self.find_element(AuthPageLocators.LOCATOR_TAB_EMAIL).click()

    def enter_email(self, word):
        search_field_email=self.find_element(AuthPageLocators.LOCATOR_AUTH_EMAIL, time=15)
        search_field_email.click()
        search_field_email.send_keys(word)
        return search_field_email

    def enter_pass(self, word):
        search_field_pass = self.find_element(AuthPageLocators.LOCATOR_AUTH_PASS)
        search_field_pass.click()
        search_field_pass.send_keys(word)
        return search_field_pass

    def click_button_auth_enter(self):
        return self.find_element(AuthPageLocators.LOCATOR_AUTH_BTN_ENTER,time=2).click()

    def click_on_link_go_to_registration(self):
        return self.find_element(AuthPageLocators.LOCATOR_LINK_GO_TO_REGISTRATION).click()

    def get_text_heading(self):
        return self.find_element(AuthPageLocators.LOCATOR_HEADING_AUTH_PAGE).text

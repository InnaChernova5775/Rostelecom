from selenium.webdriver.common.by import By
from pages.base import BasePage

class RedirectPageLocators:
    LOCATOR_IN_NAVI_BAR=(By.ID,'lk-btn')
    LOCATOR_TRANSFER_TO_PERSONAL_ACCOUNT=(By.ID,'id_app_lk_b2c')
    LOCATOR_REDIRECT_BTN_EXIT =(By.ID,'logout-btn')

class RedirectHelper(BasePage):
    def check_navi_bar(self):
        return self.find_element(RedirectPageLocators.LOCATOR_IN_NAVI_BAR,time=15).text

    def click_transfer_to_personal_account(self):
        return self.find_element(RedirectPageLocators.LOCATOR_TRANSFER_TO_PERSONAL_ACCOUNT,time=15).click()

    def click_button_redirect_exit(self):
        return self.find_element(RedirectPageLocators.LOCATOR_REDIRECT_BTN_EXIT, time=2).click()

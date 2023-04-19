from selenium.webdriver.common.by import By
from pages.base import BasePage

class PhoneRightLocators:
    LOCATOR_PHONE_CONFIRMATION= (By.XPATH, '//*[@id="page-right"]/div/div/h1')

class PhoneRightHelper(BasePage):
    def get_text_heading_on_phone_confirm_page(self):
        return self.find_element(PhoneRightLocators.LOCATOR_PHONE_CONFIRMATION, time = 12).text


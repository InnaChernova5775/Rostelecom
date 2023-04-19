from pages.base import BasePage
from selenium.webdriver.common.by import By


class EmailRightLocators:
    LOCATOR_EMAIL_CONFIRMATION=(By.XPATH,'//h1[@class="card-container__title"]')

class EmailRightHelper(BasePage):
    def get_text_heading_on_email_confirm_page(self):
        return self.find_element(EmailRightLocators.LOCATOR_EMAIL_CONFIRMATION, time = 12).text
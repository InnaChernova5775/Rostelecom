from selenium.webdriver.common.by import By
from pages.base import BasePage

class PersonalAccountLocators:
    LOCATOR_ELEM_PERSONAL_NAVI_BAR=(By.XPATH,'//p[@class="sc-dkPtRN.iqfMlY"][contains(text(),"Оплата услуг")]')
    LOCATOR_BUTTON_FOR_ME=(By.XPATH,'//p[@class="sc-dkPtRN klWXSP"][text()="Для меня"]')

class PersonalAccountHelper(BasePage):
    def check_personal_navi_bar(self):
        return self.find_element(PersonalAccountLocators.LOCATOR_BUTTON_FOR_ME, time=30).text




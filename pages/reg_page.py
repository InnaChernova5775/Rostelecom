from selenium.webdriver.common.by import By
from pages.base import BasePage


class RegPageLocators:
    LOCATOR_FIRST_NAME = (By.NAME, 'firstName')
    LOCATOR_LAST_NAME = (By.NAME, 'lastName')
    LOCATOR_REGION = (By.XPATH, '//div[@class="rt-input-container rt-select__input"]//input[@class="rt-input__input '\
                                'rt-input__input--rounded rt-input__input--orange"]')
    LOCATOR_AREA_1 = (By.XPATH, '//div[5]')
    LOCATOR_AREA_2 = (By.XPATH, '//div[8]')
    LOCATOR_EMAIL_AND_PHONE = (By.ID, 'address')
    LOCATOR_PASSWORD = (By.ID, 'password')
    LOCATOR_PASSWORD_CONFIRMATION = (By.ID, 'password-confirm')
    LOCATOR_REGISTER_BUTTON = (By.XPATH, '//button[text()=" Зарегистрироваться "]')
    LOCATOR_LINK_TO_AGREEMENT_UNDER_REG_FORM = (By.XPATH, '//a[@class="rt-link rt-link--orange"]')
    LOCATOR_LINK_TO_AGREEMENT_IN_FOOTER = (By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[2]')
    LOCATOR_LINK_TO_PRIVACY_POLICY_IN_FOOTER = (By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[1]')
    LOCATOR_AGREEMENT= (By.XPATH,'//*[@id="title"]/h1/text()')
    LOCATOR_ERROR_LETTERS_NUMBER_IN_NAME = (By.XPATH,'//span[@class="rt-input-container__meta rt-input-container__meta--error"]')
    LOCATOR_ERROR_EMAIL_OR_PHONE= (By.XPATH,'//span[contains(text(),"Введите телефон в формате +7ХХХХХХХХХХ '
                                            'или +375XXXXXXXXX, или email в формате example@email.ru")]')
    LOCATOR_ERROR_PASS_MIN_LEN= (By.XPATH,'//span[contains(text(),"Длина пароля должна быть не менее 8 символов")]')
    LOCATOR_ERROR_PASS_MAX_LEN = (By.XPATH,'//span[contains(text(),"Длина пароля должна быть не более 20 символов")]')
    LOCATOR_ERROR_PASS_RUS = (By.XPATH,'//span[contains(text(),"Пароль должен содержать только латинские буквы")]')
    LOCATOR_ERROR_PASS_DIGIT = (By.XPATH,'//span[contains(text(),"Пароль должен содержать хотя бы одну заглавную букву")]')
    LOCATOR_ERROR_PASS_LATIN = (By.XPATH,'//span[contains(text(),"Пароль должен содержать хотя бы 1 спецсимвол или хотя'
                                          ' бы одну цифру")]')
    LOCATOR_ERROR_CONFIRM_PASS = (By.XPATH,'//span[contains(text(),"Пароли не совпадают")]')


class RegPageHelper(BasePage):
    def enter_first_name(self, word):
        first_name_field = self.find_element(RegPageLocators.LOCATOR_FIRST_NAME)
        first_name_field.click()
        first_name_field.send_keys(word)
        return first_name_field

    def enter_last_name(self, word):
        last_name_field = self.find_element(RegPageLocators.LOCATOR_LAST_NAME)
        last_name_field.click()
        last_name_field.send_keys(word)
        return last_name_field

    def select_region(self):
        region_name_field = self.find_element(RegPageLocators.LOCATOR_REGION)
        region_name_field.click()
        region_name_field = self.find_element(RegPageLocators.LOCATOR_AREA_1)
        region_name_field.click()
        return region_name_field


    def select_other_region(self):
        region_name_field = self.find_element(RegPageLocators.LOCATOR_REGION)
        region_name_field.click()
        region_name_field = self.find_element(RegPageLocators.LOCATOR_AREA_2)
        region_name_field.click()
        return region_name_field


    def enter_email_or_phone(self, word):
        field_email_or_phone = self.find_element(RegPageLocators.LOCATOR_EMAIL_AND_PHONE)
        field_email_or_phone.click()
        field_email_or_phone.send_keys(word)
        return field_email_or_phone

    def enter_password_for_registration(self, word):
        pass_for_reg = self.find_element(RegPageLocators.LOCATOR_PASSWORD)
        pass_for_reg.click()
        pass_for_reg.send_keys(word)
        return pass_for_reg

    def enter_password_for_comfirmation(self, word):
        pass_for_comfirmation = self.find_element(RegPageLocators.LOCATOR_PASSWORD_CONFIRMATION)
        pass_for_comfirmation.click()
        pass_for_comfirmation.send_keys(word)
        return pass_for_comfirmation

    def click_on_button_registration(self):
        return self.find_element(RegPageLocators.LOCATOR_REGISTER_BUTTON).click()

    def click_on_link_to_agreement_under_reg_form(self):
        return self.find_element(RegPageLocators.LOCATOR_LINK_TO_AGREEMENT_UNDER_REG_FORM).click()

    def click_on_link_to_agreement_in_footer(self):
        return self.find_element(RegPageLocators.LOCATOR_LINK_TO_AGREEMENT_IN_FOOTER).click()

    def click_on_link_to_privacy_policy_in_footer(self):
        return self.find_element(RegPageLocators.LOCATOR_LINK_TO_PRIVACY_POLICY_IN_FOOTER).click()

    def check_error_letters_number_in_name(self):
        return self.find_element(RegPageLocators.LOCATOR_ERROR_LETTERS_NUMBER_IN_NAME).text

    def check_error_in_email_or_phone(self):
        return self.find_element(RegPageLocators.LOCATOR_ERROR_EMAIL_OR_PHONE).text

    def check_error_in_password_min_len(self):
        return self.find_element(RegPageLocators.LOCATOR_ERROR_PASS_MIN_LEN).text

    def check_error_in_password_max_len(self):
        return self.find_element(RegPageLocators.LOCATOR_ERROR_PASS_MAX_LEN).text

    def check_error_in_password_rus(self):
        return self.find_element(RegPageLocators.LOCATOR_ERROR_PASS_RUS).text

    def check_error_in_password_digit(self):
        return self.find_element(RegPageLocators.LOCATOR_ERROR_PASS_DIGIT).text

    def check_error_in_password_latin(self):
        return self.find_element(RegPageLocators.LOCATOR_ERROR_PASS_LATIN).text

    def check_error_incorrect_confirm_pass(self):
        return self.find_element(RegPageLocators.LOCATOR_ERROR_CONFIRM_PASS).text

    def transition_to_agreement_by_link_under_reg_form (self):
        return self.find_element(RegPageLocators.LOCATOR_LINK_TO_AGREEMENT_UNDER_REG_FORM).click()



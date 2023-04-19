import pytest


def generate_string_from_rus_chars(n):
    return "ц" * n
def generate_string_from_latin_chars(n):
    return "q" * n

def generate_multiple_digit(n):
    return int('5'* n)

def special_chars():
    return '|\\/@#$%^&*()-_=+`~?"№;:[]{}'


def test_registration_with_valid_min_values_in_name(browser, auth_page, reg_page, phone_confirm_page):
    auth_page.go_to_site()
    auth_page.click_on_link_go_to_registration()
    reg_page.enter_first_name('Ян')
    reg_page.enter_last_name('Чи')
    reg_page.select_region()
    reg_page.enter_email_or_phone('+79170000000')
    reg_page.enter_password_for_registration('AsdAsda$') #8 сиволов- граница
    reg_page.enter_password_for_comfirmation('AsdAsda$')
    reg_page.click_on_button_registration()
    assert"Подтверждение телефона"in phone_confirm_page.get_text_heading_on_phone_confirm_page()


def test_registration_with_valid_number_phone(browser, auth_page, reg_page, phone_confirm_page):
    auth_page.go_to_site()
    auth_page.click_on_link_go_to_registration()
    reg_page.enter_first_name('Лия')
    reg_page.enter_last_name('Яни')
    reg_page.select_other_region()
    reg_page.enter_email_or_phone('+375111111111')
    reg_page.enter_password_for_registration('Asdasd111')
    reg_page.enter_password_for_comfirmation('Asdasd111')
    reg_page.click_on_button_registration()
    assert"Подтверждение телефона"in phone_confirm_page.get_text_heading_on_phone_confirm_page()



@pytest.mark.parametrize("param",
                         [generate_string_from_rus_chars(29),generate_string_from_rus_chars(30),generate_string_from_rus_chars(30).upper()],
                          ids=['29 russian symbols','30 russian symbols', '30 RUSSIAN SYMBOLS'])
def test_registration_with_valid_max_values_in_name(browser,param, auth_page, reg_page, phone_confirm_page):
    auth_page.go_to_site()
    auth_page.click_on_link_go_to_registration()
    reg_page.enter_first_name(word = param)
    reg_page.enter_last_name(word = param)
    reg_page.select_region()
    reg_page.enter_email_or_phone('+375111111111')
    reg_page.enter_password_for_registration('As111111')
    reg_page.enter_password_for_comfirmation('As111111')
    reg_page.click_on_button_registration()
    assert"Подтверждение телефона"in phone_confirm_page.get_text_heading_on_phone_confirm_page()



@pytest.mark.parametrize("param",
                         [generate_string_from_latin_chars(7)+'1'+'Q', generate_string_from_latin_chars(17)+'&'+'Q',
                          generate_string_from_latin_chars(18)+'&'+'Q'],
                          ids=['9 valid symbols','19 valid symbols','19 valid symbols'])
def test_registration_with_valid_values_password(browser,param, auth_page, reg_page, email_confirm_page):
    auth_page.go_to_site()
    auth_page.click_on_link_go_to_registration()
    reg_page.enter_first_name('Анна-Мария')
    reg_page.enter_last_name('Федосеева-Шукшина')
    reg_page.select_other_region()
    reg_page.enter_email_or_phone('popular55441@mail.ru')
    reg_page.enter_password_for_registration(word= param)
    reg_page.enter_password_for_comfirmation(word= param)
    reg_page.click_on_button_registration()
    assert "Подтверждение email"in email_confirm_page.get_text_heading_on_email_confirm_page()



@pytest.mark.parametrize("param",
                         ['ф',generate_string_from_rus_chars(31), generate_string_from_rus_chars(501),
                          generate_string_from_latin_chars(30),special_chars(), 12345],
                          ids=['1 rus symbol','31 rus symbols','len> 501 rus symbols','30 latin symbol',
                               'specials','digit'])
def test_negativ_field_first_name(browser,param, auth_page, reg_page):
    auth_page.go_to_site()
    auth_page.click_on_link_go_to_registration()
    reg_page.enter_first_name(word=param)
    reg_page.select_region()
    assert "Необходимо заполнить поле кириллицей. От 2 до 30 символов."in reg_page.check_error_letters_number_in_name()




def test_negativ_with_empty_field_first_name(browser, auth_page, reg_page):
    auth_page.go_to_site()
    auth_page.click_on_link_go_to_registration()
    reg_page.enter_first_name('')
    reg_page.enter_last_name('Федосеева-Шукшина')
    reg_page.select_other_region()
    reg_page.enter_email_or_phone('popular55441@mail.ru')
    reg_page.enter_password_for_registration('Asdasdas1')
    reg_page.enter_password_for_comfirmation('Asdasdas1')
    reg_page.click_on_button_registration()
    assert "Необходимо заполнить поле кириллицей. От 2 до 30 символов."in reg_page.check_error_letters_number_in_name()



@pytest.mark.parametrize("param",
                         ['ф',generate_string_from_rus_chars(31), generate_string_from_rus_chars(501),
                          generate_string_from_latin_chars(30),special_chars(), 12345],
                          ids=['1 rus symbol','31 rus symbols','len> 500 rus symbols','30 latin symbol',
                               'specials','digit'])
def test_negativ_field_last_name(browser,param, auth_page, reg_page):
    auth_page.go_to_site()
    auth_page.click_on_link_go_to_registration()
    reg_page.enter_first_name('Анна-Мария')
    reg_page.enter_last_name(word=param)
    reg_page.select_other_region()
    assert "Необходимо заполнить поле кириллицей. От 2 до 30 символов." in reg_page.check_error_letters_number_in_name()



def test_negativ_with_empty_field_last_name(browser, auth_page, reg_page):
    auth_page.go_to_site()
    auth_page.click_on_link_go_to_registration()
    reg_page.enter_first_name('Светлана')
    reg_page.enter_last_name('')
    reg_page.select_other_region()
    reg_page.enter_email_or_phone('popular55441@mail.ru')
    reg_page.enter_password_for_registration('Asdasdas1')
    reg_page.enter_password_for_comfirmation('Asdasdas1')
    reg_page.click_on_button_registration()
    assert "Необходимо заполнить поле кириллицей. От 2 до 30 символов."in reg_page.check_error_letters_number_in_name()


def test_negativ_with_empty_field_email_or_phone(browser, auth_page, reg_page):
    auth_page.go_to_site()
    auth_page.click_on_link_go_to_registration()
    reg_page.enter_first_name('Светлана')
    reg_page.enter_last_name('Федосеева-Шукшина')
    reg_page.select_other_region()
    reg_page.enter_email_or_phone('')
    reg_page.enter_password_for_registration('Asdasdas1')
    reg_page.enter_password_for_comfirmation('Asdasdas1')
    reg_page.click_on_button_registration()
    text_error="Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
    assert text_error in reg_page.check_error_in_email_or_phone()


@pytest.mark.parametrize("param",
                         [0,5,generate_multiple_digit(500),generate_multiple_digit(13),generate_multiple_digit(12),
                          generate_multiple_digit(11),generate_multiple_digit(10),generate_string_from_latin_chars(10),
                          special_chars()],
                          ids=['zero','1 digit','500 digits','13 digits','12 digits','11 digits','10 digits',
                               'latin_symbols','specials'])
def test_negativ_with_invalid_number_phone(browser,param, auth_page, reg_page):
    auth_page.go_to_site()
    auth_page.click_on_link_go_to_registration()
    reg_page.enter_email_or_phone(word=param)
    reg_page.enter_password_for_registration('')
    text_error = "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
    assert text_error in reg_page.check_error_in_email_or_phone()


@pytest.mark.parametrize("param",
                         ['+37511111111','+3751111111111','+7111 111 111', '+7111 111 111 11'],
                          ids=['11 digits','13 digits','10 digits','12 digits'])
def test_negativ_with_invalid_mask_number_phone(browser,param, auth_page, reg_page):
    auth_page.go_to_site()
    auth_page.click_on_link_go_to_registration()
    reg_page.enter_email_or_phone(word=param)
    reg_page.enter_password_for_registration('')
    text_error = "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
    assert text_error in reg_page.check_error_in_email_or_phone()


@pytest.mark.parametrize("param",
                         ['@mail.ru',' @mail.ru'],
                          ids=['not symbol','spacing'])
def test_negativ_with_invalid_mask_email(browser,param, auth_page, reg_page):
    auth_page.go_to_site()
    auth_page.click_on_link_go_to_registration()
    reg_page.enter_email_or_phone(word=param)
    reg_page.click_on_button_registration()
    text_error = "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
    assert text_error in reg_page.check_error_in_email_or_phone()




@pytest.mark.skip(reason="Баги в продукте-описаны в баг-репорте")
@pytest.mark.parametrize("param",
                         ['%!!%@mail.ru','1@mail.ru','0@mail.ru',generate_string_from_latin_chars(1)+'@mail.ru',
                             generate_string_from_latin_chars(1001)+'@mail.ru'],
                          ids=['special','1 digit','zero','1 latin symbol', '1001 latin symbol'])
def test_negativ_with_invalid_mask_email_in_reg_form(browser,param, auth_page, reg_page):
    auth_page.go_to_site()
    auth_page.click_on_link_go_to_registration()
    reg_page.enter_first_name('Светлана')
    reg_page.enter_last_name('Федосеева-Шукшина')
    reg_page.enter_email_or_phone(word=param)
    reg_page.enter_password_for_registration('Asdasdas1')
    reg_page.enter_password_for_comfirmation('Asdasdas1')
    reg_page.click_on_button_registration()
    text_error = "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
    assert text_error in reg_page.check_error_in_email_or_phone()


@pytest.mark.parametrize("param",
                         ['',' ',generate_string_from_latin_chars(1),generate_string_from_latin_chars(7)],
                          ids=['empty str','spacing','1 symbol','7 latin symbols'])
def test_negativ_with_invalid_password_min_len(browser,param, auth_page, reg_page):
    auth_page.go_to_site()
    auth_page.click_on_link_go_to_registration()
    reg_page.enter_first_name('Иван')
    reg_page.enter_last_name('Петров')
    reg_page.enter_email_or_phone('12345@mail.ru')
    reg_page.enter_password_for_registration(word=param)
    reg_page.enter_password_for_comfirmation('')
    reg_page.click_on_button_registration()
    assert "Длина пароля должна быть не менее 8 символов"in reg_page.check_error_in_password_min_len()


@pytest.mark.parametrize("param",
                         [generate_string_from_latin_chars(21),generate_string_from_latin_chars(1001),special_chars(),
                          generate_multiple_digit(21)],
                          ids=['21 latin symbol', '1001 latin symbol','len>20 special', 'len>20 digits'])
def test_negativ_with_invalid_password_max_len(browser,param, auth_page, reg_page):
    auth_page.go_to_site()
    auth_page.click_on_link_go_to_registration()
    reg_page.enter_first_name('Иван')
    reg_page.enter_last_name('Петров')
    reg_page.enter_email_or_phone('12345@mail.ru')
    reg_page.enter_password_for_registration(word=param)
    reg_page.enter_password_for_comfirmation('')
    reg_page.click_on_button_registration()
    assert "Длина пароля должна быть не более 20 символов" in reg_page.check_error_in_password_max_len()


@pytest.mark.parametrize("param",
                         [generate_string_from_rus_chars(20),generate_string_from_rus_chars(8).upper()],
                          ids=['20 rus symbol', '8 RUS SIMBOLS'])
def test_negativ_with_invalid_password_from_rus_symbols(browser,param, auth_page, reg_page):
    auth_page.go_to_site()
    auth_page.click_on_link_go_to_registration()
    reg_page.enter_first_name('Иван')
    reg_page.enter_last_name('Петров')
    reg_page.enter_email_or_phone('12345@mail.ru')
    reg_page.enter_password_for_registration(word=param)
    reg_page.enter_password_for_comfirmation('')
    reg_page.click_on_button_registration()
    assert "Пароль должен содержать только латинские буквы" in reg_page.check_error_in_password_rus()


@pytest.mark.parametrize("param",
                         [generate_multiple_digit(8),'%^&**+!()'],
                          ids=['8 digits','9 special'])
def test_negativ_with_invalid_password_from_digits_and_special(browser,param, auth_page, reg_page):
    auth_page.go_to_site()
    auth_page.click_on_link_go_to_registration()
    reg_page.enter_first_name('Иван')
    reg_page.enter_last_name('Петров')
    reg_page.enter_email_or_phone('12345@mail.ru')
    reg_page.enter_password_for_registration(word=param)
    reg_page.enter_password_for_comfirmation('')
    reg_page.click_on_button_registration()
    assert "Пароль должен содержать хотя бы одну заглавную букву" in reg_page.check_error_in_password_digit()

@pytest.mark.parametrize("param",
                         [generate_string_from_latin_chars(20),generate_string_from_latin_chars(8).upper()],
                          ids=['20 latin lower','8 latin upper'])
def test_negativ_with_invalid_password_from_latin(browser,param, auth_page, reg_page):
    auth_page.go_to_site()
    auth_page.click_on_link_go_to_registration()
    reg_page.enter_first_name('Иван')
    reg_page.enter_last_name('Петров')
    reg_page.enter_email_or_phone('12345@mail.ru')
    reg_page.enter_password_for_registration(word=param)
    reg_page.enter_password_for_comfirmation('')
    reg_page.click_on_button_registration()
    assert "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру" in reg_page.check_error_in_password_latin()


def test_with_incorrect_confirmation_password(browser, auth_page, reg_page):
    auth_page.go_to_site()
    auth_page.click_on_link_go_to_registration()
    reg_page.enter_first_name('Иван')
    reg_page.enter_last_name('Петров')
    reg_page.select_region()
    reg_page.enter_email_or_phone('12345@mail.ru')
    reg_page.enter_password_for_registration('QQQ555qqq')
    reg_page.enter_password_for_comfirmation('QQQ444qq')
    reg_page.click_on_button_registration()
    assert "Пароли не совпадают" in reg_page.check_error_incorrect_confirm_pass()

def test_Link_agreement_under_reg_form(browser,auth_page, reg_page):
    auth_page.go_to_site()
    auth_page.click_on_link_go_to_registration()
    window_before = browser.window_handles[0]
    reg_page.click_on_link_to_agreement_under_reg_form()
    window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)
    assert browser.title =='User agreement'

def test_Link_agreement_in_footer(browser,auth_page, reg_page):
    auth_page.go_to_site()
    auth_page.click_on_link_go_to_registration()
    window_before = browser.window_handles[0]
    reg_page.click_on_link_to_agreement_in_footer()
    window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)
    assert browser.title == 'Ростелеком ID'


def test_Link_privacy_policy_in_footer(browser,auth_page, reg_page):
    auth_page.go_to_site()
    auth_page.click_on_link_go_to_registration()
    window_before = browser.window_handles[0]
    reg_page.click_on_link_to_privacy_policy_in_footer()
    window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)
    assert browser.title == 'Ростелеком ID'
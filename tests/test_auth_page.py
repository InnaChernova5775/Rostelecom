import time

def test_authorization_by_email_and_password_pozitiv(browser, auth_page,redirect_page):
    auth_page.go_to_site()
    auth_page.click_tab_email()
    auth_page.enter_email('innachernova5775@mail.ru')
    auth_page.enter_pass('12345678910Aa')
    auth_page.click_button_auth_enter()
    assert"Личный кабинет" in redirect_page.check_navi_bar()
    redirect_page.click_button_redirect_exit()


def test_tranfer_to_personal_pade(browser, auth_page, redirect_page, personal_page):
    """Tест перехода с страницы авторизации а страницу redirect_page а потом  на
    страницу личного кабинета"""
    auth_page.go_to_site()
    auth_page.click_tab_email()
    auth_page.enter_email('innachernova5775@mail.ru')
    auth_page.enter_pass('12345678910Aa')
    auth_page.click_button_auth_enter()
    redirect_page.click_transfer_to_personal_account()
    assert "Для меня" in personal_page.check_personal_navi_bar()


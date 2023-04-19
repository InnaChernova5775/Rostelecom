import pytest
from selenium import webdriver
from pages.auth_page import AuthPageHelper
from pages.reg_page import RegPageHelper
from pages.redirect_page import RedirectHelper
from pages.personal_page import PersonalAccountHelper
from pages.phone_confirm_page import PhoneRightHelper
from pages.email_confirm_page import EmailRightHelper


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.set_window_size(1400, 1000)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def auth_page(browser):
    auth_page = AuthPageHelper(browser)
    return auth_page

@pytest.fixture(scope="session")
def reg_page(browser):
    reg_page = RegPageHelper(browser)
    return reg_page

@pytest.fixture(scope="session")
def redirect_page(browser):
    redirect_page = RedirectHelper(browser)
    return redirect_page

@pytest.fixture(scope="session")
def phone_confirm_page(browser):
    phone_confirm_page = PhoneRightHelper(browser)
    return phone_confirm_page

@pytest.fixture(scope="session")
def email_confirm_page(browser):
    email_confirm_page = EmailRightHelper(browser)
    return email_confirm_page

@pytest.fixture(scope="session")
def personal_page(browser):
    personal_page = PersonalAccountHelper(browser)
    return personal_page
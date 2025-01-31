import pytest
from selenium import webdriver
import requests
from helpers import *

from faker import Faker

from locators.login_page_locators import *
from page.login_page import LoginPage
from urls import *


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        # options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
    elif request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--window-size=1920,1080")
        # options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(3)
    yield driver
    driver.quit()


@pytest.fixture()
def login():
    data_user, response = create_new_user()
    yield data_user
    access_token = data_user.get('accessToken')
    delete_user(access_token)


@pytest.fixture()
def authorization(driver, login):
    email = login['email']
    password = login['password']
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.send_email(email)
    login_page.send_password(password)
    login_page.click_button_login()
    login_page.check_order()
    return {'driver': driver, 'email': email}

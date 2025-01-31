import allure
from page.login_page import LoginPage
from page.profile_page import ProfilePage

from urls import *


@allure.suite("Личный кабинет")
class TestPersonalAccount:

    @allure.title('Тест переход по клику на «Личный кабинет»')
    def test_click_account_button_is_opened_profile_page(self, driver):
        login_page = LoginPage(driver)
        # Открыть основную страницу
        login_page.open_main_page()
        # Найдем и нажмем на кнопку "Личный кабинет"
        login_page.click_lk_button()
        assert login_page.check_form_login()  # Проверяем, найден ли элемент формы логина
        assert login_page.get_current_page_url() == LOGIN_URL

    @allure.title('Тест переход в раздел «История заказов»')
    def test_click_button_history_is_opened_order_history(self, authorization):
        driver = authorization['driver']
        profile_page = ProfilePage(driver)
        profile_page.open_profile_page()
        profile_page.click_order_history_button()
        assert profile_page.get_current_page_url() == ORDER_HISTORY_PROFILE_PAGE_URL

    @allure.title('Тест выход из аккаунта')
    def test_logout_profile_is_open_login_page(self, authorization):
        driver = authorization['driver']
        profile_page = ProfilePage(driver)
        profile_page.open_profile_page()
        profile_page.click_logout_profile_button()
        assert profile_page.get_current_page_url() and profile_page.get_current_page_url() == LOGIN_URL

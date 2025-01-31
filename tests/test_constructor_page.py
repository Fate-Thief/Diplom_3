import allure

from locators.main_page_locators import LOADER_OVERLAY
from page.constructor_page import ConstructorPage
from urls import *


@allure.suite("Проверка основного функционала")
class TestDesignerFunctional:

    @allure.title('Тест переход по клику на «Лента заказов» с основной страницы')
    def test_click_order_feed_button_is_opened_main_page(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_main_page()
        constructor_page.click_order_feed_button()
        constructor_page.wait_invisibility_element(LOADER_OVERLAY)
        assert constructor_page.get_current_page_url() == ORDER_FEED_PAGE_URL

    @allure.title('Тест переход по клику на «Конструктор» из ленты заказов')
    def test_click_constructor_button_is_opened_order_page(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_order_page()
        constructor_page.click_constructor_button()
        assert constructor_page.get_current_page_url() == BASE_URL + "/"

    @allure.title('Тест, если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient_is_opened_info_ingredient(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_main_page()
        constructor_page.click_ingredient()
        assert constructor_page.check_info_ingredient()

    @allure.title('Тест всплывающее окно закрывается кликом по крестику')
    def test_click_close_button_closed_info_ingredient(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_main_page()
        constructor_page.click_ingredient()
        constructor_page.check_info_ingredient()
        constructor_page.click_close_info_ingredient()
        assert constructor_page.wait_invisibility_info_ingredient()

    @allure.title('Тест при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_add_ingredient_is_increase_counter_ingredient(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_main_page()
        constructor_page.add_ingredient()
        assert constructor_page.get_ingredient_counter_text() == "2"

    @allure.title('Тест залогиненный пользователь может оформить заказ')
    def test_login_user_can_order(self, authorization):
        driver = authorization['driver']
        constructor_page = ConstructorPage(driver)
        constructor_page.open_main_page()
        constructor_page.add_ingredient()
        constructor_page.click_create_order_button()
        assert constructor_page.check_window_start_prepare_order()

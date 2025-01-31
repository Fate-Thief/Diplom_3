import allure

from locators.constructor_page_locators import *
from locators.main_page_locators import LOADER_OVERLAY
from page.main_page import MainPage


class ConstructorPage(MainPage):

    @allure.step("Нажать на ингредиент")
    def click_ingredient(self):
        self.wait_and_find_element(COUNTER_INGREDIENT).click()
        self.wait_invisibility_element(LOADER_OVERLAY)

    @allure.step("Ожидание информации по ингредиенту")
    def check_info_ingredient(self):
        return self.wait_and_find_element(INFO_INGREDIENT)

    @allure.step("Закрыть описание  ингредиента")
    def click_close_info_ingredient(self):
        self.wait_and_find_element(CLOSE_INFO_INGREDIENT_BUTTON).click()

    @allure.step("Ожидание закрытия окна с информацией по  ингредиенту")
    def wait_invisibility_info_ingredient(self):
        return self.wait_invisibility_element(INFO_INGREDIENT)

    @allure.step("Перенос ингридиента в Заказ")
    def add_ingredient(self):
        ingredient_element = self.wait_and_find_element(ELEMENT_INGREDIENT)
        order = self.wait_and_find_element(SPACE_ORDER)
        self.drag_and_drop(ingredient_element, order)
        self.wait_invisibility_element(LOADER_OVERLAY)

    @allure.step("Получить текст каунтера")
    def get_ingredient_counter_text(self):
        return self.get_text(COUNTER_INGREDIENT)

    @allure.step("Нажать кнопку Оформить заказ")
    def click_create_order_button(self):
        self.wait_and_find_element(PLACE_ORDER_BUTTON).click()
        self.wait_invisibility_element(LOADER_OVERLAY)

    @allure.step("Нажать кнопку Закрыть окно Заказ создан")
    def click_close_place_order(self):
        self.wait_and_find_element(CLOSE_WINDOW_START_ORDER_BUTTON).click()

    @allure.step("Создание заказа")
    def create_order(self):
        self.open_main_page()
        self.add_ingredient()
        self.click_create_order_button()
        self.wait_invisibility_element(LOADER_OVERLAY)
        new_number_order = self.get_text(NUMBER_INFO_ORDER)
        self.click_close_place_order()
        return new_number_order

    @allure.step("Ожидание окна Заказ создан")
    def check_window_start_prepare_order(self):
        return self.wait_and_find_element(WINDOW_START_PREPARE_ORDER)

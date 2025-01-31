import allure

from locators.main_page_locators import *
from locators.order_feed_locators import *
from page.main_page import MainPage


class OrderFeedPage(MainPage):

    @allure.step("Проверить исчезновение заголовка 'Все текущие заказы готовы!'")
    def wait_for_orders_ready_invisibility(self):
        self.wait_invisibility_element(ALL_ORDERS_READY)

    @allure.step("Получить текст текущих заказов")
    def get_orders_in_work_text(self):
        return self.get_text(ORDERS_IN_WORK)

    @allure.step("Нажать на созданный заказ")
    def click_order_in_history(self):
        self.wait_and_find_element(NUMBERS_ORDER_IN_HISTORY).click()

    @allure.step("Ожидание окна с  информацией о заказе")
    def check_window_info_order(self):
        return self.wait_and_find_element(INFO_ORDER)

    @allure.step("Нажать кнопку история заказов")
    def click_order_history_button(self):
        self.wait_invisibility_element(LOADER_OVERLAY)
        self.wait_and_find_element(ORDER_HISTORY_BUTTON).click()

    @allure.step("Получить номер последнего заказа из История заказов")
    def get_last_order(self):
        element = self.wait_and_find_element(NUMBERS_ORDER_IN_HISTORY)
        return element.text if element else None

    @allure.step("Проверить существование последнего номера заказа в Ленте заказов")
    def get_check_number_order(self, last_order):
        locator = (LAST_ORDER_NUMBER[0], LAST_ORDER_NUMBER[1].format(last_order=last_order))
        return self.wait_and_find_element(locator)

    @allure.step("Получить значение каунтера 'Выполнено за всё время'")
    def get_all_time_count(self):
        return int(self.get_text(ALL_TIME_ORDERS))

    @allure.step("Получить значение каунтера 'Выполнено за сегодня'")
    def get_day_time_count(self):
        return int(self.get_text(DAY_ORDERS))

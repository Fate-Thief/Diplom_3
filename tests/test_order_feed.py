import allure

from page.constructor_page import ConstructorPage
from page.order_feed_page import OrderFeedPage


@allure.suite("Проверка основного функционала (Конструктор)")
class TestOrderFeed:

    @allure.title('Тест если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_is_opened_order_info(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order_page()
        order_feed_page.click_order_in_history()
        assert order_feed_page.check_window_info_order()

    @allure.title('Тест после оформления заказа его номер появляется в разделе В работе')
    def test_new_order_after_create_have_in_work(self, authorization):
        driver = authorization['driver']
        constructor_page = ConstructorPage(driver)
        order_feed_page = OrderFeedPage(driver)
        new_number_order = constructor_page.create_order()
        constructor_page.click_order_feed_button()
        order_feed_page.wait_for_orders_ready_invisibility()
        assert new_number_order in order_feed_page.get_orders_in_work_text()

    @allure.title('Тест заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_order_history_have_in_order_feed(self, authorization):
        driver = authorization['driver']
        constructor_page = ConstructorPage(driver)
        order_feed_page = OrderFeedPage(driver)
        # создание заказа
        constructor_page.create_order()
        # открыть профиль и историю заказа
        order_feed_page.open_profile_page()
        order_feed_page.click_order_history_button()
        # получить последний заказ
        order_from_history = order_feed_page.get_last_order()
        order_feed_page.open_order_page()
        assert order_feed_page.get_check_number_order(order_from_history)

    @allure.title('Тест при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_new_order_change_all_time_order(self, authorization):
        driver = authorization['driver']
        constructor_page = ConstructorPage(driver)
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order_page()
        all_time_order = order_feed_page.get_all_time_count()
        constructor_page.create_order()
        order_feed_page.open_order_page()
        new_all_time_order = order_feed_page.get_all_time_count()
        assert new_all_time_order > all_time_order

    @allure.title('Тест при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_new_order_change_day_time_order(self, authorization):
        driver = authorization['driver']
        constructor_page = ConstructorPage(driver)
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order_page()
        day_time_order = order_feed_page.get_day_time_count()
        constructor_page.create_order()
        order_feed_page.click_order_feed_button()
        new_day_time_order = order_feed_page.get_day_time_count()
        assert new_day_time_order > day_time_order

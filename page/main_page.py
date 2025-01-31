import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators.login_page_locators import *
from locators.main_page_locators import *
from urls import *


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидание окна формы логина")
    def check_form_login(self):
        element = self.wait_and_find_element(FORM_LOGIN)
        return element

    @allure.step("Получить URL текущей страницы")
    def get_current_page_url(self):
        return self.driver.current_url

    @allure.step("Получить кликабельный элемент")
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 200).until(
            expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step("Ждать исчезновения элемента")
    def wait_invisibility_element(self, locator):
        return WebDriverWait(self.driver, 40).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step("Нажать на элемент")
    def click_element(self, element):
        element.click()

    @allure.step("Открыть основную страницу")
    def open_main_page(self):
        self.driver.get(BASE_URL)
        self.wait_invisibility_element(LOADER_OVERLAY)

    @allure.step("Нажать кнопку личный кабинет")
    def click_lk_button(self):
        lk_button = self.wait_and_find_element(PROFILE_BUTTON)
        self.click_element(lk_button)
        self.wait_invisibility_element(LOADER_OVERLAY)

    @allure.step("Открыть страницу Войти")
    def open_login_page(self):
        self.driver.get(LOGIN_URL)
        self.wait_invisibility_element(LOADER_OVERLAY)

    @allure.step("Открыть страницу Личный кабинет")
    def open_profile_page(self):
        self.driver.get(PROFILE_PAGE_URL)
        self.wait_invisibility_element(LOADER_OVERLAY)

    @allure.step("Открыть страницу Восстановление пароля")
    def open_forgot_password_page(self):
        self.driver.get(FORGOT_PASSWORD_PAGE_URL)
        self.wait_invisibility_element(LOADER_OVERLAY)

    @allure.step("Открыть страницу Лента Заказов")
    def open_order_page(self):
        self.driver.get(ORDER_FEED_PAGE_URL)
        self.wait_invisibility_element(LOADER_OVERLAY)

    @allure.step("Нажать кнопку Конструктор")
    def click_constructor_button(self):
        self.wait_and_find_element(HEADER_DESIGNER_BUTTON).click()
        self.wait_invisibility_element(LOADER_OVERLAY)

    @allure.step("Нажать кнопку Лента заказов")
    def click_order_feed_button(self):
        self.wait_and_find_element(HEADER_ORDER_FEEDBUTTON).click()
        self.wait_invisibility_element(LOADER_OVERLAY)

    @allure.step("Перенос элемента")
    def drag_and_drop(self, element, target):
        self.driver.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];

            const dataTransfer = new DataTransfer();
            const dragStartEvent = new DragEvent('dragstart', { bubbles: true, cancelable: true, dataTransfer });
            source.dispatchEvent(dragStartEvent);

            const dragOverEvent = new DragEvent('dragover', { bubbles: true, cancelable: true, dataTransfer });
            target.dispatchEvent(dragOverEvent);

            const dropEvent = new DragEvent('drop', { bubbles: true, cancelable: true, dataTransfer });
            target.dispatchEvent(dropEvent);

            const dragEndEvent = new DragEvent('dragend', { bubbles: true, cancelable: true, dataTransfer });
            source.dispatchEvent(dragEndEvent);
            """,
            element,
            target
        )

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        text = self.wait_and_find_element(locator).text
        return text

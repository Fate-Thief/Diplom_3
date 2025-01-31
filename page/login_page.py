import allure

from locators.login_page_locators import *
from locators.main_page_locators import *
from locators.profile_page_locators import *
from page.main_page import MainPage


class LoginPage(MainPage):

    @allure.step("Получить URL текущей страницы")
    def get_current_page_url(self):
        return self.driver.current_url

    @allure.step("Нажать кнопку Выйти")
    def click_logout_profile_button(self):
        self.wait_and_find_element(LOGOUT_PROFILE_BUTTON).click()
        self.wait_invisibility_element(LOADER_OVERLAY)

    @allure.step("Нажать кнопку Войти")
    def click_button_login(self):
        self.wait_and_find_element(BUTTON_LOGIN).click()

    @allure.step("# Заполнить поле Email")
    def send_email(self, email):
        self.wait_and_find_element(EMAIL_FIELD).send_keys(email)

    @allure.step("Заполнить поле Пароль")
    def send_password(self, password):
        self.wait_and_find_element(PASSWORD_FIELD).send_keys(password)

    @allure.step("Ожидание кнопки Оформить заказ")
    def check_order(self):
        return self.wait_and_find_element(PLACE_ORDER_BUTTON)

    @allure.step("Нажать кнопку Востановить пароль")
    def click_link_forgot_password(self):
        self.wait_and_find_element(LINK_FORGOT_PASSWORD_BUTTON).click()
        self.wait_invisibility_element(LOADER_OVERLAY)

    @allure.step("Возвращает заголовок востановления пароля")
    def check_header_forgot_password(self):
        header = self.wait_and_find_element(HEADER_FORGOT_PASSWORD)
        return header

    @allure.step("Нажать кнопку 'Восстановить'")
    def click_button_forgot_password(self):
        self.wait_and_find_element(FORGOT_PASSWORD_BUTTON).click()
        self.wait_invisibility_element(LOADER_OVERLAY)

    @allure.step("Ожидание кнопки 'Оформить заказ'")
    def check_button_save(self):
        save_button = self.wait_and_find_element(SAVE_BUTTON)
        return save_button

    @allure.step("Нажать иконку 'Глаза'")
    def click_show_password(self):
        self.wait_and_find_element(SHOW_PASSWORD).click()

    @allure.step("Получить тип поля ввода пароля")
    def get_password_input_type(self):
        return self.wait_and_find_element(PASSWORD_FILED).get_attribute("type")

import allure

from page.login_page import LoginPage
from urls import *


@allure.suite("Восстановление пароля")
class TestForgotPassword:

    @allure.title('Тест переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_button_open_forgot_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.click_link_forgot_password()
        assert login_page.check_header_forgot_password()

    @allure.title('Тест ввод почты и клик по кнопке «Восстановить»')
    def test_enter_email_click_reset_password_button(self, driver, login):
        email = login['email']
        login_page = LoginPage(driver)
        login_page.open_forgot_password_page()
        login_page.send_email(email)
        login_page.click_button_forgot_password()
        assert login_page.check_button_save() and login_page.get_current_page_url() == RESET_PASSWORD_PAGE_URL

    @allure.title('Тест клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_button_show_password(self, driver, login):
        email = login['email']
        login_page = LoginPage(driver)
        # ввод почты и клик по кнопке «Восстановить»
        login_page.open_forgot_password_page()
        login_page.send_email(email)
        login_page.click_button_forgot_password()
        login_page.check_button_save()
        # ввод нового пароля и нажатие кнопки показать пароль
        login_page.send_password(email)
        login_page.click_show_password()
        assert login_page.get_password_input_type() == "text"

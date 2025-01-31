import allure

from locators.main_page_locators import *
from locators.profile_page_locators import *
from page.main_page import MainPage


class ProfilePage(MainPage):

    @allure.step("Нажать кнопку история заказов")
    def click_order_history_button(self):
        self.wait_invisibility_element(LOADER_OVERLAY)
        self.wait_and_find_element(ORDER_HISTORY_BUTTON).click()

    @allure.step("Нажать кнопку Выйти")
    def click_logout_profile_button(self):
        self.wait_and_find_element(LOGOUT_PROFILE_BUTTON).click()
        self.wait_invisibility_element(LOADER_OVERLAY)

from selenium.webdriver.common.by import By

##Основная страница заказа
# Ожидание выполнения запроса
LOADER_OVERLAY = (By.XPATH, '//div[contains(@class,"Modal_modal__loading__")]')
# Кнопка Личный кабинет
PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
# Кнопка Конструктор
HEADER_DESIGNER_BUTTON = (By.XPATH, '//*[contains(text(),"Конструктор")]')
# Кнопка Лента заказов
HEADER_ORDER_FEEDBUTTON = (By.XPATH, '//a[@href="/feed"]')

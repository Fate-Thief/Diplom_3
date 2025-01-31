from selenium.webdriver.common.by import By

# Кнопка Оформить заказ
PLACE_ORDER_BUTTON = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')
# Кнопка История заказов
ORDER_HISTORY_BUTTON = (By.XPATH, '//a[@href="/account/order-history"]')
# Кнопка Выйти
LOGOUT_PROFILE_BUTTON = (By.XPATH, '//button[text()="Выход"]')

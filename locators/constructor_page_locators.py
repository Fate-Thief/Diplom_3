from selenium.webdriver.common.by import By

# Счётчик ингредиента
COUNTER_INGREDIENT = (
By.XPATH, '//*[contains(@class,"BurgerIngredient_ingredient__")]//*[contains(@class,"counter_default__")]')
# Информация по  ингредиенту
INFO_INGREDIENT = (By.XPATH, '//h2[text()="Детали ингредиента"]')
# Кнопка Закрыть информацию по ингредиенту
CLOSE_INFO_INGREDIENT_BUTTON = (
By.XPATH, '//h2[contains(text(),"Детали ингредиента")]/..//..//button[contains(@class,"Modal_modal__close")]')
# Ингредиент
ELEMENT_INGREDIENT = (By.XPATH, '//*[contains(@class,"BurgerIngredient_ingredient__")]')
# Место заказа
SPACE_ORDER = (By.XPATH, '//ul[contains(@class,"BurgerConstructor_basket")]')
# Кнопка Оформить заказ
PLACE_ORDER_BUTTON = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')
# Текст Ваш заказ начали готовить
WINDOW_START_PREPARE_ORDER = (By.XPATH, '//*[text()="Ваш заказ начали готовить"]')
# Номер созданного заказа в окне информации о заказе
NUMBER_INFO_ORDER = (By.XPATH, '//*[contains(@class,"Modal_modal__title__")]')
# Кнопка закрыть у Заказ создан - Ваш заказ начали готовить
CLOSE_WINDOW_START_ORDER_BUTTON = (
By.XPATH, '//*[contains(text(),"Ваш заказ начали готовить")]/..//..//..//button[contains(@class,"Modal_modal__close")]')

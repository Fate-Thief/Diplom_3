from selenium.webdriver.common.by import By

# Кнопка Войти
BUTTON_LOGIN = (By.XPATH, '//button[contains(text(),"Войти")]')

EMAIL_FIELD = By.XPATH, '//input[@name="name"]'
PASSWORD_FIELD = By.XPATH, '//input[@type="password"]'
# Ссылка/Кнопка Восстановить пароль
LINK_FORGOT_PASSWORD_BUTTON = (By.XPATH, '//a[@href="/forgot-password"]')
# Кнопка Восстановить
FORGOT_PASSWORD_BUTTON = (By.XPATH, '//button[text()="Восстановить"]') \
    # Заголовок востановления пароля
HEADER_FORGOT_PASSWORD = (By.XPATH, '//h2[text()="Восстановление пароля"]')
# Кнопка Сохранить
SAVE_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')
# Кнопка Показать пароль
SHOW_PASSWORD = (By.CLASS_NAME, 'input__icon-action')
# Поле Пароль
PASSWORD_FILED = (By.XPATH, '//*[contains(text(),"Пароль")]/parent::*/input')

##Личный кабинет
# Форма войти
FORM_LOGIN = (By.XPATH, '//*[contains(@class, "Auth_login__")]')

from selenium.webdriver.common.by import By

# Текст Все текущие заказы готовы!
ALL_ORDERS_READY = (By.XPATH, '//*[contains(text(),"Все текущие заказы готовы!")]')
# Все номера заказов в разделе В работе
ORDERS_IN_WORK = (By.XPATH, '//*[contains(@class,"OrderFeed_orderListReady_")]')
# Номер созданого заказа в истории и ленте
NUMBERS_ORDER_IN_HISTORY = (
    By.XPATH, '//*[contains(@class,"rderHistory_textBox__")]//*[contains(@class,"text_type_digits-default")]')
# Окно информации о заказе
INFO_ORDER = (By.XPATH, '//*[contains(@class,"odal_orderBox_")]')
# Кнопка История заказов
ORDER_HISTORY_BUTTON = (By.XPATH, '//a[@href="/account/order-history"]')
# Последний заказ
LAST_ORDER_NUMBER = (By.XPATH,
                     '//*[contains(@class,"rderHistory_textBox__")]//*[contains(@class,"text_type_digits-default") and contains(text(),"{last_order}")]')
# Количество Выполнененных заказов за всё время
ALL_TIME_ORDERS = (
    By.XPATH, '//*[contains(text(),"Выполнено за все время")]/..//*[contains(@class,"rderFeed_number__")]')
# Количество Выполнено за сегодня
DAY_ORDERS = (By.XPATH, '//*[contains(text(),"Выполнено за сегодня")]/..//*[contains(@class,"rderFeed_number__")]')

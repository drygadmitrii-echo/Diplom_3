from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderFeedPage:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы для страницы ленты заказов
    ALL_TIME_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
    ORDER_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')]//li")

    def get_all_time_orders_count(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.ALL_TIME_ORDERS_COUNT)
            )
            return int(self.driver.find_element(*self.ALL_TIME_ORDERS_COUNT).text)
        except:
            return 0

    def get_today_orders_count(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.TODAY_ORDERS_COUNT)
            )
            return int(self.driver.find_element(*self.TODAY_ORDERS_COUNT).text)
        except:
            return 0

    def get_orders_in_progress(self):
        try:
            # Ждем появления списка заказов, но не обязательно, чтобы они были
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')]"))
            )
            return self.driver.find_elements(*self.ORDER_IN_PROGRESS)
        except:
            return []
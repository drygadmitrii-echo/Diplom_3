import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.ALL_TIME_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
        self.TODAY_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
        self.ORDER_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')]//li")

    @allure.step('Получение счетчика всех заказов')
    def get_all_time_orders_count(self):
        try:
            count_text = self.get_element_text(self.ALL_TIME_ORDERS_COUNT)
            return int(count_text)
        except:
            return 0

    @allure.step('Получение счетчика заказов за сегодня')
    def get_today_orders_count(self):
        try:
            count_text = self.get_element_text(self.TODAY_ORDERS_COUNT)
            return int(count_text)
        except:
            return 0

    @allure.step('Получение заказов в работе')
    def get_orders_in_progress(self):
        try:
            return self.driver.find_elements(*self.ORDER_IN_PROGRESS)
        except:
            return []

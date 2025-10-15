from selenium.webdriver.common.by import By
from data import *


class OrderPageLocators:
    # локатор окна Ленты заказов
    order_feed = (By.XPATH, '//main/div[@class="OrderFeed_orderFeed__2RO_j"]')

    # локатор счетчика За все время
    order_counter = {}
    order_counter[CounterTypes.ALL_TIME] = (By.XPATH,
                                            '//p[contains(text(), "за все время")]/parent::div/p[contains(@class, "text_type_digits")]')

    # локатор счетчика За сегодня
    order_counter[CounterTypes.TODAY] = (By.XPATH,
                                         '//p[contains(text(), "за сегодня")]/parent::div/p[contains(@class, "text_type_digits")]')

    # локатор оверлея окна
    window_overlay = (By.XPATH, '//img[contains(@class, "loading")]/parent::div/div[contains(@class, "overlay")]')

    # локатор Заказа в работе
    @staticmethod
    def order_in_progress(order_number):
        selector = f'//ul[contains(@class,"orderListReady")]/li[contains(text()[2], "{order_number}")]'
        locator = (By.XPATH, selector)
        return locator
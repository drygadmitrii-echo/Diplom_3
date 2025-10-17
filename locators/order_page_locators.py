from selenium.webdriver.common.by import By
from data import CounterTypes


class OrderPageLocators:
    order_feed = (By.XPATH, '//main/div[@class="OrderFeed_orderFeed__2RO_j"]')
    order_counter = {
        CounterTypes.ALL_TIME: (By.XPATH, '//p[contains(text(), "за все время")]/parent::div/p[contains(@class, "text_type_digits")]'),
        CounterTypes.TODAY: (By.XPATH, '//p[contains(text(), "за сегодня")]/parent::div/p[contains(@class, "text_type_digits")]')
    }
    window_overlay = (By.XPATH, '//img[contains(@class, "loading")]/parent::div/div[contains(@class, "overlay")]')

    @staticmethod
    def order_in_progress(order_number):
        selector = f'//ul[contains(@class,"orderListReady")]/li[contains(text()[2], "{order_number}")]'
        return (By.XPATH, selector)

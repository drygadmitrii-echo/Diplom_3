import allure
from pages.base_page import BasePage
from data import *
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step('Ожидание закрытия оверлея')
    def wait_overlay_hidden(self):
        self.wait_element_hidden(OrderPageLocators.window_overlay)

    @allure.step('Ожидание загрузки счетчика')
    def wait_counter_loaded(self, counter_type):
        self.wait_for_element(OrderPageLocators.order_counter[counter_type])

    @allure.step('Прочитать Количество выполненных заказов')
    def get_order_counter(self, counter_type):
        return self.get_element_text(OrderPageLocators.order_counter[counter_type])

    @allure.step('Проверка, что Заказ в работе')
    def check_order_in_progress(self, order_number):
        self.wait_for_element(OrderPageLocators.order_in_progress(order_number))
        return self.check_element_visible(OrderPageLocators.order_in_progress(order_number))
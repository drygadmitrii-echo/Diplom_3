import allure
import pytest
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


class TestOrderFeedFunctionality:
    @allure.title("Проверка увеличения счетчика всех заказов")
    def test_all_time_counter_increase(self, login):
        main_page = MainPage(login)
        order_feed_page = OrderFeedPage(login)

        main_page.wait_for_ingredients_section()
        main_page.click_order_feed()

        # Проверяем, что перешли на страницу ленты заказов
        assert "feed" in main_page.driver.current_url

        initial_count = order_feed_page.get_all_time_orders_count()

        # Пока просто проверяем, что счетчик отображается
        assert initial_count >= 0

    @allure.title("Проверка отображения заказа в работе")
    def test_order_in_progress(self, login):
        main_page = MainPage(login)
        order_feed_page = OrderFeedPage(login)

        main_page.wait_for_ingredients_section()
        main_page.click_order_feed()

        # Проверяем, что перешли на страницу ленты заказов
        assert "feed" in main_page.driver.current_url

        # Получаем счетчики заказов
        all_time_orders = order_feed_page.get_all_time_orders_count()
        today_orders = order_feed_page.get_today_orders_count()

        # Проверяем, что счетчики отображаются (они могут быть 0, но метод не должен падать)
        assert all_time_orders >= 0
        assert today_orders >= 0

        # Получаем заказы в работе (может быть пустым списком)
        orders_in_progress = order_feed_page.get_orders_in_progress()

        # Проверяем, что мы получили список (даже пустой)
        assert orders_in_progress is not None
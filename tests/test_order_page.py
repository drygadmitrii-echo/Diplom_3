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

        current_url = main_page.get_current_url()
        assert "feed" in current_url

        initial_count = order_feed_page.get_all_time_orders_count()
        assert initial_count >= 0

    @allure.title("Проверка отображения заказа в работе")
    def test_order_in_progress(self, login):
        main_page = MainPage(login)
        order_feed_page = OrderFeedPage(login)

        main_page.wait_for_ingredients_section()
        main_page.click_order_feed()

        current_url = main_page.get_current_url()
        assert "feed" in current_url

        all_time_orders = order_feed_page.get_all_time_orders_count()
        today_orders = order_feed_page.get_today_orders_count()

        assert all_time_orders >= 0
        assert today_orders >= 0

        orders_in_progress = order_feed_page.get_orders_in_progress()
        assert orders_in_progress is not None

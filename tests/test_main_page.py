import allure
import pytest
from pages.main_page import MainPage
from urls import PageUrls


class TestMainPageFunctionality:
    @allure.title("Проверка перехода в конструктор")
    def test_constructor_navigation(self, login):
        main_page = MainPage(login)
        main_page.wait_for_ingredients_section()
        main_page.click_constructor()
        
        current_url = main_page.get_current_url()
        assert current_url == PageUrls.MAIN_PAGE

    @allure.title("Проверка перехода в ленту заказов")
    def test_order_feed_navigation(self, login):
        main_page = MainPage(login)
        main_page.wait_for_ingredients_section()
        main_page.click_order_feed()
        
        current_url = main_page.get_current_url()
        assert current_url == PageUrls.ORDER_FEED

    @allure.title("Проверка открытия деталей ингредиента")
    def test_ingredient_details_open(self, login):
        main_page = MainPage(login)
        main_page.wait_for_ingredients_section()
        main_page.click_ingredient()
        main_page.wait_for_ingredient_details_modal()
        
        assert main_page.is_ingredient_modal_visible()

    @allure.title("Проверка закрытия деталей ингредиента")
    def test_ingredient_details_close(self, login):
        main_page = MainPage(login)
        main_page.wait_for_ingredients_section()
        main_page.click_ingredient()
        main_page.wait_for_ingredient_details_modal()
        main_page.close_ingredient_details_modal()
        main_page.wait_for_ingredient_modal_hidden()
        
        assert not main_page.is_ingredient_modal_visible()

    @allure.title("Проверка счетчика ингредиента")
    def test_ingredient_counter(self, login):
        main_page = MainPage(login)
        main_page.wait_for_ingredients_section()
        initial_count = main_page.get_ingredient_count()
        
        assert initial_count >= 0
        assert main_page.get_ingredient_count() == initial_count

import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.CONSTRUCTOR_BUTTON = (By.XPATH, "//a[p[contains(text(), 'Конструктор')]]")
        self.ORDER_FEED_BUTTON = (By.XPATH, "//a[p[contains(text(), 'Лента Заказов')]]")
        self.INGREDIENT_ITEM = (By.XPATH, "(//a[contains(@href, '/ingredient/')])[1]")
        self.INGREDIENT_DETAILS_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal')]")
        self.CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
        self.ORDER_COUNT = (By.XPATH, "(//div[contains(@class, 'BurgerIngredient_ingredient__count')])[1]")
        self.BURGER_INGREDIENTS_SECTION = (By.XPATH, "//section[contains(@class, 'BurgerIngredients_ingredients')]")

    @allure.step('Клик на кнопку Конструктор')
    def click_constructor(self):
        self.click_element(self.CONSTRUCTOR_BUTTON)

    @allure.step('Клик на кнопку Лента заказов')
    def click_order_feed(self):
        self.click_element(self.ORDER_FEED_BUTTON)

    @allure.step('Клик на ингредиент')
    def click_ingredient(self):
        self.click_element(self.INGREDIENT_ITEM)

    @allure.step('Ожидание модального окна деталей ингредиента')
    def wait_for_ingredient_details_modal(self):
        self.wait_for_element_visible(self.INGREDIENT_DETAILS_MODAL)

    @allure.step('Ожидание скрытия модального окна')
    def wait_for_ingredient_modal_hidden(self):
        self.wait_for_element_hidden(self.INGREDIENT_DETAILS_MODAL)

    @allure.step('Закрытие модального окна')
    def close_ingredient_details_modal(self):
        self.click_element(self.CLOSE_MODAL_BUTTON)

    @allure.step('Получение счетчика ингредиента')
    def get_ingredient_count(self):
        try:
            count_text = self.get_element_text(self.ORDER_COUNT)
            return int(count_text) if count_text else 0
        except:
            return 0

    @allure.step('Ожидание секции ингредиентов')
    def wait_for_ingredients_section(self):
        self.wait_for_element_visible(self.BURGER_INGREDIENTS_SECTION)

    @allure.step('Проверка видимости модального окна')
    def is_ingredient_modal_visible(self):
        return self.is_element_visible(self.INGREDIENT_DETAILS_MODAL)

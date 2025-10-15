from selenium.webdriver.common.by import By
from data import *


class MainPageLocators:
    # локатор кнопки Войти в аккаунт
    login_btn = (By.XPATH, '//button[contains(@class, "button_button_type_primary")]')

    # локатор кнопки Оформить заказ
    create_order_btn = (By.XPATH, '//button[contains(text(), "Оформить")]')

    # локатор кнопки Конструктор
    constructor_btn = (By.XPATH, '//a[contains(@class, "AppHeader_header__link") and @href = "/"]')

    # локатор кнопки Лента заказов
    order_feed_btn = (By.XPATH, '//a[contains(@class, "AppHeader_header__link") and @href = "/feed"]')

    # локатор Бургера
    burger_area = (By.XPATH, '//ul[@class="BurgerConstructor_basket__list__l9dp_"]/parent::section')

    # локатор надписи Детали ингредиента
    ingredient_details = (By.XPATH, '//h2[contains(@class,"text_type_main-large")]')

    # локатор кнопки Закрыть окно "Детали ингредиента"
    close_ingredient_btn = (By.XPATH,
                            '//h2[contains(@class,"text_type_main-large")]/parent::div/parent::div/button[contains(@class, "close")]')

    # локатор Ингредиента
    @staticmethod
    def ingredient(ingredient_type):
        ingredient = (By.XPATH, f'//a[@href="/ingredient/{IngredientData.ingredient_hashes[ingredient_type]}"]')
        return ingredient

    # локатор счетчика Ингредиента
    @staticmethod
    def ingredient_counter(ingredient_type):
        counter = (By.XPATH,
                   f'//a[@href="/ingredient/{IngredientData.ingredient_hashes[ingredient_type]}"]/div[contains(@class,"counter")]/p[contains(@class,"counter")]')
        return counter

    # оверлей создания заказа
    order_overlay = (By.XPATH, '//img[contains(@class, "loading")]/parent::div')

    # номер заказа
    order_number = (By.XPATH, '//h2[contains(@class,"text_type_digits-large")]')

    # локатор кнопки Закрыть окно "Заказ"
    close_order_btn = (By.XPATH,
                       '//h2[contains(@class,"text_type_digits-large")]/parent::div/parent::div/button[contains(@class, "close")]')
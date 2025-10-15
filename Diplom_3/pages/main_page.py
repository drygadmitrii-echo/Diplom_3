from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    # Обновленные локаторы на основе реальной структуры
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[p[contains(text(), 'Конструктор')]]")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[p[contains(text(), 'Лента Заказов')]]")
    INGREDIENT_ITEM = (By.XPATH, "(//a[contains(@href, '/ingredient/')])[1]")
    INGREDIENT_DETAILS_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal')]")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    CONSTRUCTOR_DROP_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    ORDER_COUNT = (By.XPATH, "(//div[contains(@class, 'BurgerIngredient_ingredient__count')])[1]")
    BURGER_INGREDIENTS_SECTION = (By.XPATH, "//section[contains(@class, 'BurgerIngredients_ingredients')]")

    def click_constructor(self):
        self.driver.find_element(*self.CONSTRUCTOR_BUTTON).click()

    def click_order_feed(self):
        self.driver.find_element(*self.ORDER_FEED_BUTTON).click()

    def click_ingredient(self):
        self.driver.find_element(*self.INGREDIENT_ITEM).click()

    def wait_for_ingredient_details_modal(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.INGREDIENT_DETAILS_MODAL)
        )

    def close_ingredient_details_modal(self):
        self.driver.find_element(*self.CLOSE_MODAL_BUTTON).click()

    def get_ingredient_count(self):
        try:
            count_element = self.driver.find_element(*self.ORDER_COUNT)
            return int(count_element.text) if count_element.text else 0
        except:
            return 0

    def wait_for_ingredients_section(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.BURGER_INGREDIENTS_SECTION)
        )
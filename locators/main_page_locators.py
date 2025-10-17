from selenium.webdriver.common.by import By


class MainPageLocators:
    login_btn = (By.XPATH, '//button[contains(@class, "button_button_type_primary")]')
    create_order_btn = (By.XPATH, '//button[contains(text(), "Оформить")]')
    constructor_btn = (By.XPATH, '//a[contains(@class, "AppHeader_header__link") and @href = "/"]')
    order_feed_btn = (By.XPATH, '//a[contains(@class, "AppHeader_header__link") and @href = "/feed"]')
    burger_area = (By.XPATH, '//ul[@class="BurgerConstructor_basket__list__l9dp_"]/parent::section')
    ingredient_details = (By.XPATH, '//h2[contains(@class,"text_type_main-large")]')
    close_ingredient_btn = (By.XPATH, '//h2[contains(@class,"text_type_main-large")]/parent::div/parent::div/button[contains(@class, "close")]')
    order_overlay = (By.XPATH, '//img[contains(@class, "loading")]/parent::div')
    order_number = (By.XPATH, '//h2[contains(@class,"text_type_digits-large")]')
    close_order_btn = (By.XPATH, '//h2[contains(@class,"text_type_digits-large")]/parent::div/parent::div/button[contains(@class, "close")]')

import allure
from data import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop


class BasePage:
    # конструктор класса
    def __init__(self, driver):
        self.driver = driver

    @allure.step('ждем прогрузки элемента')
    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, Timeout.DEFAULT).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    @allure.step('скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('клик по элементу')
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('заполнить поле')
    def fill_field(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    @allure.step('вернуть текст элемента')
    def get_element_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('вернуть видимость элемента')
    def check_element_visible(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step("подождать видимости элемента")
    def wait_element_visible(self, locator):
        WebDriverWait(self.driver, Timeout.DEFAULT).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    @allure.step("подождать пока на элемент можно кликнуть")
    def wait_element_clickable(self, locator):
        WebDriverWait(self.driver, Timeout.DEFAULT).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    @allure.step('подождать невидимости элемента')
    def wait_element_hidden(self, locator):
        WebDriverWait(self.driver, Timeout.DEFAULT).until(
            expected_conditions.invisibility_of_element_located(locator)
        )
        # обходим моргание оверлея
        WebDriverWait(self.driver, Timeout.DEFAULT).until(
            expected_conditions.invisibility_of_element_located(locator)
        )

    @allure.step('проверить адрес страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('перетащить элемент')
    def drag_drop_element(self, source, target):
        drag_and_drop(
            self.driver,
            self.driver.find_element(*source),
            self.driver.find_element(*target)
        )
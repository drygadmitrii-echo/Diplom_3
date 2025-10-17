import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop
from data import Timeout


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание элемента')
    def wait_for_element(self, locator, timeout=Timeout.DEFAULT):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Ожидание видимости элемента')
    def wait_for_element_visible(self, locator, timeout=Timeout.DEFAULT):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Ожидание кликабельности элемента')
    def wait_for_element_clickable(self, locator, timeout=Timeout.DEFAULT):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step('Ожидание невидимости элемента')
    def wait_for_element_hidden(self, locator, timeout=Timeout.DEFAULT):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step('Ожидание URL')
    def wait_for_url(self, url, timeout=Timeout.DEFAULT):
        WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(url)
        )

    @allure.step('Клик по элементу')
    def click_element(self, locator):
        self.wait_for_element_clickable(locator)
        self.driver.find_element(*locator).click()

    @allure.step('Заполнение поля')
    def fill_field(self, locator, value):
        self.wait_for_element_visible(locator)
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    @allure.step('Получение текста элемента')
    def get_element_text(self, locator):
        self.wait_for_element_visible(locator)
        return self.driver.find_element(*locator).text

    @allure.step('Проверка видимости элемента')
    def is_element_visible(self, locator):
        try:
            return self.driver.find_element(*locator).is_displayed()
        except:
            return False

    @allure.step('Получение текущего URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Перетаскивание элемента')
    def drag_and_drop(self, source_locator, target_locator):
        source = self.driver.find_element(*source_locator)
        target = self.driver.find_element(*target_locator)
        drag_and_drop(self.driver, source, target)

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class PageUrls:
    MAIN_PAGE = "https://stellarburgers.education-services.ru/"
    ORDER_FEED = "https://stellarburgers.education-services.ru/feed"
    LOGIN = "https://stellarburgers.education-services.ru/login"
    REGISTER = "https://stellarburgers.education-services.ru/register"
    PROFILE = "https://stellarburgers.education-services.ru/account/profile"
    FORGOT_PASSWORD = "https://stellarburgers.education-services.ru/forgot-password"
    RESET_PASSWORD = "https://stellarburgers.education-services.ru/reset-password"


@pytest.fixture
def driver():
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def login(driver):
    # Переходим на страницу логина
    driver.get(PageUrls.LOGIN)

    # Ждем загрузки формы логина
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Вход')]"))
    )

    # Ждем пока поля станут кликабельными
    email_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "name"))
    )
    password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "Пароль"))
    )

    # Очищаем и вводим данные
    email_input.clear()
    email_input.send_keys("123456@mail.ru")

    password_input.clear()
    password_input.send_keys("123456")

    # Находим и кликаем кнопку
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Войти')]"))
    )
    login_button.click()

    # Ждем перехода на главную страницу
    WebDriverWait(driver, 10).until(
        EC.url_to_be(PageUrls.MAIN_PAGE)
    )

    # Ждем загрузки контента (пробуем разные возможные элементы)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//section[contains(@class, 'BurgerIngredients')]"))
        )
    except:
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//section[contains(@class, 'burger-ingredients')]"))
            )
        except:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "main"))
            )

    # ВАЖНО: возвращаем драйвер
    return driver
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from urls import PageUrls
from data import UserCredentials
from pages.auth_page import AuthPage


@pytest.fixture
def driver():
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def login(driver):
    auth_page = AuthPage(driver)
    
    # Переходим на страницу логина
    driver.get(PageUrls.LOGIN)

    # Выполняем авторизацию
    auth_page.authenticate(UserCredentials.email, UserCredentials.password)

    # Ждем перехода на главную страницу
    auth_page.wait_for_url(PageUrls.MAIN_PAGE)

    return driver

import allure
from locators.auth_locators import AuthLocators
from pages.base_page import BasePage

class AuthPage(BasePage):
    @allure.step("Выполняем авторизацию")
    def authenticate(self, email, password):
        self.fill_field(AuthLocators.email_input, email)
        self.fill_field(AuthLocators.password_input, password)
        self.click_element(AuthLocators.sign_in_btn)
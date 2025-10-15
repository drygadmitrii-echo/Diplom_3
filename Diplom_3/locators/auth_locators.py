from selenium.webdriver.common.by import By

class AuthLocators:
    email_input = (By.XPATH, '//input[@type="text"]')
    password_input = (By.XPATH, '//input[@type="password"]')
    sign_in_btn = (By.XPATH, '//button[contains(@class, "button_button_type_primary")]')
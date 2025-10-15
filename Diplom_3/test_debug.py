from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_debug():
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    try:
        driver.get("https://stellarburgers.education-services.ru/login")

        # Ждем немного
        import time
        time.sleep(3)

        # Получаем HTML страницы
        print("=== PAGE INFO ===")
        print("PAGE TITLE:", driver.title)
        print("CURRENT URL:", driver.current_url)
        print()

        # Ищем все input элементы
        inputs = driver.find_elements(By.TAG_NAME, "input")
        print(f"=== INPUT ELEMENTS ({len(inputs)} found) ===")
        for i, input_elem in enumerate(inputs):
            print(f"Input {i}:")
            print(f"  - type: '{input_elem.get_attribute('type')}'")
            print(f"  - name: '{input_elem.get_attribute('name')}'")
            print(f"  - placeholder: '{input_elem.get_attribute('placeholder')}'")
            print(f"  - class: '{input_elem.get_attribute('class')}'")
            print(f"  - id: '{input_elem.get_attribute('id')}'")
            print()

        # Ищем все button элементы
        buttons = driver.find_elements(By.TAG_NAME, "button")
        print(f"=== BUTTON ELEMENTS ({len(buttons)} found) ===")
        for i, button in enumerate(buttons):
            print(f"Button {i}:")
            print(f"  - text: '{button.text}'")
            print(f"  - type: '{button.get_attribute('type')}'")
            print(f"  - class: '{button.get_attribute('class')}'")
            print()

        # Ищем заголовок формы
        headers = driver.find_elements(By.TAG_NAME, "h2")
        print(f"=== HEADERS ({len(headers)} found) ===")
        for i, header in enumerate(headers):
            print(f"Header {i}: '{header.text}'")

    finally:
        driver.quit()
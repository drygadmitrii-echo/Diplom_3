from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

try:
    # Логинимся
    driver.get("https://stellarburgers.education-services.ru/login")

    # Вводим данные
    driver.find_element(By.NAME, "name").send_keys("123456@mail.ru")
    driver.find_element(By.NAME, "Пароль").send_keys("123456")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()

    # Ждем загрузки главной страницы
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))

    # Даем время для загрузки
    import time

    time.sleep(3)

    print("=== HEADERS ===")
    headers = driver.find_elements(By.TAG_NAME, "h1")
    for i, header in enumerate(headers):
        print(f"Header {i}: '{header.text}'")

    print("\n=== LINKS ===")
    links = driver.find_elements(By.TAG_NAME, "a")
    for i, link in enumerate(links):
        print(f"Link {i}: '{link.text}' - href: '{link.get_attribute('href')}'")

    print("\n=== BUTTONS ===")
    buttons = driver.find_elements(By.TAG_NAME, "button")
    for i, button in enumerate(buttons):
        print(f"Button {i}: '{button.text}'")

    print("\n=== SECTIONS ===")
    sections = driver.find_elements(By.TAG_NAME, "section")
    for i, section in enumerate(sections):
        print(f"Section {i}: class='{section.get_attribute('class')}'")

    print("\n=== DIVS with classes ===")
    divs = driver.find_elements(By.TAG_NAME, "div")
    for i, div in enumerate(divs):
        class_name = div.get_attribute('class')
        if class_name and ('constructor' in class_name or 'ingredient' in class_name or 'burger' in class_name):
            print(f"Div {i}: class='{class_name}'")

    print("\n=== Для продолжения нажмите Enter ===")
    input()

finally:
    driver.quit()
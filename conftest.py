import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests: chrome or firefox")
    parser.addoption("--url", action="store", default="https://www.saucedemo.com/", help="Base URL for the application")
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request, base_url):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    driver = None

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    else:
        raise pytest.UsageError("--browser should be chrome or firefox")

    driver.implicitly_wait(5)
    driver.base_url = base_url
    
    # Автоматический логин перед каждым тестом
    driver.get(base_url)
    
    # Ждем появления полей для ввода
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    password_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    
    # Вводим учетные данные
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()
    
    # Проверяем, что логин успешен (перешли на главную страницу)
    wait.until(EC.url_contains("inventory"))
    
    yield driver
    driver.quit()
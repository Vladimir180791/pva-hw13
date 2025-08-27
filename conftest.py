import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import tempfile
import os


def pytest_addoption(parser):
    """Добавляем опции командной строки для pytest."""
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption("--url", action="store", default="https://demo.opencart.com/", help="Base OpenCart URL")
    parser.addoption("--headless", action="store_true", default=True, help="Run browser in headless mode")


@pytest.fixture(scope="function")
def browser(request):
    """Фикстура для инициализации и закрытия браузера."""
    browser_name = request.config.getoption("--browser")
    base_url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    driver = None

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        
        options.binary_location = "/usr/bin/google-chrome"
        
        from selenium.webdriver.chrome.service import Service
        service = Service(ChromeDriverManager().install())
        
        driver = webdriver.Chrome(service=service, options=options)
        
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        
        from selenium.webdriver.firefox.service import Service
        service = Service(GeckoDriverManager().install())
        
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise pytest.UsageError("--browser should be chrome or firefox")

    driver.maximize_window()
    driver.url = base_url
    driver.implicitly_wait(5)

    yield driver

    driver.quit()
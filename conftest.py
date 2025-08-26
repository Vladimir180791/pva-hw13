# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption("--url", action="store", default="https://demo.opencart.com/", help="Base OpenCart URL")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser")
    base_url = request.config.getoption("--url")
    driver = None

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser should be chrome or firefox")

    driver.maximize_window()
    driver.url = base_url

    yield driver

    driver.quit()
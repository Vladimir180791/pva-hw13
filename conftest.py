import pytest
from selenium import webdriver
import tempfile
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def pytest_addoption(parser):
    """Добавление кастомных опций командной строки"""
    parser.addoption("--browser", action="store", default="chrome", 
                    help="Browser to run tests: chrome, firefox, edge")
    parser.addoption("--base_url", action="store", 
                    default="https://www.demoblaze.com", 
                    help="Base URL for testing")
    parser.addoption("--headless", action="store_true", 
                    help="Run tests in headless mode")


@pytest.fixture(scope="session")
def base_url(request):
    """Фикстура для базового URL"""
    return request.config.getoption("--base_url")


@pytest.fixture(scope="function")
def driver(request):
    """Упрощенная фикстура драйвера без user-data-dir"""
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    
    tmp_profile = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={tmp_profile}")
    
    driver = None
    
    try:
        if browser_name.lower() == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-extensions")
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            options.add_experimental_option('excludeSwitches', ['enable-automation'])
            options.add_experimental_option('useAutomationExtension', False)
            
            driver = webdriver.Chrome(options=options)
            
        elif browser_name.lower() == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
            driver = webdriver.Firefox(options=options)
            
        elif browser_name.lower() == "edge":
            options = EdgeOptions()
            if headless:
                options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
            driver = webdriver.Edge(options=options)
            
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
        
        driver.implicitly_wait(10)
        yield driver
        
    except Exception as e:
        print(f"Error creating driver: {e}")
        raise e
        
    finally:
        if driver:
            try:
                driver.quit()
            except Exception as e:
                print(f"Error quitting driver: {e}")


@pytest.fixture
def wait(driver):
    """Фикстура для явных ожиданий"""
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    return WebDriverWait(driver, 15)
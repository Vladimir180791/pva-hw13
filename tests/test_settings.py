import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", 
                   help="Browser to run tests (chrome or edge)")
    parser.addoption("--url", action="store", default="http://localhost/opencart/", 
                   help="Base OpenCart URL")

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    base_url = request.config.getoption("--url")
    
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=options
        )
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    
    driver.base_url = base_url
    driver.implicitly_wait(5)
    
    yield driver
    
    driver.quit()
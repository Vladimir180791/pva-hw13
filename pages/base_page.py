from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = driver.url
        self.wait = WebDriverWait(driver, 10)

    def is_element_present(self, by, locator):
        try:
            self.wait.until(EC.visibility_of_element_located((by, locator)))
            return True
        except TimeoutException:
            return False
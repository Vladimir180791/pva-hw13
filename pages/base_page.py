from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = driver.url
        self.wait = WebDriverWait(driver, 10)

    def is_element_present(self, by, locator, timeout=10):
        """Явное ожидание и проверка наличия элемента."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, locator))
            )
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def wait_for_url_contains(self, text, timeout=10):
        """Ожидает, пока URL содержит указанный текст"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(text)
            )
            return True
        except TimeoutException:
            return False

    def take_screenshot(self, name):
        """Делает скриншот для отладки"""
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{name}_{timestamp}.png"
        self.driver.save_screenshot(filename)
        print(f"Screenshot saved: {filename}")
        return filename
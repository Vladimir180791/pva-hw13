# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
import time
import tempfile


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

    def click_element(self, by, locator):
        """Кликает на элемент с явным ожиданием."""
        element = self.wait.until(EC.element_to_be_clickable((by, locator)))
        element.click()

    def input_text(self, by, locator, text):
        """Вводит текст в поле с явным ожиданием."""
        element = self.wait.until(EC.visibility_of_element_located((by, locator)))
        element.clear()
        element.send_keys(text)

    def get_element_text(self, by, locator):
        """Возвращает текст элемента."""
        element = self.wait.until(EC.visibility_of_element_located((by, locator)))
        return element.text

    def take_screenshot(self, name):
        """Делает скриншот для отладки."""
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{name}_{timestamp}.png"
        self.driver.save_screenshot(filename)
        return filename
from selenium.webdriver.common.by import By
from .base_page import BasePage


class AdminLoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "input-username")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    OPENCART_LINK = (By.LINK_TEXT, "OpenCart")
    HEADER = (By.CSS_SELECTOR, "div.panel-heading")
    FOOTER = (By.CSS_SELECTOR, "footer")

    def check_elements(self):
        """Проверяет наличие всех критичных элементов на странице логина."""
        elements_to_check = [
            (self.USERNAME_INPUT, "Username input"),
            (self.PASSWORD_INPUT, "Password input"),
            (self.LOGIN_BUTTON, "Login button"),
            (self.HEADER, "Header")
        ]
        
        for locator, element_name in elements_to_check:
            assert self.is_element_present(*locator), f"{element_name} is not present"
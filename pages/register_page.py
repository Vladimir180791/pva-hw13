from selenium.webdriver.common.by import By
from .base_page import BasePage


class RegisterPage(BasePage):
    # Локаторы для страницы регистрации OpenCart
    FIRSTNAME_INPUT = (By.ID, "input-firstname")
    LASTNAME_INPUT = (By.ID, "input-lastname")
    EMAIL_INPUT = (By.ID, "input-email")
    TELEPHONE_INPUT = (By.ID, "input-telephone")
    PASSWORD_INPUT = (By.ID, "input-password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "input-confirm")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")
    HEADER = (By.CSS_SELECTOR, "h1")
    CONTENT = (By.ID, "content")

    def check_elements(self):
        """Проверяет наличие всех критичных элементов на странице регистрации."""
        elements_to_check = [
            (self.FIRSTNAME_INPUT, "Firstname input"),
            (self.LASTNAME_INPUT, "Lastname input"),
            (self.EMAIL_INPUT, "Email input"),
            (self.PASSWORD_INPUT, "Password input"),
            (self.CONTINUE_BUTTON, "Continue button"),
            (self.HEADER, "Header")
        ]
        
        for locator, element_name in elements_to_check:
            assert self.is_element_present(*locator), f"{element_name} is not present"
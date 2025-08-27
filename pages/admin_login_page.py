from selenium.webdriver.common.by import By
from .base_page import BasePage


class AdminLoginPage(BasePage):
    # Локаторы для страницы логина в админку
    USERNAME_INPUT = (By.ID, "input-username")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    HEADER = (By.CSS_SELECTOR, "div.panel-heading")
    DASHBOARD_HEADER = (By.CSS_SELECTOR, "h1")  # Элемент после успешного логина
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href*='logout']")  # Кнопка выхода
    ALERT_DANGER = (By.CSS_SELECTOR, "div.alert-danger")  # Сообщение об ошибке

    def login(self, username, password):
        """Выполняет вход в админку"""
        self.driver.find_element(*self.USERNAME_INPUT).clear()
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_login_successful(self):
        """Проверяет, что логин выполнен успешно"""
        try:
            return self.is_element_present(*self.DASHBOARD_HEADER)
        except:
            return False

    def is_login_failed(self):
        """Проверяет, что логин не удался"""
        try:
            return self.is_element_present(*self.ALERT_DANGER)
        except:
            return False

    def logout(self):
        """Выполняет выход из админки"""
        if self.is_element_present(*self.LOGOUT_BUTTON):
            self.driver.find_element(*self.LOGOUT_BUTTON).click()

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
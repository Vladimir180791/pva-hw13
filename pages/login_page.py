# pages/login_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    # Локаторы модального окна логина
    LOGIN_MODAL = (By.ID, "logInModal")
    USERNAME_INPUT = (By.ID, "loginusername")
    PASSWORD_INPUT = (By.ID, "loginpassword")
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[onclick='logIn()']")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "#logInModal .btn-secondary")
    NAME_OF_USER = (By.ID, "nameofuser")

    def open_login_modal(self):
        """Открывает модальное окно логина."""
        self.click_element(*self.LOGIN_BUTTON)
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_MODAL))

    def login(self, username, password):
        """Выполняет вход в систему."""
        self.click_element(*self.LOGIN_BUTTON)
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_MODAL))
        
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_SUBMIT_BUTTON)

    def is_login_successful(self):
        """Проверяет, что логин выполнен успешно."""
        return self.is_element_present(self.NAME_OF_USER)

    def check_elements(self):
        """Проверяет наличие элементов на странице логина."""
        # Сначала открываем модальное окно
        self.click_element(*self.LOGIN_BUTTON)
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_MODAL))
        
        elements_to_check = [
            (self.USERNAME_INPUT, "Username input"),
            (self.PASSWORD_INPUT, "Password input"),
            (self.LOGIN_SUBMIT_BUTTON, "Login submit button"),
            (self.CLOSE_BUTTON, "Close button")
        ]
        
        for locator, element_name in elements_to_check:
            assert self.is_element_present(*locator), f"{element_name} is not present"
        
        # Закрываем модальное окно
        self.click_element(*self.CLOSE_BUTTON)
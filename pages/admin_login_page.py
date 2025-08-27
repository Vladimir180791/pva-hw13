from .base_page import BasePage
from selenium.webdriver.common.by import By


class AdminLoginPage(BasePage):
    # Locators
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    LOGO = (By.CLASS_NAME, "login_logo")

    def open(self):
        self.driver.get(self.base_url)

    def should_be_login_page(self):
        self.element_is_visible(self.USERNAME_FIELD)
        self.element_is_visible(self.PASSWORD_FIELD)
        self.element_is_visible(self.LOGIN_BUTTON)
        self.element_is_visible(self.LOGO)

    def login(self, username, password):
        self.find_element(self.USERNAME_FIELD).send_keys(username)
        self.find_element(self.PASSWORD_FIELD).send_keys(password)
        self.find_element(self.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text
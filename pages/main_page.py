# pages/main_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    # Локаторы главной страницы DemoBlaze
    LOGO = (By.ID, "nava")
    CATEGORIES_MENU = (By.ID, "cat")
    PRODUCTS_SECTION = (By.ID, "tbodyid")
    NEXT_BUTTON = (By.ID, "next2")
    PREV_BUTTON = (By.ID, "prev2")
    CART_BUTTON = (By.ID, "cartur")
    LOGIN_BUTTON = (By.ID, "login2")
    SIGNUP_BUTTON = (By.ID, "signin2")
    CONTACT_BUTTON = (By.CSS_SELECTOR, "a[data-target='#exampleModal']")
    ABOUT_US_BUTTON = (By.CSS_SELECTOR, "a[data-target='#videoModal']")

    def check_elements(self):
        """Проверяет наличие элементов на главной странице."""
        elements_to_check = [
            (self.LOGO, "Logo"),
            (self.CATEGORIES_MENU, "Categories menu"),
            (self.PRODUCTS_SECTION, "Products section"),
            (self.CART_BUTTON, "Cart button"),
            (self.LOGIN_BUTTON, "Login button")
        ]
        
        for locator, element_name in elements_to_check:
            assert self.is_element_present(*locator), f"{element_name} is not present"
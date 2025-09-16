# pages/cart_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage


class CartPage(BasePage):
    # Локаторы страницы корзины
    CART_TABLE = (By.CLASS_NAME, "table")
    CART_ITEMS = (By.CSS_SELECTOR, "tbody tr")
    TOTAL_PRICE = (By.ID, "totalp")
    PLACE_ORDER_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-success")
    DELETE_BUTTON = (By.CSS_SELECTOR, "a[onclick*='delete']")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "tbody tr td")

    def check_elements(self):
        """Проверяет наличие элементов на странице корзины."""
        elements_to_check = [
            (self.CART_TABLE, "Cart table"),
            (self.TOTAL_PRICE, "Total price"),
            (self.PLACE_ORDER_BUTTON, "Place order button")
        ]
        
        for locator, element_name in elements_to_check:
            assert self.is_element_present(*locator), f"{element_name} is not present"
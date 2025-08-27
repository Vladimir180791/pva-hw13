# pages/product_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProductPage(BasePage):
    # Локаторы страницы товара
    PRODUCT_NAME = (By.CLASS_NAME, "name")
    PRODUCT_PRICE = (By.CLASS_NAME, "price-container")
    PRODUCT_DESCRIPTION = (By.ID, "more-information")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "a.btn.btn-success.btn-lg")
    PRODUCT_IMAGE = (By.CLASS_NAME, "img-fluid")
    BACK_BUTTON = (By.ID, "backButton")

    def check_elements(self):
        """Проверяет наличие элементов на странице товара."""
        elements_to_check = [
            (self.PRODUCT_NAME, "Product name"),
            (self.PRODUCT_PRICE, "Product price"),
            (self.ADD_TO_CART_BUTTON, "Add to cart button"),
            (self.PRODUCT_IMAGE, "Product image"),
            (self.BACK_BUTTON, "Back button")
        ]
        
        for locator, element_name in elements_to_check:
            assert self.is_element_present(*locator), f"{element_name} is not present"
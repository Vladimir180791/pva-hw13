from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProductPage(BasePage):
    # Локаторы для страницы товара OpenCart
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "li h2, .price")
    ADD_TO_CART_BUTTON = (By.ID, "button-cart")
    QUANTITY_INPUT = (By.ID, "input-quantity")
    PRODUCT_IMAGES = (By.CSS_SELECTOR, "ul.thumbnails")
    DESCRIPTION_TAB = (By.CSS_SELECTOR, "a[href='#tab-description']")

    def check_elements(self):
        """Проверяет наличие всех критичных элементов на странице товара."""
        elements_to_check = [
            (self.PRODUCT_NAME, "Product name"),
            (self.PRODUCT_PRICE, "Product price"),
            (self.ADD_TO_CART_BUTTON, "Add to cart button"),
            (self.QUANTITY_INPUT, "Quantity input")
        ]
        
        for locator, element_name in elements_to_check:
            assert self.is_element_present(*locator), f"{element_name} is not present"
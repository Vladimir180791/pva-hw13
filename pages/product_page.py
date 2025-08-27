from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "li h2")
    PRODUCT_DESCRIPTION = (By.ID, "tab-description")
    ADD_TO_CART_BUTTON = (By.ID, "button-cart")
    QUANTITY_INPUT = (By.ID, "input-quantity")
    PRODUCT_IMAGES = (By.CSS_SELECTOR, "ul.thumbnails")
    REVIEW_TAB = (By.CSS_SELECTOR, "a[href='#tab-review']")
    SPECIFICATION_TAB = (By.CSS_SELECTOR, "a[href='#tab-specification']")

    def check_elements(self):
        """Проверяет наличие всех критичных элементов на странице товара."""
        elements_to_check = [
            (self.PRODUCT_NAME, "Product name"),
            (self.PRODUCT_PRICE, "Product price"),
            (self.ADD_TO_CART_BUTTON, "Add to cart button"),
            (self.QUANTITY_INPUT, "Quantity input"),
            (self.PRODUCT_IMAGES, "Product images")
        ]
        
        for locator, element_name in elements_to_check:
            assert self.is_element_present(*locator), f"{element_name} is not present"
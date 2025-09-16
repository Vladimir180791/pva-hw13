# pages/catalog_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage


class CatalogPage(BasePage):
    # Локаторы страницы каталога
    CATEGORY_TITLE = (By.CLASS_NAME, "card-title")
    PRODUCT_CARDS = (By.CLASS_NAME, "card")
    PRODUCT_NAMES = (By.CLASS_NAME, "hrefch")
    PRODUCT_PRICES = (By.CLASS_NAME, "price-container")
    PRODUCT_IMAGES = (By.CLASS_NAME, "card-img-top")
    PAGINATION = (By.ID, "pagination")

    def check_elements(self):
        """Проверяет наличие элементов в каталоге."""
        elements_to_check = [
            (self.CATEGORY_TITLE, "Category title"),
            (self.PRODUCT_CARDS, "Product cards"),
            (self.PRODUCT_NAMES, "Product names"),
            (self.PRODUCT_PRICES, "Product prices"),
            (self.PAGINATION, "Pagination")
        ]
        
        for locator, element_name in elements_to_check:
            assert self.is_element_present(*locator), f"{element_name} is not present"
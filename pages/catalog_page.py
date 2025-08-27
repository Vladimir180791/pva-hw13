from selenium.webdriver.common.by import By
from .base_page import BasePage


class CatalogPage(BasePage):
    # Локаторы для страницы каталога OpenCart
    CATEGORY_TITLE = (By.CSS_SELECTOR, "h2")
    PRODUCT_LAYOUT = (By.CLASS_NAME, "product-layout")
    SIDEBAR = (By.ID, "column-left")
    BREADCRUMB = (By.CLASS_NAME, "breadcrumb")
    CONTENT = (By.ID, "content")
    PRODUCT_COMPARE = (By.ID, "compare-total")

    def check_elements(self):
        """Проверяет наличие всех критичных элементов в каталоге."""
        elements_to_check = [
            (self.CATEGORY_TITLE, "Category title"),
            (self.PRODUCT_LAYOUT, "Product layout"),
            (self.BREADCRUMB, "Breadcrumb"),
            (self.CONTENT, "Content section")
        ]
        
        for locator, element_name in elements_to_check:
            assert self.is_element_present(*locator), f"{element_name} is not present"
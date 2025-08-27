from selenium.webdriver.common.by import By
from .base_page import BasePage


class CatalogPage(BasePage):
    CATEGORY_TITLE = (By.CSS_SELECTOR, "h2")
    PRODUCT_LAYOUT = (By.CLASS_NAME, "product-layout")
    SIDEBAR = (By.ID, "column-left")
    LIST_VIEW_BUTTON = (By.ID, "list-view")
    GRID_VIEW_BUTTON = (By.ID, "grid-view")
    SORT_SELECT = (By.ID, "input-sort")
    LIMIT_SELECT = (By.ID, "input-limit")
    COMPARE_BUTTON = (By.ID, "compare-total")
    BREADCRUMB = (By.CLASS_NAME, "breadcrumb")

    def check_elements(self):
        """Проверяет наличие всех критичных элементов в каталоге."""
        elements_to_check = [
            (self.CATEGORY_TITLE, "Category title"),
            (self.PRODUCT_LAYOUT, "Product layout"),
            (self.SIDEBAR, "Sidebar"),
            (self.BREADCRUMB, "Breadcrumb")
        ]
        
        for locator, element_name in elements_to_check:
            assert self.is_element_present(*locator), f"{element_name} is not present"
from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    # Обновленные локаторы для главной страницы OpenCart
    SEARCH_INPUT = (By.NAME, "search")
    CART_BUTTON = (By.CSS_SELECTOR, "#cart button")
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "form#form-currency")
    NAVIGATION_MENU = (By.CSS_SELECTOR, "nav#menu")
    SLIDESHOW = (By.CSS_SELECTOR, "div.swiper-wrapper")
    FEATURED_PRODUCTS_SECTION = (By.CSS_SELECTOR, "h3")
    FOOTER = (By.TAG_NAME, "footer")
    LOGO = (By.CSS_SELECTOR, "#logo")
    MENU_BAR = (By.CSS_SELECTOR, "ul.navbar-nav")

    def check_elements(self):
        """Проверяет наличие всех критичных элементов на странице."""
        elements_to_check = [
            (self.SEARCH_INPUT, "Search input"),
            (self.CART_BUTTON, "Cart button"),
            (self.CURRENCY_DROPDOWN, "Currency dropdown"),
            (self.NAVIGATION_MENU, "Navigation menu"),
            (self.FEATURED_PRODUCTS_SECTION, "Featured products section"),
            (self.FOOTER, "Footer"),
            (self.LOGO, "Logo")
        ]
        
        for locator, element_name in elements_to_check:
            assert self.is_element_present(*locator), f"{element_name} is not present"
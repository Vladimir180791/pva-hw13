from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    SEARCH_INPUT = (By.NAME, "search")
    CART_BUTTON = (By.ID, "cart")
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "[data-toggle='dropdown']")
    NAVIGATION_MENU = (By.CSS_SELECTOR, "nav#menu")
    SLIDESHOW = (By.CSS_SELECTOR, "div.swiper-viewport")
    FEATURED_PRODUCTS_SECTION = (By.CSS_SELECTOR, "h3")
    FOOTER = (By.TAG_NAME, "footer")
    LOGO = (By.ID, "logo")
    MENU_BAR = (By.CSS_SELECTOR, "ul.navbar-nav")

    def check_elements(self):
        """Проверяет наличие всех критичных элементов на странице."""
        elements_to_check = [
            (self.SEARCH_INPUT, "Search input"),
            (self.CART_BUTTON, "Cart button"),
            (self.CURRENCY_DROPDOWN, "Currency dropdown"),
            (self.NAVIGATION_MENU, "Navigation menu"),
            (self.SLIDESHOW, "Slideshow"),
            (self.FEATURED_PRODUCTS_SECTION, "Featured products section"),
            (self.FOOTER, "Footer"),
            (self.LOGO, "Logo"),
            (self.MENU_BAR, "Menu bar")
        ]
        
        for locator, element_name in elements_to_check:
            assert self.is_element_present(*locator), f"{element_name} is not present"
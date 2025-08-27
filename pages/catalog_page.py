from selenium.webdriver.common.by import By
from .base_page import BasePage


class CatalogPage(BasePage):
    SEARCH_INPUT = (By.NAME, "search")
    CART_BUTTON = (By.ID, "Product")
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "button.btn-link dropdown-toggle")
    NAVIGATION_MENU = (By.CSS_SELECTOR, "nav#menu")
    SLIDESHOW = (By.CSS_SELECTOR, "div#carousel-banner-0")
    FEATURED_PRODUCTS_SECTION = (By.CSS_SELECTOR, "div#content h3")
    FOOTER = (By.TAG_NAME, "footer")

    def check_elements(self):
        assert self.is_element_present(*self.SEARCH_INPUT), "Search input is not present"
        assert self.is_element_present(*self.CART_BUTTON), "Cart button is not present"
        assert self.is_element_present(*self.CURRENCY_DROPDOWN), "Currency dropdown is not present"
        assert self.is_element_present(*self.NAVIGATION_MENU), "Navigation menu is not present"
        assert self.is_element_present(*self.SLIDESHOW), "Slideshow is not present"
from .base_page import BasePage
from selenium.webdriver.common.by import By
import random


class MainPage(BasePage):
    # Locators
    LOGO = (By.CLASS_NAME, "app_logo")
    LOGIN_BUTTON = (By.ID, "login-button")
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button[class*='btn_inventory']")
    CURRENCY_SWITCHER = (By.CLASS_NAME, "product_sort_container")

    def should_be_main_page(self):
        # Проверка, что мы на главной странице после логина
        assert "inventory" in self.driver.current_url, "This is not the main page"
        self.element_is_visible(self.PRODUCTS_TITLE)
        self.element_is_visible(self.SHOPPING_CART_LINK)

    def get_product_items(self):
        return self.find_elements(self.PRODUCT_ITEMS)

    def get_random_product(self):
        products = self.get_product_items()
        return random.choice(products)

    def add_product_to_cart(self, product):
        add_button = product.find_element(*self.ADD_TO_CART_BUTTONS)
        add_button.click()
        return add_button.text.strip() == "Remove"  # Проверяем, что кнопка сменилась на "Remove"

    def get_product_name(self, product):
        return product.find_element(*self.PRODUCT_ITEM_NAMES).text

    def get_product_price(self, product):
        return product.find_element(*self.PRODUCT_ITEM_PRICES).text

    def go_to_cart(self):
        self.find_element(self.SHOPPING_CART_LINK).click()

    def switch_currency(self, option_value="lohi"):
        # lohi - low to high, hilo - high to low
        dropdown = self.find_element(self.CURRENCY_SWITCHER)
        dropdown.click()
        from selenium.webdriver.support.ui import Select
        select = Select(dropdown)
        select.select_by_value(option_value)

    def get_all_prices(self):
        prices = self.find_elements(self.PRODUCT_ITEM_PRICES)
        return [float(price.text.replace('$', '')) for price in prices]
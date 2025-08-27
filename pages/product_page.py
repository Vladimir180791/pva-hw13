from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    # Locators
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_details_name")
    PRODUCT_DESCRIPTION = (By.CLASS_NAME, "inventory_details_desc")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_details_price")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[class*='btn_inventory']")
    BACK_BUTTON = (By.ID, "back-to-products")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def should_be_product_page(self):
        self.element_is_visible(self.PRODUCT_NAME)
        self.element_is_visible(self.PRODUCT_PRICE)
        self.element_is_visible(self.ADD_TO_CART_BUTTON)

    def get_product_name(self):
        return self.find_element(self.PRODUCT_NAME).text

    def get_product_price(self):
        return self.find_element(self.PRODUCT_PRICE).text

    def add_to_cart(self):
        self.find_element(self.ADD_TO_CART_BUTTON).click()

    def back_to_products(self):
        self.find_element(self.BACK_BUTTON).click()

    def get_cart_items_count(self):
        try:
            badge = self.find_element(self.SHOPPING_CART_BADGE, time=2)
            return int(badge.text)
        except:
            return 0
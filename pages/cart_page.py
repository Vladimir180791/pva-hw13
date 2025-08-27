from .base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    # Locators
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button[class*='cart_button']")

    def should_be_cart_page(self):
        assert "cart" in self.driver.current_url, "This is not the cart page"
        self.element_is_visible((By.ID, "cart_contents_container"))

    def get_cart_items(self):
        return self.find_elements(self.CART_ITEM)

    def get_cart_item_names(self):
        items = self.get_cart_items()
        return [item.find_element(*self.CART_ITEM_NAME).text for item in items]

    def is_item_in_cart(self, item_name):
        return item_name in self.get_cart_item_names()

    def remove_item_from_cart(self, item_name=None):
        if item_name:
            items = self.get_cart_items()
            for item in items:
                if item.find_element(*self.CART_ITEM_NAME).text == item_name:
                    item.find_element(*self.REMOVE_BUTTON).click()
                    break
        else:
            self.find_element(self.REMOVE_BUTTON).click()

    def proceed_to_checkout(self):
        self.find_element(self.CHECKOUT_BUTTON).click()

    def continue_shopping(self):
        self.find_element(self.CONTINUE_SHOPPING_BUTTON).click()
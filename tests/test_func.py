import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_admin_login_logout(browser):
    browser.get(f"{browser.base_url}administration/")
    
    # Login
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "input-username"))
    ).send_keys("admin")
    
    browser.find_element(By.ID, "input-password").send_keys("admin")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    # Verify login
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "menu-dashboard"))
    )
    
    # Logout
    browser.find_element(By.LINK_TEXT, "Logout").click()
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.panel-heading"))
    )

def test_add_random_product_to_cart(browser):
    browser.get(browser.base_url)
    
    products = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-thumb"))
    )
    product = random.choice(products)
    product_name = product.find_element(By.CSS_SELECTOR, "h4 a").text
    
    product.find_element(By.CSS_SELECTOR, "button[onclick*='cart.add']").click()
    
    # Verify cart notification
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert-success"))
    )
    
    # Check cart
    browser.get(f"{browser.base_url}index.php?route=checkout/cart")
    cart_items = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.table-responsive tr"))
    )
    assert any(product_name in item.text for item in cart_items)

def test_currency_switch_main_page(browser):
    browser.get(browser.base_url)
    _test_currency_switch(browser)

def test_currency_switch_catalog_page(browser):
    browser.get(f"{browser.base_url}index.php?route=product/category&path=20")
    _test_currency_switch(browser)

def _test_currency_switch(browser):
    # Get initial prices
    initial_prices = _get_product_prices(browser)
    
    # Switch currency
    browser.find_element(By.CSS_SELECTOR, "form#form-currency").click()
    current_currency = browser.find_element(By.CSS_SELECTOR, "button strong").text
    
    new_currency = "€" if current_currency == "$" else "$"
    browser.find_element(By.NAME, "EUR" if new_currency == "€" else "USD").click()
    
    # Wait for currency change
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "button strong"), new_currency)
    )
    
    # Verify prices changed
    new_prices = _get_product_prices(browser)
    assert initial_prices != new_prices

def _get_product_prices(browser):
    return [price.text for price in browser.find_elements(By.CSS_SELECTOR, "p.price") if price.text]
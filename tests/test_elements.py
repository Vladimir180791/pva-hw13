from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_main_page_elements(browser):
    browser.get(browser.base_url)
    
    elements = [
        (By.ID, "logo"),
        (By.NAME, "search"),
        (By.CSS_SELECTOR, "div.swiper-viewport"),
        (By.CSS_SELECTOR, "footer"),
        (By.LINK_TEXT, "My Account")
    ]
    
    for locator in elements:
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located(locator))

def test_catalog_page_elements(browser):
    browser.get(f"{browser.base_url}index.php?route=product/category&path=20")
    
    elements = [
        (By.CSS_SELECTOR, "div#product-category"),
        (By.ID, "input-sort"),
        (By.ID, "input-limit"),
        (By.CSS_SELECTOR, "div.product-thumb"),
        (By.CSS_SELECTOR, "div.caption > h4 > a")
    ]
    
    for locator in elements:
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located(locator))

# Аналогичные тесты для остальных страниц (product_page, admin_login, register_page)
# ...
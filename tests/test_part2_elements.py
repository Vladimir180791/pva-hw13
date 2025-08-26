from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from pages.product_page import ProductPage
from pages.admin_login_page import AdminLoginPage
from pages.register_page import RegisterPage


def test_main_page_elements(browser):
    page = MainPage(browser)
    browser.get(browser.url)
    page.check_elements()


def test_catalog_page_elements(browser):
    page = CatalogPage(browser)
    browser.get(f"{browser.url}index.php?route=product/category&path=20")
    page.check_elements()


def test_product_page_elements(browser):
    page = ProductPage(browser)
    browser.get(f"{browser.url}index.php?route=product/category&path=20")
    product_link = browser.find_element(By.CSS_SELECTOR, "div.product-thumb a:first-child")
    product_link.click()
    page.check_elements()


def test_admin_login_page_elements(browser):
    page = AdminLoginPage(browser)
    browser.get(f"{browser.url}administration/")
    page.check_elements()


def test_register_page_elements(browser):
    page = RegisterPage(browser)
    browser.get(f"{browser.url}index.php?route=account/register")
    page.check_elements()
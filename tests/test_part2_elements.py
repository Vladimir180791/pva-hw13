import pytest
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.admin_login_page import AdminLoginPage
from pages.register_page import RegisterPage
from pages.cart_page import CartPage


class TestPart2Elements:
    @pytest.mark.usefixtures("browser")
    def test_main_page_elements(self, browser, base_url):
        page = MainPage(browser)
        page.open(base_url)
        
        # Проверяем элементы на главной странице (до логина)
        page.element_is_visible(page.LOGO)
        page.element_is_visible(page.USERNAME_FIELD)
        page.element_is_visible(page.PASSWORD_FIELD)
        page.element_is_visible(page.LOGIN_BUTTON)
        # Элемент появляется только при ошибке, поэтому не проверяем его всегда

    @pytest.mark.usefixtures("browser")
    def test_catalog_page_elements(self, browser, base_url):
        # Логинимся сначала
        login_page = AdminLoginPage(browser)
        login_page.open(base_url)
        login_page.login("standard_user", "secret_sauce")
        
        page = MainPage(browser)
        page.should_be_main_page()
        
        # Проверяем элементы каталога (главной страницы после логина)
        page.element_is_visible(page.LOGO)
        page.element_is_visible(page.PRODUCTS_TITLE)
        page.element_is_visible(page.SHOPPING_CART_LINK)
        page.element_is_visible(page.MENU_BUTTON)
        
        # Проверяем, что есть товары
        products = page.get_product_items()
        assert len(products) >= 1, "There should be at least one product on the page"

    @pytest.mark.usefixtures("browser")
    def test_product_page_elements(self, browser, base_url):
        # Логинимся сначала
        login_page = AdminLoginPage(browser)
        login_page.open(base_url)
        login_page.login("standard_user", "secret_sauce")
        
        # Переходим на страницу товара
        main_page = MainPage(browser)
        products = main_page.get_product_items()
        products[0].find_element(*main_page.PRODUCT_ITEM_NAMES).click()
        
        page = ProductPage(browser)
        page.should_be_product_page()
        
        # Проверяем элементы страницы товара
        page.element_is_visible(page.PRODUCT_NAME)
        page.element_is_visible(page.PRODUCT_DESCRIPTION)
        page.element_is_visible(page.PRODUCT_PRICE)
        page.element_is_visible(page.ADD_TO_CART_BUTTON)
        page.element_is_visible(page.BACK_BUTTON)

    @pytest.mark.usefixtures("browser")
    def test_admin_login_page_elements(self, browser, base_url):
        page = AdminLoginPage(browser)
        page.open(base_url)
        page.should_be_login_page()
        
        # Проверяем элементы страницы логина
        page.element_is_visible(page.LOGO)
        page.element_is_visible(page.USERNAME_FIELD)
        page.element_is_visible(page.PASSWORD_FIELD)
        page.element_is_visible(page.LOGIN_BUTTON)

    @pytest.mark.usefixtures("browser")
    def test_register_page_elements(self, browser, base_url):
        # Используем страницу логина как страницу "регистрации"
        page = RegisterPage(browser)
        page.open(base_url)
        page.should_be_login_page()
        
        # Проверяем те же элементы, что и на странице логина
        page.element_is_visible(page.LOGO)
        page.element_is_visible(page.USERNAME_FIELD)
        page.element_is_visible(page.PASSWORD_FIELD)
        page.element_is_visible(page.LOGIN_BUTTON)
# tests/test_part2_elements.py
import pytest
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from pages.product_page import ProductPage
from pages.admin_login_page import AdminLoginPage
from pages.register_page import RegisterPage


class TestPart2Elements:
    """Тесты для проверки наличия элементов на страницах (Часть 2 ТЗ)"""
    
    def test_main_page_elements(self, browser):
        """Тест наличия элементов на главной странице."""
        page = MainPage(browser)
        browser.get(browser.url)
        page.check_elements()
        print("✓ Главная страница: все элементы присутствуют")

    def test_catalog_page_elements(self, browser):
        """Тест наличия элементов в каталоге."""
        page = CatalogPage(browser)
        browser.get(f"{browser.url}index.php?route=product/category&path=20")
        page.check_elements()
        print("✓ Страница каталога: все элементы присутствуют")

    def test_product_page_elements(self, browser):
        """Тест наличия элементов в карточке товара."""
        page = ProductPage(browser)
        
        # Сначала переходим в каталог
        browser.get(f"{browser.url}index.php?route=product/category&path=20")
        
        # Ждем загрузки товаров и кликаем на первый товар
        page.wait.until(
            lambda driver: driver.find_elements(By.CSS_SELECTOR, "div.product-thumb")
        )
        product_links = browser.find_elements(By.CSS_SELECTOR, "div.product-thumb a")
        if product_links:
            product_links[0].click()
            
            # Проверяем элементы на странице товара
            page.check_elements()
            print("✓ Страница товара: все элементы присутствуют")
        else:
            pytest.skip("No products found in catalog")

    def test_admin_login_page_elements(self, browser):
        """Тест наличия элементов на странице логина в админку."""
        page = AdminLoginPage(browser)
        browser.get(f"{browser.url}administration/")
        page.check_elements()
        print("✓ Страница логина в админку: все элементы присутствуют")

    def test_register_page_elements(self, browser):
        """Тест наличия элементов на странице регистрации."""
        page = RegisterPage(browser)
        browser.get(f"{browser.url}index.php?route=account/register")
        page.check_elements()
        print("✓ Страница регистрации: все элементы присутствуют")
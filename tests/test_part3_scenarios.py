import pytest
from pages.admin_login_page import AdminLoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
import time


class TestPart3Scenarios:
    @pytest.mark.usefixtures("browser")
    def test_login_logout_admin(self, browser, base_url):
        login_page = AdminLoginPage(browser)
        login_page.open(base_url)
        login_page.should_be_login_page()
        
        # Логинимся
        login_page.login("standard_user", "secret_sauce")
        
        # Проверяем, что логин успешен
        main_page = MainPage(browser)
        main_page.should_be_main_page()
        
        # Разлогиниваемся через меню
        main_page.find_element(main_page.MENU_BUTTON).click()
        logout_link = main_page.find_element((By.ID, "logout_sidebar_link"))
        logout_link.click()
        
        # Проверяем, что вернулись на страницу логина
        login_page.should_be_login_page()

    @pytest.mark.usefixtures("browser")
    def test_add_to_cart_from_main_page(self, browser, base_url):
        # Логинимся
        login_page = AdminLoginPage(browser)
        login_page.open(base_url)
        login_page.login("standard_user", "secret_sauce")
        
        # Добавляем случайный товар в корзину
        main_page = MainPage(browser)
        product = main_page.get_random_product()
        product_name = main_page.get_product_name(product)
        
        # Добавляем товар в корзину
        main_page.add_product_to_cart(product)
        
        # Переходим в корзину
        main_page.go_to_cart()
        
        # Проверяем, что товар в корзине
        cart_page = CartPage(browser)
        cart_page.should_be_cart_page()
        assert cart_page.is_item_in_cart(product_name), f"Product {product_name} should be in cart"

    @pytest.mark.usefixtures("browser")
    def test_currency_switch_on_main_page(self, browser, base_url):
        # Логинимся
        login_page = AdminLoginPage(browser)
        login_page.open(base_url)
        login_page.login("standard_user", "secret_sauce")
        
        main_page = MainPage(browser)
        
        # Получаем цены до сортировки
        prices_before = main_page.get_all_prices()
        
        # Сортируем от низкой к высокой цене
        main_page.switch_currency("lohi")
        time.sleep(1)  # Даем время странице обновиться
        
        # Получаем цены после сортировки
        prices_after = main_page.get_all_prices()
        
        # Проверяем, что цены отсортированы по возрастанию
        assert prices_after == sorted(prices_before), "Prices should be sorted from low to high"

    @pytest.mark.usefixtures("browser")
    def test_currency_switch_in_catalog(self, browser, base_url):
        # Логинимся
        login_page = AdminLoginPage(browser)
        login_page.open(base_url)
        login_page.login("standard_user", "secret_sauce")
        
        main_page = MainPage(browser)
        
        # Получаем цены до сортировки
        prices_before = main_page.get_all_prices()
        
        # Сортируем от высокой к низкой цене
        main_page.switch_currency("hilo")
        time.sleep(1)  # Даем время странице обновиться
        
        # Получаем цены после сортировки
        prices_after = main_page.get_all_prices()
        
        # Проверяем, что цены отсортированы по убыванию
        assert prices_after == sorted(prices_before, reverse=True), "Prices should be sorted from high to low"
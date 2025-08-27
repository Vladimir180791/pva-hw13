import pytest
import time
from pages.admin_login_page import AdminLoginPage


class TestAdminLoginLogout:
    """Тесты для логина и разлогина в админку OpenCart"""
    
    def test_debug_admin_page(self, browser):
        """Тест для отладки - посмотрим, что на самом деле на странице"""
        page = AdminLoginPage(browser)
        browser.get(f"{browser.url}administration/")
        
        # Выводим отладочную информацию
        page.debug_page_info()
        
        # Делаем скриншот
        page.take_screenshot("admin_login_page")
        
        # Этот тест всегда проходит, он только для отладки
        assert True

    @pytest.mark.parametrize("username,password,expected_success", [
        ("demo", "demo", True),  # Стандартные credentials для демо OpenCart
        ("wrong_user", "wrong_pass", False),
        ("", "", False),
    ])
    def test_admin_login_with_different_credentials(self, browser, username, password, expected_success):
        """Тестирует логин с различными учетными данными"""
        page = AdminLoginPage(browser)
        browser.get(f"{browser.url}administration/")
        
        # Выводим отладочную информацию
        page.debug_page_info()
        
        # Проверяем, что находимся на странице логина
        assert "administration" in browser.current_url
        assert page.is_login_page(), "Not on login page"
        
        # Выполняем логин
        page.login(username, password)
        
        # Ждем результат
        time.sleep(3)
        
        if expected_success:
            # Проверяем успешный логин
            assert page.is_login_successful(), "Login should be successful but wasn't"
            print("✓ Login successful")
            
        else:
            # Проверяем неуспешный логин
            assert not page.is_login_successful(), "Login should have failed but succeeded"
            assert page.is_login_failed() or page.is_login_page(), \
                   "Should show error or stay on login page"
            print("✓ Login failed as expected")

    def test_admin_login_logout_success_flow(self, browser):
        """Тест полного цикла успешного логина и разлогина"""
        page = AdminLoginPage(browser)
        browser.get(f"{browser.url}administration/")
        
        page.debug_page_info()
        
        # Проверяем начальное состояние
        assert page.is_login_page(), "Should be on login page initially"
        
        # Логинимся
        page.login("demo", "demo")
        
        # Ждем и проверяем успешный логин
        time.sleep(3)
        assert page.is_login_successful(), "Login failed"
        print("✓ Login successful")
        
        # Разлогиниваемся
        page.logout()
        
        # Проверяем, что вернулись на страницу логина
        time.sleep(2)
        assert page.is_login_page(), "Should return to login page after logout"
        print("✓ Logout successful")

    def test_admin_login_with_invalid_credentials(self, browser):
        """Тестирует поведение при неверных учетных данных"""
        page = AdminLoginPage(browser)
        browser.get(f"{browser.url}administration/")
        
        page.debug_page_info()
        
        # Пытаемся войти с неверными данными
        page.login("invalid_user", "invalid_password")
        
        # Ждем результат
        time.sleep(3)
        
        # Проверяем, что логин не удался
        assert not page.is_login_successful(), "Login should have failed but succeeded"
        assert page.is_login_failed() or page.is_login_page(), \
               "Should show error or stay on login page"
        print("✓ Invalid login handled correctly")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])  # -s для вывода print-ов
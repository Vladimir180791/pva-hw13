import pytest
import time
from pages.admin_login_page import AdminLoginPage


class TestAdminLoginLogout:
    """Тесты для логина и разлогина в админку OpenCart"""
    
    @pytest.mark.parametrize("username,password,expected_success", [
        ("admin", "admin", True),  # Верные credentials (замените на актуальные для демо-стенда)
        ("wrong_user", "wrong_pass", False),  # Неверные credentials
        ("", "", False),  # Пустые credentials
    ])
    def test_admin_login_with_different_credentials(self, browser, username, password, expected_success):
        """Тестирует логин с различными учетными данными"""
        page = AdminLoginPage(browser)
        browser.get(f"{browser.url}administration/")
        
        # Проверяем, что находимся на странице логина
        assert "administration" in browser.current_url
        page.check_elements()
        
        # Выполняем логин
        page.login(username, password)
        
        # Даем время для обработки логина
        time.sleep(2)
        
        if expected_success:
            # Проверяем успешный логин
            assert page.is_login_successful(), "Login should be successful but wasn't"
            assert "dashboard" in browser.current_url.lower() or "common/dashboard" in browser.current_url
            
            # Выполняем logout
            page.logout()
            
            # Проверяем, что вернулись на страницу логина
            page.wait.until(lambda driver: "login" in driver.current_url.lower())
            assert "login" in browser.current_url.lower()
            
        else:
            # Проверяем неуспешный логин
            assert page.is_login_failed(), "Login should have failed but didn't"
            assert "administration" in browser.current_url or "login" in browser.current_url

    def test_admin_login_logout_success_flow(self, browser):
        """Тест полного цикла успешного логина и разлогина"""
        page = AdminLoginPage(browser)
        browser.get(f"{browser.url}administration/")
        
        # Проверяем начальное состояние - страница логина
        assert "administration" in browser.current_url
        page.check_elements()
        
        # Логинимся с правильными credentials (замените на актуальные)
        # На демо-стенде обычно: username="demo", password="demo"
        page.login("demo", "demo")
        
        # Ждем и проверяем успешный логин
        page.wait.until(
            lambda driver: page.is_login_successful() or page.is_login_failed(),
            message="Login process didn't complete in time"
        )
        
        assert page.is_login_successful(), "Successful login was expected but failed"
        assert any(keyword in browser.current_url.lower() 
                  for keyword in ["dashboard", "common/dashboard", "admin"]), \
               f"Not redirected to dashboard after login. Current URL: {browser.current_url}"
        
        print("✓ Login successful")
        
        # Выполняем logout
        page.logout()
        
        # Проверяем, что вернулись на страницу логина
        page.wait.until(
            lambda driver: "login" in driver.current_url.lower(),
            message="Logout didn't redirect to login page"
        )
        
        assert "login" in browser.current_url.lower(), \
               f"Not redirected to login page after logout. Current URL: {browser.current_url}"
        
        # Проверяем, что элементы страницы логина снова доступны
        page.check_elements()
        
        print("✓ Logout successful")

    def test_admin_login_with_invalid_credentials(self, browser):
        """Тестирует поведение при неверных учетных данных"""
        page = AdminLoginPage(browser)
        browser.get(f"{browser.url}administration/")
        
        # Пытаемся войти с неверными данными
        page.login("invalid_user", "invalid_password")
        
        # Ждем появления сообщения об ошибке или остаемся на странице логина
        page.wait.until(
            lambda driver: page.is_login_failed() or "login" in driver.current_url.lower(),
            message="No response to invalid login attempt"
        )
        
        # Проверяем, что логин не удался
        assert not page.is_login_successful(), "Login should have failed but succeeded"
        assert page.is_login_failed() or "login" in browser.current_url.lower(), \
               "No error message shown for invalid credentials"
        
        print("✓ Invalid login handled correctly")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
import pytest


class TestPart1Setup:
    """Тесты для проверки настройки окружения"""
    
    def test_browser_launch(self, driver, base_url):
        """Тест запуска браузера и открытия базового URL"""
        driver.get(base_url)
        assert "DEMOBLAZE" in driver.title
        assert driver.current_url == base_url + "/"
    
    def test_browser_window_size(self, driver, base_url):
        """Тест размера окна браузера"""
        driver.get(base_url)
        window_size = driver.get_window_size()
        assert window_size['width'] >= 1920
        assert window_size['height'] >= 1080
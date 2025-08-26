def test_admin_login_logout(browser):
    page = AdminLoginPage(browser)
    browser.get(f"{browser.url}administration/")

    page.login("admin", "admin")
    assert page.is_logged_in(), "Login was unsuccessful"

    page.logout()

    page.wait.until(EC.url_contains("login"))
    assert "login" in browser.current_url
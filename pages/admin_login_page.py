class AdminLoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "input-username")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.TAG_NAME, "button")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href*='logout']")
    USER_PROFILE = (By.CSS_SELECTOR, "img.img-profile")

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_logged_in(self):
        return self.is_element_present(*self.USER_PROFILE)

    def logout(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()
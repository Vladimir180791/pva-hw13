def test_login_modal_elements(self, driver, base_url, wait):
    """Проверка элементов в модальном окне логина"""
    driver.get(base_url)
    
    # Ждем полной загрузки страницы
    wait.until(EC.presence_of_element_located((By.ID, "login2")))
    
    # Используем JavaScript для клика, чтобы избежать проблем с видимостью
    login_button = driver.find_element(By.ID, "login2")
    driver.execute_script("arguments[0].click();", login_button)
    
    # Ожидание появления модального окна
    wait.until(EC.visibility_of_element_located((By.ID, "logInModal")))
    
    elements_to_check = [
        (By.ID, "loginusername", "Поле username"),
        (By.ID, "loginpassword", "Поле password"),
        (By.XPATH, "//button[text()='Log in']", "Кнопка Login"),
        (By.CLASS_NAME, "modal-title", "Заголовок модального окна"),
    ]
    
    for by, value, element_name in elements_to_check:
        try:
            element = wait.until(EC.visibility_of_element_located((by, value)))
            assert element.is_displayed(), f"Элемент {element_name} не отображается"
        except Exception as e:
            # Если элемент не найден, делаем скриншот и продолжаем
            driver.save_screenshot(f"error_{element_name}.png")
            raise e
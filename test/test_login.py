import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import yaml

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from utils.screenshot_utils import save_screenshot

with open("config/config.yml", "r") as file:
    config = yaml.safe_load(file)

def test_valid_login(driver):
    driver.get(config["base_url"] + "/login")
    login_page = LoginPage(driver)
    login_page.enter_username(config["username"])
    login_page.enter_password(config["password"])
    save_screenshot(driver, "login_exitoso", "data")
    login_page.click_login()
    assert "Escritorio - control_web" in driver.title
    save_screenshot(driver, "login_exitoso", "pantalla_principal")    

def test_invalid_login(driver):
    driver.get(config["base_url"] + "/login")
    login_page = LoginPage(driver)
    login_page.enter_username("usuario@correo.com")
    login_page.enter_password("123456")
    save_screenshot(driver, "login_fallido", "data")
    login_page.click_login()
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element(
            (By.TAG_NAME, "body"),
            "Usuario o contraseña invalido."
        )
    )
    assert "Usuario o contraseña invalido." in driver.page_source
    save_screenshot(driver, "login_fallido", "pantalla_login")

def logout(driver):
    driver.get(config["base_url"] + "/logout")

if __name__ == "__main__":
    for test in [test_valid_login, test_invalid_login]:
        driver = webdriver.Firefox()
        try:
            test(driver)
        finally:
            driver.quit()
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import yaml
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

# cargar configuracion desde config.yml
with open("config/config.yml", "r") as file:
    config = yaml.safe_load(file)

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def save_screenshot(driver, nameTest, nameFile):
    os.makedirs(f"screenshots/{nameTest}", exist_ok=True)
    filename = f"screenshots/{nameTest}/{nameFile}.png"
    driver.save_screenshot(filename)


def test_valid_login(driver, request):
    driver.get(config["base_url"] + "/login")
    login_page = LoginPage(driver)
    login_page.enter_username(config["username"])
    login_page.enter_password(config["password"])
    save_screenshot(driver, "login_exitoso", "data")
    login_page.click_login()
    assert "Escritorio - control_web" in driver.title
    save_screenshot(driver, "login_exitoso", "pantalla_principal")

def test_invalid_login(driver, request):
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
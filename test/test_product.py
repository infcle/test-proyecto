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
from pages.product.list_page import ProductPage
from pages.product.product_page import ProductPage
from utils.screenshot_utils import save_screenshot
import time 

# cargar configuracion desde config.yml
with open("config/config.yml", "r") as file:
    config = yaml.safe_load(file)

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def login(driver):
    """Función auxiliar para iniciar sesión antes de entrar a productos."""
    driver.get(config["base_url"] + "/login")
    login_page = LoginPage(driver)
    login_page.enter_username(config["username"])
    login_page.enter_password(config["password"])
    login_page.click_login()
    WebDriverWait(driver, 5).until(
        EC.title_contains("Escritorio - control_web")
    )

def test_crear_producto_exitoso(driver):
    login(driver)
    driver.get(config["base_url"] + "/admin/products/create")
    product_page = ProductPage(driver)

    product_page.enter_name("Producto QA")
    product_page.enter_description("Producto de prueba con imagen")
    product_page.toggle_sellable()
    product_page.enter_min_stock(15)
    product_page.upload_image(r"C:\Users\Elmer\Pictures\ataud\ataud_1.jpg")
    save_screenshot(driver, "producto_exitoso", "pantalla_guardado")

    
    time.sleep(1)
    product_page.click_save()


    # Esperar confirmación (puede ser mensaje o redirección)
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Producto creado con éxito")
    )
    assert "Producto creado con éxito" in driver.page_source


def test_crear_producto_nombre_vacio(driver):
    login(driver)
    driver.get(config["base_url"] + "/admin/products/create")
    product_page = ProductPage(driver)

    # No llenamos el nombre (campo obligatorio)
    product_page.enter_description("Producto sin nombre")
    product_page.upload_image("imagenes/prueba.jpg")
    product_page.click_save()

    save_screenshot(driver, "producto_nombre_vacio", "pantalla_error")

    # Esperar el mensaje de error
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "El campo nombre es obligatorio")
    )

    assert "El campo nombre es obligatorio" in driver.page_source

import sys
import os
import yaml
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.product.list_page import ProductPage
from pages.product.product_page import ProductPage
from utils.screenshot_utils import save_screenshot
from utils.test_helpers import capture_screenshot_on_failure, wait_for_element_with_screenshot


# cargar configuracion desde config.yml
config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yml')
with open(config_path, "r") as file:
    config = yaml.safe_load(file)

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

@capture_screenshot_on_failure("producto_exitoso_error")
def test_crear_producto_exitoso(driver):
    login(driver)
    driver.get(config["base_url"] + "/admin/products/create")
    product_page = ProductPage(driver)

    product_page.enter_name("Producto QA")
    product_page.enter_description("Producto de prueba")
    product_page.toggle_sellable()
    product_page.enter_min_stock(15)

    save_screenshot(driver, "producto_exitoso", "pantalla_guardado")

    product_page.click_save()

    wait_for_element_with_screenshot(
        driver,
        (By.CSS_SELECTOR, "h3.fi-no-notification-title"),
        15,
        "producto_exitoso_error"
    )
    print("Producto creado")
    assert "Producto creado" in driver.page_source

def test_crear_producto_nombre_vacio(driver):
    login(driver)
    driver.get(config["base_url"] + "/admin/products/create")
    product_page = ProductPage(driver)

    # No llenamos el nombre (campo obligatorio)
    product_page.enter_description("Producto sin nombre")    
    product_page.toggle_sellable()

    save_screenshot(driver, "producto_nombre_vacio", "antes_guardar")

    # Intentar enviar formulario
    product_page.click_save()

    # Verificar que el campo "name" está inválido en frontend usando el id real
    nombre_input = driver.find_element(By.ID, "data.name")  # id exacto según tu input
    is_valid = driver.execute_script("return arguments[0].checkValidity();", nombre_input)
    validation_message = driver.execute_script("return arguments[0].validationMessage;", nombre_input)

    assert is_valid is False, "El campo nombre debería ser inválido por estar vacío"
    print(f"Mensaje de validación: {validation_message}")

    save_screenshot(driver, "producto_nombre_vacio", "validacion_frontend")

if __name__ == "__main__":
    for test in [test_crear_producto_exitoso, test_crear_producto_nombre_vacio]:
        driver = webdriver.Firefox()
        try:
            test(driver)
        finally:
            driver.quit()
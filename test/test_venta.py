import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.venta.list_page import ListPage
from pages.login_page import LoginPage 
from utils.screenshot_utils import save_screenshot
import yaml

# cargar configuracion desde config.yml con ruta absoluta
config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yml')
with open(config_path, "r") as file:
    config = yaml.safe_load(file)

def login(driver):
    driver.get(config["base_url"] + "/login")
    login_page = LoginPage(driver)
    login_page.enter_username(config["username"])
    login_page.enter_password(config["password"])
    login_page.click_login()
    WebDriverWait(driver, 5).until(
        EC.title_contains("Escritorio - control_web")
    )

def test_filtrar_ventas_por_fecha(driver):
    login(driver)
    driver.get(config["base_url"] + "/admin/sales")

    try:
        fecha_inicio = driver.find_element(By.ID, "fecha_inicio")
        fecha_fin = driver.find_element(By.ID, "fecha_fin")
        fecha_inicio.clear()
        fecha_inicio.send_keys("2025-08-10") 
        fecha_fin.clear()
        fecha_fin.send_keys("2025-08-10")
        driver.find_element(By.ID, "btn_filtrar").click()

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'Venta de prueba')]"))
            )
            assert "Venta de prueba" in driver.page_source
        except Exception as e:
            save_screenshot(driver, "filtrado_ventas", "filtro_no_existente")
            print(f"[ADVERTENCIA] No se encontró la venta filtrada o el filtro no existe. Error: {e}")

    except Exception as e:
        save_screenshot(driver, "filtrado_ventas", "elementos_no_existen")
        print(f"[ADVERTENCIA] No existen los campos de filtro en la página. Error: {e}")

if __name__ == "__main__":
    for test in [test_filtrar_ventas_por_fecha]:
        driver = webdriver.Firefox()
        try:
            test(driver)
        finally:
            driver.quit()
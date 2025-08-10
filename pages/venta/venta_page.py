from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class VentaPage(BasePage):
    CUSTOMER_DROPDOWN = (By.ID, "data.customer_id")
    CUSTOMER_DROPDOWN_PLACEHOLDER = (By.CSS_SELECTOR, ".grid:nth-child(2) > .fi-input-wrp .choices__placeholder")
    CUSTOMER_DROPDOWN_OPEN = (By.CSS_SELECTOR, ".is-open > .choices__inner")
    DESCRIPTION_INPUT = (By.ID, "data.description")
    SAVE_BUTTON = (By.ID, "save-button")  # Ajusta si el id es distinto

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def select_customer(self, customer_name):
        print("Seleccionando cliente:", customer_name)
        time.sleep(0.2)
        # Abrir dropdown
        self.click_element(self.CUSTOMER_DROPDOWN_PLACEHOLDER)
        time.sleep(0.5)
        print("Abriendo dropdown de clientes")
        self.wait_for_element(self.CUSTOMER_DROPDOWN_OPEN)
        self.click_element(self.CUSTOMER_DROPDOWN_OPEN)
        
        # Buscar la opción por texto visible (ajusta el selector según tu HTML)
        option_xpath = f"//div[contains(@class, 'choices__item') and text()='{customer_name}']"
        option = self.driver.find_element(By.XPATH, option_xpath)
        option.click()

    def enter_description(self, description):
        time.sleep(0.2)
        self.enter_text(self.DESCRIPTION_INPUT, description)

    def click_save(self):
        time.sleep(0.2)
        self.click_element(self.SAVE_BUTTON)

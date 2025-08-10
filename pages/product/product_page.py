from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import os

class ProductPage(BasePage):
    NAME_INPUT = (By.ID, "data.name")
    DESCRIPTION_INPUT = (By.ID, "data.description")
    IS_SELLABLE_SWITCH = (By.ID, "data.is_sellable")
    IS_SERVICE_SWITCH = (By.ID, "data.is_service")
    MIN_STOCK_INPUT = (By.ID, "data.min_stock")
    IMAGE_INPUT = (By.CSS_SELECTOR, "input[type='file']")
    IMAGE_PREVIEW = (By.CSS_SELECTOR, ".filepond--image-preview")
    SAVE_BUTTON = (By.ID, "key-bindings-1")

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )    

    def enter_name(self, name):
        self.enter_text(self.NAME_INPUT, name)

    def enter_description(self, description):
        self.enter_text(self.DESCRIPTION_INPUT, description)

    def toggle_sellable(self):
        self.click_element(self.IS_SELLABLE_SWITCH)

    def toggle_service(self):
        self.click_element(self.IS_SERVICE_SWITCH)

    def enter_min_stock(self, min_stock):
        self.enter_text(self.MIN_STOCK_INPUT, min_stock)

    def upload_image(self, relative_path):
        file_path = os.path.abspath(relative_path)

        input_file = self.wait_for_element(self.IMAGE_INPUT)
        self.driver.execute_script("arguments[0].style.display = 'block';", input_file)
        input_file.send_keys(file_path)

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".filepond--image-preview"))
        )

    def click_save(self):
        self.click_element(self.SAVE_BUTTON)
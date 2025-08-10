from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    NEW_PRODUCT = (By.LINK_TEXT, "Crear Producto")

    def click_new_product(self):
        self.click_element(self.NEW_PRODUCT)

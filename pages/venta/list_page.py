from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ListPage(BasePage):
    NEW_VENTA = (By.LINK_TEXT, "Crear Venta")

    def click_new_venta(self):
        self.click_element(self.NEW_VENTA)

    def get_venta_list(self):
        # Aquí puedes implementar la lógica para obtener la lista de ventas
        pass
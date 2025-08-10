from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class LoginPage(BasePage):
    USERNAME_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.TAG_NAME, "button")

    def enter_username(self, username):
        time.sleep(1)
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        time.sleep(1)
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        time.sleep(1)
        self.click_element(self.LOGIN_BUTTON)

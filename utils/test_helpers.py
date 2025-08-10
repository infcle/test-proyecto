from functools import wraps
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.screenshot_utils import save_screenshot

def capture_screenshot_on_failure(screenshot_name):
    """Decorador para capturar screenshot al fallar un test."""
    def decorator(func):
        @wraps(func)
        def wrapper(driver, *args, **kwargs):
            try:
                return func(driver, *args, **kwargs)
            except Exception:
                save_screenshot(driver, screenshot_name, "error")
                raise
        return wrapper
    return decorator

def wait_for_element_with_screenshot(driver, locator, timeout, screenshot_name):
    """Helper para esperar un elemento y capturar pantalla si timeout, sin interrumpir el flujo."""
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    except TimeoutException:
        save_screenshot(driver, screenshot_name, "timeout_exception")
        return None  # No lanza excepción, solo retorna None
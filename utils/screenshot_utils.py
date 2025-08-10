import os

def save_screenshot(driver, nameTest, nameFile):
    os.makedirs(f"screenshots/{nameTest}", exist_ok=True)
    filename = f"screenshots/{nameTest}/{nameFile}.png"
    driver.save_screenshot(filename)

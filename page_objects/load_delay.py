from selenium.webdriver.common.by import By

load_btn = (By.CSS_SELECTOR, ".btn.btn-primary")


class LoadDelay:
    def __init__(self, driver):
        self.driver = driver

    def get_load_btn(self):
        return self.driver.find_element(load_btn[0], load_btn[1])

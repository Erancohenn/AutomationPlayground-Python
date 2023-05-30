from selenium.webdriver.common.by import By
dynamic_id_btn = (By.CSS_SELECTOR, ".btn.btn-primary")


class DynamicID:
    def __init__(self, driver):
        self.driver = driver

    def get_dynamic_id_btn(self):
        return self.driver.find_element(dynamic_id_btn[0], dynamic_id_btn[1])

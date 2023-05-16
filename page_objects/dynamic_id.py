from selenium.webdriver.common.by import By

dynamicid_btn = (By.CSS_SELECTOR, ".btn.btn-primary")
class DynamicID:
    def __init__(self, driver):
        self.driver = driver

    def get_dynamicid_btn(self):
        return self.driver.find_element(dynamicid_btn[0], dynamicid_btn[1])

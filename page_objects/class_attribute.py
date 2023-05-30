from selenium.webdriver.common.by import By

class_attribute_btn = (By.CSS_SELECTOR, ".btn-primary")


class ClassAttribute:
    def __init__(self, driver):
        self.driver = driver

    def get_class_atr_blue_btn(self):
        return self.driver.find_element(class_attribute_btn[0], class_attribute_btn[1])

from selenium.webdriver.common.by import By
hidden_btn = (By.ID, "hidingButton")


class Scrollbars:
    def __init__(self, driver):
        self.driver = driver

    def get_hidden_btn(self):
        return self.driver.find_element(hidden_btn[0], hidden_btn[1])

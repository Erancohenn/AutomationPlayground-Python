from selenium.webdriver.common.by import By
trigger_btn = (By.ID, "ajaxButton")
after_click = (By.CLASS_NAME, "bg-success")


class ClientSideDelay:
    def __init__(self, driver):
        self.driver = driver

    def get_trigger_btn(self):
        return self.driver.find_element(trigger_btn[0], trigger_btn[1])

    def get_after_click(self):
        return self.driver.find_element(after_click[0], after_click[1])

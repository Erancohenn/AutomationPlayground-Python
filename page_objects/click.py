from selenium.webdriver.common.by import By
click_btn = (By.ID, "badButton")


class Click:
    def __init__(self, driver):
        self.driver = driver

    def get_click_btn(self):
        return self.driver.find_element(click_btn[0], click_btn[1])

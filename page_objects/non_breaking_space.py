from selenium.webdriver.common.by import By
my_btn = (By.XPATH, "//button[text()='My\u00a0Button']")


class NonBreakingSpace:
    def __init__(self, driver):
        self.driver = driver

    def get_my_btn(self):
        return self.driver.find_element(my_btn[0], my_btn[1])

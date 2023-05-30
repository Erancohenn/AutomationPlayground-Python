from selenium.webdriver.common.by import By
green_btn = (By.ID, "greenButton")
blue_btn = (By.ID, "blueButton")


class HiddenLayers:
    def __init__(self, driver):
        self.driver = driver

    def get_green_btn(self):
        return self.driver.find_element(green_btn[0], green_btn[1])

    def get_blue_btn(self):
        return self.driver.find_element(blue_btn[0], blue_btn[1])

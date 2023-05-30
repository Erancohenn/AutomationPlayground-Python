from selenium.webdriver.common.by import By
click_first_btn = (By.CLASS_NAME, "text-primary")
click_after_btn = (By.CLASS_NAME, "text-warning")
number_of_clicks = (By.ID, "clickCount")


class MouseOver:
    def __init__(self, driver):
        self.driver = driver

    def get_click_first_btn(self):
        return self.driver.find_element(click_first_btn[0], click_first_btn[1])

    def get_click_after_btn(self):
        return self.driver.find_element(click_after_btn[0], click_after_btn[1])

    def get_number_of_clicks(self):
        return self.driver.find_element(number_of_clicks[0], number_of_clicks[1])
    
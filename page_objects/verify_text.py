from selenium.webdriver.common.by import By
normal_txt = (By.XPATH, "//span[normalize-space(.)='Welcome UserName!']")


class VerifyText:
    def __init__(self, driver):
        self.driver = driver

    def get_click_btn(self):
        return self.driver.find_element(normal_txt[0], normal_txt[1])
    
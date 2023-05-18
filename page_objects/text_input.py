from selenium.webdriver.common.by import By
txt_field = (By.ID, "newButtonName")
update_btn = (By.ID, 'updatingButton')


class TextInput:
    def __init__(self, driver):
        self.driver = driver

    def get_txt_field(self):
        return self.driver.find_element(txt_field[0], txt_field[1])

    def get_update_btn(self):
        return self.driver.find_element(update_btn[0], update_btn[1])
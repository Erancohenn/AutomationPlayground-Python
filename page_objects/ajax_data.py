from selenium.webdriver.common.by import By
ajax_btn = (By.ID, "ajaxButton")
after_ajax_txt = (By.CLASS_NAME, 'bg-success')


class AjaxData:
    def __init__(self, driver):
        self.driver = driver

    def get_ajax_btn(self):
        return self.driver.find_element(ajax_btn[0], ajax_btn[1])

    def get_ajax_txt(self):
        return self.driver.find_element(after_ajax_txt[0], after_ajax_txt[1])


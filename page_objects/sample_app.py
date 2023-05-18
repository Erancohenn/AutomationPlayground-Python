from selenium.webdriver.common.by import By
user_bar = (By.NAME, "UserName")
password_bar = (By.NAME, "Password")
login_btn = (By.ID, "login")
login_status = (By.ID, "loginstatus")


class SampleApp:
    def __init__(self, driver):
        self.driver = driver

    def get_user_bar(self):
        return self.driver.find_element(user_bar[0], user_bar[1])

    def get_pass_bar(self):
        return self.driver.find_element(password_bar[0], password_bar[1])

    def get_login_btn(self):
        return self.driver.find_element(login_btn[0], login_btn[1])

    def get_login_status(self):
        return self.driver.find_element(login_status[0], login_status[1])
    
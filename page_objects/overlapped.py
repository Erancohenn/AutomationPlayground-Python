from selenium.webdriver.common.by import By
id_bar = (By.ID, "id")
name_bar = (By.ID, "name")
subject_bar = (By.ID, "subject")


class Overlapped:
    def __init__(self, driver):
        self.driver = driver

    def get_id_bar(self):
        return self.driver.find_element(id_bar[0], id_bar[1])

    def get_name_bar(self):
        return self.driver.find_element(name_bar[0], name_bar[1])

    def get_subject_bar(self):
        return self.driver.find_element(subject_bar[0], subject_bar[1])

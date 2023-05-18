from selenium.webdriver.common.by import By
start_btn = (By.ID, "startButton")
stop_btn = (By.ID, "stopButton")
progress_bar = (By.ID, "progressBar")


class ProgressBar:
    def __init__(self, driver):
        self.driver = driver

    def get_start_btn(self):
        return self.driver.find_element(start_btn[0], start_btn[1])

    def get_stop_btn(self):
        return self.driver.find_element(stop_btn[0], stop_btn[1])

    def get_progress_bar(self):
        return self.driver.find_element(progress_bar[0], progress_bar[1])
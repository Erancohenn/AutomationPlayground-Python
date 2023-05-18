from selenium.webdriver.common.by import By

hide_btn = (By.ID, "hideButton")
removed_btn = (By.ID, "removedButton")
zero_width_btn = (By.ID, "zeroWidthButton")
overlapped_btn = (By.ID, "overlappedButton")
opacity_0 = (By.ID, "transparentButton")
visibility_hidden = (By.ID, "invisibleButton")
display_none = (By.ID, "notdisplayedButton")
offscreen = (By.ID, "offscreenButton")


class Visibility:
    def __init__(self, driver):
        self.driver = driver

    def get_hide_btn(self):
        return self.driver.find_element(hide_btn[0], hide_btn[1])

    def get_removed_btn(self):
        return self.driver.find_element(removed_btn[0], removed_btn[1])

    def get_zero_width_btn(self):
        return self.driver.find_element(zero_width_btn[0], zero_width_btn[1])

    def get_overlapped_btn(self):
        return self.driver.find_element(overlapped_btn[0], overlapped_btn[1])

    def get_opacity_0(self):
        return self.driver.find_element(opacity_0[0], opacity_0[1])

    def get_visibility_hidden(self):
        return self.driver.find_element(hide_btn[0], hide_btn[1])

    def get_display_none(self):
        return self.driver.find_element(display_none[0], display_none[1])

    def get_offscreen(self):
        return self.driver.find_element(offscreen[0], offscreen[1])


from selenium.webdriver.common.by import By
table_columns = (By.XPATH, "//span[@role= 'columnheader']")
table_rows = (By.XPATH, "//div[@role='row']")
box_value = (By.CLASS_NAME, "bg-warning")


class DynamicTable:
    def __init__(self, driver):
        self.driver = driver

    def get_table_columns(self):
        return self.driver.find_element(table_columns[0], table_columns[1])

    def get_table_rows(self):
        return self.driver.find_element(table_rows[0], table_rows[1])

    def get_box_value(self):
        return self.driver.find_element(box_value[0], box_value[1])


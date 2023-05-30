from selenium.webdriver.common.by import By

dynamic_id_page = (By.LINK_TEXT, "Dynamic ID")
class_attribute_page = (By.LINK_TEXT, "Class Attribute")
hidden_layers_page = (By.LINK_TEXT, "Hidden Layers")
load_delay_page = (By.LINK_TEXT, "Load Delay")
ajax_data_page = (By.LINK_TEXT, "AJAX Data")
client_side_delay_page = (By.LINK_TEXT, "Client Side Delay")
click_page = (By.LINK_TEXT, "Click")
text_input_page = (By.LINK_TEXT, "Text Input")
scrollbars_page = (By.LINK_TEXT, "Scrollbars")
dynamic_table_page = (By.LINK_TEXT, "Dynamic Table")
verify_txt_page = (By.LINK_TEXT, "Verify Text")
progress_bar_page = (By.LINK_TEXT, "Progress Bar")
visibility_page = (By.LINK_TEXT, "Visibility")
sample_app_page = (By.LINK_TEXT, "Sample App")
mouse_over_page = (By.LINK_TEXT, "Mouse Over")
non_breaking_space_page = (By.LINK_TEXT, "Non-Breaking Space")
overlapped_page = (By.LINK_TEXT, "Overlapped Element")


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def get_dynamic_id_page(self):
        return self.driver.find_element(dynamic_id_page[0], dynamic_id_page[1])

    def get_class_attribute_page(self):
        return self.driver.find_element(class_attribute_page[0], class_attribute_page[1])

    def get_hidden_layers_page(self):
        return self.driver.find_element(hidden_layers_page[0], hidden_layers_page[1])

    def get_load_delay_page(self):
        return self.driver.find_element(load_delay_page[0], load_delay_page[1])

    def get_ajax_data_page(self):
        return self.driver.find_element(ajax_data_page[0], ajax_data_page[1])

    def get_client_side_delay_page(self):
        return self.driver.find_element(client_side_delay_page[0], client_side_delay_page[1])

    def get_click_page(self):
        return self.driver.find_element(click_page[0], click_page[1])

    def get_text_input_page(self):
        return self.driver.find_element(text_input_page[0], text_input_page[1])

    def get_scrollbars_page(self):
        return self.driver.find_element(scrollbars_page[0], scrollbars_page[1])

    def get_dynamic_table_page(self):
        return self.driver.find_element(dynamic_table_page[0], dynamic_table_page[1])

    def get_verify_txt_page(self):
        return self.driver.find_element(verify_txt_page[0], verify_txt_page[1])

    def get_progress_bar_page(self):
        return self.driver.find_element(progress_bar_page[0], progress_bar_page[1])

    def get_visibility_page(self):
        return self.driver.find_element(visibility_page[0], visibility_page[1])

    def get_sample_app_page(self):
        return self.driver.find_element(sample_app_page[0], sample_app_page[1])

    def get_mouse_over_page(self):
        return self.driver.find_element(mouse_over_page[0], mouse_over_page[1])

    def get_non_breaking_space_page(self):
        return self.driver.find_element(non_breaking_space_page[0], non_breaking_space_page[1])

    def get_overlapped_page(self):
        return self.driver.find_element(overlapped_page[0], overlapped_page[1])




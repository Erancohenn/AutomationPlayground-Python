import time

from selenium.webdriver.common.by import By

import main.manage_pages as page
from main.ui_actions import UiActions
from main.verifications import Verifications
import tests.conftest as conf
import page_objects.ajax_data as ajax
import page_objects.mouse_over as mouse
from main.common_ops import wait, For
import page_objects.click as click
import page_objects.visibility as visible


class WebFlows:
    @staticmethod
    def dynamic_id_flow():
        """
        This test verifies the element text with expected text.
        """

        UiActions.click(page.main_page.get_dynamic_id_page())   # Clicking on Dynamic id page.
        actual_txt = page.dynamic_id_page.get_dynamic_id_btn().text    # Getting element text.
        exp_txt = "Button with Dynamic ID"      # Expected result.
        Verifications.verify_equals(actual_txt, exp_txt)    # The verification.

    @staticmethod
    def class_atrr_flow():
        """
        This test verifies the popup text with expected text.
        """

        UiActions.click(page.main_page.get_class_attribute_page())     # Clicking on Class attribute page.
        UiActions.click(page.class_atrr_page.get_class_atr_blue_btn())     # Clicking the BLUE button.
        alert_obj = conf.driver.switch_to.alert    # Switching to alert popup.
        alert_txt = alert_obj.text     # Getting popup alert text.
        exp_txt = 'Primary button pressed'     # Expected text.
        alert_obj.accept()      # Accept alert popup.
        Verifications.verify_equals(alert_txt, exp_txt)    # The verification.

    @staticmethod
    def hidden_layers_flow():
        """
        This test checks if the blue button is displayed
        after clicking the green button.
        """
        UiActions.click(page.main_page.get_hidden_layers_page())    # Clicking on Hidden layers page.
        UiActions.click(page.hidden_layers_page.get_green_btn())    # clicking the green button.
        Verifications.is_displayed(page.hidden_layers_page.get_blue_btn())    # The verification.

    @staticmethod
    def load_delay_flow():
        """
        This test checks if the button is displayed
        after load delay.
        """
        UiActions.click(page.main_page.get_load_delay_page())    # Clicking on Load delay page.
        UiActions.click(page.load_delay_page.get_load_btn())    # Clicking after delay button.
        Verifications.is_displayed(page.load_delay_page.get_load_btn())    # The verification.

    @staticmethod
    def ajax_data_flow():
        """
        This test checks if the element is displayed
        after pressing the Ajax Request button.
        """
        UiActions.click(page.main_page.get_ajax_data_page())    # Clicking on AJAX Data page.
        UiActions.click(page.ajax_data_page.get_ajax_btn())    # Clicking on ajax button.
        wait(For.ELEMENT_DISPLAYED, ajax.after_ajax_txt)    # Waiting for element to be displayed.
        Verifications.is_displayed(page.ajax_data_page.get_ajax_txt())    # The verification.

    @staticmethod
    def client_side_delay_flow():
        """
        This test verifies text of an element
        created by client side button.
        """

        UiActions.click(page.main_page.get_client_side_delay_page())    # Clicking on Client Side Delay page.
        UiActions.click(page.client_side_delay_page.get_trigger_btn())    # Clicking on trigger button.
        conf.driver.implicitly_wait(20)
        after_txt = page.client_side_delay_page.get_after_click().text    # Getting the new element text.
        exp_txt = 'Data calculated on the client side.'    # Expected text.
        Verifications.verify_equals(after_txt, exp_txt)    # The verification

    @staticmethod
    def click_flow():
        """
        This test checks if element is clickable.
        """

        UiActions.click(page.main_page.get_click_page())    # Clicking on Click page.
        UiActions.move_to_elem_click(page.click_page.get_click_btn())    # Moving to 'Click' button.
        Verifications.is_clickable(click.click_btn)    # The verification.

    @staticmethod
    def text_input_flow():
        """
        This test verifies the user input with
        element text.
        """

        UiActions.click(page.main_page.get_text_input_page())    # Clicking on Click page.
        text_field = page.test_input_page.get_txt_field()    # Inserting element to variable.
        update_btn = page.test_input_page.get_update_btn()    # Inserting element to variable.
        user_input = "Just Checking !"    # Inserting wanted text to variable.
        UiActions.update_text(text_field, user_input)    # Sending text to element.
        UiActions.click(update_btn)    # Clicking on update btn.
        text_field_txt = text_field.get_attribute('value')    # Getting element attribute to variable.
        Verifications.verify_equals(user_input, text_field_txt)    # The verification.

    @staticmethod
    def scrollbars_flow():
        """
        This test verifies visibility of element
        """

        UiActions.click(page.main_page.get_scrollbars_page())    # Clicking on Scrollbars page.
        hidden = page.scrollbars_page.get_hidden_btn()    # Inserting element to variable.
        UiActions.scroll_to_elem(hidden)    # Scrolling to elem.
        Verifications.is_displayed(hidden)    # The verification.

    @staticmethod
    def dynamic_table_flow():
        """
        This test verifies equals between elements.
        """

        UiActions.click(page.main_page.get_dynamic_table_page())    # Clicking on Dynamic Table page.
        columns = page.dynamic_table_page.get_table_columns()    # Inserting elements to list.
        rows = page.dynamic_table_page.get_table_rows()    # Inserting elements to list.
        columns_index = 0    # Initialising columns_index variable.
        cpu_chrome_table = ''    # Initialising cpu_chrome_table variable.

        # finding CPU column
        for i in range(len(columns)):
            if columns[i].text == "CPU":
                columns_index = i
                break

        rows_len = len(rows)    # Inserting the length of row's list to variable.

        # finding Chrome's row and getting CPU value.
        for i in range(rows_len):
            if 'Chrome' in rows[i].text:
                chrome_cpu = rows[i].find_elements_by_tag_name('span')
                cpu_chrome_table = chrome_cpu[columns_index].text
                break

        box_value = page.dynamic_table_page.get_box_value().text    # Inserting element text to variable.
        box_values = box_value.split(":")    # Splitting box_value to list.
        actual_chrome_cpu_box = box_values[1].strip()    # Removing spaces.
        Verifications.verify_equals(cpu_chrome_table, actual_chrome_cpu_box)    # The verification.

    @staticmethod
    def verify_text_flow():
        """
        This test verifies element with expected text.
        """

        UiActions.click(page.main_page.get_verify_txt_page())    # Clicking on Verify Text page.
        normal_txt = page.verify_text_page.get_normal_txt().text    # Inserting element text to variable.
        exp_txt = 'Welcome UserName!'    # Expected text
        Verifications.verify_equals(normal_txt, exp_txt)    # The verification

    @staticmethod
    def progress_bar_flow():
        """
        This test verifies element attribute
        with expected text.
        """

        UiActions.click(page.main_page.get_progress_bar_page())    # Clicking on Progress Bar page.
        start = page.progress_bar_page.get_start_btn()    # Inserting element to variable.
        stop = page.progress_bar_page.get_stop_btn()    # Inserting element to variable.
        progress_bar = page.progress_bar_page.get_progress_bar()    # Inserting element to variable.
        progress_bar_score = progress_bar.get_attribute("aria-valuenow")    # Inserting element's attribute to variable.
        UiActions.click(start)    # Clicking on element.
        wait(For.ELEMENT_DISPLAYED, (By.XPATH, "//div[@aria-valuenow='75']"))   # Waiting for element to be displayed
        UiActions.click(stop)    # Clicking on element.
        Verifications.verify_equals(progress_bar_score, "75")    # The verification

    @staticmethod
    def visibility_flow():
        """
        This test Verifies visibility of elements.
        """

        UiActions.click(page.main_page.get_visibility_page())    # Clicking on Visibility page.

        # buttons
        hide_btn = page.visibility_page.get_hide_btn()    # Inserting element to variable.
        overlapped_btn = page.visibility_page.get_overlapped_btn()    # Inserting element to variable.
        UiActions.click(hide_btn)    # Clicking on element.

        # display assertion
        Verifications.is_not_displayed(visible.removed_btn)    # Checking if element is NOT displayed
        Verifications.is_not_displayed(visible.zero_width_btn)    # Checking if element is NOT displayed
        Verifications.is_displayed(overlapped_btn)    # Checking if element is displayed
        Verifications.is_not_displayed(visible.opacity_0)    # Checking if element is NOT displayed
        Verifications.is_not_displayed(visible.visibility_hidden)    # Checking if element is NOT displayed
        Verifications.is_not_displayed(visible.display_none)    # Checking if element is NOT displayed
        Verifications.is_not_displayed(visible.offscreen)    # Checking if element is NOT displayed

    @staticmethod
    def sample_app_flow():
        """
        This test verifies element text with
        expected text.
        """

        UiActions.click(page.main_page.get_sample_app_page())    # Clicking on Visibility page.
        password = "pwd"    # Expected password.
        user = "user"    # Expected username.
        login_exp_text = 'Welcome, user!'    # Expected login text.
        logout_exp_text = 'User logged out.'    # Expected logout text.
        user_bar = page.sample_app_page.get_user_bar()    # Inserting element to variable.
        pass_bar = page.sample_app_page.get_pass_bar()    # Inserting element to variable.
        login_btn = page.sample_app_page.get_login_btn()    # Inserting element to variable.

        # the login process
        UiActions.update_text(user_bar, user)    # Sending text to username bar.
        UiActions.update_text(pass_bar, password)    # Sending text to password bar.
        UiActions.click(login_btn)    # Clicking on login button.
        login_status = page.sample_app_page.get_login_status()    # Inserting element to variable.
        Verifications.verify_equals(login_status.text, login_exp_text)    # The verification
        time.sleep(3)

        # log out process
        UiActions.click(login_btn)    # Clicking on logout button.
        Verifications.verify_equals(login_status.text, logout_exp_text)    # The verification

    @staticmethod
    def mouse_over_flow():
        """
        This test verifies the user input with
        element text.
        """

        UiActions.click(page.main_page.get_mouse_over_page())    # Clicking on Mouse Over page.
        exp_num_of_clicks = "2"    # Expected number of clicks.
        click_first_btn = page.mouse_over_page.get_click_first_btn()    # Inserting element to variable.
        UiActions.move_to_elem(click_first_btn)    # Moving to element.
        wait(For.ELEMENT_EXIST, mouse.click_after_btn)    # Waiting for element to be existed.
        click_after_btn = page.mouse_over_page.get_click_after_btn()    # Inserting element to variable.
        UiActions.double_click_elem(click_after_btn)    # Double-clicking on elem.
        number_of_clicks = page.mouse_over_page.get_number_of_clicks().text    # Inserting element text to variable.
        number_of_clicks = str(number_of_clicks)    # Converting variable to string.
        Verifications.verify_equals(number_of_clicks, exp_num_of_clicks)    # The verification

    @staticmethod
    def non_breaking_space_flow():
        """
        This test checks if element is displayed.
        """

        UiActions.click(page.main_page.get_non_breaking_space_page())    # Clicking on Non-Breaking Space page.
        my_button = page.non_breaking_page.get_my_btn()    # Inserting element to variable.
        Verifications.is_displayed(my_button)    # The verification

    @staticmethod
    def overlapped_flow():
        """
        This test verifies elements attributes with
        given text.
        """

        UiActions.click(page.main_page.get_overlapped_page())    # Clicking on Overlapped page.
        id_txt = 'fakeid'    # Expected id text.
        name_txt = 'Liverpool'    # Expected name text.
        subject_txt = 'test01'    # Expected subject text.
        id_bar = page.overlapped_page.get_id_bar()    # Inserting element to variable.
        name_bar = page.overlapped_page.get_name_bar()    # Inserting element to variable.
        subject_bar = page.overlapped_page.get_subject_bar()    # Inserting element to variable.

        # scroll & fill the fields
        UiActions.scroll_to_elem(id_bar)    # Scrolling to element.
        UiActions.update_text(id_bar, id_txt)    # Sending text to id bar.
        UiActions.scroll_to_elem(name_bar)    # Scrolling to element.
        UiActions.update_text(name_bar, name_txt)    # Sending text to name bar.
        UiActions.scroll_to_elem(name_bar)    # Scrolling to element.
        UiActions.update_text(subject_bar, subject_txt)    # Sending text to subject bar.

        Verifications.verify_equals(id_bar.get_attribute('value'), id_txt)    # The verification
        Verifications.verify_equals(name_bar.get_attribute('value'), name_txt)    # The verification
        Verifications.verify_equals(subject_bar.get_attribute('value'), subject_txt)    # The verification











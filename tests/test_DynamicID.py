
import time
import unittest
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from main.common_func import CommonFunc
from selenium.webdriver.common.action_chains import ActionChains
import main.manage_pages as page
from main.ui_actions import UiActions
from main.workflows.web_flows import WebFlows


class Tests(unittest.TestCase):

    @pytest.mark.usefixtures("setup_and_teardown")
    def test_DynamicID(self):
        WebFlows.dynamic_id_flow()

    @pytest.mark.usefixtures("setup_and_teardown")
    def test_class_attribute(self):
        WebFlows.class_atrr_flow()

    @pytest.mark.usefixtures("setup_and_teardown")
    def test_hidden_layers(self):
        WebFlows.hidden_layers_flow()

    def test_load_delay(self):
        common = CommonFunc("http://localhost:3000", '')
        driver = common.start_session()
        btn_load = driver.find_element_by_link_text('Load Delay')
        btn_load.click()
        common.close_session(driver)

    def test_ajax_data(self):
        common = CommonFunc("http://localhost:3000", 'ajax')
        driver = common.start_session()
        driver.find_element_by_id('ajaxButton').click()
        wait = WebDriverWait(driver, 15)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'bg-success')))
        common.close_session(driver)

    def test_client_side_delay(self):
        common = CommonFunc("http://localhost:3000", 'clientdelay')
        driver = common.start_session()
        driver.find_element_by_id('ajaxButton').click()
        driver.implicitly_wait(20)
        act_txt = driver.find_element_by_class_name('bg-success').text
        exp_txt = 'Data calculated on the client side.'
        self.assertEqual(act_txt , exp_txt)
        common.close_session(driver)

    def test_click(self):
        common = CommonFunc("http://localhost:3000", 'click')
        driver = common.start_session()
        btn_click = driver.find_element_by_id('badButton')
        action = ActionChains(driver)
        action.move_to_element(btn_click).click()
        atrr = btn_click.get_attribute('class')
        print(atrr)
        common.close_session(driver)

    def test_text_input(self):
        common = CommonFunc("http://localhost:3000", 'textinput')
        driver = common.start_session()
        driver.find_element_by_id('newButtonName').send_keys('yuval abdu bennet - insendia')
        the_btn = driver.find_element_by_id('updatingButton')
        the_btn.click()
        input_txt = driver.find_element_by_id('newButtonName').get_attribute('value')
        self.assertEqual(the_btn.text, input_txt)
        common.close_session(driver)

    def test_scrollbars(self):
        common = CommonFunc("http://localhost:3000", 'scrollbars')
        driver = common.start_session()
        hidden = driver.find_element_by_id('hidingButton')
        driver.execute_script("arguments[0].scrollIntoView();", hidden)
        time.sleep(6)
        common.close_session(driver)

    def test_dynamic_table(self):
        common = CommonFunc("http://localhost:3000", 'dynamictable')
        driver = common.start_session()
        columns = driver.find_elements_by_xpath("//span[@role= 'columnheader']")
        rows = driver.find_elements_by_xpath("//div[@role='row']")
        columns_index = 0
        cpu_chrome_table = ''

        # finding CPU column
        for i in range(len(columns)):
            if columns[i].text == "CPU":
                columns_index = i
                print(columns_index)
                break

        # finding Chrome's row and get CPU value.
        rows_len = len(rows)

        for i in range(rows_len):
            if 'Chrome' in rows[i].text:
                rr = rows[i].find_elements_by_tag_name('span')
                cpu_chrome_table = rr[columns_index].text
                print(rr)

                break

        box_value = driver.find_element_by_class_name('bg-warning').text
        box_values = box_value.split(":")
        actual_chrome_cpu_box = box_values[1].strip()
        self.assertEqual(cpu_chrome_table, actual_chrome_cpu_box)
        common.close_session(driver)

    def test_verify_text(self):
        common = CommonFunc("http://localhost:3000", 'verifytext')
        driver = common.start_session()
        normal_txt = driver.find_element_by_xpath("//span[normalize-space(.)='Welcome UserName!']").text
        print("Normalized Text: ", normal_txt)
        self.assertEqual(normal_txt, "Welcome UserName!")
        common.close_session(driver)

    def test_progress_bar(self):
        common = CommonFunc("http://localhost:3000", 'progressbar')
        driver = common.start_session()
        start = driver.find_element_by_id("startButton")
        stop = driver.find_element_by_id("stopButton")
        progress_bar = driver.find_element_by_id("progressBar")
        progress_bar_score = progress_bar.get_attribute("aria-valuenow")
        start.click()
        wait = WebDriverWait(driver, 30)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@aria-valuenow='75']")))
        stop.click()
        print("progress bar score is: " , progress_bar_score)
        self.assertEqual(progress_bar_score, "75")
        time.sleep(3)
        common.close_session(driver)

    def test_visibility(self):
        common = CommonFunc("http://localhost:3000", 'visibility')
        driver = common.start_session()

        # buttons
        hide_btn = driver.find_element_by_id("hideButton")
        removed_btn = driver.find_element_by_id("removedButton")
        zero_width_btn = driver.find_element_by_id("zeroWidthButton")
        overlapped_btn = driver.find_element_by_id("overlappedButton")
        opacity_0 = driver.find_element_by_id("transparentButton")
        visibility_hidden = driver.find_element_by_id("invisibleButton")
        display_none = driver.find_element_by_id("notdisplayedButton")
        offscreen = driver.find_element_by_id("offscreenButton")
        hide_btn.click()

        #display assertion


        self.assertFalse(zero_width_btn.is_displayed())
        self.assertTrue(overlapped_btn.is_displayed())  # This element is displayed
        self.assertFalse(opacity_0.is_displayed())
        self.assertFalse(visibility_hidden.is_displayed())
        self.assertFalse(display_none.is_displayed())
        self.assertFalse(offscreen.is_displayed())

    def test_sample_app(self):
        common = CommonFunc("http://localhost:3000", 'sampleapp')
        driver = common.start_session()
        password = "pwd"
        user_bar = driver.find_element_by_name("UserName")
        pass_bar = driver.find_element_by_name("Password")
        login_btn = driver.find_element_by_id("login")

        # the login process
        user_bar.send_keys("user")
        pass_bar.send_keys(password)
        login_btn.click()
        login_status = driver.find_element_by_id("loginstatus")
        self.assertEqual(login_status.text, "Welcome, user!")
        time.sleep(3)

        # log out process
        login_btn.click()
        self.assertEqual(login_status.text, "User logged out.")
        time.sleep(3)
        common.close_session(driver)

    def test_mouse_over(self):
        common = CommonFunc("http://localhost:3000", 'mouseover')
        driver = common.start_session()
        action = ActionChains(driver)
        click_first_btn = driver.find_element_by_class_name("text-primary")
        action.move_to_element(click_first_btn).perform()
        click_after_btn = driver.find_element_by_class_name("text-warning")
        action.double_click(click_after_btn).perform()
        number_of_clicks = driver.find_element_by_id("clickCount").text
        number_of_clicks = str(number_of_clicks)
        print("number of click is:  " , number_of_clicks)
        self.assertEqual(number_of_clicks, "2")
        time.sleep(3)
        common.close_session(driver)

    def test_non_breaking_space(self):
        common = CommonFunc("http://localhost:3000", 'nbsp')
        driver = common.start_session()
        # using Non Breaking Space
        my_button = driver.find_element_by_xpath("//button[text()='My\u00a0Button']")
        self.assertTrue(my_button.is_displayed())
        common.close_session(driver)

    def test_overlapped(self):
        common = CommonFunc("http://localhost:3000", 'overlapped')
        driver = common.start_session()
        id_bar = driver.find_element_by_id("id")
        name_bar = driver.find_element_by_id("name")
        subject_bar = driver.find_element_by_id("subject")

        # scroll & fill the fields
        driver.execute_script("arguments[0].scrollIntoView(true);", id_bar)
        id_bar.send_keys("fakeid")
        driver.execute_script("arguments[0].scrollIntoView(true);", name_bar)
        name_bar.send_keys("blabla")
        driver.execute_script("arguments[0].scrollIntoView(true);", subject_bar)
        subject_bar.send_keys("test 01")
        time.sleep(10)




import unittest
import pytest
from main.workflows.web_flows import WebFlows


class Tests(unittest.TestCase):

    def test_dynamic_id(self):
        """
        This test verifies the element text with expected text.
        """
        WebFlows.dynamic_id_flow()

    def test_class_attribute(self):
        """
        This test verifies the popup text with expected text.
        """
        WebFlows.class_atrr_flow()

    def test_hidden_layers(self):
        """
        This test checks if the blue button is displayed
        after clicking the green button.
        """
        WebFlows.hidden_layers_flow()

    def test_load_delay(self):
        """
        This test checks if the button is displayed
        after load delay.
        """
        WebFlows.load_delay_flow()

    def test_ajax_data(self):
        """
        This test checks if the element is displayed
        after pressing the Ajax Request button.
        """
        WebFlows.ajax_data_flow()

    def test_client_side_delay(self):
        """
        This test verifies text of an element
        created by client side button.
        """
        WebFlows.client_side_delay_flow()

    def test_click(self):
        """
        This test checks if element is clickable.
        """
        WebFlows.click_flow()

    def test_text_input(self):
        """
        This test verifies the user input with
        element text.
        """
        WebFlows.text_input_flow()

    def test_scrollbars(self):
        """
        This test verifies visibility of element
        """
        WebFlows.scrollbars_flow()

    def test_dynamic_table(self):
        """
        This test verifies equals between elements.
        """
        WebFlows.dynamic_table_flow()

    def test_verify_text(self):
        """
        This test verifies element with expected text.
        """
        WebFlows.verify_text_flow()

    def test_progress_bar(self):
        """
        This test verifies element attribute
        with expected text.
        """
        WebFlows.progress_bar_flow()

    def test_visibility(self):
        """
        This test Verifies visibility of elements.
        """
        WebFlows.visibility_flow()

    def test_sample_app(self):
        """
        This test verifies element text with
        expected text.
        """
        WebFlows.sample_app_flow()

    def test_mouse_over(self):
        """
        This test verifies the user input with
        element text.
        """
        WebFlows.mouse_over_flow()

    def test_non_breaking_space(self):
        """
       This test checks if element is displayed.
       """
        WebFlows.non_breaking_space_flow()

    def test_overlapped(self):
        """
        This test verifies elements attributes with
        given text.
        """
        WebFlows.overlapped_flow()



from selenium.webdriver.remote.webelement import WebElement
from main.common_ops import wait, For


class Verifications:
    @staticmethod
    def verify_equals(actual, expected):
        """
        Verifying equal between actual and expected
        :param actual: actual result
        :param expected: expected result
        :type: actual: any
        :type: expected: any
        """
        assert actual == expected, "Verify Equals Failed, Actual:" + str(actual) + "is not Equals to Expected: " + str(expected)

    @staticmethod
    def is_displayed(elem: WebElement):
        """
        Checking if element is displayed
        :param: elem
        :type: WebElement
        """
        assert elem.is_displayed(), "Verify is displayed Failed, Element:" + elem.text + "is not displayed"

    @staticmethod
    def is_clickable(elem):
        """
        Checking if element is Clickable
        :param: elem
        :type: WebElement
        """
        wait(For.ELEMENT_TO_BE_CLICKABLE, elem), "Verify is clickable Failed"

    @staticmethod
    def is_not_displayed(elem: WebElement):
        """
        Checking if element is NOT displayed
        :param: elem
        :type: WebElement
        """
        wait(For.ELEMENT_NOT_DISPLAYED, elem), 'Element is Visible'



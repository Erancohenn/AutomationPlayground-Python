from selenium.webdriver.remote.webelement import WebElement
import tests.conftest as conf


class UiActions:
    @staticmethod
    def click(elem: WebElement):
        """
        press Click on element
        :param: elem
        :type: WebElement
        """
        elem.click()

    @staticmethod
    def update_text(elem: WebElement, text):
        """
        send input to element
        :param: elem
        :type: WebElement
        """
        elem.send_keys(text)

    @staticmethod
    def mouse_hover(elem1: WebElement, elem2: WebElement):
        """
        mouse hover on element & click
        :param: elem1 , elem2
        :type: WebElement
        """
        conf.action.move_to_element(elem1).move_to_element(elem2).click().preform()

    @staticmethod
    def move_to_elem(elem: WebElement):
        """
        moving mouse on element
        :param: elem
        :type: WebElement
        """
        conf.action.move_to_element(elem).perform()

    @staticmethod
    def move_to_elem_click(elem: WebElement):
        """
        moving mouse & click on element
        :param: elem
        :type: WebElement
        """
        conf.action.move_to_element(elem).click()

    @staticmethod
    def scroll_to_elem(elem: WebElement):
        """
        scrolling to element
        :param: elem
        :type: WebElement
        """
        conf.driver.execute_script("arguments[0].scrollIntoView();", elem)

    @staticmethod
    def double_click_elem(elem: WebElement):
        """
        double clicking on element
        :param: elem
        :type: WebElement
        """
        conf.action.double_click(elem).perform()

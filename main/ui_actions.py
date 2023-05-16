from selenium.webdriver.remote.webelement import WebElement

import tests.conftest as conf


class UiActions:
    @staticmethod
    def click(elem: WebElement):
        elem.click()

    @staticmethod
    def update_text(elem: WebElement, text):
        elem.sendkeys(text)

    @staticmethod
    def mouse_hover(elem1: WebElement, elem2: WebElement):
        conf.action.move_to_element(elem1).move_to_element(elem2).click().preform()

    @staticmethod
    def get_txt(elem: WebElement):
        elem.text

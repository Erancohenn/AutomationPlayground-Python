
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tests.conftest as conf


def wait(for_element, elem):
    """
    type of wait to put on element
    :param: for_element: specific sort of Wait
    :param: elem: Web element
    """
    if for_element == "element_exists":
        WebDriverWait(conf.driver, 20).until(EC.presence_of_element_located((elem[0], elem[1])))
    if for_element == "element_displayed":
        WebDriverWait(conf.driver, 20).until(EC.visibility_of_element_located((elem[0], elem[1])))
    if for_element == "element_to_be_clickable":
        WebDriverWait(conf.driver, 20).until(EC.element_to_be_clickable((elem[0], elem[1])))
    if for_element == "element_not_displayed":
        WebDriverWait(conf.driver, 20).until(EC.invisibility_of_element((elem[0], elem[1])))


class For:
    ELEMENT_EXIST = 'element_exists'
    ELEMENT_DISPLAYED = 'element_displayed'
    ELEMENT_TO_BE_CLICKABLE = 'element_to_be_clickable'
    ELEMENT_NOT_DISPLAYED = 'element_not_displayed'

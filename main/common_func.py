import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class CommonFunc:

    def __init__(self, baseurl, bla):
        self.baseurl = baseurl
        self.bla = bla

    def start_session(self):
        """
        :param bla:
        :return:
        """
        driver = webdriver.Chrome(ChromeDriverManager().install())  # opens chrome
        driver.get(f"{self.baseurl}/{self.bla}")  # go to url
        driver.set_page_load_timeout(10)  # wait 10 sec for page to load
        return driver  # return driver

    def close_session(self, driver):
        yield driver  # opens chrome, go to url, return driver
        time.sleep(5)
        driver.quit()

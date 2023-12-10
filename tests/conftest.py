import pytest
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
from main.manage_pages import ManagePages

driver = None
action = None


@pytest.fixture(scope='function')
def setup_and_teardown(request):
    globals()['driver'] = get_chrome()  # opens chrome
    driver.get(f"http://localhost:3000/")  # go to url
    driver.set_page_load_timeout(10)  # wait 10 sec for page to load
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    ManagePages.init_pages()
    yield
    time.sleep(5)
    driver.quit()


def get_chrome():
    chrome_driver = selenium.webdriver.Chrome(ChromeDriverManager().install())
    return chrome_driver

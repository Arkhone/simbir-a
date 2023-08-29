import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import settings as s

from utils.base_ops import BaseOps


@pytest.fixture(scope="session")
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(s.UI_URL)
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture(scope="session")
def login(driver):
    user = BaseOps(driver)
    user.input_text(s.LOGIN_FIELD, s.TEST_LOGIN)
    user.click_on(s.LOGIN_BTN)
    user.wait_for_text(s.PSWD_NAME_FIELD, s.TEST_LOGIN)
    user.input_text(s.PSWD_FIELD, s.TEST_PSWD)
    user.click_on(s.LOGIN_BTN)
    user.wait_for_url(s.DISK_URL)
    yield user
    driver.refresh()
    user.click_on(s.ACC_ICON)
    user.wait_for_text(s.USERNAME, s.TEST_LOGIN)
    user.click_on(s.LOGOUT_BTN)


@pytest.fixture()
def word_example():
    return os.path.abspath("Файл для копирования.docx")


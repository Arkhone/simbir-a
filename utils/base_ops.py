import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseOps:

    def __init__(self, driver):
        self.driver = driver

    def click_on(self, locator, locator_type="xpath"):
        element = self.driver.find_element(locator_type, locator)
        element.click()
        logging.info('Clicked on the element: %s', locator)

    def find_an_element(self, locator, locator_type="xpath"):
        element = self.driver.find_element(locator_type, locator)
        logging.info('Find the element with this %s locator', locator)
        return element

    def wait_for_text(self, locator, text, locator_type="xpath",):
        wait = WebDriverWait(self.driver, 120, poll_frequency=0.5)
        wait.until(EC.text_to_be_present_in_element((locator_type, locator), text_=text))
        logging.info('Waiting for %s in the element %s', text, locator)

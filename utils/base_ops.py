import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BaseOps:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 120, poll_frequency=0.5)

    def click_on(self, locator, locator_type="xpath"):
        element = self.driver.find_element(locator_type, locator)
        element.click()
        logging.info('Clicked on the element: %s', locator)

    def double_click(self, locator, locator_type="xpath"):
        element = self.driver.find_element(locator_type, locator)
        action = ActionChains(self.driver)
        action.double_click(element).perform()
        logging.info('Clicked X2 on the element: %s', locator)

    def find_an_element(self, locator, locator_type="xpath"):
        element = self.driver.find_element(locator_type, locator)
        logging.info('Find the element with this %s locator', locator)
        return element

    def wait_for_text(self, locator, text, locator_type="xpath", ):
        self.wait.until(EC.text_to_be_present_in_element((locator_type, locator), text_=text))
        logging.info('Waiting for %s in the element %s', text, locator)

    def wait_for_element(self, locator, locator_type="xpath"):
        self.wait.until(EC.visibility_of_element_located((locator_type, locator)))
        logging.info('Waiting for element with %s', locator)

    def wait_for_url(self, url):
        self.wait.until(EC.url_to_be(url))
        logging.info('URL is %s', url)

    def clear_field(self, locator, locator_type="xpath"):
        element = self.driver.find_element(locator_type, locator)
        element.clear()
        logging.info('Element with %s locator is cleared', locator)

    def get_text(self, locator, locator_type="xpath"):
        text = self.find_an_element(locator, locator_type).text
        return text

    def input_text(self, locator, text, locator_type="xpath"):
        self.find_an_element(locator, locator_type).send_keys(text)

    def change_value(self, css, attribute_name, text):
        js_code = f"document.querySelector('{css}').setAttribute('{attribute_name}', '{text}')"
        self.driver.execute_script(js_code)
        value = self.driver.find_element(By.CSS_SELECTOR, css).get_attribute(attribute_name)
        logging.info('Element value is %s ', value)

    def get_value(self, attribute_name, locator, locator_type="xpath"):
        return self.driver.find_element(locator_type, locator).get_attribute(attribute_name)


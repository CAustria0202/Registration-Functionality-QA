from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BaseDriver:
    # Initialize the BaseDriver class with a WebDriver instance
    def __init__(self, driver):
        self.driver = driver

    # Wait for all elements located by the given locator to be present in the DOM
    def wait_for_presence_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 30)  
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return list_of_elements

    # Wait for a single element located by the given locator to be present in the DOM
    def wait_for_presence_of_the_element(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 30)  
        element_located = wait.until(EC.presence_of_element_located((locator_type, locator)))
        return element_located

    # Wait until an element located by the given locator is clickable
    def wait_until_elements_to_be_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 30)  
        clickable_element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return clickable_element

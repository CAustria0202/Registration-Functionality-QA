from Base.base_driver import BaseDriver
from Data.locators import WebsiteLocators
from selenium.webdriver.common.by import By

class ThankYouPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def locate_successful_message(self):
        return self.wait_for_presence_of_the_element(By.XPATH, WebsiteLocators.SUCCESSFUL_MESSAGE)

    def successful_message(self):
        return self.locate_successful_message()
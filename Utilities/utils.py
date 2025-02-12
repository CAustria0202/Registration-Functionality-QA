import os
import time
from selenium.webdriver.support.wait import WebDriverWait
from Base.base_driver import BaseDriver
from selenium import webdriver
from selenium.webdriver.common.by import By

class Utils(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Verify the alert message matched the expected message
    def verify_alert(self, driver, expected_message):
        alert = driver.switch_to.alert
        assert alert.text == expected_message, f"Alert message did not match! Expected: '{expected_message}', Found: '{alert.text}'"
        alert.accept()

    # Assert if the actual text matches the expected text
    def assert_element_text(self, actual_text, expected_text, message="Text did not match!"):
        assert actual_text == expected_text, f"{message}\nExpected: '{expected_text}', Found: '{actual_text}'"

    # Wait for the page to fully load by checking the document ready state
    def wait_for_page_load(self, driver, timeout=10):
        try:
            WebDriverWait(driver, timeout).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            print("Page fully loaded.")
        except Exception as e:
            print(f"Page did not load within {timeout} seconds: {e}")

    # Take a screenshot and save it in the specified directory
    def take_screenshot(self, directory="Screenshot", filename_prefix="screenshot"):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Project root directory
        screenshot_dir = os.path.join(base_dir, directory)

        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_name = os.path.join(screenshot_dir, f"{filename_prefix}_{timestamp}.png")

        if self.driver:
            self.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved at: {os.path.abspath(screenshot_name)}")
        else:
            print("Driver not initialized. Screenshot not taken.")

        print(f"Saving screenshot to: {os.path.abspath(screenshot_name)}")

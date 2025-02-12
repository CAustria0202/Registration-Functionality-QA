import pytest
from Base.base_driver import BaseDriver
from Pages.index_page import RegistrationPage
from Pages.thank_you_page import ThankYouPage
from Utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestVerifyRegistrationForm:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        # Declaration of the Object
        self.reg_page = RegistrationPage(self.driver)
        self.base_drive = BaseDriver
        self.utils = Utils(self.driver)
        self.ty_page = ThankYouPage(self.driver)

    # Test case to verify successful registration with valid credentials
    def test_valid_credentials(self):
        # Submitting valid registration details
        self.reg_page.click_submit("John", "Doe", "valid_user@example.com", "09088175555", "Juan Luna Business", "Retail", "Kalayaan St.", "Pampanga", "San Fernando", "2307")
        # Verify the success alert
        self.utils.verify_alert(self.driver, "PASS: User credentials are valid.")

        # Wait for the page to load and validate the success message
        self.utils.wait_for_page_load(self.driver)
        success_register = self.ty_page.successful_message().text
        self.utils.assert_element_text(success_register, "Your Registration is Successful!")

        # Take a screenshot of the successful registration
        self.utils.take_screenshot(filename_prefix="test_valid_credentials")

    # Test case for valid email but invalid phone number
    def test_valid_email_invalid_number(self):
        self.reg_page.click_submit("John", "Doe", "valid_user@example.com", "+6390881755556", "Juan Luna Business", "Retail", "Kalayaan St.", "Pampanga", "San Fernando", "2307")
        error_message = self.reg_page.mobile_err2().text
        self.utils.assert_element_text(error_message, "Enter a valid 11-digit mobile number starting with 09", "Mobile Number error message mismatch")

        self.utils.take_screenshot(filename_prefix="test_valid_email_invalid_number")

    # Test case for invalid email and valid phone number
    def test_invalid_email_valid_number(self):
        self.reg_page.click_submit("John", "Doe", "invalid_user@example", "09088175555", "Juan Luna Business", "Retail", "Kalayaan St.", "Pampanga", "San Fernando", "2307")
        error_message = self.reg_page.email_err2().text
        self.utils.assert_element_text(error_message, "Enter a valid email address (e.g., user@example.com)", "Email Address error message mismatch")

        self.utils.take_screenshot(filename_prefix="test_invalid_email_valid_number")

    # Test case for not registered email but valid phone number
    def test_not_registered_email_valid_number(self):
        self.reg_page.click_submit("John", "Doe", "invalid_user@example.com", "09088175555", "Juan Luna Business", "Retail", "Kalayaan St.", "Pampanga", "San Fernando", "2307")
        self.utils.verify_alert(self.driver, "FAIL: Invalid credentials. Please enter the correct email and phone number.")

        self.utils.take_screenshot(filename_prefix="test_not_registered_email_valid_number")

    # Test case for empty email and phone number
    def test_empty_email_and_phone(self):
        self.reg_page.click_submit("John", "Doe", "", "", "Juan Luna Business", "Retail", "Kalayaan St.", "Pampanga", "San Fernando", "2307")
        error_message1 = self.reg_page.email_err1().text
        error_message2 = self.reg_page.mobile_err1().text
        self.utils.assert_element_text(error_message1, "Please input your email address", "Email Address error message mismatch")
        self.utils.assert_element_text(error_message2, "Please input your mobile number", "Mobile Number error message mismatch")

        self.utils.take_screenshot(filename_prefix="test_empty_email_and_phone")

    # Test case for special characters in email and phone fields
    def test_special_characters_email_phone(self):
        self.reg_page.click_submit("John", "Doe", "!@#user@#$%^", "!@#user@#$%^", "Juan Luna Business", "Retail", "Kalayaan St.", "Pampanga", "San Fernando", "2307")
        error_message1 = self.reg_page.email_err2().text
        error_message2 = self.reg_page.mobile_err2().text
        self.utils.assert_element_text(error_message1, "Enter a valid email address (e.g., user@example.com)", "Email Address error message mismatch")
        self.utils.assert_element_text(error_message2, "Enter a valid 11-digit mobile number starting with 09", "Mobile Number error message mismatch")

        self.utils.take_screenshot(filename_prefix="test_special_characters_email_phone")

    # Test case for empty inputs on business information fields
    def test_empty_input_on_business_information(self):
        self.reg_page.click_submit("John", "Doe", "valid_user@example.com", "09088175555", "", "Please Select", "", "", "", "")
        error_message1 = self.reg_page.business_err1().text
        error_message2 = self.reg_page.industry_err().text
        error_message3 = self.reg_page.address_err().text
        error_message4 = self.reg_page.province_err().text
        error_message5 = self.reg_page.city_err().text
        error_message6 = self.reg_page.zip_err().text
        self.utils.assert_element_text(error_message1, "Please input your business name", "Business Name error message mismatch")
        self.utils.assert_element_text(error_message2, "Select an industry type", "Industry Type error message mismatch")
        self.utils.assert_element_text(error_message3, "Enter your address", "Address error message mismatch")
        self.utils.assert_element_text(error_message4, "Enter your province", "Province error message mismatch")
        self.utils.assert_element_text(error_message5, "Enter your city/municipality", "City/Municipality error message mismatch")
        self.utils.assert_element_text(error_message6, "Enter a valid 4-5 digit zip code", "Zip code error message mismatch")

        self.utils.take_screenshot(filename_prefix="test_empty_input_on_business_information")

    # Test case for special characters in business name
    def test_special_characters_business_name(self):
        self.reg_page.click_submit("John", "Doe", "valid_user@example.com", "09088175555", "Juan Lun@ Business!", "Retail", "Kalayaan St.", "Pampanga", "San Fernando", "2307")
        error_message1 = self.reg_page.business_err2().text
        self.utils.assert_element_text(error_message1, "Business name can only contain letters, numbers, spaces, and the symbols (.-,&)", "Business Name error message mismatch")

        self.utils.take_screenshot(filename_prefix="test_special_characters_business_name")

    # Test case for submitting the form without agreeing to privacy policy and terms
    def test_submit_by_not_clicking_checkbox(self):
        self.reg_page.submit_without_checkbox("John", "Doe", "valid_user@example.com", "09088175555", "Juan Luna Business", "Retail", "Kalayaan St.", "Pampanga", "San Fernando", "2307")
        error_message1 = self.reg_page.privacy_err().text
        error_message2 = self.reg_page.terms_err().text
        self.utils.assert_element_text(error_message1, "You must agree to the Privacy Policy", "Privacy Policy error message mismatch")
        self.utils.assert_element_text(error_message2, "You must agree to the Terms and Conditions", "Terms and Conditions error message mismatch")

        self.utils.take_screenshot(filename_prefix="test_submit_by_not_clicking_checkbox")

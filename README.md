# Automated Testing: User Registration Functionality

This project is designed to automate the testing of the User Registration Page and validate various input scenarios using Selenium WebDriver with Python. The goal is to ensure that the registration form behaves as expected with both valid and invalid inputs and that appropriate error messages are displayed when necessary.

Design and Thought Process:
* Test Coverage: We focused on both positive (valid inputs) and negative (invalid inputs) test cases to ensure the robustness of the registration functionality.
* Data Validation: Each input field is validated against specific criteria (e.g., email format, phone number format) to avoid common issues.
* Error Handling: The test verifies that appropriate error messages are displayed when invalid data is entered.
* Automation: Selenium WebDriver is used to simulate user interaction with the form and to validate the registration results.

Potential Issues and Preventive Measures
* Incorrect input validation: Ensured by regular expressions and boundary checks.
* Special character handling: Tested to prevent security vulnerabilities.
* Dropdown validation: Avoids selecting default or placeholder values.

# Test Case Table

| **Test Case ID** | **Test Case Description** | **Test Steps** | **Test Data** | **Expected Result** | **Remarks** |
|------------------|---------------------------|----------------|---------------|---------------------|-------------|
| TC01 | Validate successful registration with valid credentials | 1. Fill in all fields with valid data <br> 2. Click on the Submit button | First Name: John <br> Last Name: Doe <br> Email: valid_user@example.com <br> Mobile: 09088175555 <br> Business Name: Juan Luna Business <br> Industry: Retail <br> Province: Pampanga <br> City: San Fernando <br> Zip: 2307 | "Your Registration is Successful!" | Successful registration confirmation |
| TC02 | Validate registration with valid email and invalid mobile number | 1. Fill in all fields with valid data except mobile number <br> 2. Click on the Submit button | Email: valid_user@example.com <br> Mobile: +6390881755556 | Error message: "Enter a valid 11-digit mobile number starting with 09" | Mobile number format validation |
| TC03 | Validate registration with invalid email and valid mobile number | 1. Fill in all fields with valid data except email <br> 2. Click on the Submit button | Email: invalid_user@example <br> Mobile: 09088175555 | Error message: "Enter a valid email address (e.g., user@example.com)" | Email format validation |
| TC04 | Validate registration with non-registered email and valid mobile number | 1. Fill in all fields with a non-registered email <br> 2. Click on the Submit button | Email: invalid_user@example.com <br> Mobile: 09088175555 | Alert: "FAIL: Invalid credentials. Please enter the correct email and phone number." | Validation for unregistered email |
| TC05 | Validate registration with empty email and phone number | 1. Leave email and phone fields blank <br> 2. Click on the Submit button | Email: (empty) <br> Mobile: (empty) | Error message: "Please input your email address" <br> "Please input your mobile number" | Validation for required fields |
| TC06 | Validate registration with special characters in email and phone number | 1. Fill in email and phone number fields with special characters <br> 2. Click on the Submit button | Email: !@#user@#$%^ <br> Mobile: !@#user@#$%^ | Error message: "Enter a valid email address" <br> "Enter a valid 11-digit mobile number" | Validation for special characters |
| TC07 | Validate registration with empty business information fields | 1. Leave business information fields blank <br> 2. Click on the Submit button | Business Name: (empty) <br> Industry: (empty) <br> Address: (empty) <br> Province: (empty) <br> City: (empty) <br> Zip: (empty) | Error messages for each field: <br> "Please input your business name" <br> "Select an industry type" <br> "Enter your address" <br> "Enter your province" <br> "Enter your city/municipality" <br> "Enter a valid 4-5 digit zip code" | Validation for all required business fields |
| TC08 | Validate registration with special characters in business name | 1. Fill in the business name with special characters <br> 2. Click on the Submit button | Business Name: Juan Lun@ Business! | Error message: "Business name can only contain letters, numbers, spaces, and the symbols (.-,&)" | Validation for business name format |
| TC09 | Validate registration without agreeing to the privacy policy and terms | 1. Fill in all fields <br> 2. Submit without checking the Privacy Policy and Terms checkbox | - | Error message: "You must agree to the Privacy Policy" <br> "You must agree to the Terms and Conditions" | Validation for checkbox selection |


Tools and Technologies Used:
* Programming Language: Python
* Automation Tool: Selenium WebDriver
* Browser: Google Chrome
* Testing Framework: Pytest
* GitHub for version control

Test Flow:
1. Correct Credentials: The test enters a valid email and mobile number combination and verifies successful registration.
2. Incorrect Credentials: The test enters an invalid email or mobile number and checks for failure.

# Requirements

* Python 3.12.3
* pip (24.0) and setuptools
* [venv](<https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>) (recommended)

# Instalation

1. Download or clone the repository 
2. Open a terminal
3. Go to the project root directory "/Registration-Functionality-QA/".
4. Create a virtual environment: `py -m venv venv`
5. Activate the virtual environment executing the following script: `.\venv\Scripts\activate`
6. Execute the following command to download the necessary libraries:  `pip install -r requirements.txt`

# Test Execution

1. Open a terminal
2. From the project root directory run: `pytest -v --html=report.html --self-contained-html`

# Configuration

By default, tests will be executed in Chrome (normal mode). Preferences can be changed in "../config.ini" file

# Results

To check the report, open the '/Reports/report.html' file once the execution has finished.
To check the Screenshots, open the '/Screenshot/' folder once the execution has finished.

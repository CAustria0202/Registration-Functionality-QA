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

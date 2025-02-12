
class WebsiteLocators:

    #LOCATORS BY ID
    FIRST_NAME = "firstname"
    LAST_NAME = "lastname"
    EMAIL = "email"
    MOBILE = "mobile"
    BUSINESS = "business"
    INDUSTRY = "industryType"
    ADDRESS = "address"
    PROVINCE = "province"
    CITY = "city"
    ZIP = "zipCode"
    PRIV = "privacyPolicy"
    TERMS = "termsConditions"
    SUBMIT = "//input[@value='Submit']"

    #XPATH FOR ERROR MESSAGES
    FIRST_NAME_ERROR1 = "//small[normalize-space()='Please input your first name']"
    FIRST_NAME_ERROR2 = "//small[contains(text(),'Enter a valid first name (alphabetic characters on')]"
    LAST_NAME_ERROR1 = "//small[normalize-space()='Please input your last name']"
    LAST_NAME_ERROR2 = "//small[contains(text(),'Enter a valid last name (alphabetic characters onl')]"
    EMAIL_ERROR1 = "//small[normalize-space()='Please input your email address']"
    EMAIL_ERROR2 = "//small[contains(text(),'Enter a valid email address (e.g., user@example.co')]"
    MOBILE_ERROR1 = "//small[normalize-space()='Please input your mobile number']"
    MOBILE_ERROR2 = "//small[contains(text(),'Enter a valid 11-digit mobile number starting with')]"
    BUSINESS_ERROR1 = "//small[normalize-space()='Please input your business name']"
    BUSINESS_ERROR2 = "//small[contains(text(),'Business name can only contain letters, numbers, s')]"
    INDUSTRY_ERROR = "//small[normalize-space() = 'Select an industry type']"
    ADDRESS_ERROR = "// small[normalize-space() = 'Enter your address']"
    PROVINCE_ERROR = "// small[normalize-space() = 'Enter your province']"
    CITY_ERROR = "// small[normalize-space() = 'Enter your city/municipality']"
    ZIP_ERROR = "// small[normalize-space() = 'Enter a valid 4-5 digit zip code']"
    PRIVACY_ERROR = "// small[normalize-space() = 'You must agree to the Privacy Policy']"
    TERMS_ERROR = "// small[normalize-space() = 'You must agree to the Terms and Conditions']"

    #LOCATE THE MESSAGE ON THANK YOU PAGE
    SUCCESSFUL_MESSAGE = "//h1[normalize-space()='Your Registration is Successful!']"
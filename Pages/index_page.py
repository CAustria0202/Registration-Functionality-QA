import time
from selenium.webdriver.common.by import By
from Data.locators import WebsiteLocators
from Base.base_driver import BaseDriver
from selenium.webdriver.support.select import Select

class RegistrationPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Method to find and return the clickable input element
    def firstname(self):
        return self.wait_until_elements_to_be_clickable(By.ID, WebsiteLocators.FIRST_NAME)

    def lastname(self):
        return self.wait_until_elements_to_be_clickable(By.ID, WebsiteLocators.LAST_NAME)

    def email(self):
        return self.wait_until_elements_to_be_clickable(By.ID, WebsiteLocators.EMAIL)

    def mobile(self):
        return self.wait_until_elements_to_be_clickable(By.ID, WebsiteLocators.MOBILE)

    def business(self):
        return self.wait_until_elements_to_be_clickable(By.ID, WebsiteLocators.BUSINESS)

    def industry(self):
        self.wait_for_presence_of_all_elements(By.ID, WebsiteLocators.INDUSTRY)
        return self.wait_until_elements_to_be_clickable(By.ID, WebsiteLocators.INDUSTRY)

    def address(self):
        return self.wait_until_elements_to_be_clickable(By.ID, WebsiteLocators.ADDRESS)

    def province(self):
        return self.wait_until_elements_to_be_clickable(By.ID, WebsiteLocators.PROVINCE)

    def city(self):
        return self.wait_until_elements_to_be_clickable(By.ID, WebsiteLocators.CITY)

    def zip(self):
        return self.wait_until_elements_to_be_clickable(By.ID, WebsiteLocators.ZIP)

    def priv(self):
        return self.wait_until_elements_to_be_clickable(By.ID, WebsiteLocators.PRIV)

    def terms(self):
        return self.wait_until_elements_to_be_clickable(By.ID, WebsiteLocators.TERMS)

    def submit_button(self):
        return self.wait_until_elements_to_be_clickable(By.XPATH, WebsiteLocators.SUBMIT)

    # Method to find and return the error message of the element
    def firstname_err(self):
        return self.wait_for_presence_of_the_element(By.XPATH, WebsiteLocators.FIRST_NAME_ERROR1)

    def firstname_err1(self):
        return self.wait_for_presence_of_the_element(By.XPATH, WebsiteLocators.FIRST_NAME_ERROR2)

    def lastname_err(self):
        return self.wait_for_presence_of_the_element(By.XPATH, WebsiteLocators.LAST_NAME_ERROR1)

    def lastname_err1(self):
        return self.wait_for_presence_of_the_element(By.XPATH, WebsiteLocators.LAST_NAME_ERROR2)

    def email_err1(self):
        return self.wait_for_presence_of_the_element(By.XPATH, WebsiteLocators.EMAIL_ERROR1)

    def email_err2(self):
        return self.wait_for_presence_of_the_element(By.XPATH, WebsiteLocators.EMAIL_ERROR2)

    def mobile_err1(self):
        return self.wait_for_presence_of_the_element(By.XPATH, WebsiteLocators.MOBILE_ERROR1)

    def mobile_err2(self):
        return self.wait_for_presence_of_the_element(By.XPATH, WebsiteLocators.MOBILE_ERROR2)

    def business_err1(self):
        return self.wait_for_presence_of_the_element(By.XPATH, WebsiteLocators.BUSINESS_ERROR1)

    def business_err2(self):
        return self.wait_for_presence_of_the_element(By.XPATH, WebsiteLocators.BUSINESS_ERROR2)

    def industry_err(self):
        return self.wait_for_presence_of_the_element(By.XPATH, WebsiteLocators.INDUSTRY_ERROR)

    def address_err(self):
        return self.wait_for_presence_of_the_element(By.XPATH, WebsiteLocators.ADDRESS_ERROR)

    def province_err(self):
        return self.wait_for_presence_of_the_element(By.XPATH, WebsiteLocators.PROVINCE_ERROR)

    def city_err(self):
        return self.wait_for_presence_of_the_element(By.XPATH, WebsiteLocators.CITY_ERROR)

    def zip_err(self):
        return self.wait_for_presence_of_the_element(By.XPATH, WebsiteLocators.ZIP_ERROR)

    def privacy_err(self):
        return self.wait_for_presence_of_the_element(By.XPATH, WebsiteLocators.PRIVACY_ERROR)

    def terms_err(self):
        return self.wait_for_presence_of_the_element(By.XPATH, WebsiteLocators.TERMS_ERROR)

    #Methods for interacting with form input fileds
    def enter_firstname(self, fname):
        self.firstname().click()
        self.firstname().send_keys(fname)

    def enter_lastname(self, lname):
        self.lastname().click()
        self.lastname().send_keys(lname)

    def enter_email(self, emailadd):
        self.email().click()
        self.email().send_keys(emailadd)

    def enter_mobile(self, mob):
        self.mobile().click()
        self.mobile().send_keys(mob)

    def enter_business(self, bus):
        self.business().click()
        self.business().send_keys(bus)

    def enter_industry(self, text):
        drp = self.industry()
        drp.click()
        drop_down = Select(drp)
        drop_down.select_by_visible_text(text)

    def enter_addr(self, addr):
        self.address().click()
        self.address().send_keys(addr)

    def enter_province(self, prov):
        self.province().click()
        self.province().send_keys(prov)

    def enter_city(self, cty):
        self.city().click()
        self.city().send_keys(cty)

    def enter_zip(self, zp):
        self.zip().click()
        self.zip().send_keys(zp)

    def enter_privacy(self):
        self.priv().click()

    def enter_terms(self):
        self.terms().click()

    def enter_submit(self):
        self.submit_button().click()

    # Consolidated individual form field entry methods into one method to reduce code repetition.
    # This method calls all the necessary input functions and submits the form with the provided data.
    def click_submit(self, fname, lname, emailadd, mob, bus, text, addr, prov, cty, zp):
        self.enter_firstname(fname)
        self.enter_lastname(lname)
        self.enter_email(emailadd)
        self.enter_mobile(mob)
        self.enter_business(bus)
        self.enter_industry(text)
        self.enter_addr(addr)
        self.enter_province(prov)
        self.enter_city(cty)
        self.enter_zip(zp)
        self.enter_privacy()
        self.enter_terms()
        self.enter_submit()

    # SPECIFIC CASE: This method calls all the necessary input functions except checkboxes and submits the form with the provided data.
    def submit_without_checkbox(self, fname, lname, emailadd, mob, bus, text, addr, prov, cty, zp):
        self.enter_firstname(fname)
        self.enter_lastname(lname)
        self.enter_email(emailadd)
        self.enter_mobile(mob)
        self.enter_business(bus)
        self.enter_industry(text)
        self.enter_addr(addr)
        self.enter_province(prov)
        self.enter_city(cty)
        self.enter_zip(zp)
        self.enter_submit()
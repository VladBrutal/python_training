# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from contact import Contact

class HW13(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    
    def test_add_contact(self):
        wd = self.wd
        self.open_addressbook_page(wd)
        self.login_to_the_page(wd, username="admin", password="secret")
        self.add_new_contacts(wd, Contact(firstname="Anthony", middlename="Marshon", lastname="Davis", nickname="The Brow"
                              , company="Los Angeles Lakers", address="Staples Center",
                              phone_home="+1234567890", email="ad@lakers.com", homepage="lakers.com", address2="Staples Center"))
        self.move_back_home_page(wd)
        self.logout_from_page(wd)

    # def test_add_contact_empty_value(self):
    #     wd = self.wd
    #     self.open_addressbook_page(wd)
    #     self.login_to_the_page(wd, username="admin", password="secret")
    #     self.add_new_contacts(wd, firstname="", middlename="", lastname="", nickname=""
    #                           , company="", address="",
    #                           phone_home="", email="", homepage="", address2="")
    #     self.move_back_home_page(wd)
    #     self.logout_from_page(wd)

    def logout_from_page(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def move_back_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def add_new_contacts(self, wd, contact):
        # add new contact
        wd.find_element_by_link_text("add new").click()
        # fill the form of new contact
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.phone_home)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        # submit group creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()


    def login_to_the_page(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_addressbook_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import Select
import unittest
import datetime
from contact import Contact

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.open_add_new_page(wd)
        self.create_new_contact(wd, Contact(firstname="test firstname", middlename="test middlename",
                                            lastname="test lastname", nickname="test nickname",
                                            photo="C:\\fakepath\\Untitled.jpg",
                                            title="test title", company="test company", address="test address",
                                            home="test home", mobile="test mobile", work="test work", fax="test fax",
                                            email="test email", email2="test email2", email3="test email3",
                                            homepage="test homepage", birthday="11 May 1977",
                                            anniversary="3 June 1959", address2="test address2",
                                            phone2="test phone2", notes="test notes"))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_group_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def create_new_contact(self, wd, contact):
        # fill contact form
        self.change_value_by_name(wd, "firstname", contact.firstname)
        self.change_value_by_name(wd, "middlename", contact.middlename)
        self.change_value_by_name(wd, "lastname", contact.lastname)
        self.change_value_by_name(wd, "nickname", contact.nickname)
        self.change_value_by_name(wd, "photo", contact.photo)
        self.change_value_by_name(wd, "title", contact.title)
        self.change_value_by_name(wd, "company", contact.company)
        self.change_value_by_name(wd, "address", contact.address)
        self.change_value_by_name(wd, "home", contact.home)
        self.change_value_by_name(wd, "mobile", contact.mobile)
        self.change_value_by_name(wd, "work", contact.work)
        self.change_value_by_name(wd, "fax", contact.fax)
        self.change_value_by_name(wd, "email", contact.email)
        self.change_value_by_name(wd, "email2", contact.email2)
        self.change_value_by_name(wd, "email3", contact.email3)
        self.change_value_by_name(wd, "homepage", contact.homepage)
        self.change_contact_date(wd, "Birthday", contact.birthday)
        self.change_contact_date(wd, "Anniversary", contact.anniversary)
        self.change_value_by_name(wd, "address2", contact.address2)
        self.change_value_by_name(wd, "phone2", contact.phone2)
        self.change_value_by_name(wd, "notes", contact.notes)
        # submit group creation
        wd.find_element_by_css_selector("[name = submit]:last-child").click()

    def change_value_by_name(self, wd, name, text):
        wd.find_element_by_name(name).click()
        wd.find_element_by_name(name).clear()
        wd.find_element_by_name(name).send_keys(text)

    def upload_contact_photo(self, wd, name, text):
        wd.find_element_by_name(name).click()
        wd.find_element_by_name(name).send_keys(text)
        
    def change_contact_date(self, wd, date_label, date):
        d_xpath = "//label[contains(text(), '"+date_label+"')]//following-sibling::select[1]"
        m_xpath = "//label[contains(text(), '"+date_label+"')]//following-sibling::select[2]"
        y_xpath = "//label[contains(text(), '"+date_label+"')]//following-sibling::input[1]"
        wd.find_element_by_xpath(d_xpath).click()
        Select(wd.find_element_by_xpath(d_xpath)).select_by_visible_text(date.split()[0])
        wd.find_element_by_xpath(d_xpath).click()
        wd.find_element_by_xpath(m_xpath).click()
        Select(wd.find_element_by_xpath(m_xpath)).select_by_visible_text(date.split()[1])
        wd.find_element_by_xpath(m_xpath).click()
        wd.find_element_by_xpath(y_xpath).click()
        wd.find_element_by_xpath(y_xpath).clear()
        wd.find_element_by_xpath(y_xpath).send_keys(date.split()[2])

    def open_add_new_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

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

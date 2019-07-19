import os
import time

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact(contact, wd)
        # submit contact creation
        wd.find_element_by_css_selector("[name = submit]:last-child").click()

    def edit(self, searched_lastname, searched_firstname, contactEdit):
        wd = self.app.wd
        self.app.change_value_by_name("searchstring", searched_lastname + ' ' + searched_firstname)
        # start edit contact
        wd.find_element_by_xpath("//td[contains(text(), 'test firstname')]//following-sibling::td[5]").click()
        # fill contact form
        self.fill_contact(contactEdit, wd)
        # update contact
        wd.find_element_by_css_selector("[name = update]:last-child").click()
        self.app.return_to_homepage()

    def fill_contact(self, contact, wd):
        self.app.change_value_by_name("firstname", contact.firstname)
        self.app.change_value_by_name("middlename", contact.middlename)
        self.app.change_value_by_name("lastname", contact.lastname)
        self.app.change_value_by_name("nickname", contact.nickname)
        wd.find_element_by_name("photo").send_keys(os.path.abspath("test_image.jpg"))
        self.app.change_value_by_name("title", contact.title)
        self.app.change_value_by_name("company", contact.company)
        self.app.change_value_by_name("address", contact.address)
        self.app.change_value_by_name("home", contact.home)
        self.app.change_value_by_name("mobile", contact.mobile)
        self.app.change_value_by_name("work", contact.work)
        self.app.change_value_by_name("fax", contact.fax)
        self.app.change_value_by_name("email", contact.email)
        self.app.change_value_by_name("email2", contact.email2)
        self.app.change_value_by_name("email3", contact.email3)
        self.app.change_value_by_name("homepage", contact.homepage)
        self.change_contact_date("Birthday", contact.birthday)
        self.change_contact_date("Anniversary", contact.anniversary)
        self.app.change_value_by_name("address2", contact.address2)
        self.app.change_value_by_name("phone2", contact.phone2)
        self.app.change_value_by_name("notes", contact.notes)

    def change_contact_date(self, date_label, date):
        d_xpath = "//label[contains(text(), '" + date_label + "')]//following-sibling::select[1]"
        m_xpath = "//label[contains(text(), '" + date_label + "')]//following-sibling::select[2]"
        y_xpath = "//label[contains(text(), '" + date_label + "')]//following-sibling::input[1]"
        self.app.select_element_in_dropdown(d_xpath, date.split()[0])
        self.app.select_element_in_dropdown(m_xpath, date.split()[1])
        self.app.change_value_by_xpath(y_xpath, date.split()[2])

    def delete(self, searched_lastname, searched_firstname):
        wd = self.app.wd
        self.app.change_value_by_name("searchstring", searched_lastname + ' ' + searched_firstname)
        wd.find_element_by_xpath("//td[contains(text(), '"+searched_lastname+"')]//preceding-sibling::td[@class='center']").click()
        wd.find_element_by_xpath("//input[@value = 'Delete']").click()
        wd.switch_to_alert().accept()
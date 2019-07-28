import os
from model.contact import Contact
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
        self.app.return_to_homepage()
        self.contact_cache = None

    def edit_first_contact(self, contactEdit):
        wd = self.app.wd
        # start edit contact
        wd.find_element_by_xpath("//tr[@name = 'entry'][1]//td[8]").click()
        # fill contact form
        self.fill_contact(contactEdit, wd)
        # update contact
        wd.find_element_by_css_selector("[name = update]:last-child").click()
        self.app.return_to_homepage()
        self.contact_cache = None

    def fill_contact(self, contact, wd):
        self.app.change_value_by_name("firstname", contact.firstname)
        self.app.change_value_by_name("middlename", contact.middlename)
        self.app.change_value_by_name("lastname", contact.lastname)
        self.app.change_value_by_name("nickname", contact.nickname)
        if contact.photo is not None:
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
        if date is not None:
            d_xpath = "//label[contains(text(), '" + date_label + "')]//following-sibling::select[1]"
            m_xpath = "//label[contains(text(), '" + date_label + "')]//following-sibling::select[2]"
            y_xpath = "//label[contains(text(), '" + date_label + "')]//following-sibling::input[1]"
            self.app.select_element_in_dropdown(d_xpath, date.split()[0])
            self.app.select_element_in_dropdown(m_xpath, date.split()[1])
            self.app.change_value_by_xpath(y_xpath, date.split()[2])

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//td[@class = 'center'][1]//input").click()
        wd.find_element_by_xpath("//input[@value = 'Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text('home').click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.return_to_homepage()
        return len(wd.find_elements_by_xpath("//tr[position()>1]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.return_to_homepage()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[position()>1]"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                lastname = element.find_element_by_xpath("td[2]").text
                firstname = element.find_element_by_xpath("td[3]").text
                self.contact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname))
        return list(self.contact_cache)



    # def edit(self, searched_lastname, searched_firstname, contactEdit):
    #     wd = self.app.wd
    #     self.app.change_value_by_name("searchstring", searched_lastname + ' ' + searched_firstname)
    #     # start edit contact
    #     wd.find_element_by_xpath("//td[contains(text(), 'test firstname')]//following-sibling::td[5]").click()
    #     # fill contact form
    #     self.fill_contact(contactEdit, wd)
    #     # update contact
    #     wd.find_element_by_css_selector("[name = update]:last-child").click()
    #     self.app.return_to_homepage()
    #
    # def delete(self, searched_lastname, searched_firstname):
    #         wd = self.app.wd
    #         self.app.change_value_by_name("searchstring", searched_lastname + ' ' + searched_firstname)
    #         wd.find_element_by_xpath(
    #             "//td[contains(text(), '" + searched_lastname + "')]//preceding-sibling::td[@class='center']").click()
    #         wd.find_element_by_xpath("//input[@value = 'Delete']").click()
    #         wd.switch_to_alert().accept()
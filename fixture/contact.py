import os
import random
import time

from model.contact import Contact
import re


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

    def edit_some_contact(self, contactEdit, index):
        wd = self.app.wd
        # start edit contact
        self.open_contact_to_edit_by_index(index)
        # fill contact form
        self.fill_contact(contactEdit, wd)
        # update contact
        wd.find_element_by_css_selector("[name = update]:last-child").click()
        self.app.return_to_homepage()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()
        # xpath_index = str(index + 1)
        # wd.find_element_by_xpath("//tr[@name = 'entry'][" + xpath_index + "]//td[8]").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

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

    def delete_some_contact(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value = 'Delete']").click()
        wd.switch_to_alert().accept()
        time.sleep(1)
        wd.find_element_by_link_text('home').click()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//td[@class = 'center']//input")[index].click()

    def count(self):
        wd = self.app.wd
        self.app.return_to_homepage()
        return len(wd.find_elements_by_xpath("//tr[position()>1]"))

    def index_of_contact_on_page(self, contact):
        wd = self.app.wd
        s = []
        for element in wd.find_elements_by_xpath("//tr[position()>1]"):
            cont_id = element.find_element_by_name("selected[]").get_attribute("value")
            s.append(cont_id)
        return s.index(contact.id)
        # return list(list(s)).index(contact.id)

    def get_contact_list(self):
            wd = self.app.wd
            self.app.return_to_homepage()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[position()>1]"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                lastname = element.find_element_by_xpath("td[2]").text
                firstname = element.find_element_by_xpath("td[3]").text
                address = element.find_element_by_xpath("td[4]").text
                all_emails = element.find_element_by_xpath("td[5]").text
                all_phones = element.find_element_by_xpath("td[6]").text
                self.contact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname, address=address,
                                  all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
            return list(self.contact_cache)


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")

        return Contact(firstname=firstname, lastname=lastname, id=id, address=address, home=home, mobile=mobile,
                       work=work, phone2=phone2, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, mobile=mobile, work=work, phone2=phone2)

    def get_contacts_in_group_list(self, group):
        wd = self.app.wd
        self.app.select_element_in_dropdown("//select[@name='group']", group.name)
        list = []
        for element in wd.find_elements_by_xpath("//tr[position()>1]"):
            id = element.find_element_by_name("selected[]").get_attribute("value")
            lastname = element.find_element_by_xpath("td[2]").text
            firstname = element.find_element_by_xpath("td[3]").text
            address = element.find_element_by_xpath("td[4]").text
            all_emails = element.find_element_by_xpath("td[5]").text
            all_phones = element.find_element_by_xpath("td[6]").text
            list.append(Contact(id=id, lastname=lastname, firstname=firstname, address=address,
                                              all_phones_from_home_page=all_phones,
                                              all_emails_from_home_page=all_emails))
        return list

    def contact_out_of_group(self, group):
        all_contacts = self.get_contact_list()
        contacts_in_group = self.get_contacts_in_group_list(group)
        contacts_out_of_group = [item for item in all_contacts if item not in contacts_in_group]
        if len(contacts_out_of_group) == 0:
            self.create(Contact(firstname="test firstname_add_to_group", middlename="test middlename", lastname="test lastname"))
            all_contacts = self.get_contact_list()
            contacts_in_group = self.get_contacts_in_group_list(group)
            contacts_out_of_group = [item for item in all_contacts if item not in contacts_in_group]
        return random.choice(contacts_out_of_group)

    def add_contact_to_group(self, contact, group):
        wd = self.app.wd
        self.select_contact_by_index(self.index_of_contact_on_page(contact))
        var1 = group.name
        self.app.select_element_in_dropdown("//select[@name='to_group']", group.name)
        wd.find_element_by_name("add").click()
        self.app.return_to_homepage()

    def remove_contact_from_group(self, contact, group):
        wd = self.app.wd
        self.app.select_element_in_dropdown("//select[@name='group']", group.name)
        self.select_contact_by_index(self.index_of_contact_on_page(contact))
        wd.find_element_by_name("remove").click()
        self.app.return_to_homepage()



    def only_id_sorted_list(self, list_of_item):
        l = []
        for element in list_of_item:
            id = element.id
            l.append(Contact(id=id))
        return sorted(l, key=Contact.id_or_max)

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
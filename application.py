from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

# General methods----------------------

    def login(self, username, password):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()
        self.open_home_page()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def change_value_by_name(self, name, text):
        wd = self.wd
        wd.find_element_by_name(name).click()
        wd.find_element_by_name(name).clear()
        wd.find_element_by_name(name).send_keys(text)

    def change_value_by_xpath(self, path, text):
        wd = self.wd
        wd.find_element_by_xpath(path).click()
        wd.find_element_by_xpath(path).clear()
        wd.find_element_by_xpath(path).send_keys(text)

    def select_element_in_dropdown(self, path, value):
        wd = self.wd
        wd.find_element_by_xpath(path).click()
        Select(wd.find_element_by_xpath(path)).select_by_visible_text(value)
        wd.find_element_by_xpath(path).click()

    def destroy(self):
        wd = self.wd
        wd.quit()

# Group methods----------------------

    def create_group(self, group):
        wd = self.wd
        self.open_group_page()
        # start group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def open_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def return_to_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

# Contact methods----------------------

    def create_new_contact(self, contact):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.change_value_by_name("firstname", contact.firstname)
        self.change_value_by_name("middlename", contact.middlename)
        self.change_value_by_name("lastname", contact.lastname)
        self.change_value_by_name("nickname", contact.nickname)
        wd.find_element_by_name("photo").send_keys(os.path.abspath("test_image.jpg"))
        self.change_value_by_name("title", contact.title)
        self.change_value_by_name("company", contact.company)
        self.change_value_by_name("address", contact.address)
        self.change_value_by_name("home", contact.home)
        self.change_value_by_name("mobile", contact.mobile)
        self.change_value_by_name("work", contact.work)
        self.change_value_by_name("fax", contact.fax)
        self.change_value_by_name("email", contact.email)
        self.change_value_by_name("email2", contact.email2)
        self.change_value_by_name("email3", contact.email3)
        self.change_value_by_name("homepage", contact.homepage)
        self.change_contact_date("Birthday", contact.birthday)
        self.change_contact_date("Anniversary", contact.anniversary)
        self.change_value_by_name("address2", contact.address2)
        self.change_value_by_name("phone2", contact.phone2)
        self.change_value_by_name("notes", contact.notes)
        # submit group creation
        wd.find_element_by_css_selector("[name = submit]:last-child").click()

    def upload_contact_photo(self, name, text):
        wd = self.wd
        wd.find_element_by_name(name).click()
        wd.find_element_by_name(name).send_keys(text)

    def change_contact_date(self, date_label, date):
        d_xpath = "//label[contains(text(), '" + date_label + "')]//following-sibling::select[1]"
        m_xpath = "//label[contains(text(), '" + date_label + "')]//following-sibling::select[2]"
        y_xpath = "//label[contains(text(), '" + date_label + "')]//following-sibling::input[1]"
        self.select_element_in_dropdown(d_xpath, date.split()[0])
        self.select_element_in_dropdown(m_xpath, date.split()[1])
        self.change_value_by_xpath(y_xpath, date.split()[2])

from selenium import webdriver
from selenium.webdriver.support.ui import Select
# from fixture.helper_manager import session, group, contact
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def change_value_by_name(self, name, text):
        wd = self.wd
        if text is not None:
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

    def return_to_homepage(self):
        wd = self.wd
        wd.find_element_by_xpath("//a[contains(text(),'home')]").click()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        wd = self.wd
        wd.quit()





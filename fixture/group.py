from model.group import Group
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # start group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()
        self.group_cache = None

    def fill_group_form(self, group):
        self.app.change_value_by_name("group_name", group.name)
        self.app.change_value_by_name("group_header", group.header)
        self.app.change_value_by_name("group_footer", group.footer)

    def edit_first_group(self):
        self.edit_group_by_index(0)


    def edit_group_by_index(self, group, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    def edit_group_by_id(self, group, id):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_id(id)
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None



    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_id(id)
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def open_group_page(self):
        wd = self.app.wd
        #if not wd.current_url.endswith("/group.php") and len(wd.find_element_by_name("new") > 0):
        wd.find_element_by_link_text("groups").click()

    def return_to_group_page(self):
        wd = self.app.wd
        #if not wd.current_url.endswith("/group.php") and len(wd.find_element_by_name("new") > 0):
        wd.find_element_by_link_text("group page").click()

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

    def group_with_contacts(self):
        wd = self.app.wd
        self.open_group_page()
        self.get_group_list()
        self.app.return_to_homepage()
        for el in self.get_group_list():
            self.app.select_element_in_dropdown("//select[@name='group']", el.name)
            if len(wd.find_elements_by_xpath("//tr[position()>1]")) > 0:
                break
        return el

    def get_group_properties(self):
        wd = self.app.wd
        self.open_group_page()
        self.get_group_list()
        self.app.return_to_homepage()
        for el in self.get_group_list():
            self.app.select_element_in_dropdown("//select[@name='group']", el.name)
            if len(wd.find_elements_by_xpath("//tr[position()>1]")) > 0:
                break
        return el

    def group_with_contacts_is_present(self):
        wd = self.app.wd
        for el in self.get_group_list():
            self.app.return_to_homepage()
            self.app.select_element_in_dropdown("//select[@name='group']", el.name)
            if len(wd.find_elements_by_xpath("//tr[position()>1]")) > 0:
                return True
            else:
                return False

    def delete_all_groups(self):
        wd = self.app.wd
        self.open_group_page()
        for element in wd.find_elements_by_css_selector("span.group"):
            element.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()


    # def edit(self, searched_group, group):
    #     wd = self.app.wd
    #     self.open_group_page()
    #     # search and check group
    #     wd.find_element_by_xpath("//span[contains(text(), '"+searched_group+"')]//input").click()
    #     # start edit group
    #     wd.find_element_by_css_selector("[name = edit]:last-child").click()
    #     # fill group form
    #     self.fill_group_form(group)
    #     # submit group creation
    #     wd.find_element_by_name("update").click()
    #     self.return_to_group_page()

    # def delete(self, searched_group):
    #     wd = self.app.wd
    #     self.open_group_page()
    #     # search and check group
    #     wd.find_element_by_xpath("//span[contains(text(), '"+searched_group+"')]//input").click()
    #     # delete edit group
    #     wd.find_element_by_xpath("//input[@name = 'delete'][1]").click()
    #     self.return_to_group_page()
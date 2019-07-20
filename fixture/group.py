

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

    def fill_group_form(self, group):
        self.app.change_value_by_name("group_name", group.name)
        self.app.change_value_by_name("group_header", group.header)
        self.app.change_value_by_name("group_footer", group.footer)

    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_group_page()
        # search and check group
        wd.find_element_by_xpath("//span[@class = 'group'][1]//input").click()
        # start edit group
        wd.find_element_by_css_selector("[name = edit]:last-child").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        # search and check group
        wd.find_element_by_xpath("//span[@class = 'group'][1]//input").click()
        # delete edit group
        wd.find_element_by_xpath("//input[@name = 'delete'][1]").click()
        self.return_to_group_page()

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

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
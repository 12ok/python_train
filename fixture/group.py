class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        # open group page
        wd.find_element_by_link_text("groups").click()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def fill_form(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def delete_first_group(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit delete
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def edit_first_group(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
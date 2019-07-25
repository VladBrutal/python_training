


class SessionContactHelper:

    def __init__(self, app):
        self.app = app

    def login_to_the_page(self, username, password):
        wd = self.app.wd
        self.app.open_addressbook_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout_from_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
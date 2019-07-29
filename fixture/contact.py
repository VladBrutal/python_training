
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def move_back_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def add_new(self, contact):
        wd = self.app.wd
        # add new contact
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit group creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.move_back_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.phone_home)
        self.change_field_value("email", contact.email)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("address2", contact.address2)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.move_back_home_page()

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        # open editing form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill contact from
        self.fill_contact_form(new_contact_data)
        # submit changes
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.move_back_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

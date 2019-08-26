from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def move_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php")
                and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()

    def add_new(self, contact):
        wd = self.app.wd
        # add new contact
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit group creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.move_to_home_page()
        self.contact_cache = None

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
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_id(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.move_to_home_page()
        self.contact_cache = None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, new_contact_data, index):
        wd = self.app.wd
        self.select_contact_by_id(index)
        # open editing form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill contact from
        self.fill_contact_form(new_contact_data)
        # submit changes
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.move_to_home_page()
        self.contact_cache = None

    def select_contact_by_id(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_contact(self):
        self.select_contact_by_id(0)

    def count(self):
        wd = self.app.wd
        self.move_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.move_to_home_page()
            # wd.find_elements_by_id("search_count")
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                contact_id = element.find_element_by_name("selected[]").get_attribute("id")
                f_name = element.find_element_by_css_selector('[name] td:nth-of-type(3)').text
                l_name = element.find_element_by_css_selector('[name] td:nth-of-type(2)').text
                # contact_id = element.find_element_by_name("selected[]").get_attribute("id")
                # l_name = element.find_element_by_xpath('//tr[3]/td[2]').text
                # f_name = element.find_element_by_xpath('//tr[3]/td[3]').text
                self.contact_cache.append(Contact(id=contact_id, firstname=f_name, lastname=l_name))
        return list(self.contact_cache)

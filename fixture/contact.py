from selenium.webdriver.support.select import Select
from fixture import group
from model.contact import Contact
import re


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
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("phone2", contact.secondary_phone)
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
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # wd.find_element_by_name('Delete').click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.move_to_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # wd.find_element_by_name('Delete').click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.move_to_home_page()
        self.contact_cache = None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, new_contact_data, index):
        wd = self.app.wd
        # self.move_to_home_page()
        # open editing form
        wd.find_element_by_xpath("(//img[@alt='Edit'])[%d]" % index).click()
        # fill contact from
        self.fill_contact_form(new_contact_data)
        # submit changes
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.move_to_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, new_contact_data, id):
        wd = self.app.wd
        # self.select_contact_by_id(id)
        wd.find_element_by_xpath("(//img[@alt='Edit'])[%s]" % id).click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.move_to_home_page()
        self.contact_cache = None

    def link_c_to_g_by_id(self, id, group_id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[4]/select").click()
        Select(wd.find_element_by_xpath("//div[@id='content']/form[2]/div[4]/select")).select_by_visible_text("nameYip")
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.move_to_home_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s" % id).click()

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def count(self):
        wd = self.app.wd
        self.move_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.move_to_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                l_name = cells[1].text
                f_name = cells[2].text
                address = cells[3].text
                all_email = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, lastname=l_name, firstname=f_name,
                                                  address=address, all_email=all_email
                                                  , all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.move_to_home_page()
        # wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[%d]/td[8]/a/img" % (index+2)).click()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.move_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        # self.open_contact_to_edit_by_index(index)
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address =  wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(id=id, lastname=lastname,firstname=firstname, address=address,
                       email=email, email2=email2, email3=email3,
                       home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, secondary_phone=secondary_phone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, secondary_phone=secondary_phone)
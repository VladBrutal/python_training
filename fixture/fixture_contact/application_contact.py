from selenium import webdriver

from fixture.fixture_contact.contact import ContactHelper
from fixture.fixture_contact.session_contact import SessionContactHelper


class ApplicationContactFixture:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionContactHelper(self)
        self.contact = ContactHelper(self)

    def open_addressbook_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.wd.quit()

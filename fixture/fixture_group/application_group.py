from selenium import webdriver

from fixture.fixture_group.group import GroupHelper
from fixture.fixture_group.session_group import SessionGroupHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
      # self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.session = SessionGroupHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

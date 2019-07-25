# -*- coding: utf-8 -*-

import pytest
from model.contact import Contact
from fixture.application_contact import ApplicationContactFixture


@pytest.fixture
def app(request):
    fixture = ApplicationContactFixture()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login_to_the_page(username="admin", password="secret")
    app.add_new_contacts(Contact(firstname="Anthony", middlename="Marshon", lastname="Davis", nickname="The Brow"
                         , company="Los Angeles Lakers", address="Staples Center",
                         phone_home="+1234567890", email="ad@lakers.com",
                         homepage="lakers.com", address2="Staples Center"))
    app.session.logout_from_page()


def test_add_contact_empty_value(app):
    app.session.login_to_the_page(username="admin", password="secret")
    app.add_new_contacts(Contact(firstname="", middlename="", lastname="", nickname=""
                         , company="", address="",
                         phone_home="", email="", homepage="", address2=""))
    app.session.logout_from_page()

# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new(Contact(firstname="Anthony", middlename="Marshon", lastname="Davis", nickname="The Brow"
                                , company="Los Angeles Lakers", address="Staples Center",
                                phone_home="+1234567890", email="ad@lakers.com",
                                homepage="lakers.com", address2="Staples Center"))
    app.session.logout()


def test_add_contact_empty_value(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new(Contact(firstname="", middlename="", lastname="", nickname=""
                                , company="", address="",
                                phone_home="", email="", homepage="", address2=""))
    app.session.logout()

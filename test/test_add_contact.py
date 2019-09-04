# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Anthony", middlename="Marshon", lastname="Davis", nickname="The Brow"
                      , company="Los Angeles Lakers", address="Staples Center",
                      home_phone="+1234567890", mobile_phone="149521", work_phone="9876543", secondary_phone="123098",
                      email="ad@lakers.com", homepage="lakers.com", address2="Staples Center")
    app.contact.add_new(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_add_contact_empty_value(app):
#     app.contact.add_new(Contact(firstname="", middlename="", lastname="", nickname=""
#                                 , company="", address="",
#                                 phone_home="", email="", homepage="", address2=""))

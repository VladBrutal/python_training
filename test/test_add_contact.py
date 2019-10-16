# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.add_new(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert old_contacts == new_contacts
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, firstname=contact.firstname.strip())

        clean_new_contacts = map(clean, new_contacts)
        assert sorted(clean_new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

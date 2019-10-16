import random

from model.contact import Contact


def test_delete_some_contact(app, db, check_ui):
    precondition_contact_existence(app)
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, firstname=contact.firstname.strip())

        clean_new_contacts = map(clean, new_contacts)
        assert sorted(clean_new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


def precondition_contact_existence(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="Test FN", middlename="Test MN", lastname="Test LN"))

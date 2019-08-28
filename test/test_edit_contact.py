from random import randrange

from model.contact import Contact
from test.test_del_contact import precondition_contact_existence


def test_edit_some_contact(app):
    precondition_contact_existence(app)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Edited firstname", lastname="Edited lastname")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_edit_first_contact_middle_name(app):
#     precondition_contact_existence(app)
#     app.contact.edit_first_contact(Contact(middlename="New Walter Louis"))
#
#
# def test_edit_first_contact_lastname_name(app):
#     precondition_contact_existence(app)
#     app.contact.edit_first_contact(Contact(lastname="New Davis"))

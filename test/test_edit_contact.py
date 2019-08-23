from model.contact import Contact
from test.test_del_contact import precondition_contact_existence


def test_edit_first_contact_first_name(app):
    precondition_contact_existence(app)
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="New Baron")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_edit_first_contact_middle_name(app):
#     precondition_contact_existence(app)
#     app.contact.edit_first_contact(Contact(middlename="New Walter Louis"))
#
#
# def test_edit_first_contact_lastname_name(app):
#     precondition_contact_existence(app)
#     app.contact.edit_first_contact(Contact(lastname="New Davis"))

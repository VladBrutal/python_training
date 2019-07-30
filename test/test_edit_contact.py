from model.contact import Contact
from test.test_del_contact import precondition_contact_existence


def test_edit_first_contact_first_name(app):
    precondition_contact_existence(app)
    app.contact.edit_first_contact(Contact(firstname="New Baron"))


def test_edit_first_contact_middle_name(app):
    precondition_contact_existence(app)
    app.contact.edit_first_contact(Contact(middlename="New Walter Louis"))


def test_edit_first_contact_lastname_name(app):
    precondition_contact_existence(app)
    app.contact.edit_first_contact(Contact(lastname="New Davis"))

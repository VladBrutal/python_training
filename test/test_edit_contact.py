from model.contact import Contact

def test_edit_first_contact_first_name(app):
    app.contact.edit_first_contact(Contact(firstname="New Baron"))
    app.session.logout()


def test_edit_first_contact_middle_name(app):
    app.contact.edit_first_contact(Contact(middlename="New Walter Louis"))
    app.session.logout()


def test_edit_first_contact_lastname_name(app):
    app.contact.edit_first_contact(Contact(lastname="New Davis"))
    app.session.logout()

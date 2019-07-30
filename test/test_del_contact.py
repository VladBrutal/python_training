from model.contact import Contact


def test_delete_first_contact(app):
    precondition_contact_existence(app)
    app.contact.delete_first_contact()


def precondition_contact_existence(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="Test FN", middlename="Test MN", lastname="Test LN"))

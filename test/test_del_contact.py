from model.contact import Contact


def test_delete_first_contact(app):
    precondition_contact_existence(app)
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts


def precondition_contact_existence(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="Test FN", middlename="Test MN", lastname="Test LN"))

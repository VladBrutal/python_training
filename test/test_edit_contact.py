from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact_no_changes()
    app.session.logout()


def test_edit_first_contact_edit(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact_changed(Contact(firstname="", middlename="", lastname="", nickname="AD"
                                                   , company="", address="",
                                                   phone_home="", email="", homepage="", address2=""))
    app.session.logout()

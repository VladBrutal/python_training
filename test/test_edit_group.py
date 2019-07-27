from model.group import Group


def test_edit_first_group_no_changes(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group_no_changes()
    app.session.logout()

def test_edit_first_group_changed(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group_changed(Group(name="", header="AbraKadabra", footer=""))
    app.session.logout()
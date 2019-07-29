from model.group import Group


def test_edit_group_name(app):
    app.group.edit_first_group(Group(name="New Group"))
    app.session.logout()


def test_edit_group_header(app):
    app.group.edit_first_group(Group(name="New Header"))
    app.session.logout()


def test_edit_group_footer(app):
    app.group.edit_first_group(Group(name="New Footer"))
    app.session.logout()

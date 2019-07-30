from model.group import Group
from test.test_del_group import precondition_group_existence


def test_edit_group_name(app):
    precondition_group_existence(app)
    app.group.edit_first_group(Group(name="New Group"))


def test_edit_group_header(app):
    precondition_group_existence(app)
    app.group.edit_first_group(Group(name="New Header"))


def test_edit_group_footer(app):
    precondition_group_existence(app)
    app.group.edit_first_group(Group(name="New Footer"))
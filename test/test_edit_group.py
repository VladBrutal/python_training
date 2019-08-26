from random import randrange

from model.group import Group
from test.test_del_group import precondition_group_existence


def test_edit_some_group(app):
    precondition_group_existence(app)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New Group")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_edit_group_header(app):
#     precondition_group_existence(app)
#     app.group.edit_first_group(Group(name="New Header"))
#
#
# def test_edit_group_footer(app):
#     precondition_group_existence(app)
#     app.group.edit_first_group(Group(name="New Footer"))
import random
from model.group import Group
from test.test_del_group import precondition_group_existence


def test_edit_some_group(app, db, check_ui):
    precondition_group_existence(app, db)
    old_groups = db.get_group_list()
    edit_group_data = Group(name="New Group")
    group = random.choice(old_groups)
    app.group.edit_group_by_id(edit_group_data, group.id)
    new_groups = db.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    clean_old_groups = map(clean, old_groups)
    clean_new_groups = map(clean, new_groups)
    assert sorted(clean_old_groups, key=Group.id_or_max) == sorted(clean_new_groups, key=Group.id_or_max)
    if check_ui:
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        clean_new_groups = map(clean, new_groups)
        assert sorted(clean_new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


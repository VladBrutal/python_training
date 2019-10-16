import random
from model.group import Group


def test_delete_some_group(app, db, check_ui):
    precondition_group_existence(app, db)
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == app.group.count()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        clean_new_groups = map(clean, new_groups)
        assert sorted(clean_new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def precondition_group_existence(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="new reserve group"))

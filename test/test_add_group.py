# -*- coding: utf-8 -*-
from model.group import Group
# from data.groups import testdata
# @pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])


def test_add_group(app, db, json_groups, check_ui):  # we want to download test data from the module data in package groups
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        def clean(group):
            return Group(id=group.id, name=group.name.strip())

        clean_new_groups = map(clean, new_groups)
        assert sorted(clean_new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

from model.group import Group


def test_delete_first_group(app):
    precondition_group_existence(app)
    app.group.delete_first_group()


def precondition_group_existence(app):
    if app.group.count() == 0:
        app.group.create(Group(name="new reserve group"))

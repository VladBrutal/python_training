# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Home Work 1", header="HW Header 1", footer="HW Footer 1"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

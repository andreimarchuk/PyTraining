# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="test group", header="test group header", footer="test group footer"))


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test group", header="test group header", footer="test group footer"))
    app.group.edit_first_group(Group(name="testEdit group"))


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="testEdit group"))
    app.group.delete_first_group()


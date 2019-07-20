# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="test group", header="test group header", footer="test group footer"))
    app.session.logout()


def test_edit_group(app):
    app.group.edit("test group", Group(name="testEdit group"))
    app.session.logout()


def test_delete_group(app):
    app.group.delete("testEdit group")


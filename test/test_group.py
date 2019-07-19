# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group(name="test group", header="test group header", footer="test group footer"))
    app.session.logout()

def test_edit_group(app):
    app.session.login("admin", "secret")
    app.group.edit("test group", Group(name="testEdit group", header="testEdit group header", footer="testEdit group footer"))
    app.session.logout()

def test_delete_group(app):
    app.session.login("admin", "secret")
    app.group.delete("testEdit group")
    app.session.logout()


# def test_add_empty_group(app):
#     app.session.login("admin", "secret")
#     app.group.create(Group(name="", header="", footer=""))
#     app.session.logout()

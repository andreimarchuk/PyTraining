# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.hm.session.login("admin", "secret")
    app.hm.group.create(Group(name="test name", header="test header", footer="test footer"))
    app.hm.session.logout()

def test_add_empty_group(app):
    app.hm.session.login("admin", "secret")
    app.hm.group.create(Group(name="", header="", footer=""))
    app.hm.session.logout()

# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.hm.session.login("admin", "secret")
    app.hm.group.create(Group(name="test name", header="test header", footer="test footer"))
    app.hm.session.logout()

def test_add_empty_group(app):
    app.hm.session.login("admin", "secret")
    app.hm.group.create(Group(name="", header="", footer=""))
    app.hm.session.logout()

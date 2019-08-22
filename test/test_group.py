# -*- coding: utf-8 -*-
from model.group import Group
import random
import pytest
import string
from data.groups import testdata

#@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])

def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    #assert len(old_groups) + 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

def test_edit_some_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test group", header="test group header", footer="test group footer"))
    old_groups = db.get_group_list()
    group_to_edit = random.choice(old_groups)
    group = Group(name="testEdit group", header="testEdit group header", footer="testEdit group footer")
    group.id = group_to_edit.id
    app.group.edit_group_by_id(group, group.id)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[old_groups.index(group_to_edit)] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="testEdit group"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



def test_delete_all_groups(app):
    app.group.delete_all_groups()


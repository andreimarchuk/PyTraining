# -*- coding: utf-8 -*-
from model.group import Group
import random
import pytest
import string

def random_string(prefix, maxlen):
    #symbols = string.ascii_letters + string.digits
    symbols = string.ascii_letters + string.digits + " "*5 + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(3, maxlen))])

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name_", 10), header=random_string("header_", 8), footer=random_string("footer_", 12))
    for i in range(5)
]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test group", header="test group header", footer="test group footer"))
    old_groups = app.group.get_group_list()
    index = random.randrange(len(old_groups))
    group = Group(name="testEdit group")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="testEdit group"))
    old_groups = app.group.get_group_list()
    index = random.randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups

def test_delete_all_groups(app):
    app.group.delete_all_groups()


# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from model.contact import Contact
from model.group import Group
import pytest
import re
import random
from data.contacts import testdata


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_edit_contact(app, db, contact, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test firstname", lastname="test lastname"))
    old_contacts = db.get_contact_list()
    contact_to_edit = random.choice(old_contacts)
    contact.id = contact_to_edit.id
    index_in_old_contacts = old_contacts.index(contact_to_edit)
    index_on_page = app.contact.index_of_contact_on_page(contact_to_edit)
    app.contact.edit_some_contact(contact, index_on_page)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index_in_old_contacts] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


def test_delete_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test firstname", middlename="test middlename", lastname="test lastname"))
    old_contacts = db.get_contact_list()
    contact_to_delete = random.choice(old_contacts)
    index_in_old_contacts = old_contacts.index(contact_to_delete)
    index_on_page = app.contact.index_of_contact_on_page(contact_to_delete)
    app.contact.delete_some_contact(index_on_page)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index_in_old_contacts:index_in_old_contacts+1] = []
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


def test_compare_some_contact_data_from_home_edit_pages(app):
    index = random.randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_compare_contacts_data_from_home_page_db(app, db):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for element in contact_from_home_page:
        index = contact_from_home_page.index(element)
        assert element.lastname == contacts_from_db[index].lastname
        assert element.firstname == contacts_from_db[index].firstname
        assert element.address == contacts_from_db[index].address
        assert element.all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db[index])
        assert element.all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db[index])


def test_add_some_contact_to_some_group(app, db):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test firstname", middlename="test middlename", lastname="test lastname"))
    if app.group.count() == 0:
        app.group.create(Group(name="test group", header="test group header", footer="test group footer"))
    group = random.choice(app.group.get_group_list())
    app.return_to_homepage()
    contact = app.contact.contact_out_of_group(group)
    old_contacts_in_group = app.contact.get_contacts_in_group_list(group)
    app.select_element_in_dropdown("//select[@name='group']", "[all]")
    app.contact.add_contact_to_group(contact, group)
    new_contacts_in_group = db.get_contacts_in_group_list(group)
    old_contacts_in_group.append(contact)
    assert app.contact.only_id_sorted_list(old_contacts_in_group) == app.contact.only_id_sorted_list(new_contacts_in_group)


def test_remove_some_contact_from_some_group(app, db):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test firstname", middlename="test middlename", lastname="test lastname"))
    if app.group.count() == 0:
        app.group.create(Group(name="test group", header="test group header", footer="test group footer"))
    if app.group.group_with_contacts_is_present() is False:
        app.select_element_in_dropdown("//select[@name='group']", "[all]")
        test_add_some_contact_to_some_group(app, db)
    group = app.group.group_with_contacts()
    contact = random.choice(app.contact.get_contact_list())
    old_contacts_in_group = app.contact.get_contacts_in_group_list(group)
    app.contact.remove_contact_from_group(contact, group)
    new_contacts_in_group = db.get_contacts_in_group_list(group)
    new_contacts_in_group.append(contact)
    assert app.contact.only_id_sorted_list(old_contacts_in_group) == app.contact.only_id_sorted_list(new_contacts_in_group)




def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                map(lambda x: clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))



def trim_list_in_list():
    List1 = []
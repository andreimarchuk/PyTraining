# -*- coding: utf-8 -*-
import time
from model.contact import Contact
import re
import random
import pytest
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    #symbols = string.ascii_letters + string.digits + " "*5 + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(3, maxlen))])


testdata = [
    Contact(firstname=random_string("firstname_", 10), middlename=random_string("middlename_", 10),
                               lastname=random_string("lastname_", 10), nickname=random_string("nickname_", 8), photo="C:\\fakepath\\Untitled.jpg",
                               title=random_string("title_", 6), company=random_string("company_", 10), address=random_string("address_", 8),
                               home=random_string("home_", 6), mobile=random_string("mobile_", 10), work=random_string("work_", 8), fax=random_string("fax_", 6),
                               email=random_string("email_", 10), email2=random_string("email2_", 8), email3=random_string("email3_", 6),
                               homepage=random_string("homepage_", 10), birthday="11 May 1977",
                               anniversary="3 June 1959", address2=random_string("address2_", 8),
                               phone2=random_string("phone2_", 6), notes=random_string("notes_", 20))
    for i in range(1)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_edit_contact(app, contact):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test firstname", lastname="test lastname"))
    old_contacts = app.contact.get_contact_list()
    index = random.randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_some_contact(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test firstname", middlename="test middlename", lastname="test lastname"))
    old_contacts = app.contact.get_contact_list()
    index = random.randrange(len(old_contacts))
    app.contact.delete_some_contact(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts


def test_compare_some_contact_data_from_home_edit_pages(app):
    index = random.randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


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
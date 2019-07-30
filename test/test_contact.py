# -*- coding: utf-8 -*-
import time
from model.contact import Contact
from random import randrange


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="test firstname", middlename="test middlename",
                               lastname="test lastname", nickname="test nickname", photo="C:\\fakepath\\Untitled.jpg",
                               title="test title", company="test company", address="test address",
                               home="test home", mobile="test mobile", work="test work", fax="test fax",
                               email="test email", email2="test email2", email3="test email3",
                               homepage="test homepage", birthday="11 May 1977",
                               anniversary="3 June 1959", address2="test address2",
                               phone2="test phone2", notes="test notes")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test firstname", lastname="test lastname"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="editTest firstname", middlename="editTest middlename",
                               lastname="editTest lastname", nickname="editTest nickname", photo="C:\\fakepath\\Untitled.jpg",
                               title="editTest title", company="editTest company", address="editTest address",
                               home="editTest home", mobile="editTest mobile", work="editTest work", fax="editTest fax",
                               email="editTest email", email2="editTest email2", email3="editTest email3",
                               homepage="editTest homepage", birthday="25 May 1980",
                               anniversary="25 June 1980", address2="editTest address2",
                               phone2="editTest phone2", notes="editTest notes")
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
    index = randrange(len(old_contacts))
    app.contact.delete_some_contact(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

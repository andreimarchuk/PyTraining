from pytest_bdd import given, when, then, scenario
from model.contact import Contact
import allure
import random


@scenario('contacts.feature', 'Add new contact')
def test_add_new_contact():
    pass

@scenario('contacts.feature', 'Delete some contact')
def test_delete_some_contact():
    pass

@scenario('contacts.feature', 'Edit some contact')
def test_edit_some_contact():
    pass

@given('a contact list')
def contact_list(db):
    return db.get_contact_list()


@given('a contact with <firstname>, <lastname>')
def new_contact(firstname, lastname):
    return Contact(firstname=firstname, lastname=lastname)


@when('I add the contact to the list')
@allure.step('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then('the new contact list is equal to the old list with the added contact')
@allure.step('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test firstname_bdd", lastname="test lastname_bdd"))
    return db.get_contact_list()

@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@when('I delete the contact from the list')
@allure.step('I delete the contact from the list')
def delete_contact(app, random_contact):
    index_on_page = app.contact.index_of_contact_on_page(random_contact)
    app.contact.delete_some_contact(index_on_page)


@then('the new contact list is equal to the old list without deleted contact')
@allure.step('the new contact list is equal to the old list without deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts

@when('I edit the contact from the list')
@allure.step('I edit the contact from the list')
def edit_contact(app, random_contact, new_contact):
    new_contact.id = random_contact.id
    index_on_page = app.contact.index_of_contact_on_page(random_contact)
    app.contact.edit_some_contact(new_contact, index_on_page)

@then('the new contact list is equal to the old list with edited contact')
@allure.step('the new contact list is equal to the old list with edited contact')
def verify_contact_edited(db, non_empty_contact_list, random_contact, new_contact, app):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[non_empty_contact_list.index(random_contact)] = new_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




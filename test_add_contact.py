# -*- coding: utf-8 -*-
import pytest
from application import Application
from contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login("admin", "secret")
    app.create_new_contact(Contact(firstname="test firstname", middlename="test middlename",
                                       lastname="test lastname", nickname="test nickname",
                                       photo="C:\\fakepath\\Untitled.jpg",
                                       title="test title", company="test company", address="test address",
                                       home="test home", mobile="test mobile", work="test work", fax="test fax",
                                       email="test email", email2="test email2", email3="test email3",
                                       homepage="test homepage", birthday="11 May 1977",
                                       anniversary="3 June 1959", address2="test address2",
                                       phone2="test phone2", notes="test notes"))
    app.logout()

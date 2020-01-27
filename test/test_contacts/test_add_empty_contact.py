# -*- coding: utf-8 -*-
from model.contacts import Contacts


def test_add_empty_contact(app):
    app.contacts.add_empty_contact(Contacts())




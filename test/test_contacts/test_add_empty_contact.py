# -*- coding: utf-8 -*-
from model.contacts import Contacts


def test_add_empty_contact(app):
    old_contacts = app.contacts.get_contacts_list()
    contact = Contacts()
    app.contacts.add_empty_contact(contact)
    new_contacts = app.contacts.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    # проверка сравнения старого и нового списка с добавлением элемента
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)




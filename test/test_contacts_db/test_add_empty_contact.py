# -*- coding: utf-8 -*-
from model.contacts import Contacts


def test_add_empty_contact(app, db, check_ui):
    old_contacts = db.get_contacts_list()
    contact = Contacts()
    app.contacts.add_empty_contact(contact)
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = db.get_contacts_list()
    # проверка сравнения старого и нового списка с добавлением элемента
    old_contacts.append(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contacts.id_or_max) == sorted(app.contacts.get_contacts_list(),
                                                                      key=Contacts.id_or_max)




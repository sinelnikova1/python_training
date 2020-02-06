# -*- coding: utf-8 -*-
from model.contacts import Contacts


def test_modify_fio(app):
    contact = Contacts(firstname="Alina42", middlename="Ivanovna43", lastname="Lallala43")
    if app.contacts.count() == 0:
        app.contacts.add_information_of_person(contact)
    old_contacts = app.contacts.get_contacts_list()
    contact.id = old_contacts[0].id
    app.contacts.modify_data_from_details(contact)
    new_contacts = app.contacts.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)


def test_modify_email(app):
    contact = Contacts(firstname="Alina", middlename="Ivanovna", lastname="Lallala")
    change_email = Contacts(email="email_lion4334_857@kf.it", email2="email2433@kfd.ru",
                                                   email3="ren4343k@kdf.ri")
    if app.contacts.count() == 0:
        app.contacts.add_information_of_person(contact)
    old_contacts = app.contacts.get_contacts_list()
    change_email.id = old_contacts[0].id
    app.contacts.modify_data_from_details(change_email)
    new_contacts = app.contacts.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = change_email
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)



# -*- coding: utf-8 -*-
from model.contacts import Contacts
from random import randrange


def test_modify_fio(app):
    contact = Contacts(firstname="Полина532544", middlename="Ivanovna43", lastname="Земляковrererа")
    if app.contacts.count() == 0:
        app.contacts.add_information_of_person(contact)
    old_contacts = app.contacts.get_contacts_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contacts.modify_contact_by_index(index, contact)
    new_contacts = app.contacts.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)


#def test_modify_email(app):
#    contact = Contacts(firstname="Alina", middlename="Ivanovna", lastname="Lallala")
#    change_email = Contacts(email="email_lion4334_857@kf.it", email2="email2433@kfd.ru",
#                                                   email3="ren4343k@kdf.ri")
#    if app.contacts.count() == 0:
#        app.contacts.add_information_of_person(contact)
#    old_contacts = app.contacts.get_contacts_list()
#    index = randrange(len(old_contacts))
#    change_email.id = old_contacts[index].id
#    app.contacts.modify_contact_by_index(index, change_email)
#    new_contacts = app.contacts.get_contacts_list()
#    assert len(old_contacts) == len(new_contacts)
#    old_contacts[index] = change_email
#    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)



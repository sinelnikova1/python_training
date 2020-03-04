# -*- coding: utf-8 -*-
from model.contacts import Contacts
import random


def test_modify_fio(app, db, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.contacts.add_information_of_person(
            Contacts(firstname="firstname1", middlename="middlename1", lastname="lastname1", nickname="nickname1",
                     title="title1", address="address1", company="company1", home="home1", mobile="mobile1",
                     work="work1",
                     fax="fax1", email="email1", email2="email2", email3="email3", homepage="homepage1",
                     address2="address2", phone2="phone2", notes="notes1"))
#    if app.contacts.count() == 0:
#        app.contacts.add_information_of_person(contact)
    old_contacts = db.get_contacts_list()
    random_contact = random.choice(old_contacts)
    contact = Contacts(firstname="Полина532544", middlename="Ivanovna43", lastname="Земляковrererа")
    app.contacts.modify_contact_by_id(random_contact.id, contact)
    old_contacts.remove(random_contact)
    new_contacts = db.get_contacts_list()
    old_contacts.append(contact)
    assert len(old_contacts) == len(new_contacts)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contacts.id_or_max) == sorted(app.Contacts.get_group_list(),
                                                                      key=Contacts.id_or_max)


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



# -*- coding: utf-8 -*-
from model.contacts import Contacts


def test_add_contact(app):
    old_contacts = app.contacts.get_contacts_list()
    contact = Contacts(firstname="Petr", middlename="Petrovich", lastname="Petrov",
         nickname="superman", title=u"Электрик", address=u"Санкт-Петербург, ул. Большевиков 178",
         company=u"ООО Супергаз", home="9899899554", mobile="45555445554", work="55665585", fax="7888556",
         email="emaifortest1@hfkf.ri", email2="email2@kfd.ru", email3="renk@kdf.ri", homepage="homepage.ti",
         bday="16", bmonth="July", byear="1980", aday="10", amonth="May", ayear="2010", address2="LA 45 Oxford St. 549",
         phone2="home", notes="some notes for this")
    app.contacts.add_information_of_person(contact)
    new_contacts = app.contacts.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    # проверка сравнения старого и нового списка с добавлением элемента
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)




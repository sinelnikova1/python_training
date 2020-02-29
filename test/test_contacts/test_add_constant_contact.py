from model.contacts import Contacts
import pytest
from data.contact import constant as testdata

@pytest.mark.parametrize("contact", testdata, ids=[str(x) for x in testdata])

def test_add_contact(app, contact):
   # contact = json_contacts
    old_contacts = app.contacts.get_contacts_list()
    app.contacts.add_information_of_person(contact)
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = app.contacts.get_contacts_list()
    # проверка сравнения старого и нового списка с добавлением элемента
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)






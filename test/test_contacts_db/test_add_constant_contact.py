from model.contacts import Contacts
import pytest
from data.contact import constant as testdata

@pytest.mark.parametrize("contact", testdata, ids=[str(x) for x in testdata])

def test_add_contact(app, db, contact, check_ui):
    old_contacts = db.get_contacts_list()
    app.contacts.add_information_of_person(contact)
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = db.get_contacts_list()
    old_contacts.append(contact)
  # проверка сравнения старого и нового списка с добавлением элемента
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contacts.id_or_max) == sorted(app.contacts.get_contacts_list(),
                                                                      key=Contacts.id_or_max)






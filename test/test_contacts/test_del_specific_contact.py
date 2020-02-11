from model.contacts import Contacts
from random import randrange


def test_delete_specific_contact(app):
    contact = Contacts(firstname="Alina", middlename="Ivanovna", lastname="Lallala", email="gghf@urte.tu")
    if app.contacts.count() == 0:
        app.contacts.add_information_of_person(contact)
    old_contacts = app.contacts.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contacts.delete_contact_by_index(index)
    new_contacts = app.contacts.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

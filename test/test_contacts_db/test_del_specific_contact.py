from model.contacts import Contacts
import random


def test_delete_specific_contact(app, db, check_ui):
    contact = Contacts(firstname="Alina", middlename="Ivanovna", lastname="Lallala", email="gghf@urte.tu")
    if len(db.get_contacts_list()) == 0:
        app.contacts.add_information_of_person(contact)
    old_contacts = db.get_contacts_list()
    random_contact = random.choice(old_contacts)
    app.contacts.delete_contact_by_id(random_contact.id)
    new_contacts = db.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contacts.id_or_max) == sorted(app.Contacts.get_contacts_list(),
                                                                      key=Contacts.id_or_max)

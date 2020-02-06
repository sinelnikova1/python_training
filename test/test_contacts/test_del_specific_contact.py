from model.contacts import Contacts


def test_delete_specific_contact(app):
    contact = Contacts(firstname="Alina", middlename="Ivanovna", lastname="Lallala")
    if app.contacts.count() < 2:
        while app.contacts.count() < 2:
            app.contacts.add_information_of_person(contact)
    old_contacts = app.contacts.get_contacts_list()
    app.contacts.delete_specific_contact()
    new_contacts = app.contacts.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[1:2] = []
    assert old_contacts == new_contacts

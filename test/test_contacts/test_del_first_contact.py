from model.contacts import Contacts


def test_delete_first_contact(app):
    contact = Contacts(firstname="Alina", middlename="Ivanovna", lastname="Lallala")
    if app.contacts.count() == 0:
        app.contacts.add_information_of_person(contact)
    old_contacts = app.contacts.get_contacts_list()
    app.contacts.delete_first_contact()
    new_contacts = app.contacts.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    # удаляем только один элемент, т.к. вырезка включает левую границу, но не включает правую,
    # т.е. удаляем первый элемент
    old_contacts[0:1] = []
    assert old_contacts == new_contacts


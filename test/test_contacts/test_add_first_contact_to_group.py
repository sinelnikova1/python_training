from model.contacts import Contacts


def test_add_first_contact_to_group(app):
    if app.contacts.count() == 0:
        app.contacts.add_information_of_person(Contacts(firstname="Alina", middlename="Ivanovna", lastname="Lallala"))
    app.contacts.add_first_contact_to_group()

from model.contacts import Contacts


def test_delete_all_contacts(app):
    if app.contacts.count() == 0:
        app.contacts.add_information_of_person(Contacts(firstname="Alina", middlename="Ivanovna", lastname="Lallala"))
    app.contacts.delete_all_contacts()
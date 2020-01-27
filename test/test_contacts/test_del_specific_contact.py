from model.contacts import Contacts


def test_delete_specific_contact(app):
    if app.contacts.count() < 2:
        while app.contacts.count() < 2:
            app.contacts.add_information_of_person(Contacts(firstname="test", middlename="test", lastname="test"))
    app.contacts.delete_specific_contact()

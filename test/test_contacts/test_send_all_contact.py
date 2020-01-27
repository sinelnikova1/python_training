from model.contacts import Contacts


def test_send_all_contacts(app):
    if app.contacts.count() == 0:
        app.contacts.add_information_of_person(Contacts(firstname="test", middlename="test", lastname="test"))
    app.contacts.send_all_contacts()

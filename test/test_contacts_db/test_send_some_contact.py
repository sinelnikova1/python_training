from model.contacts import Contacts
from random import randrange


def test_send_some_contacts(app):
    if app.contacts.count() == 0:
        app.contacts.add_information_of_person(Contacts(firstname="test", middlename="test", lastname="test",
                                                        email="fdjdf@utr.ri"))
    old_contacts = app.contacts.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contacts.send_some_contacts(index)

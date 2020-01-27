from model.contacts import Contacts
from model.group import Group

def test_add_all_contacts_to_group(app):
    if app.contacts.count() < 2 and app.group.count() == 0:
        while app.contacts.count() < 2:
            app.contacts.add_information_of_person(Contacts(firstname="Alina", middlename="Ivanovna", lastname="Lallala"))
            app.group.create(Group(name="test"))
    app.contacts.add_all_contacts_to_group()
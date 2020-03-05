import random
from fixture.orm import ORMFixture
from model.contacts import Contacts
from model.group import Group

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    if len(db.get_contacts_list()) == 0:
        app.contacts.create(Contacts(firstname="Alina", middlename="Ivanovna", lastname="Lallala", email="gghf@urte.tu"))
    if len(db.get_group_list()) == 0:
        group = Group(name="name test", header="header test", footer="footer test")
        app.group.create(group)
    random_group = random.choice(db.get_group_list())
    random_contact = random.choice(db.get_contacts_list())
    if random_contact in orm.get_contacts_not_in_group(random_group):
        app.contacts.add_contact_to_group_by_id(random_contact.id, random_group.id)
    app.contacts.add_contact_to_group_by_id(random_contact.id, random_group.id)
    contact_in_group = orm.get_contacts_in_group(random_group)
    contact_not_in_group = orm.get_contacts_not_in_group(random_group)
    assert random_contact in contact_in_group
    assert random_contact not in contact_not_in_group
    print ('\n\n' + " contact_id: " + random_contact.id + "; lastname: ", random_contact.lastname +
           '\n' + " added to group " +
           '\n' + " group_id: " + random_group.id + "; name: " + random_group.name)

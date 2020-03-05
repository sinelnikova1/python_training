from model.contacts import Contacts
from timeit import timeit


def test_contact_list(app, db, check_ui):
    print(timeit(lambda: app.group.get_contacts_list(), number=1))
    def clean(contact):
        return Contacts(id=contact.id, name = contact.firstname.strip())
    print(timeit(lambda: map(clean,db.get_contacts_list()), number=1000))
    assert False #sorted(ui_list, key = Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
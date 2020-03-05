from model.contacts import Contacts


def test_contact_list(app, db):
    check_ui = app.contacts.get_contacts_list()
    def clean(contact):
        return Contacts(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
    check_db = map(clean, db.get_contacts_list())
    assert sorted(check_ui, key=Contacts.id_or_max) == sorted(check_db, key=Contacts.id_or_max)

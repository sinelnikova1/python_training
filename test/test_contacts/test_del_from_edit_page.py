from model.contacts import Contacts


def test_del_from_edit_page(app):
    if app.contacts.count() == 0:
        app.contacts.add_information_of_person(Contacts(firstname="test", middlename="test", lastname="test"))
    app.contacts.delete_first_contact_from_edit_page()

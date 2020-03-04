from model.contacts import Contacts


def test_delete_all_contacts(app, db, check_ui):
    old_contacts = db.get_contacts_list()
    contact = Contacts(firstname="Alina", middlename="Ivanovna", lastname="Lallala")
    if app.contacts.count() == 0:
        app.contacts.add_information_of_person(contact)
    app.contacts.delete_all_contacts()
    new_contacts = db.get_contacts_list()
    # каждому элементу списка присваиваем пустое значение (0), т.е. удаляем
    for i in range(len(old_contacts)):
        old_contacts = []
    assert len(old_contacts) - len(new_contacts) == 0
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contacts.id_or_max) == sorted(app.Contacts.get_contacts_list(),
                                                                      key=Contacts.id_or_max)
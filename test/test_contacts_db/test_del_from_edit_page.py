from model.contacts import Contacts
import random


# тест при клике на кнопку редактирования в строке контакта
def test_del_from_edit_page(app, db, check_ui):
    contact = Contacts(firstname="Alina", middlename="Ivanovna", lastname="Lallala")
    if app.contacts.count() == 0:
        app.contacts.add_information_of_person(contact)
    old_contacts = db.get_contacts_list()
    random_contact = random.choice(old_contacts)
    index = old_contacts.index(random_contact)
    app.contacts.delete_some_contact_by_id(random_contact.id)
    new_contacts = db.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    # удаление выбранного элемента
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contacts.id_or_max) == sorted(app.Contacts.get_contacts_list(),
                                                                      key=Contacts.id_or_max)


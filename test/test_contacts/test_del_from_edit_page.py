from model.contacts import Contacts
from random import randrange


# тест при клике на кнопку редактирования в строке контакта
def test_del_from_edit_page(app):
    contact = Contacts(firstname="Alina", middlename="Ivanovna", lastname="Lallala")
    if app.contacts.count() == 0:
        app.contacts.add_information_of_person(contact)
    old_contacts = app.contacts.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contacts.delete_some_contact_from_edit_page(index)
    new_contacts = app.contacts.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    # удаление выбранного элемента
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts


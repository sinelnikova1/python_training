from model.contacts import Contacts
import allure

#@pytest.mark.parametrize("contact", testdata, ids=[str(x) for x in testdata])


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    with allure.step('Given a contact list'):
        old_contacts = db.get_contacts_list()
    with allure.step('When I add a contact %s to the list' % contact):
        app.contacts.add_information_of_person(contact)
    with allure.step('Then the new contact list is equal to the old list with added contact'):
        assert len(old_contacts) + 1 == app.contacts.count()
        new_contacts = db.get_contacts_list()
        # проверка сравнения старого и нового списка с добавлением элемента
        old_contacts.append(contact)
        #assert old_contacts == new_contacts
        if check_ui:
         assert sorted(new_contacts, key=Contacts.id_or_max) == sorted(app.contacts.get_contacts_list(), key=Contacts.id_or_max)





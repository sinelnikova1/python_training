import re
from model.contacts import Contacts


def test_general_info_on_home_page(app, db):
    contact = Contacts(firstname="Petr", middlename="Petrovich", lastname="Petrov",
         nickname="superman", title=u"Электрик", address=u"Санкт-Петербург, ул. Большевиков 178",
         company=u"ООО Супергаз", home="9899899554", mobile="45555445554", work="55665585", fax="7888556",
         email="emaifortest1@hfkf.ri", email2="email2@kfd.ru", email3="renk@kdf.ri", homepage="homepage.ti",
         bday="16", bmonth="July", byear="1980", aday="10", amonth="May", ayear="2010", address2="LA 45 Oxford St. 549",
         phone2="home", notes="some notes for this")
    if len(db.get_contacts_list()) == 0:
        app.contacts.add_information_of_person(contact)
    contact_from_home_page = sorted(app.contacts.get_contacts_list(), key=Contacts.id_or_max)
    contact_from_db = sorted(db.get_contacts_list(), key=Contacts.id_or_max)
    assert len(contact_from_db) == len(contact_from_home_page)
    for i in range(len(contact_from_home_page)):
        assert contact_from_home_page[i].id == contact_from_db[i].id
        assert clear(contact_from_home_page[i].lastname) == clear(contact_from_db[i].lastname)
        assert clear(contact_from_home_page[i].firstname) == clear(contact_from_db[i].firstname)
        assert clear(contact_from_home_page[i].address) == clear(contact_from_db[i].address)
        assert contact_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db[i])
        assert contact_from_home_page[i].all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db[i])


def merge_emails_like_on_home_page(contacts):
    return "\n".join(filter(lambda x: x != "",  # удаляются пустые строки. что не удалилось - склеивается (последний шаг)
                                filter(lambda x: x is not None,  #выкидываются все пустые элементы
                                       [contacts.email, contacts.email2, contacts.email3])))

#очищаем лишние символы
def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contacts):
    return "\n".join(filter(lambda x: x != "",  # удаляются пустые строки. что не удалилось - склеивается (последний шаг)
                            map(lambda x: clear(x),  #удаляются лишние символы)
                                filter(lambda x: x is not None,  #выкидываются все пустые элементы
                                       [contacts.home, contacts.mobile, contacts.work, contacts.phone2]))))
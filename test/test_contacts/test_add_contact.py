from model.contacts import Contacts
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation
    # будет сгенерирована случайная длина случайных символов не превышающая максимальную
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contacts(firstname="", middlename="", lastname="", nickname="", title="", address="", company="", home="",
                     mobile="", work="", fax="", email="", email2="", email3="", homepage="", address2="", phone2="",
                     notes="")] + [
            Contacts(firstname= random_string("firstname ", 10), middlename=random_string("middlename ", 20),
             lastname= random_string("lastname ", 15), nickname= random_string("nickname ", 5),
             title= random_string(u"title ", 10), address=random_string("address ", 30),
             company= random_string(u"company ", 20), home=random_string("home phone ", 12),
             mobile=random_string("mobile phone ", 12), work=random_string("work phone ", 12),
             fax=random_string("fax ", 13), email=random_string("email1 ", 70), email2=random_string("email2 ", 19),
             email3=random_string("email3 ", 50), homepage=random_string("homepage ", 45),
                     address2=random_string("address2 ", 12), phone2=random_string("phone2 ", 12),
                     notes=random_string("notes ", 100))
    for i in range(5)
    ]

@pytest.mark.parametrize("contact", testdata, ids=[str(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contacts.get_contacts_list()
    app.contacts.add_information_of_person(contact)
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = app.contacts.get_contacts_list()
    # проверка сравнения старого и нового списка с добавлением элемента
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)






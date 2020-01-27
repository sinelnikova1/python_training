# -*- coding: utf-8 -*-
from model.contacts import Contacts


def test_modify_fio(app):
    app.contacts.modify_data_from_details(Contacts(firstname="Irina", middlename="Alexandrovna", lastname="Alisa"))


def test_modify_email(app):
    app.contacts.modify_data_from_details(Contacts(email="email_lion_857@kf.it", email2="email2@kfd.ru",
                                                   email3="renk@kdf.ri"))

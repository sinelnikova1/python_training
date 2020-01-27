# -*- coding: utf-8 -*-
from model.contacts import Contacts


def test_update_email(app):
    app.contacts.update_email(Contacts(firstname="Irina", middlename="Alexandrovna", lastname="Alili",
         nickname="superman", title=u"Электрик", address=u"Санкт-Петербург, ул. Большевиков 178",
         company=u"ООО Супергаз", home="9899899554", mobile="45555445554", work="55665585", fax="7888556",
         email="email_lion_857@kf.it", email2="email2@kfd.ru", email3="renk@kdf.ri", homepage="homepage.ti",
         bday="16", bmonth="July", byear="1980", aday="10", amonth="May", ayear="2010", address2="LA 45 Oxford St. 549",
         phone2="home", notes="some notes for this"))

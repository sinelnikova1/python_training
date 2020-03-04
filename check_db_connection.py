import pymysql.cursors
from fixture.db import DbFixture


db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

#группы
#try:
 #   groups = db.get_group_list()
#    for group in groups:
#        print(group)
#    print(len(groups))
#finally:
 #   db.destroy()

#контакты
try:
    contacts = db.get_contacts_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    db.destroy()
import pymysql.cursors
#from fixture.db import DbFixture
from fixture.orm import ORMFixture
from model.group import Group


#db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


#группы
#try:
 #   groups = db.get_group_list()
#    for group in groups:
#        print(group)
#    print(len(groups))
#finally:
 #   db.destroy()

#контакты
#try:
#    contacts = db.get_contacts_list()
#    for contact in contacts:
#        print(contact)
#    print(len(contacts))
#finally:
#    db.destroy()

try:
    l = db.get_contacts_not_in_group(Group(id="576")) # l - list
    for item in l:
        print(item)
    print(len(l))
finally:
    pass
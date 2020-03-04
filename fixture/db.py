import pymysql.cursors
from model.group import Group
from model.contacts import Contacts

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit = True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name = name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contacts_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, middlename from addressbook where deprecated = '0000-00-00 00:00:00' ")
            for row in cursor:
                (id, firstname, lastname, middlename) = row
                list.append(Contacts(id=str(id), firstname = firstname, lastname=lastname, middlename=middlename))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
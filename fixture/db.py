import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, address2, email, email2, email3, home, mobile, work, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, address2, email, email2, email3, home, mobile, work, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                    address2=address2, email=email, email2=email2, email3=email3, home=home,
                                    mobile=mobile, work=work, phone2=phone2))
        finally:
            cursor.close()
        return list

    def get_contacts_in_group_list(self, group):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id from address_in_groups where group_id='"+group.id+"'")
            for row in cursor:
                id = row[0]
                list.append(Contact(id=str(id)))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

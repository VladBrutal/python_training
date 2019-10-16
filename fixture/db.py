import pymysql
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
            cursor.execute("select id, firstname, middlename, lastname, nickname, company, address, mobile, home, "
                           "work, email, homepage, address2, phone2 from addressbook")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, address,
                 home_phone, mobile_phone, work_phone, email, homepage, address2, secondary_phone) = row
                list.append(Contact(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname,
                                    nickname=nickname, company=company, address=address, home_phone=home_phone,
                                    mobile_phone=mobile_phone, work_phone=work_phone, email=email, homepage=homepage,
                                    address2=address2, secondary_phone=secondary_phone))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

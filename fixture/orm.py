from datetime import datetime
from model.group import Group
from model.contact import Contact
from pony.orm import *
from pymysql.converters import decoders


class ORMFixture:
    db = Database()  # Object which helps build connection to DB

    class ORMGroup(db.Entity):  # We need to describe number of conditions and connect them with table
        _table_ = 'group_list'
        id = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")

    class ORMContact(db.Entity):  # We need to describe number of conditions and connect them with table
        _table_ = 'addressbook'
        id = PrimaryKey(int, column="id")
        firstname = Optional(str, column="firstname")
        middlename = Optional(str, column="middlename")
        lastname = Optional(str, column="lastname")
        nickname = Optional(str, column="nickname")
        company = Optional(str, column="company")
        address = Optional(str, column="address")
        home_phone = Optional(str, column="home")
        mobile_phone = Optional(str, column="mobile")
        work_phone = Optional(str, column="work")
        email = Optional(str, column="email")
        homepage = Optional(str, column="homepage")
        address2 = Optional(str, column="address2")
        secondary_phone = Optional(str, column="phone2")
        deprecated = Optional(datetime, column="deprecated")

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()  # Making matching of properties of described
        # classes with the tables and fields of this described class
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id),
                           firstname=contact.firstname, middlename=contact.middlename, lastname=contact.lastname,
                           nickname=contact.nickname, company=contact.company, address=contact.address,
                           home_phone=contact.home_phone, mobile_phone=contact.mobile_phone,
                           work_phone=contact.work_phone, secondary_phone=contact.secondary_phone, email=contact.email,
                           homepage=contact.homepage, address2=contact.address2)

        return list(map(convert, contacts))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))


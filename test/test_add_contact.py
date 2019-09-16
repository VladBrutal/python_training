# -*- coding: utf-8 -*-
import string
import random
import pytest

from model.contact import Contact


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_number(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits  # + string.punctuation
    random_combination = "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return prefix + random_combination + "@" + "".join(
        random.sample(random_combination, len(random_combination))) + ".com"


def random_string_int_address(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "=" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + ".com"


contact_test_data = [Contact(firstname="", middlename="", lastname="", nickname="", company=""
                             , address="", home_phone="", mobile_phone="",
                             work_phone="", secondary_phone="", email="", homepage="", address2="")] + [
                        Contact(firstname=random_string("First Name", 10), middlename=random_string("Middle Name", 15)
                                , lastname=random_string("Last Name", 15),
                                nickname=random_string("Nickname", 15)
                                , company=random_string("Company", 20), address=random_string("Address", 20),
                                home_phone=random_string_number("H", 9), mobile_phone=random_string_number("M", 9),
                                work_phone=random_string_number("W", 9), secondary_phone=random_string_number("P", 9),
                                email=random_string_email("email", 10)
                                , homepage=random_string_int_address("Homepage", 15),
                                address2=random_string("Address2", 20))
                        for i in range(5)
                    ]


@pytest.mark.parametrize("contact", contact_test_data, ids=[repr(x) for x in contact_test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

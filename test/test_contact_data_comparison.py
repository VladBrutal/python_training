import re
from random import randrange

from test.test_del_contact import precondition_contact_existence


def test_comparison_random_contact_home_and_edit_page(app):
    precondition_contact_existence(app)
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert clear2(contact_from_home_page.address) == clear2(contact_from_edit_page.address)
    assert contact_from_home_page.all_email == merge_emails_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def clear2(s):
    re.sub("[  ]", "", s)


def merge_emails_like_on_home_page(contact):
    email_data = [contact.email, contact.email2, contact.email3]
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, email_data))))

# def merge_data_from_address_field(contact):
#     return "".join(filter(lambda x: x != "\n", contact.address))

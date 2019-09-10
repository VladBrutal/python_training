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
    assert clear(merge_data_from_address_field(contact_from_home_page)) == clear(merge_data_from_address_field(contact_from_edit_page))
    # assert clear(contact_from_home_page.address) == clear(contact_from_edit_page.address)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_email == merge_emails_like_on_home_page(contact_from_edit_page)


# def phones_on_contact_view_page(app):
#     contact_from_view_page = app.contact.get_contact_from_view_page()[0]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page()[0]
#     assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    phones_data = [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.secondary_phone]
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, phones_data))))


def merge_emails_like_on_home_page(contact):
    email_data = [contact.email, contact.email2, contact.email3]
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, email_data))))


def merge_data_from_address_field(contact):
    return "".join(filter(lambda x: x != "\n", contact.address))

import re
from random import randrange

from model.contact import Contact
from test.test_del_contact import precondition_contact_existence


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.secondary_phone == contact_from_edit_page.secondary_phone


def test_comparison_contacts_home_page_and_db(app, db):
    precondition_contact_existence(app)
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()
    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(contact_from_db, key=Contact.id_or_max)
    
    # assert contact_from_home_page.firstname == contact_from_db.firstname
    # assert contact_from_home_page.lastname == contact_from_db.lastname
    # assert clear2(contact_from_home_page.address) == clear2(contact_from_db.address)
    # assert contact_from_home_page.all_email == merge_emails_like_on_home_page(contact_from_db)


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


def merge_phones_like_on_home_page(contact):
    phones_data = [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.secondary_phone]
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, phones_data))))

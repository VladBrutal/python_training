import random

from model.contact import Contact
from test.test_del_contact import precondition_contact_existence


def test_link_random_contact_to_random_group(app, db, check_ui):
    precondition_contact_existence(app)
    precondition_c_to_g_connection()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.link_c_to_g_by_id(contact.id)  #  add contact to the group method
    # edit_contact_data = Contact(firstname="Edited firstname", lastname="Edited lastname", home_phone="293847",
    #                             mobile_phone="354679", work_phone="183756", secondary_phone="542000")
    # app.contact.edit_contact_by_id(edit_contact_data, contact.id)
    new_contacts = app.contact.get_contact_list()
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, firstname=contact.firstname.strip())

        clean_new_contacts = map(clean, new_contacts)
        assert sorted(clean_new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


def precondition_c_to_g_connection():
    pass
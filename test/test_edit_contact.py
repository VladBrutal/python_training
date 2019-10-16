import random

from model.contact import Contact
from test.test_del_contact import precondition_contact_existence


def test_edit_some_contact(app, db, check_ui):
    precondition_contact_existence(app)
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    edit_contact_data = Contact(firstname="Edited firstname", lastname="Edited lastname", home_phone="293847",
                                mobile_phone="354679", work_phone="183756", secondary_phone="542000")
    app.contact.edit_contact_by_id(edit_contact_data, contact.id)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, firstname=contact.firstname.strip())

        clean_new_contacts = map(clean, new_contacts)
        assert sorted(clean_new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

import random

from model.contact import Contact


def test_modify_first_contact_name(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Name", middlename="Middle", lastname="Surname"))
    old_contacts = db.get_contact_list()
    old_contact = random.choice(old_contacts)
    contact = Contact(id=old_contact.id, firstname="Anna", middlename="Sergeevna", lastname="Makarova", nik="anna",
                      title="Ms")
    app.contact.modify_contact_by_id(contact, old_contact.id)
    new_contacts = db.get_contact_list()
    for i in range(len(old_contacts)):
        if old_contacts[i].id == old_contact.id:
            old_contacts[i] = contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_first_contact_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Name", middlename="Middle", lastname="Surname"))
    old_contacts = db.get_contact_list()
    old_contact = random.choice(old_contacts)
    contact = Contact(id=old_contact.id, lastname=old_contact.lastname, firstname=old_contact.firstname,
                      home="+7(812)852-12-52", mobile="+7(911)852-96-96", work="+7(495)123-52-52", fax="999")
    app.contact.modify_contact_by_id(contact, old_contact.id)
    new_contacts = db.get_contact_list()
    for i in range(len(old_contacts)):
        if old_contacts[i].id == old_contact.id:
            old_contacts[i] = contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

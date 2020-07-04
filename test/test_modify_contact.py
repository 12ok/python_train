from random import randrange

from model.contact import Contact


def test_modify_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Name", middlename="Middle", lastname="Surname"))
    contact = Contact(firstname="Anna", middlename="Sergeevna", lastname="Makarova", nik="anna", title="Ms")
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_first_contact_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Name", middlename="Middle", lastname="Surname"))
    contact = Contact(home="+7(812)852-12-52", mobile="+7(911)852-96-96", work="+7(495)123-52-52", fax="999")
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    contact.lastname = old_contacts[index].lastname
    contact.firstname = old_contacts[index].firstname
    app.contact.modify_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

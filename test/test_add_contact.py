# -*- coding: utf-8 -*-
from model.contact import Contact


# test падает если есть символы ' \
# оставила полный вывод в repr для проверки какие данные указывались
def test_add_contact(app, data_contacts):
    contact = data_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

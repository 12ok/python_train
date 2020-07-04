from model.contact import Contact


def test_modify_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Name", middlename="Middle", lastname="Surname"))
    contact = Contact(firstname="Anna", middlename="Sergeevna", lastname="Makarova", nik="anna", title="Ms")
    old_contacts = app.contact.get_contact_list()
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_first_contact_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Name", middlename="Middle", lastname="Surname"))
    contact = Contact(home="+7(812)852-12-52", mobile="+7(911)852-96-96", work="+7(495)123-52-52", fax="999")
    old_contacts = app.contact.get_contact_list()
    contact.id = old_contacts[0].id
    contact.lastname = old_contacts[0].lastname
    contact.firstname = old_contacts[0].firstname
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

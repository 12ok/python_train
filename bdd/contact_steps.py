from pytest_bdd import given, when, then

from model.contact import Contact
import random


@given('a contact list')
def contact_list(db):
    return db.get_contact_list()


@given('a contact with <firstname>, <middlename> and <lastname>')
def new_contact(firstname, middlename, lastname):
    return Contact(firstname=firstname, middlename=middlename, lastname=lastname)


@given('a non-empty contact list')
def non_empty_contact_list(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Name", middlename="Middle", lastname="Surname"))
    return db.get_contact_list()


@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I add the contact to the list')
def add_contact(app, new_contact):
    app.contact.create(new_contact)


@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@when('I modify the contact from the list')
def modify_contact(app, random_contact, new_contact):
    app.contact.modify_contact_by_id(new_contact, random_contact.id)


@then('the new list is equal to the old list with the added contact')
def verify_contact_added(db, new_contact, contact_list):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@then('the new list is equals to the old list without the delete contact')
def verify_contact_deleted(db, random_contact, non_empty_contact_list):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@then('the new list is equals to the old list with modify contact')
def verify_contact_modify(db, new_contact, non_empty_contact_list, random_contact):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    for i in range(len(old_contacts)):
        if old_contacts[i].id == random_contact.id:
            old_contacts[i] = new_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

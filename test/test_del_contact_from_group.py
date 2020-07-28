from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random


def test_delete_contact_from_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Name", middlename="Middle", lastname="Surname"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    # old_contacts = db.get_contact_list()
    # old_groups = db.get_group_list()
    orm_db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    old_contacts_in_group = orm_db.get_contacts_in_group(Group(id='144'))
    contact = random.choice(old_contacts_in_group)
    app.contact.delete_from_group(contact.id, '144')
    old_contacts_in_group.remove(contact)
    new_contacts_in_group = orm_db.get_contacts_in_group(Group(id='144'))
    assert old_contacts_in_group == new_contacts_in_group

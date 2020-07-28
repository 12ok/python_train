from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Name", middlename="Middle", lastname="Surname"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_contacts = db.get_contact_list()
    old_groups = db.get_group_list()
    orm_db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    contact = random.choice(old_contacts)
    group = random.choice(old_groups)
    old_contacts_from_group = orm_db.get_contacts_in_group(group)
    app.contact.add_to_group(contact.id, group.id)
    old_contacts_from_group.append(contact)
    new_contacts_from_group = orm_db.get_contacts_in_group(group)
    assert old_contacts_from_group == new_contacts_from_group

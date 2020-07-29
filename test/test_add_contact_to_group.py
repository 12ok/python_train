from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, db, orm_db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Name", middlename="Middle", lastname="Surname"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    # Если нет контактов без групп, добавляем новый контакт
    if len(orm_db.get_contacts_without_group()) == 0:
        app.contact.create(Contact(firstname="Name", middlename="Middle", lastname="Surname"))
    contacts_without_groups = orm_db.get_contacts_without_group()
    # Берем случайный контакт без групп
    contact = random.choice(contacts_without_groups)
    group = random.choice(old_groups)
    old_contacts_in_group = orm_db.get_contacts_in_group(group)
    app.contact.add_to_group(contact.id, group.id)
    old_contacts_in_group.append(contact)
    new_contacts_in_group = orm_db.get_contacts_in_group(group)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)

from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random


def test_delete_contact_from_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Name", middlename="Middle", lastname="Surname"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    orm_db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    # Проверяем если в БД нет групп с контактами, добавляем контакт в группу
    if len(db.get_groups_with_contact()) == 0:
        random_contact = random.choice(db.get_contact_list())
        random_group = random.choice(db.get_group_list())
        app.contact.add_to_group(random_contact.id, random_group.id)
    # Получаем список групп к котором добавлен контакт
    group_with_contact = db.get_groups_with_contact()
    group = random.choice(group_with_contact)
    old_contacts_in_group = orm_db.get_contacts_in_group(group)
    contact = random.choice(old_contacts_in_group)
    app.contact.delete_from_group(contact.id, group.id)
    old_contacts_in_group.remove(contact)
    new_contacts_in_group = orm_db.get_contacts_in_group(group)
    assert len(old_contacts_in_group) == len(new_contacts_in_group)
    assert old_contacts_in_group == new_contacts_in_group

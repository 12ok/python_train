import random
import re

from model.group import Group


def clear(group):
    return Group(id=group.id, name=re.sub(" +", " ", group.name).strip())


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="for test"))
    old_groups = db.get_group_list()
    old_group = random.choice(old_groups)
    new_group = Group(id=old_group.id, name="new group")
    app.group.modify_group_by_id(new_group, old_group.id)
    new_groups = db.get_group_list()
    for i in range(len(old_groups)):
        if old_groups[i].id == old_group.id:
            old_groups[i] = new_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(map(clear, new_groups), key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                             key=Group.id_or_max)


def test_modify_group_header(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(header="for test"))
    old_groups = db.get_group_list()
    old_group = random.choice(old_groups)
    new_group = Group(id=old_group.id, name=old_group.name, header="new header")
    app.group.modify_group_by_id(new_group, old_group.id)
    new_groups = db.get_group_list()
    for i in range(len(old_groups)):
        if old_groups[i].id == old_group.id:
            old_groups[i] = new_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(map(clear, new_groups), key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                             key=Group.id_or_max)


def test_modify_group_footer(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(footer="for test"))
    old_groups = db.get_group_list()
    old_group = random.choice(old_groups)
    new_group = Group(id=old_group.id, name=old_group.name, footer="new header")
    app.group.modify_group_by_id(new_group, old_group.id)
    new_groups = db.get_group_list()
    for i in range(len(old_groups)):
        if old_groups[i].id == old_group.id:
            old_groups[i] = new_group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(map(clear, new_groups), key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                             key=Group.id_or_max)

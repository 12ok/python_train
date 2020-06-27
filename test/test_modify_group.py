from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="for test"))
    app.group.modify_first_group(Group(name="new group"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="for test"))
    app.group.modify_first_group(Group(header="new header"))


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="for test"))
    app.group.modify_first_group(Group(footer="new footer"))

from model.contact import Contact


def test_modify_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Name", middlename="Middle", lastname="Surname"))
    app.contact.modify_first_contact(
        Contact(firstname="Anna", middlename="Sergeevna", lastname="Makarova", nik="anna", title="Ms"))


def test_modify_first_contact_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Name", middlename="Middle", lastname="Surname"))
    app.contact.modify_first_contact(
        Contact(home="+7(812)852-12-52", mobile="+7(911)852-96-96", work="+7(495)123-52-52", fax="999"))

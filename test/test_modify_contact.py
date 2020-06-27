from model.contact import Contact


def test_modify_first_contact_name(app):
    app.contact.modify_first_contact(
        Contact(firstname="Anna", middlename="Sergeevna", lastname="Makarova", nik="anna", title="Ms"))


def test_modify_first_contact_contact(app):
    app.contact.modify_first_contact(
        Contact(home="+7(812)852-12-52", mobile="+7(911)852-96-96", work="+7(495)123-52-52", fax="999"))

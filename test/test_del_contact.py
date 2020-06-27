from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Name", middlename="Middle", lastname="Surname"))
    app.contact.delete_first_contact()

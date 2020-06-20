from model.contact import Contact


def test_edit_first_contact(app):
    contact = Contact("Anna", "Sergeevna", "Makarova", "anna", "Ms", "The test", "street 100", "8127418596",
                      "9110000000", "8121112233", "555", "mail1@rr.ru", "mail2@tt.ru",
                      "mail3@yy.ru", "www", "10", "April", "1985", "23", "December", "2030", "city street",
                      "12", "none")
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(contact)
    app.session.logout()

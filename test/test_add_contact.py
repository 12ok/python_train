# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    contact = Contact("Oleg", "Petrovich", "Ivanov", "opi", "Mr", "The name", "street 10", "8121234556",
                      "9112223355", "8127418523", "123", "mailone@rr.rr", "mailtwo@tt.tt",
                      "mailthree@yy.yy", "www", "10", "April", "1985", "23", "December", "2030", "city street",
                      "12", "none")
    app.session.login(username="admin", password="secret")
    app.contact.create(contact)
    app.session.logout()

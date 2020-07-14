# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import string
import random
import re


def clear_end_spase(s):
    return re.sub(" $", "", s)


def random_string_alpha(prefix, maxlen):
    symbols = string.ascii_letters + " "
    return clear_end_spase(prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]))


def random_string_digit(prefix, maxlen):
    symbols = string.digits + " +()-"
    return clear_end_spase(prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]))


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "
    return clear_end_spase(prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]))


testdata = [Contact(firstname="", middlename="", lastname="", nik="", title="", company="", address="", home="",
                    mobile="", work="", fax="",
                    email="", email2="", email3="", page="", address2="", phone2="", notes="")] + [
               Contact(firstname=random_string_alpha("name", 5), middlename=random_string_alpha("middlename", 10),
                       lastname=random_string_alpha("lastname", 10), nik=random_string("nik", 5),
                       title=random_string_alpha("", 2), company=random_string("", 8), address=random_string("", 10),
                       home=random_string_digit("hp", 11),
                       mobile=random_string_digit("mp", 8), work=random_string_digit("wp", 7),
                       fax=random_string_digit("f", 5),
                       email=random_string("e1", 10), email2=random_string("e2", 15), email3=random_string("e3", 20),
                       page=random_string("page", 15), address2=random_string("", 10),
                       phone2=random_string_digit("2p", 12), notes=random_string("", 10)) for i in range(5)]


# test падает если есть символы ' \
# оставила полный вывод в repr для проверки какие данные указывались
@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

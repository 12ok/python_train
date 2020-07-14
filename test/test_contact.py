import re
from random import randrange


def test_contact_on_home_page(app):
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == clear_end_spase(contact_from_edit_page.firstname)
    assert contact_from_home_page.lastname == clear_end_spase(contact_from_edit_page.lastname)
    assert contact_from_home_page.address == clear_end_spase(contact_from_edit_page.address)
    assert contact_from_home_page.all_emails == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def clear(s):
    return clear_end_spase(re.sub("[() -]", "", s))


def clear_end_spase(s):
    return re.sub(" $", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))

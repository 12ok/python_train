from model.contact import Contact
import re


def test_all_contacts_from_home_page_to_db(app, db):
    contacts_homepage = sorted(app.contact.get_contact_list(), key=Contact.id_or_max, )
    contacts_db = sorted(db.get_contact_list_full(), key=Contact.id_or_max)
    # Проверка что кол-во контактов в UI и БД совпадает
    assert len(contacts_homepage) == len(contacts_db)
    for i in range(len(contacts_homepage)):
        assert contacts_homepage[i].firstname == clear_end_spase(contacts_db[i].firstname)
        assert contacts_homepage[i].lastname == clear_end_spase(contacts_db[i].lastname)
        assert contacts_homepage[i].address == clear_end_spase(contacts_db[i].address)
        assert contacts_homepage[i].all_emails == merge_emails_like_on_home_page(contacts_db[i])
        assert contacts_homepage[i].all_phones_from_home_page == merge_phones_like_on_home_page(
            contacts_db[i])


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

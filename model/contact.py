from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nik=None, title=None, company=None, address=None,
                 home=None, mobile=None, work=None, fax=None, email=None,
                 email2=None, email3=None, page=None, address2=None, phone2=None, notes=None, id=None,
                 all_phones_from_home_page=None, all_emails=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nik = nik
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.page = page
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails = all_emails

    def __repr__(self):
        return "%s:%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % (
        self.id, self.firstname, self.middlename, self.lastname, self.nik, self.title, self.company, self.address,
        self.home, self.mobile, self.work, self.fax, self.email, self.email2, self.email3, self.page, self.address2,
        self.phone2, self.notes)

    def __eq__(self, other):
        return (
                       self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

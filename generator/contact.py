from model.contact import Contact
import string
import random
import re
import getopt
import sys
import os.path
import jsonpickle

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
                    mobile="", work="", fax="", email="", email2="", email3="", page="", address2="", phone2="",
                    notes="")] + [
               Contact(firstname=random_string_alpha("name", 5), middlename=random_string_alpha("middlename", 10),
                       lastname=random_string_alpha("lastname", 10), nik=random_string("nik", 5),
                       title=random_string_alpha("", 2),
                       company=random_string("", 8), address=random_string("", 10), home=random_string_digit("hp", 11),
                       mobile=random_string_digit("mp", 8), work=random_string_digit("wp", 7),
                       fax=random_string_digit("f", 5),
                       email=random_string("e1", 10), email2=random_string("e2", 15), email3=random_string("e3", 20),
                       page=random_string("page", 15), address2=random_string("", 10),
                       phone2=random_string_digit("2p", 12), notes=random_string("", 10)) for i in range(5)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w")as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

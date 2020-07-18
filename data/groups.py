import random
import string
import re

from model.group import Group

constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]


def clear(s):
    return re.sub(" +", " ", s)


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    random_string = prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return clear(random_string)


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 15))
    for i in range(5)]

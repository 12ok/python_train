import random
import string
import re
import os.path
import json
import getopt
import sys

from model.group import Group

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def clear(s):
    return re.sub(" +", " ", s)


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    random_string = prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return clear(random_string)


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 15))
    for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w")as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))

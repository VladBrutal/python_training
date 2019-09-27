from model.group import Group
import random
import string

constant_data = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2"),
    Group(name="name3", header="header3", footer="footer3"),
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 11), footer=random_string("footer", 12))
    for i in range(5)
    # for name in ["", random_string("name", 10)]
    # for header in ["", random_string("header", 11)]
    # for footer in ["", random_string("footer", 12)]
]
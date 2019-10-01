from model.group import Group
import random
import string
import os.path
import jsonpickle
import getopt  # helps with reading of the options of command line
import sys  # recive access to this options

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])  # "n" sets amount of the data entered
except getopt.GetoptError as err:  # "f" file where "n:" will put data.
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/groups.json"

for o,  a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 11), footer=random_string("footer", 12))
    for i in range(n)
    # for name in ["", random_string("name", 10)]
    # for header in ["", random_string("header", 11)]
    # for footer in ["", random_string("footer", 12)]
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

    # out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    # "dumps" command convert some data structure into a string in json format
    # "default" function using in cases when json doesnt know how to convert data

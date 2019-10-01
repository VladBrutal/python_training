
from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import json
import getopt  # helps with reading of the options of command line
import sys  # recive access to this options

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/contacts.json"

for o,  a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_number(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits  # + string.punctuation
    random_combination = "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return prefix + random_combination + "@" + "".join(
        random.sample(random_combination, len(random_combination))) + ".com"


def random_string_int_address(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "=" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + ".com"


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", company=""
                             , address="", home_phone="", mobile_phone="",
                             work_phone="", secondary_phone="", email="", homepage="", address2="")] + [
                        Contact(firstname=random_string("First Name", 10), middlename=random_string("Middle Name", 15)
                                , lastname=random_string("Last Name", 15),
                                nickname=random_string("Nickname", 15)
                                , company=random_string("Company", 20), address=random_string("Address", 20),
                                home_phone=random_string_number("H", 9), mobile_phone=random_string_number("M", 9),
                                work_phone=random_string_number("W", 9), secondary_phone=random_string_number("P", 9),
                                email=random_string_email("email", 10)
                                , homepage=random_string_int_address("Homepage", 15),
                                address2=random_string("Address2", 20))
                        for i in range(n)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

# with open(file, "w") as out:
#     out.write(json.dumps(contact_test_data, default=lambda x: x.__dict__, indent=2))

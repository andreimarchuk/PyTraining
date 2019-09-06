from model.contact import Contact
import random
import string
import os
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "h:f:", ["number of contacts", "file"])
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


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(3, maxlen))])


testdata = [
    Contact(firstname=random_string("firstname_", 10), middlename=random_string("middlename_", 10),
                               lastname=random_string("lastname_", 10), nickname=random_string("nickname_", 8), photo="C:\\fakepath\\Untitled.jpg",
                               title=random_string("title_", 6), company=random_string("company_", 10), address=random_string("address_", 8),
                               home=random_string("home_", 6), mobile=random_string("mobile_", 10), work=random_string("work_", 8), fax=random_string("fax_", 6),
                               email=random_string("email_", 10), email2=random_string("email2_", 8), email3=random_string("email3_", 6),
                               homepage=random_string("homepage_", 10), birthday="11 May 1977",
                               anniversary="3 June 1959", address2=random_string("address2_", 8),
                               phone2=random_string("phone2_", 6), notes=random_string("notes_", 20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
from model.group import Group
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    #symbols = string.ascii_letters + string.digits + " "*5 + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(3, maxlen))])

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name_", 10), header=random_string("header_", 8), footer=random_string("footer_", 12))
    for i in range(5)
]
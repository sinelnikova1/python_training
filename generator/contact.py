from model.contacts import Contacts
import random
import string
import os.path
import jsonpickle
import getopt
import sys

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

constant = [
    Contacts(firstname="firstname1", middlename="middlename1", lastname="lastname1", nickname="nickname1",
             title="title1", address="address1", company="company1", home="home1", mobile="mobile1", work="work1",
             fax="fax1", email="email1", email2="email2", email3="email3", homepage="homepage1", address2="address2",
             phone2="phone2", notes="notes1"),
    Contacts(firstname="firstname2", middlename="middlename2", lastname="lastname2", nickname="nickname2",
         title="title2", address="address2", company="company2", home="home2", mobile="mobile2", work="work2",
         fax="fax2", email="email1_2", email2="email2_2", email3="email3_2", homepage="homepage2", address2="address2_2",
         phone2="phone2_2", notes="notes2"),
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation
    # будет сгенерирована случайная длина случайных символов не превышающая максимальную
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contacts(firstname="", middlename="", lastname="", nickname="", title="", address="", company="", home="",
                     mobile="", work="", fax="", email="", email2="", email3="", homepage="", address2="", phone2="",
                     notes="")] + [
            Contacts(firstname= random_string("firstname ", 10), middlename=random_string("middlename ", 20),
             lastname= random_string("lastname ", 15), nickname= random_string("nickname ", 5),
             title= random_string(u"title ", 10), address=random_string("address ", 30),
             company= random_string(u"company ", 20), home=random_string("home phone ", 12),
             mobile=random_string("mobile phone ", 12), work=random_string("work phone ", 12),
             fax=random_string("fax ", 13), email=random_string("email1 ", 70), email2=random_string("email2 ", 19),
             email3=random_string("email3 ", 50), homepage=random_string("homepage ", 45),
                     address2=random_string("address2 ", 12), phone2=random_string("phone2 ", 12),
                     notes=random_string("notes ", 100))
    for i in range(n)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent =2)
    out.write(jsonpickle.encode(testdata))
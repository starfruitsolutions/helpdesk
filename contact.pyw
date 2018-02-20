import os
import pickle
from easygui import *

username = os.popen("echo %USERNAME%").read()
appDataDir = os.popen("echo %appdata%"+'/helpdesk').read().replace("\n", "")

msg = "Enter your  contact information"
title = "Contact Info"
fieldNames = ["Name","Email","Phone"]
fieldValues = []  # we start with blanks for the values
fieldValues = multenterbox(msg,title, fieldNames)

# make sure that none of the fields was left blank
while 1:
    if fieldValues == None: break
    errmsg = ""
    for i in range(len(fieldNames)):
      if fieldValues[i].strip() == "":
        errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
    if errmsg == "": break # no problems found
    fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)

fullContact= {"name": fieldValues[0], "email": fieldValues[1], "phone": fieldValues[2]}

try:
    contacts= pickle.load(open(appDataDir +"/contacts.p", "rb"))
except (OSError, IOError) as e:
    contacts={}
contacts[username]=fullContact
pickle.dump( contacts, open( appDataDir +"/contacts.p", "wb"))
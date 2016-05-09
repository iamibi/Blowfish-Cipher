#!/usr/bin/env python

from datetime import datetime
from getpass import getpass

def login():
    print ("Date: %s\nLogin Time: %s"%(str(datetime.now().date()), str(datetime.now().time()))) 
    login = str(raw_input("Login: "))
    password = getpass()

    print ("password: ", password)

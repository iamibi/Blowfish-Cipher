#!/usr/bin/env python

import os, sys, pickle
try:
    import Login
except ImportError as Ir:
    sys.exit("Import Error: %s"%(str(Ir)))

class createID(object):
    def __init__(self):
        self.login = ''
        self.password = ''
    def ID(self):
        print ("Enter a login ID: "),
        while True:
            self.login = str(input().strip())
            if self.login.isalnum() and self.login[0].isalpha() and 3 < len(self.login) < 16:
                break
            print ("Invalid login name.")
            print ("Login name can contain alphabets and/or numbers")
        print ("Enter a new password: "),

#TODO-----------------------
        while True:
            
if __name__ == '__main__':
    if not os.path.exists("shadow"):
        ch = str(input("There is no user currently added. Create one? [Yes/No] "))
        if ch in 'Yes yes y Y'.split():
            createID()
        elif ch in 'No N no n'.split():
            Login.login()
    

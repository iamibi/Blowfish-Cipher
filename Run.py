#!/usr/bin/env python

import os, sys, getpass
try:
    import Login, RootChecker
except ImportError as Ir:
    sys.exit("Import Error: %s"%(str(Ir)))

if __name__ == '__main__':
    try:
        if not os.path.exists("shadow"):
            ch = str(raw_input("There are no user currently added. Create one? [Yes/No]"))
            if ch in "yes Yes y Y".split():
                pssw = getpass.getpass("[sudo] password for superuser: ")
                RootChecker.RootCheck(pssw)
                createID()
            elif ch in 'No N no n'.split():
                sys.exit("Exiting...")
            else:
                sys.exit("Invalid Option")
            os.chmod("shadow", 440)
        else:
            Login.login()
    except KeyboardInterrupt:
        sys.exit()

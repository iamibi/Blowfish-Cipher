import pickle, os, sys, getpass

try:
    from CreateID import createID
    import BlowfishCipher
except ImportError as ir:
    sys.exit("File Error: %s"%(str(ir)))

class RootCheck(object):
    
    _pssw = 'ibrahim123'
    _count = 0
    
    def __init__(self, password):
        while True:
            if self._pssw == password:
                createID()
                sys.exit("User added successfully")
            else:
                if self._count == 3:
                    self._count = 0
                    sys.exit("Wrong Password entered three times")
                self._count += 1
                print ("Wrong password, Try again")
                password = getpass.getpass("[sudo] password for superuser: ")

import pickle, sys
from datetime import datetime
from getpass import getpass
try:
    import PasswordChecker
except ImportError as ir:
    sys.exit("Import Error: %s"%(str(ir)))

def login():
    print ("Date: %s\nLogin Time: %s"%(str(datetime.now().date()), str(datetime.now().time()))) 
    login = str(raw_input("Login: "))
    try:
        with open ("shadow", "rb") as data:
            temp = pickle.load(data)
    except pickle.PickleError as pk:
        sys.exit("File Error: %s"%(str(pk)))
    new = temp.split(':')
    if new[0] != login:
        sys.exit("The username doesn't exist")
    password = getpass()
    PasswordChecker.Cipher(login, password, 'd')

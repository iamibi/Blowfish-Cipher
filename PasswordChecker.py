try:
    from BlowfishCipher import blowfishCTR
except ImportError as IR:
    raise Exception("Import Error: %s"%(str(IR)))

import pickle, sys

#This function is needed to be called for checking or creating a new password
def Cipher(login, password, mode):
    key  = 'this is a test key'
    if mode[0] == "e":
        encryptedmsg = blowfishCTR(mode[0], key, password)
        try:
            with open("shadow", "wb") as data:
                pickle.dump("%s:%s"%(login, encryptedmsg), data)
        except pickle.PickleError as pk:
            raise Exception("File Error: %s"%(str(pk)))

    elif mode[0] == "d":
        try:
            with open("shadow", "rb") as data:
                content = pickle.load(data)
        except pickle.PickleError as pk:
            raise Exception("File Error: %s"%(str(pk)))
        new = content.split(':')
        if new[0] == login:
            decryptmsg = blowfishCTR(mode[0], key, new[1])
        else:
            sys.exit("Invalid Credentials")
        
        if decryptmsg == password:
            print ("Logging in...")
        else:
            print ("Wrong Password, Try Again")

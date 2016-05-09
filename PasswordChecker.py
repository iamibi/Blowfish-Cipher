#!/usr/bin/env python

try:
    from BlowfishCipher import blowfishCTR
except ImportError as IR:
    raise Exception("Import Error: %s"%(str(IR)))

#This function is needed to be called for checking or creating a new password
def Cipher(password, mode):
    key  = 'this is a test key'
    #data = raw_input("Enter your message: ")
    if mode[0] == "e":
        encryptedmsg = blowfishCTR('e', key, password)
        try:
            with open("shadow", "wb") as data:
                pickle.dump(encryptedmsg, data)
        except pickle.PickleError as pk:
            raise Exception("File Error: %s"%(str(pk)))
        encryptedmsg = ""

    elif mode[0] == "d":
        try:
            with open("shadow", "rb") as data:
                content = pickle.load(data)
        except pickle.PickleError as pk:
            raise Exception("File Error: %s"%(str(pk)))
        decryptmsg = blowfishCTR('d', key, content)

        if decryptmsg == password:
            print ("Logging in...")
        else:
            raise Exception("The password you entered is not correct. Please try again...")
        decryptmsg = ""

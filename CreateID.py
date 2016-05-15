import getpass, sys

try:
    import PasswordChecker
except ImportError as ir:
    sys.exit("File Error: %s"%(str()))

class createID(object):
    def __init__(self):
        self.login = ''
        self.password = ''
        self.confirmP = ''
        self.ID()
        
    def ID(self):
        print ("Enter a login ID: "),
        while True:
            self.login = str(raw_input().strip())
            if self.login.isalnum() and self.login[0].isalpha() and 3 < len(self.login) < 16:
                break
            if not 3 < len(self.login) < 16:
                print ("The login length must be between 4 - 15 characters")
            else:
                print ("Invalid login name."),
                print ("Login name can contain alphabets and/or numbers")
                print ("Enter again: "),

        while True:
            self.password = getpass.getpass()
            if 6 <= len(self.password) <= 32 and self.passwordCheck(self.password) == True:
                break
            if not 6 <= len(self.password) <= 32:
                print ("Password length must be within 6 - 32")
            else:
                print ("Password should contain alpha-numeric and/or special characters")

        while True:
            self.confirmP = getpass.getpass("Confirm Password:")
            if self.confirmP == self.password:
                break
            else:
                sys.exit("Passwords don't match")
        PasswordChecker.Cipher(self.login, self.password, 'e')
        
    def passwordCheck(self, pssw):
        flag = False
        
        alpha = False
        num = False
        special = False
        invalid = False
        
        for i in xrange(0, len(pssw), 1):
            if pssw[i].isalpha():
                alpha = True
            elif pssw[i].isdigit():
                num = True
            elif pssw[i] in "! @ # $ & * . _".split():
                special = True
            else:
                invalid = True
                return False

        if alpha:
            return True

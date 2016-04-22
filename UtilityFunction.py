# --------------------------------------------------------------
# utility functions

from struct import pack, unpack

def fourByte2int(bytestr):
    """ convert a 4-byte string to an int (long) """
    return unpack('!L', bytestr)[0]

def eightByte2int(bytestr):
    """ convert a 8-byte string to an int (long long) """
    return unpack('!Q', bytestr)[0]

def int2fourByte(x):
    """ convert a number to a 4-byte string, high order 
        truncation possible (in Python x could be a BIGNUM)
    """
    return pack('!L', x)

def xor(s1, s2):
    """ XORs the two input byte strings returning a result 
        the length of the shorter one 
    
        zip() into pairs of chars up to the length of the 
        shorter string, XORing the pair.  
    """
    return ''.join([chr(ord(a)^ord(b)) for a,b in zip(s1, s2)])

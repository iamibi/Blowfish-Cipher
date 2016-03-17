import sys

try:
    from struct import pack, unpack
except ImportError as imperr:
    sys.exit("Import Error: %s"%(str(imperr)))

try:
    def fourBytetoInt(bstring):
        return unpack('L', bstring)[0]
    def eightBytetoInt(bstring):
        return unpack('Q', bstring)[0]
    def inttoFourByte(x):
        return pack('L', x)
    def XOR(x, y):
        return ''.join([chr(ord(a) ^ ord(b)) for a, b in zip(x, y)])
except RuntimeError as RE:
    sys.exit("Error: %s"%(str(RE)))

def text2hex(string):

    r="0x"

    for i in string:

        r+=hex(ord(i))[2:]

    return int(r, 16)

if( __name__ == "__main__" ):

    import sys

    if( 2 == len(sys.argv) ) print(text2hex(sys.argv[2]))

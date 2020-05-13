def encrypt(plaintext, key, autokey=False):

    plaintext = "".join(plaintext.upper().split())

    key = "".join(key.upper().split())

    if( autokey ): key+=plaintext

    if( len(key) == 0 ): return plaintext

    key_idx = 0

    ciphertext = ""

    #iterate through list were the letters A-Z are actually numbers in the range 0-25
    for p in [ ord(letter) - ord('A') for letter in plaintext]:

        ciphertext += chr((( p + ord(key[key_idx]) - ord('A') ) % 26 ) + ord('A'))

        #update key_idx
        key_idx+=1
        if( key_idx == len(key) ): key_idx = 0

    return ciphertext


def decrypt(ciphertext, key, autokey=False, invalid_idxs=None):

    ciphertext = "".join(ciphertext.upper().split())

    key = "".join(key.upper().split())

    if( len(key) == 0 ): return plaintext

    key_idx = 0

    plaintext = ""

    #iterate through list were the letters A-Z are actually numbers in the range 0-25
    for p in [ ord(letter) - ord('A') for letter in ciphertext]:

        if( invalid_idxs==None or key_idx not in invalid_idxs ):
            char = chr((( p - ord(key[key_idx]) - ord('A') ) % 26 ) + ord('A'))
        else:
            char = key[key_idx]

        plaintext += char
        if( autokey ): key+=char

        #update key_idx
        key_idx+=1
        if( key_idx == len(key) ): key_idx = 0

    return plaintext

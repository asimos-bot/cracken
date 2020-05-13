#return a dict with the letter frequency of each letter in the english alphabet

lf_english = {

            'E': 0.1203,
            'T': 0.0910,
            'A': 0.0812,
            'O': 0.0768,
            'I': 0.0731,
            'N': 0.0695,
            'S': 0.0628,
            'R': 0.0602,
            'H': 0.0592,
            'D': 0.0432,
            'L': 0.0398,
            'U': 0.0288,
            'C': 0.0271,
            'M': 0.0261,
            'F': 0.0230,
            'Y': 0.0211,
            'W': 0.0209,
            'G': 0.0203,
            'P': 0.0182,
            'B': 0.0149,
            'V': 0.0111,
            'K': 0.0069,
            'X': 0.0017,
            'Q': 0.0011,
            'J': 0.0010,
            'Z': 0.0007
        }

lf_portuguese = {

            'A': 0.1462,
            'E': 0.1257,
            'O': 0.1073,
            'S': 0.0781,
            'R': 0.0653,
            'I': 0.0618,
            'N': 0.0505,
            'D': 0.0499,
            'M': 0.0474,
            'U': 0.0463,
            'T': 0.0434,
            'C': 0.0388,
            'L': 0.0278,
            'P': 0.0252,
            'V': 0.0167,
            'G': 0.0130,
            'H': 0.0128,
            'Q': 0.0120,
            'B': 0.0104,
            'F': 0.0102,
            'Z': 0.0047,
            'J': 0.0040,
            'X': 0.0021,
            'K': 0.0002,
            'Y': 0.0001,
            'W': 0.0001
        }

def lf(text):

    #format given text
    text = "".join([ i for i in text.upper() if ord(i) >= ord('A') and ord(i) <= ord('Z')])

    #get english alphabet
    alphabet = { chr(i):0 for i in range(ord('A'), ord('Z')+1) }

    for letter in text:
        alphabet[letter]+=1

    #turn number of repetitions into frequency
    for letter in alphabet:
        alphabet[letter] /= len(text)

    return alphabet

def lf_auto_crack(text_initial, letter_frequency):

    text_initial = text_initial.upper()

    #format given text
    text = "".join([ i for i in text_initial if ord(i) >= ord('A') and ord(i) <= ord('Z')])

    #func for sorted()
    itemgetter = lambda x: x[1]

    #transform letter frequency of the language into a list of lists, sort them, and them take out the frequency, leaving the characters in order
    lf_list_lang = [ i[0] for i in sorted( letter_frequency.items(), key=itemgetter)]
    lf_list_text = [ i[0] for i in sorted( lf(text).items(), key=itemgetter)]

    #merge the two lists into a dict where the key is the cipher character and the value is the plaintext counterpart
    convertion = { chars[0]: chars[1] for chars in tuple(zip(lf_list_text, lf_list_lang)) }

    #convert given ciphertext using the convertion dict
    return "".join([ convertion[c] if ord(c) >= ord('A') and ord(c) <= ord('Z') else c for c in text_initial ])

def lf_pretty(lf_dict):

    itemgetter = lambda x: x[1]

    print("| ciphertext\t| english\t| portuguese |")

    lf_list_english = sorted(lf_english.items(), key=itemgetter)
    lf_list_portuguese = sorted(lf_portuguese.items(), key=itemgetter)

    i=0

    for char,frequency in sorted(lf_dict.items(), key=itemgetter):

        print("%c : %.2f%%\t" % (char, frequency*100), end="")
        print("%c : %.2f%%\t" % (lf_list_english[i][0], lf_list_english[i][1]*100), end="")
        print("%c : %.2f%%" % (lf_list_portuguese[i][0], lf_list_portuguese[i][1]*100))

        i+=1

def lf_manual_crack(text_initial):

    text_initial = text_initial.upper()

    choice = ""

    #key are cipher and values are plain
    convertion = {}

    while( True ):

        #changed letters show as lower case
        current_text = "".join([ convertion[c].lower() if c in convertion else c for c in text_initial ])

        lf_pretty(lf(text_initial))

        print("convertion dict: ", convertion)

        print(current_text)

        print("commands: | reset | change | delete | help | exit |")

        choice = input()

        if( choice == "exit" ):
            return current_text

        elif( choice == "help" ):

            print("reset -> undo all changes")
            print("change -> change one letter for another")
            print("delete -> unchange a changed letter")
            print("help -> print this prompt")
            print("exit -> bye")

        elif( choice == "delete" ):

            choice = input("input changed char to delete:").upper()[0]

            if( choice not in convertion.values()):
                print("no letter was changed to this value")
                continue
            elif( len(choice) == 0 ):
                print("cancelled")
                continue

            #delete value from dict
            del convertion[list(convertion.keys())[list(convertion.values()).index(choice)]]

        elif( choice == "change" ):

            l_from = input("choose letter to change from:").upper()

            if(l_from in convertion):
                print("letter was already changed")
                continue

            if(len(l_from)==0):
                print("cancelled")
                continue

            l_from = l_from[0]

            l_to = input("choose letter to change to:").upper()

            if(l_to in convertion.values()):
                print("a letter was already changed to this one")
                continue


            if( len(l_to) == 0 ):
                print("cancelled")
                continue

            l_to = l_to[0]

            convertion[l_from] = l_to

        elif( choice == "reset" ):
            convertion = {}
        else:
            print("invalid command")

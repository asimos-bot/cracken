#return a list
#[n_repetitions_of_given_substring, space_between ]
#it ignores the first find, returning None if the substring doesn't repeat or if space between repetitions change
def repetitions(text, substring, start=0):

    result = [-1]

    idx = 0
    last_idx=-1
    start_idx = start

    while( True ):

        #get index of a substring like this one, starting search from start_idx
        idx = text.find(substring, start_idx)

        #return if nothing was found
        if( idx == -1 ):
            if( result[0] == 0 or result == -1 or len(result[1:]) != len(set(result[1:])) ):
                return None
            else:
                return (result[0], result[1])

        #avoid getting same idx or an overlapping one
        start_idx = idx+len(substring)

        #update number of repetitions
        result[0]+=1

        #if a substring like this one was already found
        if( last_idx != -1 ):

            result.append(idx-last_idx-len(substring))
            last_idx = idx

        #if this is the first match
        else:

            last_idx = idx

#apply the 'repetitions' function to all possible substrings with length 'n' in the text, and then make a dict out of it
def kasiski(text, n):

    result = dict()

    for i in range(len(text)-n):

        current_substring = text[i:i+n]

        if current_substring not in result:

            rep_result = repetitions(text, current_substring, i)

            if( rep_result != None ): result[current_substring] = rep_result

    return result

from functools import reduce

#get factors of a number
def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))) if n!=0 else {0}

from collections import OrderedDict

def kasiski_pretty(text, n):

    print("| substring | repetitions | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |")

    k = kasiski(text, n)

    k = OrderedDict([ (i, (k[i][0], k[i][1])) for i in sorted(k, key=lambda x: k[x][0], reverse=True)])

    f_repetitions = { i:0 for i in range(2, 26) }

    for sub in k:

        print("{:>12}".format(sub), end="")

        f = factors(k[sub][1])

        print("{:>12}".format(k[sub][0]), end="")

        print("  | ", end="")

        for i in range(2, 26):

            if( i in f ): f_repetitions[i] += k[sub][0]

            print([" ", "X"][i in f], end="")

            print([" | ", "  | "][i>=10],end="")

        print()

    print("| substring | repetitions | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |")

    sum_f = sum(f_repetitions.values())

    for factor in sorted(f_repetitions, key=lambda x: f_repetitions[x], reverse=True):

        print("%d: %.2f%%\t" % (factor, f_repetitions[factor]/sum_f*100))

import vigenere

#interactive prompt
def kasiski_manual_crack(text):

    choice=""

    formated_text = "".join([ i for i in text.upper() if ord(i) <= ord('Z') and ord('A') <= ord(i)])

    key="aaa"
    invalid_idxs=[]
    autokey=False

    while(True):

        print(vigenere.decrypt(text, key, autokey, invalid_idxs))

        print("autokey: {}\tinvalid_idxs={}".format(autokey, invalid_idxs))
        print("commands: | substrings | key | autokey | help |")

        choice = input("command: ")

        if( choice == "substrings" ):

            n = int(input("substring length: "))

            kasiski_pretty(formated_text, n)

            input()

        elif( choice == "key" ):

            key = input("input key(zeros will be seen as nothing): ").upper()

            invalid_idxs = [ i for i in range(len(key)) if key[i] == 0 ]

        elif( choice == "autokey" ):

            autokey = not autokey

        elif( choice == "help" ):

            print("susbtrings->get factors of the number of characters between substrings repetitions")
            print("key->set key to use(use zero for undefined spaces)")
            print("autokey->toogle autokey mode on/off")
            print("help->print this panel")

        else:

            continue

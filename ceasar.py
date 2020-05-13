def ceasar(text, n):

    result=""

    for i in text.upper():

        if( ord(i) <= ord('Z') and ord(i) >= ord('A') ):

            if( ord(i)+n > ord('Z') ):

                result+=chr(ord(i) + n - ord('Z') + ord('A') -1)

            else:

                result+=chr(ord(i)+n)

        else:

            result+=i

    return result

def decrypt(text):

    possibilities=[]

    for i in range(1, 26):

        possibilities.append(ceasar(text, i))

    return possibilities

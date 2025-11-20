#NEED TO PULL SOME MODULE???? importing discord.py??? - figure that out?
#GET BASE TO WORK AND UPLOAD TO GITHUB


let_num_conversion = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12,
                      'M':13,'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23,
                      'X':24, 'Y':25, 'Z':26
                      }

def get_input(): #USE TRY EXCEPT HERE
    base = input('Enter the word or sentence you would like to encode: ')
    key = input('Enter a single word you would like to shift by: ')
    #check_alpha(base, key)
    words = separate_words(base)
    encode(words, key)

    #FINISH


def check_alpha(pl_base, pl_key):
    counter1 = 0
    counter2 = 0
    for i in pl_base: #CHECK CLASS NOTES FOR HOW TO MAKE THIS MORE EFFICIENT
        if (i.isalpha() or i.isspace): #LETTING NUMBERS THROUGH???
            counter1 += 1
            print(counter1) #TEMP
        else:
            pass
    for j in pl_key: #CHECK CLASS NOTES FOR HOW TO MAKE THIS MORE EFFICIENT
        if (j.isalpha()):
            counter2 += 1
            print(counter2) #TEMP
        else:
            pass
    if (counter1 == len(pl_base) and counter2 == len(pl_key)):
        print("test passed") #TEMP
    else:
        print("Invalid input. Please only enter letters and spaces.")
        get_input()


def separate_words(pl_base):
    words = []
    words = pl_base.split(' ')
    '''
    #Below is what I was originally trying to make work before researched better option
    counter1 = 0
    for k in pl_base:
        word = ''
        if k.isspace():
            counter2 = 0
            while counter2 < counter1:
                word += pl_base[counter2]
                counter2 += 1
            words.append(word)
        else:
            pass
        counter1 += 1
    words.append(pl_base)
    '''
    return words


#BELOW SHOULD BE WORKING NOW
def encode(pl_words, pl_key):
    print(pl_words)
    counter = 0
    encoded = ''
    counter2 = 0
    for l in pl_words:
        for m in pl_words[counter2]:
            x = let_num_conversion.get(m.upper())
            n = pl_key[(counter % len(pl_key))]
            y = let_num_conversion.get(n.upper())
            shift = (x + y) % 26
            #getting the key from value: https://www.geeksforgeeks.org/python/python-get-key-from-value-in-dictionary/
            #NEED TO CITE - using without ANOTHER loop
            #letter = let_num_conversion[shift]
            letter = list(filter(lambda z: let_num_conversion[z] == shift, let_num_conversion))
            if m.isupper():
                letter1 = letter[0]
            else:
                letter1 = letter[0].lower()
            encoded += letter1
            counter += 1
        counter2 += 1
        encoded += ' '
    print(encoded)


get_input()
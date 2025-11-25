# Add certificate??

import string

ascii_letters_plus = string.ascii_letters + " " #adjsuted version to include spaces (used in check_alpha())
                                                #and not just using + whitespace b/c only want spaces and no others
#Using the below dictionary to store the number values corresponding to the letters (non ASCII codes)
let_num_conversion = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12,
                      'M':13,'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23,
                      'X':24, 'Y':25, 'Z':26
                      }


def get_input():
    """ This function gets the input for the base and key for the encoding from the user. It will then run
        the check_alpha(), separate_words(), and encode() commands. Uses try-except to control traceback errors.

        """
    try:
        base = input('Enter the word or sentence you would like to encode: ')
        key = input('Enter a single word you would like to shift by: ')
        check_alpha(base, key)
        words = separate_words(base)
        encode(words, key)
    except KeyboardInterrupt:
        print("\nGoodbye") #If user exits the code at any point, "goodbye" will print out
        exit()
    except (ValueError, IndexError):
        print("Invalid input. Please try again.")
        get_input()
        exit()


def check_alpha(pl_base, pl_key):
    """ This function checks to see if a user inputted base and key are following the requirements, i.e. pl_base
        consists only of letters and spaces and pl_key consists of only letters, and that neither are blank.

        Arguments:
            pl_base (str): the inputted base to encode (the word/phrase being encoded)
            pl_key (str): the inputted key to encode by (what controls the shift)

        Assumptions:
            Assumes that pl_base and pl_key are strings, but if not, this command should catch that and rerun
            get_input().

        """
    if (pl_base == "") or (pl_key == ""):
        print("Invalid input. Please do not leave either input blank.")
        get_input()
        exit() #used so once reruns doesn't try to continue with invalid input
    else:
        pass
    # For the below two conditional statements, used the strings module to check the base and key
    # without needing to have a loop for each of them with multiple counters (and comparing counters).
    # I was able to do this using this source: https://www.geeksforgeeks.org/python/python-string-module/
    if all(char in string.ascii_letters for char in pl_key):
        pass
    else:
        print("Invalid key. Please enter a one word key with only letters.")
        get_input()
        exit() #used so once reruns doesn't try to continue with invalid input

    if all(char in ascii_letters_plus for char in pl_base):
        pass
    else:
        print("Invalid word or sentence to encode. Please enter only letters or spaces.") #REPHARSE
        get_input()
        exit() #used so once reruns doesn't try to continue with invalid input


def separate_words(pl_base):
    """ This function checks to see if a user inputted year is a leap year in the Hebrew calendar.

        Arguments:
            pl_base (str): the inputted base to encode (the word/phrase being encoded)

        Returns:
            words (list): the list of words separated by spaces (so if the input is a sentence, each word in
            the sentence is its own index in the list, in order)

        Assumptions:
            Assumes that pl_base is a string.

        """
    # In order to split any sentences up, used the command .split(' '), which will automatically put the words
    # into a list. I found out about this function through researching what I wanted to accomplish and
    # found the following source: https://realpython.com/python-split-string/. I didn't know that there was a built-n
    # command that could do this, and this made my code much simpler (and actually works all the time).
    words = pl_base.split(' ')
    return words


def encode(pl_words, pl_key):
    """ This function checks to see if a user inputted year is a leap year in the Hebrew calendar.

        Arguments:
            pl_words (list): the list of words from the inputted base, if it was a sentence, each word has its
            own index in the list, in order
            pl_key (str): the inputted key to encode by (what controls the shift)

        Assumptions:
            Assumes that pl_words is a list and that pl_key is a string.

        """
    counter = 0
    encoded = ''
    counter2 = 0
    for l in pl_words:
        for m in pl_words[counter2]:
            x = let_num_conversion.get(m.upper())
            n = pl_key[(counter % len(pl_key))]
            y = let_num_conversion.get(n.upper())
            shift = (x + y) % 26
            # While writing this next part initially, I could not remember how to get keys from values in
            # dictionaries, so I used the following source to help me:
            # https://www.geeksforgeeks.org/python/python-get-key-from-value-in-dictionary/
            # This source offered a couple of ways to get this information, but I used the one that more closely
            # matched what we have previously learned in this class.
            for key, val in let_num_conversion.items():
                if val == shift:
                    letter = key
                    break
                else:
                    pass
            if m.isupper():
                letter1 = letter
            else:
                letter1 = letter.lower()
            encoded += letter1
            counter += 1
        counter2 += 1
        encoded += ' '
    print("Your encode phrase is:", encoded)


get_input()

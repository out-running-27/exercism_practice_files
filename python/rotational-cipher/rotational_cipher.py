
from collections import deque
import string


def rotate(text, key):
    alphabet = string.ascii_lowercase
    cypher_text = deque(string.ascii_lowercase)

    # rotate alphabet based on key
    cypher_text.rotate(key*-1)

    # find index of each letter in standard alphabet and add to encrypt text
    encrypt_text = ""

    for letter in text:
        index = alphabet.find(letter.lower())
        if index >= 0:
            encrypt_letter = cypher_text[index]

            # check to match case of original letter
            if letter.isupper():
                encrypt_letter = encrypt_letter.upper()
            encrypt_text += encrypt_letter

        else:  # not a letter
            encrypt_text += letter

    return encrypt_text

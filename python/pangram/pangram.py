from string import ascii_lowercase


def is_pangram(sentence):
    sentence = sentence.lower()
    return all([letter in sentence for letter in ascii_lowercase])

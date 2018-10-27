import re
from string import punctuation


def word_count(phrase):
    stripped = [word.strip(punctuation) for word in re.split(r'[\s,_]+', phrase.lower())]
    return {i: stripped.count(i) for i in set(stripped) if i}

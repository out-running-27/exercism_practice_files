import re


def verify(isbn):
    isbn = isbn.replace('-', '')
    if re.match("\d{9}[\dX]$", isbn):
        digits = [int(x) if x != 'X' else 10 for x in isbn]
        isbn_sum = sum([n * int(digits[10 - n]) for n in range(10, 0, -1)])
        return isbn_sum % 11 == 0
    else:
        return False


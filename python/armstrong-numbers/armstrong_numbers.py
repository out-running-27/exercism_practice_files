def is_armstrong(number):
    """
        takes an integer, and sums each digit to the power of the digit
        if the sum of powers equals the original number, return true

        123 -> 1^3 + 2^3 + 3^3 == 36, because 36 != 123, it is not an armstrong number
        153 -> 1^3 + 5^3 + 3^3 == 153, because 153 == 153, it is an armstrong number
    """
    running_total = 0

    num_of_digits = len(str(number))

    for digit in str(number):
        running_total += int(digit) ** num_of_digits

    return number == running_total


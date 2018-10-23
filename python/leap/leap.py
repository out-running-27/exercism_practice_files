def is_leap_year(year):
    # if not divisible by 4 is not leap year
    if year % 4 != 0:
        return False
    # year is divisible by 100 but not 400 is not LY
    elif year % 100 == 0 and year % 400 != 0:
        return False
    # year is divisible by four and above condition does not apply
    else:
        return True

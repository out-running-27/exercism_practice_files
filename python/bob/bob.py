def hey(phrase):

    phrase = phrase.strip()
    is_yell = phrase.isupper()

    if phrase == "":
        return "Fine. Be that way!"
    elif phrase.endswith("?") and is_yell:
        return "Calm down, I know what I'm doing!"
    elif phrase.endswith("?") and not is_yell:
        return "Sure."
    elif is_yell:
        return "Whoa, chill out!"
    else:
        return "Whatever."
